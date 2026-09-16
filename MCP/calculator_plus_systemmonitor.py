import re
import psutil
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("MyFirstMCPServer")

# =====================================================================
# [보안 설정] 허용된 드라이브 형태만 입력받도록 화이트리스트 정규식 정의
# 예: "C:\", "D:\", "c:\", "d:\" 등 단독 드라이브 루트 경로만 허용 (UNC 경로 \\ 완전 차단)
# =====================================================================
ALLOWED_DRIVE_PATTERN = re.compile(r"^[a-zA-Z]:\\$")

# --- 계산 도구 ---

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """a와 b를 더한 값을 반환합니다."""
    return a + b

@mcp.tool()
def subtract_numbers(a: float, b: float) -> float:
    """a에서 b를 뺀 값을 반환합니다."""
    return a - b

@mcp.tool()
def multi_numbers(a: float, b: float) -> float:
    """a와 b를 곱한 값을 반환합니다."""
    return a * b

@mcp.tool()
def divide_numbers(a: float, b: float) -> str:
    """a를 b로 나눕니다. b = 0인 경우 예외 처리됩니다."""
    if b == 0:
        return "오류: 0으로 나눌 수 없습니다."
    return str(a / b)

@mcp.tool()
def power_numbers(base: float, exponent: float) -> str:
    """거듭제곱을 계산합니다. (오버플로우 방지 적용)"""
    # 극단적인 지수 입력으로 인한 서버 다운(OverflowError) 방지
    if abs(exponent) > 1000:
        return "오류: 지수(exponent) 값이 너무 큽니다. (최대 ±1000 허용)"
    try:
        return str(base ** exponent)
    except OverflowError:
        return "오류: 계산 결과가 표현 범위를 초과했습니다."
    except Exception:
        return "오류: 계산 중 에러가 발생했습니다."

# --- 시스템 모니터링 도구 ---

@mcp.tool()
def get_cpu_usage() -> str:
    """현재 CPU 전체 사용률(%)과 코어별 사용률을 반환합니다. (블로킹 최소화)"""
    # interval을 0.1초로 단축하여 서버 멈춤 현상 최소화
    per_cpu = psutil.cpu_percent(interval=0.1, percpu=True)
    total_cpu = round(sum(per_cpu) / len(per_cpu), 1) if per_cpu else 0.0
    
    result = f"전체 CPU 사용률: {total_cpu}%\n"
    result += f"코어별 사용률: {per_cpu}"
    return result

@mcp.tool()
def get_memory_status() -> dict:
    """현재 RAM(메모리) 전체 용량, 사용량, 잔여 용량 및 사용률(%)을 반환합니다."""
    mem = psutil.virtual_memory()
    gb = 1024 ** 3
    return {
        "total_gb": round(mem.total / gb, 2),
        "used_gb": round(mem.used / gb, 2),
        "available_gb": round(mem.available / gb, 2),
        "usage_percent": mem.percent
    }

@mcp.tool()
def get_disk_status(path: str = "C:\\") -> dict:
    """지정한 드라이브(기본값 C:\)의 전체 디스크 용량 및 사용률을 반환합니다. (UNC 경로 차단 적용)"""
    # 1. UNC 경로 주입 방지: C:\ 또는 D:\ 형태만 허용
    if not ALLOWED_DRIVE_PATTERN.match(path):
        return {"error": "보안 거부: 올바른 드라이브 문자 형식(예: C:\\, D:\\)만 입력 가능합니다."}
    
    try:
        disk = psutil.disk_usage(path)
        gb = 1024 ** 3
        return {
            "drive": path,
            "total_gb": round(disk.total / gb, 2),
            "used_gb": round(disk.used / gb, 2),
            "free_gb": round(disk.free / gb, 2),
            "usage_percent": disk.percent
        }
    except Exception:
        # 2. 내부 에러 메시지(str(e))를 숨겨 정보 노출 방지
        return {"error": "지정한 드라이브를 찾을 수 없거나 접근할 수 없습니다."}

if __name__ == "__main__":
    mcp.run()
