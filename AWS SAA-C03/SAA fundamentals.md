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
   
# AWS Identity and Access Management(IAM)
- IAM이란?
  - AWS 리소스에 대한 인증(Authentication) 및 인가(Authorization)를 중앙에서 관리하는 서비스
- IAM의 핵심 특징 3가지
  1. 글로벌 서비스(Global Service): 리전에 종속되지 않고 전 세계 모든 리전에서 동일하게 적용
  2. 최소 권한의 원칙(Least Privilege): 기본적으로 모든 요청은 거부(Deny)되어 있음. 필요한 권한만 최소한으로 부여하는 것이 AWS 보안의 기본
  3. 무료 서비스: IAM 사용 자체는 추가 비용이 전혀 들지 않음
- IAM의 4가지 핵심 구성 요소
  - Root User: 계정 생성 시 만들어지는 최고 관리자
    - 절대적 권한을 가진 계정으로 일상적 사용 절대 지양
    - MFA 설정 후 일상적 작업을 위한 IAM User/Role 생성 권장
  - IAM User: 실제 사람이나 애플리케이션 1명
    - Root User을 통해 최소한의 권한을 부여하여 특정 업무를 위해 생성한 User
    - 콘솔 접근용 비밀번호 또는 CLI/SDK 접근용 Access Key/Secrets Access Key 보유
  - IAM Group: IAM User들의 집합
    - 그룹에 Policy를 Attach하고, Group에 User을 추가하여 동일한 권한을 여러 User에 한 번에 부여 가능
    - 그룹 자체가 로그인하거나 인증받을 수는 없고, 그룹을 레이어링(그룹 안에 그룹)할 수 없음
    - 한 User가 여러 Group에 포함되는 것은 가능
  - IAM Role: 사람이 아닌 AWS 서비스나 임시 사용자가 맡는 탈
    - 장기 자격 증명(비밀번호/Access Key)가 없음. 임시 보안 자격 증명(STS) 사용
- IAM Policy와 동작 원리
  - Policy는 JSON 형식 문서로 작성되며, "누가 무엇을 할 수 있는지" 정의함
  - 명시적 거부가 항상 명시적 허용을 압도함
    - 기본 상태: Implicit Deny(암묵적 거부)
    - Allow 정책이 있음 -> Allow
    - Allow와 Deny가 동시에 존재 -> Deny
  - ex)
  - {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",          // Allow(허용) 또는 Deny(거부)
      "Action": "s3:GetObject",     // 수행할 작업
      "Resource": "arn:aws:s3:::my-bucket/*" // 대상 리소스
    }
  ]
}

- SAA-C03 유형 정리
  유형 1. EC2 인스턴스가 S3 버킷에 접근해야 하는 상황
  - 오답 패턴: EC2 내부 코드에 Access Key / Secret Key를 직접 하드코딩하거나 파일로 저장
  - 정답 키워드: EC2에 IAM Role(역할)을 할당함
    - 이유: IAM Role을 사용하면 AWS STS가 자동으로 임시 자격 증명을 갱신해주므로 키 유출 위험이 없어짐
  유형 2. 다른 AWS 계정(Cross-Account)의 리소스에 접근할 때
  - 상황: A계정의 EC2가 B계정의 S3 버킷에 접근하거나 작업을 수행해야 함
  - 정답 키워드: Cross-Account IAM Role 생성 및 스위치
    - B계정에서 A계정을 신뢰하는 IAM Role을 만들고, A계정 사용자가 이 Role을 맡아 작업함.
  유형 3. 계정 생성 후 초기 보안 설정(Root 계정 관리)
  - 상황: AWS 계정을 새로 생성했을 때 가장 먼저 해야 하는 보안 조치는?
  - 정답 키워드
    1. Root 계정에 MFA 즉시 설정
    2. Root계정 Access Key 생성 X / 삭제
    3. 일상 작업을 위한 별도 IAM User / Role 생성 및 최소 권한 부여
  유형 4. IAM User의 CLI/SDK 접근을 위한 자격 증명
  - 상황: 개발자가 웹 콘솔이 아닌 Terminal(CLI)에서 AWS 명령어를 실행하려고 함
  - 정답 키워드: Access Key ID & Secret Access Key 발급
    - 비밀번호는 웹 콘솔 접속용, Access Key는 CLI/API 호출용

+ IAM Permissions Boundary
1) Permissions Boundary(권한 경계)란?
   - IAM 사용자나 역할에 일반적인 정책을 아무리 많이 부여하더라도, 권한 경계가 그어놓은 한계선을 넘어서는 권한을 행사할 수 없도록 막는 역할을 하는 경계
   - Permissions Boundary자체는 권한을 부여하는 기능이 아니라 오직 개체가 가질 수 있는 **권한의 상한선**만 결정함

2) 실제 작동 방식
   - 사용자의 최종 실행 권한은 IAM 정책과 Permissoins Boundary의 교집합으로 결정됨.
   - 즉, 사용자의 IAM Policy에 모든 권한이 붙어있어도, Permissions Boundary가 S3(예시)로 한정되어있다면 해당 사용자는 S3에만 접근할 수 있음
  
3) 사용 이유
   - 가장 대표적인 목적은 권한 상승(Privilege Escalation) 방지 및 권한 위임
   - 시나리오: 회사의 중앙 보안팀이 개발자 팀에게 스스로 필요한 IAM Role과 User를 직접 생성할 수 있는 권한을 위임해주기를 원함
   - 위험 요소: 개발자가 마음대로 IAM Role을 만들 수 있게 하면, AdministratorAccess 권한을 가진 최고 관리자 역할을 새로 만들어 스스로 부여할 위험이 있음(권한 상승/Privilege Escalation)
   - 해결책: 개발자에게 IAM User/Role 생성 권한을 주되, 새로 만드는 모든 User/Role에는 반드시 지정된 Permissions Boundary를 결합해야만 생성이 가능하도록 조건을 걸어둠
  
4) 시험 혼동 가능 요소
- Permissions Boundaries vs SCP vs Resource-based Policy
- Permissions Boundaries
  - 적용 대상: 단일 IAM User/Role
  - 목적: 특정 사용자/역할의 권한 상한선 지정 및 권한 상승 방지
  - Root 계정 영향: 영향 없음
- SCP(Service Control Policy)
  - 적용 대상: AWS Organizations의 계정/OU 전체
  - 목적: 계정 전체에서 특정 AWS 서비스 사용 자체를 금지
  - Root 계정 영향: Root계정을 포함한 계정 내 모든 사용자에게 영향
- Resouce-based Policy
  - 적용 대상: S3, SQS 등 특정 리소스 자체
  - 목적: 리소스에 접근할 수 있는 외부/내부 주체 지정
 
- 간단 요약
  - Permissions Boundary는 권한을 직접 주는 게 아니라, IAM User/Role이 넘지 못할 최대 권한의 상한선을 설정하는 기능
  - 개발자에게 IAM Role 생성 권한을 안전하게 위임(권한 상승 방지)할 때 사용

# AWS EC2(Elastic Compute Cloud)
  
