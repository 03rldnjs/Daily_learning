import customtkinter as ctk   # customtkinter 라이브러리를 이 코드에서 ctk로 부르기로
import random  # random함수 활용을 위한 random 라이브러리 추가
import threading  # 멀티스레딩 제어 라이브러리
# 파이썬은 기본적으로 싱글 스레드 방식을 사용하므로 threading 라이브러리를 추가해야 연산과 화면 표현이 동시에 진행될 수 있음
import time # 시간 관리 라이브러리
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# 데이터 시각화 도구인 matplotlib차트를 tkinter가 인식할 수 있는 위젯으로 변환하는 역할
import matplotlib.pyplot as plt
# 데이터를 바탕으로 선 그래프, 바 차트 등을 그려주는 시각화 라이브러리

# CustomTkinter 기본 테마 설정 (다크 모드)
ctk.set_appearance_mode("dark")  # 다크모드
ctk.set_default_color_theme("blue")  # 기본 색상 설정 -> blue

class CloudSimulatorApp(ctk.CTk): # 기초 클래스 형성
    def __init__(self):
        super().__init__() 
        # super().은 부모 클래스를 가리키는 대명사
        # CloudSimulatorApp이라는 자식 클래스를 만들었는데, customtkiner가 미리 만들어 둔 부모클래서의 기능을 그대로 물려받겠다는 의미
        # 즉, 부모 클래스의 능력을 상속받기 원할 때 사용하는 표현

        self.title("Resource-Pool Autoscaling Simulator")  # 프로그램 title 설정
        self.geometry("1200x750")  # GUI창 크기 설정

        # --- 데이터 초기화 --- (기본값 설정)
        self.is_simulating = False  
        self.time_step = 0
        self.server_count = 4    # 서버 개수 default값: 4개

        self.data_A = {}
        self.data_B = {}

        self.create_layout()

    def create_layout(self):
        """전체 화면 레이아웃 분할"""
        self.top_panel = ctk.CTkFrame(self, corner_radius=15, height=100)
        self.top_panel.pack(fill="x", padx=20, pady=10)
        self.create_top_panel()

        self.main_area = ctk.CTkFrame(self, fg_color="transparent")
        self.main_area.pack(fill="both", expand=True, padx=20, pady=10)

        self.scenarios_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.scenarios_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.create_scenarios_view()

        self.right_frame = ctk.CTkFrame(self.main_area, width=300)
        self.right_frame.pack(side="right", fill="both", padx=(10, 0))
        self.create_right_panel()

    def create_top_panel(self):
        """상단 제어 패널"""
        title = ctk.CTkLabel(self.top_panel, text="Cloud Simulator (Resource-Pool Mode)", font=("Arial", 20, "bold"))
        title.pack(side="left", padx=20, pady=20)

        # 메인 버튼 (시작 / 리셋 공용으로 상태에 따라 변환)
        self.start_btn = ctk.CTkButton(
            self.top_panel, 
            text="START SIMULATION", 
            fg_color="#1f535d", 
            hover_color="#163e46", 
            font=("Arial", 13, "bold"), 
            command=self.handle_main_button
        )
        self.start_btn.pack(side="right", padx=20, pady=20)

        self.user_input = ctk.CTkOptionMenu(self.top_panel, values=["3", "4", "5", "6"], width=80)
        self.user_input.set("4")
        self.user_input.pack(side="right", padx=10)

        self.ent_label = ctk.CTkLabel(self.top_panel, text="SERVERS (Pie-Split):", font=("Arial", 14))
        self.ent_label.pack(side="right", padx=5)

    def create_scenarios_view(self):
        """시나리오 뷰 및 차트 내장"""
        self.frame_A = ctk.CTkFrame(self.scenarios_frame, corner_radius=15)
        self.frame_A.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        label_A = ctk.CTkLabel(self.frame_A, text="Scenario A: Conventional (Total Shared Pool Crash) ❌", font=("Arial", 14, "bold"), text_color="#ff5555")
        label_A.pack(pady=10)

        self.frame_B = ctk.CTkFrame(self.scenarios_frame, corner_radius=15)
        self.frame_B.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        label_B = ctk.CTkLabel(self.frame_B, text="Scenario B: P2P Balancing (Total Pool Stabilized)  ", font=("Arial", 14, "bold"), text_color="#55ff55")
        label_B.pack(pady=10)

        plt.style.use("dark_background")

        self.fig_A, self.ax_A = plt.subplots(figsize=(4, 3), dpi=100)
        self.fig_A.patch.set_facecolor("#2b2b2b")
        self.ax_A.set_facecolor("#2b2b2b")
        self.canvas_A = FigureCanvasTkAgg(self.fig_A, master=self.frame_A)
        self.canvas_A.get_tk_widget().pack(fill="both", expand=True, padx=10)

        self.fig_B, self.ax_B = plt.subplots(figsize=(4, 3), dpi=100)
        self.fig_B.patch.set_facecolor("#2b2b2b")
        self.ax_B.set_facecolor("#2b2b2b")
        self.canvas_B = FigureCanvasTkAgg(self.fig_B, master=self.frame_B)
        self.canvas_B.get_tk_widget().pack(fill="both", expand=True, padx=10)

        self.status_A = ctk.CTkLabel(self.frame_A, text="TOTAL SUM: - / 100\nSTATUS: Ready", justify="left", font=("Arial", 13, "bold"))
        self.status_A.pack(pady=15)

        self.status_B = ctk.CTkLabel(self.frame_B, text="TOTAL SUM: - / 100\nSTATUS: Ready", justify="left", font=("Arial", 13, "bold"))
        self.status_B.pack(pady=15)

        self.update_charts()

    def create_right_panel(self):
        """로그 및 트리거 패널"""
        trigger_label = ctk.CTkLabel(self.right_frame, text="EVENT TRIGGER", font=("Arial", 14, "bold"))
        trigger_label.pack(pady=(15, 5))

        self.spike_btn = ctk.CTkButton(self.right_frame, text="TRIGGER UNCONTROLLED\nSPIKE (Server Last)", fg_color="#8a1f1f", hover_color="#631616", height=60, font=("Arial", 13, "bold"), command=self.trigger_spike, state="disabled")
        self.spike_btn.pack(fill="x", padx=15, pady=10)

        log_label = ctk.CTkLabel(self.right_frame, text="LOGS", font=("Arial", 14, "bold"))
        log_label.pack(pady=(20, 5))

        self.log_text = ctk.CTkTextbox(self.right_frame, fg_color="#1e1e1e", font=("Consolas", 12))
        self.log_text.pack(fill="both", expand=True, padx=15, pady=15)
        self.add_log("SYSTEM: Resource-Pool Simulator ready.")

    def add_log(self, message):
        self.log_text.insert("end", time.strftime("[%H:%M:%S] ") + message + "\n")
        self.log_text.see("end")

    def update_charts(self):
        """차트 갱신 및 GUI 강제 새로고침"""
        self.ax_A.clear()
        self.ax_A.set_ylim(0, 120)  
        self.ax_A.axhline(y=100, color='red', linestyle='--', alpha=0.7, label="Max Pool Capacity (100)")
        for s_id, y_values in self.data_A.items():
            self.ax_A.plot(y_values, label=f"Server {s_id}")
        if self.data_A: self.ax_A.legend(loc="upper left", fontsize=8)
        self.fig_A.tight_layout()
        self.canvas_A.draw()

        self.ax_B.clear()
        self.ax_B.set_ylim(0, 120)
        self.ax_B.axhline(y=100, color='red', linestyle='--', alpha=0.7, label="Max Pool Capacity (100)")
        for s_id, y_values in self.data_B.items():
            self.ax_B.plot(y_values, label=f"Server {s_id}")
        if self.data_B: self.ax_B.legend(loc="upper left", fontsize=8)
        self.fig_B.tight_layout()
        self.canvas_B.draw()

        self.update()

    def handle_main_button(self):
        """[신규 변경] 버튼 텍스트가 RESET 이면 리셋을, 아니면 시뮬레이션을 시작함"""
        if self.start_btn.cget("text") == "RESET SYSTEM 🔄":
            self.reset_simulator()
        else:
            self.start_simulation()

    def start_simulation(self):
        if not self.is_simulating:
            self.server_count = int(self.user_input.get())
            self.data_A = {}
            self.data_B = {}
            self.time_step = 0

            base_pie = 60 // self.server_count
            for i in range(1, self.server_count + 1):
                self.data_A[i] = [base_pie]
                self.data_B[i] = [base_pie]

            self.is_simulating = True
            self.start_btn.configure(state="disabled") # 실행 중에는 버튼 잠금
            self.user_input.configure(state="disabled")
            self.spike_btn.configure(state="normal", text=f"TRIGGER UNCONTROLLED\nSPIKE (Server {self.server_count})")
            
            self.status_A.configure(text=f"TOTAL SUM: {base_pie * self.server_count} / 100\nSTATUS: Normal Running", text_color="white")
            self.status_B.configure(text=f"TOTAL SUM: {base_pie * self.server_count} / 100\nSTATUS: Normal Running", text_color="white")

            self.add_log(f"SYSTEM: Pool Simulator started. Allocated: {base_pie * self.server_count}")

            self.sim_thread = threading.Thread(target=self.simulation_loop, daemon=True)
            self.sim_thread.start()

    def simulation_loop(self):
        """평상시 루프"""
        while self.is_simulating:
            self.time_step += 1

            for s_id in self.data_A.keys():
                next_A = max(5, min(40, self.data_A[s_id][-1] + random.randint(-2, 2)))
                self.data_A[s_id].append(next_A)

                next_B = max(5, min(40, self.data_B[s_id][-1] + random.randint(-2, 2)))
                self.data_B[s_id].append(next_B)

            sum_A = sum([v[-1] for v in self.data_A.values()])
            sum_B = sum([v[-1] for v in self.data_B.values()])
            self.status_A.configure(text=f"TOTAL SUM: {sum_A} / 100\nSTATUS: Stable")
            self.status_B.configure(text=f"TOTAL SUM: {sum_B} / 100\nSTATUS: Stable")

            self.update_charts()
            time.sleep(0.5)

    def trigger_spike(self):
        self.spike_btn.configure(state="disabled")
        self.add_log(f"EVENT: Heavy traffic incoming on Server {self.server_count}!")
        
        self.is_simulating = False 
        spike_thread = threading.Thread(target=self.process_spike, daemon=True)
        spike_thread.start()

    def process_spike(self):
        target_server = self.server_count

        # 🚀 [한 사이클: 총 6단계의 실시간 시간 흐름]
        for step in range(1, 7):
            self.time_step += 1
            
            # --- [공통] 1~3단계: P2P 제어 없이 두 시나리오 모두 폭주 유입 (긴장감 조성) ---
            if step <= 3:
                for s_id in self.data_A.keys():
                    if s_id == target_server:
                        # 마지막 서버의 파이 요구량이 매 단계 +11씩 폭등!
                        self.data_A[s_id].append(self.data_A[s_id][-1] + 11)
                        self.data_B[s_id].append(self.data_B[s_id][-1] + 11)
                    else:
                        self.data_A[s_id].append(self.data_A[s_id][-1] + random.randint(-1, 1))
                        self.data_B[s_id].append(self.data_B[s_id][-1] + random.randint(-1, 1))
                        
            # --- [분기] 4~6단계: 임계점 도달 후 시나리오별 극적인 대조 연출 ---
            else:
                # ❌ 시나리오 A: 제어 장치가 없으므로 계속 폭주하여 100을 돌파(크래시)
                for s_id in self.data_A.keys():
                    if s_id == target_server:
                        self.data_A[s_id].append(self.data_A[s_id][-1] + 11)
                    else:
                        self.data_A[s_id].append(self.data_A[s_id][-1])

                # 🛡️ 시나리오 B: [4단계가 되는 순간] 100 직전(95 내외)에서 P2P 비상 제어 발동!
                # 주변 서버들의 자원을 '순간적으로' 확 회수하여 아래로 강하게 꺾어버림
                if step == 4:
                    self.add_log("🚨 ALERT: Total Pool imminent! P2P Emergency Intercept active.")
                
                for s_id in self.data_B.keys():
                    if s_id == target_server:
                        # 폭주 서버도 자원을 양보받아 안정권으로 툭 떨어짐
                        self.data_B[s_id].append(38)
                    else:
                        # ⭐ 핵심 연출: 주변 서버들이 자기 파이를 한 자릿수(6%)로 확 줄이며 그래프가 아래로 뚝 떨어짐!
                        self.data_B[s_id].append(6)

            # --- [실시간 차트 및 텍스트 데이터 반영] ---
            sum_A = sum([v[-1] for v in self.data_A.values()])
            sum_B = sum([v[-1] for v in self.data_B.values()])
            
            # 시나리오 A 상태 표시
            if sum_A >= 100:
                self.status_A.configure(text=f"TOTAL SUM: {sum_A} / 100\nSTATUS: POOL CRASHED 💥", text_color="#ff5555")
            else:
                self.status_A.configure(text=f"TOTAL SUM: {sum_A} / 100\nSTATUS: Resource Rising", text_color="#ffaa00")
            
            # 시나리오 B 상태 표시 (절대 100을 넘지 않음)
            if step >= 4:
                self.status_B.configure(text=f"TOTAL SUM: {sum_B} / 100\nSTATUS: P2P Mitigated Successfully 🛡️", text_color="#55ff55")
            else:
                self.status_B.configure(text=f"TOTAL SUM: {sum_B} / 100\nSTATUS: Resource Rising", text_color="#ffaa00")

            self.update_charts()
            time.sleep(0.6) # 그래프가 꺾이는 순간을 뚜렷하게 인지할 수 있도록 지연시간 최적화

        # --- [최종 사이클 종료 및 마감] ---
        time.sleep(0.2)
        final_sum_A = sum([v[-1] for v in self.data_A.values()])
        final_sum_B = sum([v[-1] for v in self.data_B.values()])

        self.add_log(f"Scenario A CRASH: Total allocation reached {final_sum_A}/100.")
        self.add_log(f"Scenario B SUCCESS: P2P balancing capped total load safely at {final_sum_B}/100.")
        
        self.update_charts()
        
        # 사이클이 완전히 끝났으므로 리셋 버튼 활성화
        self.start_btn.configure(state="normal", text="RESET SYSTEM 🔄", fg_color="#d35400", hover_color="#b33921")
        
    def reset_simulator(self):
        """[신규 추가] 데이터를 깨끗이 초기화하고 화면을 첫 기동 상태로 되돌리는 함수"""
        self.is_simulating = False
        self.time_step = 0
        
        # 데이터 딕셔너리 비우기
        self.data_A = {}
        self.data_B = {}

        # 상단 패널 컨트롤 잠금 해제 및 원래 디자인 복구
        self.user_input.configure(state="normal")
        self.start_btn.configure(text="START SIMULATION", fg_color="#1f535d", hover_color="#163e46")
        self.spike_btn.configure(state="disabled", text="TRIGGER UNCONTROLLED\nSPIKE (Server Last)")

        # 상태 라벨 초기화
        self.status_A.configure(text="TOTAL SUM: - / 100\nSTATUS: Ready", text_color="white")
        self.status_B.configure(text="TOTAL SUM: - / 100\nSTATUS: Ready", text_color="white")

        self.add_log("SYSTEM: Simulator has been reset. Ready for next setup.")
        
        # 차트 싹 밀어버리기
        self.update_charts()


if __name__ == "__main__":
    app = CloudSimulatorApp()
    app.mainloop()
