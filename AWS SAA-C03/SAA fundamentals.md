# AWS ELB(Elastic Load Balancer)
- ELB(Elastic Load Balancer)란?
  - AWS에서 제공하는 부하 분산 서비스
  - 인터넷에서 수많은 사용자 요청이 몰려올 때 특정 서버 한 대에 과부하가 걸리지 않도록 트래픽을 여러 서버로 공평하게 나누어 전달하는 트래픽 교통정리원
 
- ELB가 필요한 이유
  1. 고가용성(High Availablity): 서버 한 두 대가 고장 나더라도 정상 작동 중인 다른 서버로 트래픽을 돌려 서비스가 중단되지 않도록 함.
  2. 유연한 확장성: Auto Scaling 그룹과 결합하면, 서버가 늘어나거나 줄어들 때 알아서 신규 서버를 감지하고 트래픽을 분산해 줌.
  3. 상태 검사: 주기적으로 백엔드 서버에 핑을 보내 살아있는지 확인하고, Unhealty 상태인 서버에는 트래픽을 보내지 않음
 
- ELB의 4가지 종류
  1. ALB(Application Load Balancer)
     - 계층: Layer 7(애플리케이션 계층)
     - 주요 프로토콜: HTTP, HTTPS, gRPC 등
     - 처리 속도: 밀리초(ms) 단위
     - IP 주소: 가변 IP
     - 마이크로서비스 & 컨테이너 베이스 어플리케이션에 적합
     - URL/헤더 기반 세부 라우
  2. NLB(Network Load Balancer)
     - 계층: Layer 4(네트워크 계층)
     - 주요 프로토콜: TCP, UDP, TLS
     - 처리 속도: 마이크로초 단위(초저지연)
     - IP 주소: 고정 IP(Elastic IP)
     - 초당 수백만 건 폭발적 트래픽 처리
  3. GWLB(Gateway Load Balancer)
     - 계층: Layer 3/4 (네트워크/전송 계층)
     - 주요 프로토콜: IP 프로토콜 패킷
     - 처리 속도: 패킷 수준 레이어 처리
     - IP 주소: 고정 IP/GENEVE 프로토콜
     - 방화벽/IDS 등 제3자 보안 가상 머신 통과
  4. CLB(Classic Load Balancer - 구형)
     - 계층: Layer 4 / Layer 7
     - 주요 프로토콜: HTTP, HTTPS(Layer 7), TCP(Layer 4) 등
     - 처리 속도: 일반
     - IP 주소: 가변 IP
     - //사용 지양//

  -> 웹/앱 트래픽이고 세부 라우팅 규칙이 필요하다 = ALB
  -> 초저지연, 고정 IP 필수, TCP/UDP 통신, 대규모 트래픽 = NLB
  -> 인라인 방화벽/보안 패킷 분석기 통과 시 = GLB

- ELB의 동작 방식/주요 기능
  1. 리스너
     - 로드밸런서가 외부에서 들어오는 요청을 감지하는 통로(HTTP 80 포트, HTTPS 443 포트)
  2. 대상 그룹(Target Group)
     - 로드밸런서가 트래픽을 전달할 목적지 서버들의 묶음
     - 대상 유형: EC2 인스턴스, IP 주소(온프레미스 연동 가능), Lambda 함수, ECS 컨테이너
  3. 헬스 체크(Health Check)
     - 로드밸런서가 대상 그룹 안의 서버들에 주기적으로 요청을 보내 정상이면 Healthy, 응답이 없으면 Unhealthy로 판단
     - Unhealty로 판정된 서버에는 트래픽을 보내지 않음
  4. 고정 세션(Sticky Sesstions) - 쿠키 사용(7일 유지 / 기간 조정 불가)
     - 웹 애플리케이션 쿠키를 이용해 특정 클라이언트의 모든 요청이 **항상 동일한** EC2 인스턴스로 전달되도록 유효기간 동안 고정하는 기능
  5. SSL 종단(SSL Termination / Offloading)
     - 클라이언트와 로드밸런서 사이는 HTTPS 암호화 통신을 하고, 로드밸런서와 내부 EC2 사이는 HTTP(복호화) 통신을 함으로써 백엔드 서버의 암호화 연산 부담을 줄임
    
- SAA-C03 유형 정리
  - 유형 1. URL 경로나 도메인 이름에 따른 트래픽 분산
    - 문제 상황: /api 요청은 API 서버로, /images 요청은 이미지 서버로 보내고 싶다
    - 정답 키워드: ALB의 경로 기반 라우팅
      
  - 유형 2. 고정 IP 주소가 필요하거나, 엄청난 실시간 트래픽 처리
    - 문제 상황: 클라이언트 방화벽에 로드밸런서 IP를 화이트리스트로 등록해야 해서 IP가 바뀌면 안 되거나, 초당 수백만 건의 TCP(Layer 4)트래픽을 처리해야 함
    - 정답 키워드: NLB(AZ당 Elastic IP 할당 가능)
   
  - 유형 3. 세션 데이터가 특정 서버 인스턴스 메모리에만 저장되어 있는 경우
    - 문제 상황: 사용자가 로그인 후 페이지를 이동할 때마다 로그아웃되는 현상이 발생
    - 정답 키워드: ALB의 Sticky Session(고정 세션) 활성화(단, 완전한 stateless 아키텍처를 위해서는 ElasticCache/DynamoDB 도입이 더 우수한 정답)
   
  - 유형 4. 보안 강화를 위한 보안 그룹(Security Group) 구성
    - 문제 상황: EC2 인스턴스가 인터넷에 직접 노출되지 않고 오직 로드밸런서를 통해서만 접근 가능하게 설정하고 싶다
    - 정답 설정:
      - ALB Security Group: Inbound 0.0.0.0/0 (80(HTTP)/443(HTTPS))
      - EC2 Security Group: Inbound ALB의 Security Group ID(80(HTTP)/443(HTTPS)) -> IP 대역 대신 ALB 보안 그룹 자체를 소스로 지정
  - 유형 5. 멀티 도메인에 대한 SSL 인증서 처리
    - 문제 상황: 로드밸런서 하나에 a.com, b.com 등 여러 도메인의 HTTPS 요청을 모두 처리해야 함.
    - 정답 키워드: ALB + SNI(Server Name Indication) 지원 및 ACM (AWS Certificate Manager) 연동
   
  
