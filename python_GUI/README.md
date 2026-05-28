# 💱 실시간 환율 계산기 (Tkinter Exchange Calculator)
[GUI_currency_exchange_plus.py](./GUI_currency_exchange_plus.py)

Python의 `tkinter` 라이브러리를 활용하여 제작한 GUI 기반 환율 계산기입니다.

## 🚀 Key Features & Defensive Coding
- **Defensive Coding:** `try-except ValueError`를 활용한 문자 입력 차단 및 음수/빈 값 예외 처리
- **DRY Principle:** 중복 코드를 최소화하고 공통 마무리 로직 통합
- **Data Binding:** `StringVar()`를 활용한 라디오 버튼 상태 실시간 동기화

## 💡 배운 점 (Retrospective)
### 왜 `from tkinter import *`보다 `import tkinter as tk`인가? / why 'import tkinter as tk' is 'better than from tkinter import'
1. **이름 충돌 방지 (prevent name collision): 내장 함수나 변수가 덮어씌워져 발생하는 원인 모를 버그 예방
2. **명확한 출처 (Readability):** `tk.` 접두어를 통해 어떤 위젯이 어떤 라이브러리에서 왔는지 한눈에 파악할 수 있어 협업과 유지보수에 유리 can apprehend the root of widget at a glance so has an advantage at collaboration and program maintenance
