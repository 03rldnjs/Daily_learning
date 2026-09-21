import os
import logging
import sys
import re # 정규식 모듈 추가
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from mcp.server.mcpserver import MCPServer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "s3_mcp_access.log")

# ---------------------------------------------------------------------
# [보안 설정]
# 허용할 버킷 화이트리스트 (None이면 제한 없음, 지정 시 해당 버킷만 접근 허용)
# 예: ALLOWED_BUCKETS = ["my-safe-bucket-2026", "mcp-test-bucket"]
# ---------------------------------------------------------------------
ALLOWED_BUCKETS = None  

def sanitize_text(input_str: str) -> str:
    """
    로그 및 LLM 출력 인젝션/터미널 이스케이프 공격 방지를 위해 
    모든 제어문자(ASCII 0~31, 127)를 '_'로 정제
    """
    if not input_str:
        return ""
    # \x00-\x1f (줄바꿈, 탭, ANSI 이스케이프 등 제어문자 전체) 및 \x7f (DEL) 제거
    return re.sub(r'[\x00-\x1f\x7f]', '_', str(input_str))

# ---------------------------------------------------------------------
# [로깅 설정] 
# ---------------------------------------------------------------------
logger = logging.getLogger("AWS_S3_MCP")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')

file_handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# ---------------------------------------------------------------------
# [MCP 서버 초기화]
# ---------------------------------------------------------------------
mcp = MCPServer("AWS S3 Manager Server")

def get_s3_client():
    return boto3.client("s3")


# ---------------------------------------------------------------------
# [MCP Tools 정의]
# ---------------------------------------------------------------------

@mcp.tool()
def list_s3_buckets() -> str:
    """현재 AWS 계정에 소유한 모든 S3 버킷 목록을 반환합니다."""
    logger.info("[TOOL CALL] list_s3_buckets")
    try:
        s3 = get_s3_client()
        response = s3.list_buckets()
        buckets = response.get("Buckets", [])
        
        if not buckets:
            return "계정에 생성된 S3 버킷이 없습니다."
        
        result_lines = ["=== AWS S3 버킷 목록 ==="]
        count = 0
        for bucket in buckets:
            name = sanitize_text(bucket.get("Name"))
            created = bucket.get("CreationDate")
            
            # 화이트리스트 필터링
            if ALLOWED_BUCKETS is not None and name not in ALLOWED_BUCKETS:
                continue
                
            result_lines.append(f"- {name} (생성일: {created})")
            count += 1
            
        logger.info(f"[SUCCESS] list_s3_buckets | Filtered Buckets: {count}")
        return "\n".join(result_lines)

    except ClientError as e:
        error_code = e.response.get("Error", {}).get("Code", "Unknown")
        logger.error(f"[AWS ERROR] list_s3_buckets | Code: {error_code} | Details: {e}")
        return f"AWS 요청 처리 중 오류가 발생했습니다. (사유: {error_code})"
    except Exception as e:
        logger.exception("[SYSTEM ERROR] list_s3_buckets | Unexpected error")
        return "시스템 내부 오류가 발생했습니다. 관리자 로그를 확인하세요."


@mcp.tool()
def list_s3_objects(bucket_name: str, prefix: str = "") -> str:
    """
    지정한 S3 버킷 내부의 파일/폴더 객체 목록을 조회합니다.
    """
    # 입력값 정제
    safe_bucket = sanitize_text(bucket_name)
    safe_prefix = sanitize_text(prefix)
    logger.info(f"[TOOL CALL] list_s3_objects | bucket='{safe_bucket}', prefix='{safe_prefix}'")

    # 신뢰 경계 (화이트리스트 검증)
    if ALLOWED_BUCKETS is not None and bucket_name not in ALLOWED_BUCKETS:
        logger.warning(f"[UNAUTHORIZED ACCESS ATTEMPT] Bucket: '{safe_bucket}' is not allowed.")
        return f"접근 거부: '{safe_bucket}' 버킷은 보안 정책상 접근이 허용되지 않았습니다."

    try:
        s3 = get_s3_client()
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        contents = response.get("Contents", [])
        is_truncated = response.get("IsTruncated", False)
        
        if not contents:
            return f"버킷 '{safe_bucket}' (Prefix: '{safe_prefix}') 에 존재하는 파일이 없습니다."
        
        result_lines = [f"=== 버킷 [{safe_bucket}] 객체 목록 (Prefix: '{safe_prefix}') ==="]
        for obj in contents:
            key = sanitize_text(obj.get("Key"))
            size_bytes = obj.get("Size", 0)
            size_kb = round(size_bytes / 1024, 2)
            last_modified = obj.get("LastModified")
            result_lines.append(f"- {key} | {size_kb} KB | 수정일: {last_modified}")
            
        # 1,000개 초과 시 안내 문구 추가 (페이지네이션 처리)
        if is_truncated:
            result_lines.append("\n[주의] 조회된 객체가 1,000개를 초과하여 일부만 표시되었습니다.")

        logger.info(f"[SUCCESS] list_s3_objects | Bucket: '{safe_bucket}', Count: {len(contents)}, Truncated: {is_truncated}")
        return "\n".join(result_lines)

    except ClientError as e:
        error_code = e.response.get("Error", {}).get("Code", "Unknown")
        logger.error(f"[AWS ERROR] list_s3_objects | Bucket: '{safe_bucket}' | Code: {error_code} | Details: {e}")
        
        if error_code == "NoSuchBucket":
            return f"오류: '{safe_bucket}' 버킷이 존재하지 않습니다."
        elif error_code == "AccessDenied":
            return f"오류: '{safe_bucket}' 버킷 목록을 읽을 권한이 없습니다."
        return f"AWS ClientError 발생 ({error_code})"
    except Exception as e:
        logger.exception(f"[SYSTEM ERROR] list_s3_objects | Bucket: '{safe_bucket}'")
        return "시스템 내부 오류가 발생했습니다. 관리자 로그를 확인하세요."


if __name__ == "__main__":
    logger.info("=== AWS S3 MCP Server 시작 ===")
    
    # 서버 실행 시 화이트리스트 상태 경고 출력
    if ALLOWED_BUCKETS is None:
        logger.warning("[SECURITY WARNING] ALLOWED_BUCKETS가 설정되지 않았습니다. 모든 버킷에 접근할 수 있습니다.")
    else:
        logger.info(f"[SECURITY INFO] ALLOWED_BUCKETS 활성화됨: {ALLOWED_BUCKETS}")
        
    mcp.run()
