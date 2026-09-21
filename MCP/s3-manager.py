import os
import logging
import sys
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from mcp.server.mcpserver import MCPServer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "s3_mcp_access.log")

# ---------------------------------------------------------------------
# [로깅 설정] 
# MCP 표준 입출력(stdout) 방해를 막기 위해 로그는 sys.stderr 및 파일로 출력
# ---------------------------------------------------------------------
logger = logging.getLogger("AWS_S3_MCP")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')

# 파일 로그 핸들러
file_handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# 터미널(stderr) 로그 핸들러
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


# ---------------------------------------------------------------------
# [MCP 서버 초기화]
# ---------------------------------------------------------------------
mcp = MCPServer("AWS S3 Manager Server")

def get_s3_client():
    """
    boto3 S3 클라이언트를 생성합니다.
    ~/.aws/credentials 파일이나 환경변수에 설정된 AWS 자격 증명을 자동으로 참조합니다.
    """
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
        for bucket in buckets:
            name = bucket.get("Name")
            created = bucket.get("CreationDate")
            result_lines.append(f"- {name} (생성일: {created})")
            
        logger.info(f"[SUCCESS] list_s3_buckets | Total Buckets: {len(buckets)}")
        return "\n".join(result_lines)

    except ClientError as e:
        error_code = e.response.get("Error", {}).get("Code", "Unknown")
        logger.error(f"[AWS ERROR] list_s3_buckets | Code: {error_code} | {e}")
        return f"AWS ClientError 발생 ({error_code}): 권한 또는 자격 증명을 확인하세요."
    except Exception as e:
        logger.error(f"[SYSTEM ERROR] list_s3_buckets | Exception: {type(e).__name__} - {e}")
        return f"오류 발생: {str(e)}"


@mcp.tool()
def list_s3_objects(bucket_name: str, prefix: str = "") -> str:
    """
    지정한 S3 버킷 내부의 파일/폴더 객체 목록을 조회합니다.
    
    Args:
        bucket_name (str): 조회할 S3 버킷 이름
        prefix (str): 검색할 경로 프레픽스 (예: 'logs/', 'images/2026/')
    """
    logger.info(f"[TOOL CALL] list_s3_objects | bucket='{bucket_name}', prefix='{prefix}'")
    try:
        s3 = get_s3_client()
        
        # S3 객체 목록 조회 (최대 1,000개 기본)
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        contents = response.get("Contents", [])
        
        if not contents:
            return f"버킷 '{bucket_name}' (Prefix: '{prefix}') 에 존재하는 파일이 없습니다."
        
        result_lines = [f"=== 버킷 [{bucket_name}] 객체 목록 (Prefix: '{prefix}') ==="]
        for obj in contents:
            key = obj.get("Key")
            size_bytes = obj.get("Size", 0)
            size_kb = round(size_bytes / 1024, 2)
            last_modified = obj.get("LastModified")
            result_lines.append(f"- {key} | {size_kb} KB | 수정일: {last_modified}")
            
        logger.info(f"[SUCCESS] list_s3_objects | Bucket: '{bucket_name}', Count: {len(contents)}")
        return "\n".join(result_lines)

    except ClientError as e:
        error_code = e.response.get("Error", {}).get("Code", "Unknown")
        logger.error(f"[AWS ERROR] list_s3_objects | Bucket: '{bucket_name}' | Code: {error_code} | {e}")
        if error_code == "NoSuchBucket":
            return f"오류: '{bucket_name}' 버킷이 존재하지 않습니다."
        elif error_code == "AccessDenied":
            return f"오류: '{bucket_name}' 버킷 목록을 읽을 권한이 없습니다."
        return f"AWS ClientError 발생 ({error_code})"
    except Exception as e:
        logger.error(f"[SYSTEM ERROR] list_s3_objects | Exception: {type(e).__name__} - {e}")
        return f"오류 발생: {str(e)}"


if __name__ == "__main__":
    logger.info("=== AWS S3 MCP Server 시작 ===")
    mcp.run()
