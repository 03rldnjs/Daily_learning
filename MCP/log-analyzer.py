import os
import re
from pathlib import Path
from mcp.server.mcpserver import MCPServer

# MCP(Model Context Protocol) 서버 인스턴스를 생성합니다.
# AI 모델(Claude 등)이 이 이름("Log & File Analyzer")으로 서버 도구들을 인식하게 됩니다.
mcp = MCPServer("Log & File Analyzer")

# =====================================================================
# [보안 설정] 샌드박스(Sandbox) 기본 디렉토리 설정
# =====================================================================
# raw string(r"...")을 사용해 윈도우 경로의 역슬래시(\)가 탈출 문자로 해석되는 것을 방지합니다.
# .resolve()를 호출하여 상대 경로나 심볼릭 링크를 '실제 절대 경로'로 완전히 변환합니다.
# 이 경로와 그 하위 폴더 이외의 영역에 대한 접근은 모두 차단됩니다.
ALLOWED_BASE_DIR = Path(r"C:\Users\03rld\OneDrive\바탕 화면\AWS study\mcp-quickstart").resolve()

# 윈도우 OS 시스템에서 특별한 의미를 갖는 '예약 장치 이름(Reserved Device Names)' 집합입니다.
# 파일 이름으로 이 단어들을 사용해 접근을 시도하면(예: NUL.txt, CON), 
# OS 수준에서 프로그램이 입출력 대기 상태에 빠져(Hang/Block) 서버가 멈추는 DoS 공격이 발생할 수 있습니다.
WINDOWS_RESERVED_NAMES = {
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
}

def validate_safe_path(target_path_str: str) -> Path:
    """
    [핵심 보안 함수] 사용자/AI가 전달한 경로가 안전한지 검증합니다.
    1. 상대 경로(`../`)를 계산하여 실제 최종 위치를 파악합니다.
    2. 윈도우 예약어 접근을 차단합니다.
    3. 허용된 샌드박스 범위(ALLOWED_BASE_DIR)를 벗어나는지 확인합니다.
    4. 보안 위반 시 내부 서버 경로 정보를 숨기고 일관된 예외를 던집니다.
    """
    try:
        # 입력받은 문자열 경로를 Path 객체로 만든 후, .resolve()로 정규화(Canonicalization)합니다.
        # 예: "C:\allowed\dir\..\..\Windows\system32" -> "C:\Windows\system32"로 계산됨.
        target_path = Path(target_path_str).resolve()
        
        # 1. 윈도우 예약 장치 이름 검증
        # target_path.stem은 확장자를 제외한 파일/폴더 이름입니다 (예: "CON.txt" -> "CON").
        # 대소문자 구분을 없애기 위해 .upper()로 변환 후 비교합니다.
        if target_path.stem.upper() in WINDOWS_RESERVED_NAMES:
            raise PermissionError("보안 거부: 예약된 시스템 장치 이름에는 접근할 수 없습니다.")
        
        # 2. 샌드박스 영역 이탈 여부 검증
        # .relative_to(A)는 target_path가 A의 하위 경로인 경우 'A로부터의 상대 경로'를 반환합니다.
        # 만약 target_path가 ALLOWED_BASE_DIR의 하위 폴더가 아니라면 ValueError 예외가 발생합니다.
        target_path.relative_to(ALLOWED_BASE_DIR)
        
        # 검증을 성공적으로 통과한 안전한 Path 객체를 반환합니다.
        return target_path

    except PermissionError as pe:
        # 예약어 검증에서 명시적으로 던진 PermissionError는 그대로 상위로 전달합니다.
        raise pe
    
    except Exception:
        # Path Traversal(경로 이탈)이나 기타 변환 실패 시 들어오는 구간입니다.
        # [정보 노출 방지(Information Disclosure)]
        # 자세한 오류 내부 메시지(예: "C:\Users\... 에 접근 불가")를 반환하면 공격자에게 디렉토리 구조를 알려주게 됩니다.
        # 따라서 상세 원인을 추적할 수 없도록 모호하고 일반화된 에러 메시지만 출력합니다.
        raise PermissionError("보안 거부: 접근 권한이 없거나 허용된 작업 영역(경로)을 벗어났습니다.")


@mcp.tool()
def list_directory(dir_path: str = ".") -> str:
    """
    지정한 디렉토리 폴더 내의 파일과 폴더 목록을 반환합니다. (보안 적용)
    """
    try:
        # 1. 전달받은 경로의 안전성을 먼저 검증합니다. (실패 시 예외 발생 후 catch 블록으로 이동)
        safe_path = validate_safe_path(dir_path)
        
        # 2. 파일/폴더 존재 여부 및 디렉토리 여부를 검사합니다.
        # 두 경우 모두 동일한 메시지를 반환하여 특정 경로의 '존재 유무'를 공격자가 유추하기 어렵게 만듭니다.
        if not safe_path.exists():
            return "Error: 지정한 파일 또는 디렉토리를 찾을 수 없습니다."
        if not safe_path.is_dir():
            return "Error: 지정한 파일 또는 디렉토리를 찾을 수 없습니다."

        # 3. 폴더 내부 항목들의 목록을 가져옵니다.
        items = os.listdir(safe_path)
        result = []
        for item in items:
            full_path = safe_path / item
            # 항목이 디렉토리면 [DIR], 파일이면 [FILE]로 표기합니다.
            kind = "[DIR]" if full_path.is_dir() else "[FILE]"
            # 파일인 경우 용량을 KB 단위로 계산하고, 디렉토리면 "-"로 표기합니다.
            size = f"{full_path.stat().st_size / 1024:.1f} KB" if full_path.is_file() else "-"
            # 문자열 정렬 포맷팅을 사용해 출력 결과를 보기 좋게 맞춥니다.
            result.append(f"{kind:<7} {item:<30} ({size})")
        
        # 목록을 줄바꿈 문자로 합쳐서 반환합니다.
        return "\n".join(result) if result else "폴더가 비어 있습니다."
        
    except Exception as e:
        # 예외 발생 시 내부 시스템 정보(Traceback 등)를 노출하지 않고 모호한 에러만 반환합니다.
        return "Error: 에러 발생"


@mcp.tool()
def read_last_logs(file_path: str, lines_count: int = 20) -> str:
    """
    특정 로그 파일의 마지막 N줄을 읽어서 반환합니다. (보안 및 용량 제한 적용)
    """
    try:
        # 1. 경로 보안 검증
        safe_path = validate_safe_path(file_path)

        # 2. 대상이 실제 존재하는 '파일'인지 검사
        if not safe_path.exists() or not safe_path.is_file():
            return "Error: 지정한 파일 또는 디렉토리를 찾을 수 없습니다."

        # 3. [가용성 보장 / DoS 방어] 메모리 과부하 방지를 위한 파일 용량 제한
        # st_size는 바이트(Byte) 단위이므로 1024 * 1024 로 나누어 MB 단위로 변환합니다.
        file_size_mb = safe_path.stat().st_size / (1024 * 1024)
        if file_size_mb > 50:
            return f"Error: 파일 용량이 너무 큽니다 ({file_size_mb:.1f}MB). 50MB 이하 파일만 읽을 수 있습니다."

        # 4. 파일 읽기 작업 수행
        # errors="ignore" 옵션을 주어 로그 파일 내 인코딩이 깨진 문자(Non-UTF8)가 있더라도 튕기지 않고 무시합니다.
        with open(safe_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            # 파이썬 리스트 슬라이싱 [-N:] 을 사용해 파일의 마지막 N개 줄만 가져옵니다.
            last_lines = lines[-lines_count:]
            return "".join(last_lines)
            
    except Exception as e:
        return "Error: 에러 발생"


@mcp.tool()
def search_log_errors(file_path: str, keywords: str = "ERROR,CRITICAL,FAILED", max_results: int = 100) -> str:
    """
    로그 파일에서 에러 키워드가 포함된 행을 추출합니다. (보안 및 개수 제한 적용)
    """
    try:
        # 1. 경로 보안 검증
        safe_path = validate_safe_path(file_path)

        # 2. 존재 여부 및 파일 확인
        if not safe_path.exists() or not safe_path.is_file():
            return "Error: 지정한 파일 또는 디렉토리를 찾을 수 없습니다."

        # 3. 쉼표(,)로 구분된 키워드 문자열을 리스트로 분리하고, 대문자로 통일합니다.
        # 공백 제거(.strip()) 후 대문자 변환(.upper())
        keyword_list = [k.strip().upper() for k in keywords.split(",")]
        matched_lines = []

        # 4. 파일을 한 줄씩 읽어가며 검색 (메모리 효율적인 방식)
        # enumerate(f, 1)을 사용하여 1번 줄부터 줄 번호(idx)를 함께 추적합니다.
        with open(safe_path, "r", encoding="utf-8", errors="ignore") as f:
            for idx, line in enumerate(f, 1):
                # 읽어온 줄도 대문자로 바꿔 키워드 포함 여부를 비교합니다 (대소문자 무시 검색 효과).
                if any(kw in line.upper() for kw in keyword_list):
                    matched_lines.append(f"Line {idx}: {line.strip()}")
                    
                    # [가용성 보장 및 Context Limit 방어]
                    # 매칭된 결과가 max_results(기본 100개)에 도달하면 읽기를 즉시 중단합니다.
                    # AI(Claude)에게 너무 긴 응답이 전달되어 토큰을 과도하게 소비하거나 멈추는 현상을 방지합니다.
                    if len(matched_lines) >= max_results:
                        matched_lines.append(f"\n... (최대 {max_results}개까지만 표시됩니다)")
                        break

        if not matched_lines:
            return f"키워드 ({keywords})에 해당되는 로그가 없습니다."

        return "\n".join(matched_lines)
        
    except Exception as e:
        return f"Error: 에러 발생"


# 스크립트가 직접 실행될 때만 MCP 서버를 가동합니다.
if __name__ == "__main__":
    mcp.run()
