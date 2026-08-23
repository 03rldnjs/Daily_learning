# AWS Config
AWS의 설정 상태를 지속적으로 기록하고, 변경 이력을 추적하며, 사전 정의된 규칙에 부합하는지 준수 여부를 평가하는 관리 서비스
-> AWS 리소스 상태 전용 cctv 및 감사관
- 핵심 기능
  설정 이력 기록: 특정 리소스가 시간에 따라 어떻게 변경되었는지 타임라인 형태로 기록함
  규정 준수 평가: S3, 보안 그룹 등에 대한 규칙을 정해두고, 이를 위반하면 위반 상태로 표시해 줌
  자동 수정: 위반 사항이 발견되면 Systems Manager Automation 등을 연결해 자동으로 설정을 올바르게 복구
  리소스간 관계 파악: 보안 그룹이 어떤 EC2 인스턴스나 EBS와 연결되어 있는지 등 리소스간의 연관관계를 시각적으로 보여줌

- 출제 포인트
  Configuration History(설정 이력 추적)
  Compliance Check(규정/정책 준수 평가)
  Auditing/Change Management(감사 및 변경 관리)
  Resource Relationships(리소스 간 관계 추적)

- 헷갈리기 쉬운 서비스
  1. CloudTrail vs Config
  CloudTrail: 누가 무슨 API를 호출했는지 행위를 기록
  Config: 그 행위의 결과로 리소스의 설정 상태가 어떻게 변했는지 기록

  2. Inspector vs Config
  Inspector: EC2 내부, 컨테이너, Lambda등의 취약점 주기적 자동 진단
  Config: 리소스의 설정 규칙 위반을 모니터링

  3. Trusted Advisor vs Config
  Trusted Advisor: AWS 모범 사례를 기반으로 한 종합적인 가이드(비용, 성능, 보안 등) 제공
  Config: 사용자가 정의한 맞춤형 컴플라이언스 규칙에 맞춰 커스텀 모니터링 가능

- 구체적인 문항 예시
  액세스 키가 60일이 지나면 자동으로 비활성화되는 기업 규정이 있음.
  규정에 맞지 않는 접근 키를 확인할 수 있는 AWS 서비스는?
  -> AWS Config의 핵심 기능 4가지 중 '규정 준수 평가' 영역에 해당함

- 4가지 핵심 기능별 문제 유형 예시
  - 규정 준수 평가: 60일이 지난 Access Key나, 퍼블릭으로 열린 S3 버킷처럼 회사 보안 정책을 위반한 리소스 식별
  - 자동 수정: 규정을 위반한 Access Key를 식별했을 때, 사람의 개입 없이 자동으로 비활성화하고 싶다
  - 설정 이력 기록: 특정 보안 그룹의 규칙이 과거 30일 동안 어떻게 변경되었는지 타임라인 변경 내역을 주적하고 싶다
  - 특정 EBS 볼륨이 삭제되기 전에 이 볼륨이 어떤 EC2 인스턴스에 연결되어 있었는지 연관관계를 확인하고 싶
   
---

# Shield Advanced가 보호하는 리소스
-> 먼저, Shield Advanced는 명백한 '리소스'에만 보호를 제공함
CloudFront, Elastic IPs(EC2), ALB/ELB, Route 53, Global Acceleratoro
(+ EC2는 직접적으로 보호되는 것이 아니라, Elastic IP 주소와 연관되어있는 경우에만 보호를 제공받음)

---

# Amazon EMR(Elastic MapReduce)
AWS에서 제공하는 클라우드형 대규모 빅데이터 처리 도구
Apache Spark, Hadoop, Presto, Hive 같은 대표적인 오픈소스 빅데이터 프레임워크를 클릭 몇 번으로 쉽게 구성해서 PB(페타바이트) 급 데이터를 분산 처리할 수 있게 해줌

- 출제 포인트
  Big Data Processing / Analytics
  Apache Spark, Hadoop, Presto, Hive (오픈소스 프레임워크 제품명이 지문에 대놓고 등장)
  Petabyte-scale (페타바이트 규모의 대용량 데이터)
  EC2 Cluster (여러 대의 EC2를 노드로 묶어 분산 처리)

- 유사 서비스 비교 (EMR vs Athena vs Redshift)
  Amazon EMR: 오픈소스 프레임워크 기반 빅데이터 분산 처리
  Amazon Athena: S3에 저장된 데이터를 SQL 문법으로 서버리스 분석
  (데이터베이스나 스토리지가 아니라, S3에 저장된 데이터를 직접 조회하는 서버리스 대화형 쿼리 서비스)
  Amazon Redshift: 페타바이트 급 데이터 웨어하우스, 데이터 분석도 제공

---

# AWS Developer Support plans의 계정 담당자 수 및 케이스 오픈 제한 규칙
지정된 1명의 담당자만 기술 지원 케이스 작성 & 문의
담당자는 1명으로 제한되지만, 그 1명이 오픈할 수 있는 문의 케이스의 개수는 무제한

+ All support plan 비교
  Basic: 담당자 제한 없지만 기술문의가 아닌 일반 문의만 가능
  Developer: 1명, 영업시간 내 이메일로 가능(12시간 이내 응답)
  Business: 담당자수 무제한, 24/7 이메일, 전화, 채팅(1시간 이내 응답)
  Enterprise: 담당자수 무제한, 24/7 이메일, 전화, 채팅(치명적 오류 시 15분 이내 응답), 지정 TAM 제

---

# AWS EventBridge
- 핵심 기능 3가지
  - 이벤트 버스
    서로 다른 어플리케이션이나 서비스들이 서로 직접 연결되지 않고도 중앙 이벤트 통로를 통해 데이터를 주고받게 만들어주는 이벤트 기반 아키텍처
  - 타사 SaaS 통합
    AWS 내부 서비스뿐만 아니라 외부 SaaS 어플리케이션의 이벤트도 코딩 없이 바로 받아서 AWS 서비스로 연결할 수 있음
  - 스케줄링(EventBridge Scheduler)
    Cron 표현식을 이용해 '매일 밤 12시', '매주 월요일 2시'같은 정기적인 작업을 예약 실행할 수 있음

- 출제 키워드
  Event-Driven Architecture
  Decouple applications(SQS, SNS와의 공통점)
  SaaS Integration
  Scheduled Rules / Cron

- Decoupling 관점에서 SNS, SQS와의 차이점
  - Amazon SQS(Queue 방식)
    버퍼를 통한 시간적 디커플링
    생산자가 메시지를 던져두면 소비자가 자기 속도에 맞춰 메시지를 가져옴 -> 소비자가 잠시 다운되어도 메시지는 안전하게 쌓여있음
  - Amazon SNS(Pub/Sub방식)
    Fan-out을 통한 1:N 디커플링
    하나의 이벤트 발생 시 이메일, SMS, Lambda, SQS 등 여러 수신처에 동시에 즉시 Push하여 전달
  - Amazon EventBridge(Event Bus 방식)
    컨텐츠 패턴 규칙 기반의 스마트 디커플링
    이벤트의 내용을 읽어서 조건에 따라 정교하게 라우팅해줌. AWS 서비스 및 타사와의 연동에 특화되어 있음

---

# 예약 인스턴스가 가능한 AWS 서비스

- Amazon EC2:
  가장 표준적인 RI 모델로, 가상 서버 용량을 미리 예약하고 최대 72~75%의 할인을 받음
  표준 RI와 사양 변경이 가능한 Convertible RI로 나뉨
- Amazon RDS:
  관계형 데이터베이스 인스턴스용 예약 요금제
  Reserved DB Instance라고 부르며, 24시간 계속 구동되는 DB 인프라 특성상 RI 사용시 할인 효과가 매우 큼
- Amazon DynamoDB:
  NoSQL(비관계형) 데이터베이스. 스키마가 엄격하지 않으며 Key-Value 모델과 Document 모델을 지원함
  읽기/쓰기 용량 단위에 대해 미리 예약하여 할인을 받는 Reserved Capacity 방식을 지원함
- Amazon ElastiCache/MemoryDB:
  Redis/Memcached 기반의 인메모리 캐시 및 데이터베이스 서비스
  Reserved Nodes 형태로 1년/3년 약정을 통해 노드 비용 할인을 받음
- Amazon Redshift:
  대규모 데이터 웨어하우스 서비스로 데이터 분석도 제공함
  Reserved Nodes 개념으로 노드 비용을 크게 절감할 수 있음
  
---

# AWS Organizations의 통합 결제 기능

- 4대 핵심 규칙
  1. 단일 결제 주체: 조직의 관리 계정이 모든 연결된 계정의 비용을 일괄 지불함
  2. 볼륨 할인 공유: AWS의 대부분의 리소스는 사용량이 늘어날수록 GB당 단가가 낮아지는데, 계정을 통합하면서 할인 구간이 상승하여 더 저렴한 단가로 서비스 이용이 가능함
  3. RI 및 Savings Plans 혜택 공유: 한 멤버 계정에서 구매한 RI나 Savings Plans를 해당 계정이 다 쓰지 못해 남는 경우, 조직 내 다른 멤버 계정의 온디맨드 사용량으로 할인이 자동으로 넘어감
  4. 무료 티어 합산: 무료 티어 혜택은 계정마다 적용되는 것이 아니라, 조직 전체를 통틀어 1개 계정 분량만 통합 합산되어 적용됨

- RI / Savings Plans 할인 공유 조건 및 주의사항
  1. 조건 일치 필수: 인스턴스 타입, 리전, AZ 등의 사양이 일치해야 할인이 공유됨
  2. 비활성화 옵션: 조직 관리자는 필요에 따라 특정 계정 간에 RI/Savings Plans 할인이 공유되지 않도록 비활성화할 수 있음

# AWS Storage Gateway
- 온프레미스와 AWS 클라우드 스토리지를 연결해주는 하이브리드 클라우드 스토리지 (서비스의 이름 그대로 스토리지를 이어주는 문/서비스)
- 온프레미스 서버의 로컬 캐시를 사용한다는 점이 핵심
- AWS에 모든 데이터를 보관하지만, 자주 사용하는 데이터는 온프레미스 장비의 로컬 캐시에 남겨두어 빠른 응답 속도 제공

- Storage Gateway의 3가지 핵심 세부 유형
  1. S3 File Gateway(파일 형태)
     - 연결 방식: NFS, SMB 표준 '파일' 프로토콜 사용
     - 작동: 온프레미스의 파일 데이터를 AWS S3의 객체 형태로 저장
     - 유스케이스: 온프레미스 앱이 기존 파일 시스템 방식 그대로 S3에 파일을 백업 및 저장하고 싶을 때
  2. Volume Gateway(블록 형태)
     - 연결 방식: iSCSI 블록 스토리지 프로토콜 사용
     - 작동: 온프레미스 서버에 가상 하드디스크처럼 붙여 쓰며(EBS와 비슷한 운영), 백업본은 EBS Snapshot으로 저장
     - 운영 모드(정반대의 두 개 방식)
       - Cached Volume: 전체 데이터는 S3에 두고, 자주 쓰는 데이터만 로컬 캐시에 보관
       - Stored Volume: 전체 데이터는 로컬에 보관하고, AWS에는 백업본만 비동기 복사
  3. Tape Gateway(테이프 백업 형태)
     - 연결 방식: iSCSI-VTL(가상 테이프 라이브러리)
     - 작동: 기존 온프레미스의 실물 물리 테이프 백업 시스템을 대체하여 S3 Glacier / Glacier Deep Archive에 장기 보관
    
- CLF-C02 시험용 정답 키워드
  - hybrid Cloud storage: 온프레미스와 AWS를 잇는 다리 역할(스토리지)
  - On-premises Local Cache: 클라우드로 전송되는 데이터의 로컬 읽기/쓰기 속도 향상
  - NFS / SMB / iSCSI: '기존 온프레미스 프로토콜을 수정 없이 그대로 사용'

# Legacy Third-party Database
- Legacy: 옛날에 만들어져서 오래된 구형 시스템/소프트웨어
- Third-party: AWS 자체 서비스가 아닌 제 3의 외부 전문 업체가 만든 소프트웨어
- 합친 의미: AWS에서 관리형 서비스로 공식 지원하지 않는 외부 업체의 오래되거나 특수한 데이터베이스

- Legacy Third-party Database를 운영할 수 있는 AWS 서비스 = EC2 인스턴스
  AWS RDS가 지원하지 않는 마이너하거나 오래된 레거시 DB는 AWS가 자동으로 설치해주거나 관리해 줄 수 없음
  따라서 사용자가 직접 빈 가상 서버(EC2)를 하나 임대한 뒤, OS 위에 해당 레거시 DB 설치 파일을 직접 올려서 운영하는 방법밖에 없음

- Amazon EC2의 3대 키워드
  1. Legacy / Custom / Unsupported Software (특수/오래된/미지원 소프트웨어)
     - 지문에 RDS나 DynamoDB 등 관리형 서비스에서 지원하지 않는 비표준 DB나 소프트웨어를 실행해야한다고 할 때
  2. Full OS Access / OS-level Control / Root Access (OS 제어권 필요)
     - OS 단에 직접 접속해서 제어해야하는 경우(RDS같은 완전 관리형 서비스는 OS에 대한 접근 권한이 주어지지 않음)
     - Amazon EC2가 IaaS(Infra as a Service)이기 때문에 가능함
  3. Install custom plugins or database engines (커스텀 플러그인 / 엔진 설치)
     - 관리형 DB 서비스가 제공하는 기본 설정 범위를 벗어나 직접 환경을 개조해야 할 때


# Amazon S3 + CloudFront
- Amazon S3(객체 스토리지 - 원본 저장소)
  - 대용량 비디오, 이미지, 문서 같은 정적 객체를 가장 저렴하고 안전하게 보관할 수 있는 글로벌 스토리지
- Amazon CloudFront(CDN/Content Delivery Network)
  - 전 세계에 배치된 Edge Location 네트워크를 이용해 S3에 있는 파일들을 캐싱해 두고, 전 세계 사용자에게 가장 낮은 지연 시간으로 쏘아주는 역할
 
-> Origin(Amazon S3) + CDN/Distribution(Amazon CloudFront) = 전 세계 빠른 정적 컨텐츠 배포

- EFS나 EBS는 정적 컨텐츠의 빠른 배포에 적합하지 않은 이유
 1. Amazon EFS(Elastic File System):
    - 리눅스 EC2 인스턴스 여러대에 동시에 마운트해서 사용하는 네트워크 공유 파일 시스템
    - CloudFront와 바로 연결 불가, 비용도 S3에 비해 매우 비쌈
   
 2. Amazon EBS(Elastic Block Storage):
    - 특정 EC2 인스턴스 1대에 직접 연결되는 단일 가상 하드디스크(HDD/SSD)
    - 전 세계에 멀티미디어 파일을 직접 서빙하는 용도로 사용되지 않음
   
# AWS CloudFront와 연동 가능한 주요 AWS 리소스/오리진
- Amazon S3 Bucket
  - 가장 대표적인 조합. 이미지, 비디오 파일 등 정적 웹 자산 저장 및 전송
- Application Load Balancer(ALB)
  - 동적 웹 어플리케이션 앞단에서 글로벌 캐싱 및 SSL/TLS 오프로딩 처리
- Amazon EC2 instance
  - 단일 EC2 웹 서버 퍼블릭 IP/DNS를 직접 오리진으로 지정하여 전송 속도 향상
- AWS Elemental MediaStore / MediaPackage
  - 비디오 스트리밍 및 라이브 방송 컨텐스 전송
- Amazon API Gateway
  - REST API / HTTP API 응답을 캐싱하고 전 세계 엣지에서 빠르게 응답
- AWS Lambda
  - 오리진은 아니지만, CloudFront 엣지 로케이션에서 코드를 직접 실행하여 요청/응답을 조작 및 커스텀 로직 처리 가능
+ AWS 외부에 있는 HTTP/HTTPS 웹 서버도 URL 주소만 입력하면 CloudFront CDN 적용 가능
+ Third-party Cloud Storage / Web Server에도 CloudFront 적용 가

# AWS 공동 책임 모델 구분법
- 클라우드 자체에 대한 관리/보안 -> AWS의 책임
- 클라우드 내부에 대한 관리/보안 -> customer/고객의 책임

- 헷갈리는 선지
  1. Account password policies (= IAM password polices)
     - 그냥 Account라고 언급하면, 고객이 소유한 AWS 계정 내의 사용자 비밀번호 정책임
     - 이는 클라우드 '자체'에 대한 관리/보안이라고 볼 수 없음 -> 따라서 고객의 책임
  2. Patching of storage systems
     - 스토리지 '시스템'을 패치하고 업데이트하는 것은 클라우드 '자체'에 대한 관리/보안임 -> 따라서 AWS의 책임
     - 주의: 만약 지문이 Patching of EC2 OS / Guest OS -> 이는 클라우드 내부에 대한 관리/보안이므로 고객의 책임
    
# AWS Web Application Firewall
- 웹 어플리케이션 계층(Layer 7)으로 들어오는 HTTP/HTTPS 악성 요청을 차단하는 방화벽
- 웹 요청의 '입구'역할을 하는 HTTP/HTTPS 엔드포인트 서비스들에 직접 연결되어 보호하는 기능

- AWS WAF를 적용할 수 있는 주요 서비스 목록
  - Application Load Balancer(ALB)
    - 이름에서 알 수 있듯, 어플리케이션 레이어(L7) 전용 로드 밸런서로, WAF를 연결하면 웹 트래픽이 EC2나 컨테이너로 전달되기 전 가장 앞단에서 악성 웹 트래픽을 미리 필터링할 수 있음
  - Amazon CloudFront
    - 글로벌 CDN(Content Delivery Network) 서비스의 엣지 로케이션 레벨에서 WAF를 적용할 수 있음
      악성 트래픽이 원본 서버(S3, ALB 등)까지 도달하지도 못하게 전 세계 엣지에서 사전에 차단하는데 매우 효과적
  - Amazon API Gateway
    - 백엔드 서버로 들어오는 API 요청을 보호하기 위해 연결. 악성 파라미터나 SQL Injection이 포함된 API 호출을 차단함
   
- 시험에 자주 나오는 WAF 특징(WAF vs Shield)
  - WAF(Layer 7 보호)
    - HTTP/HTTPS 요청 내용을 뜯어보고 SQL Injection, XSS, 특정 IP 차단, 봇 컨트롤 수행
  - AWS Shield(standard 기준 Layer 3/4 보호)
    - 볼륨형 대규모 DDoS 공격 차단 전용 서비스 (Shield Advanced 사용 시 WAF 기능이 일부 포함되어 Layer 7에 대한 보호도 가능해짐)
   
# Amazon API Gateway
- 개발자가 종류와 규모에 상관없이 API를 손쉽게 생성, 게시, 유지 관리, 모니터링 및 보안 처리할 수 있게 해주는 완전 관리형 API 프론트엔드 서비스
- 클라이언트(모바일 앱, 웹 브라우저 등)와 백엔드 서비스(AWS Lambda, EC2, DynamoDB 등) 사이에서 교통정리를 해주는 단일 진입점 역할을 함
- 핵심 기능
  1. 서비리스 지원: AWS Lambda와 결합하여 서버를 직접 관리하지 않고 완벽한 서버리스 아키텍처를 구축할 수 있음
  2. 트래픽 관리 및 제어: 갑작스러운 트래픽 폭주 시 Throttling(요청 제한) 및 Rate Limiting(초당 요청 수 제한)기능을 제공하여 백엔드 시스템이 과부하로 다운되는 것을 막아줌
  3. 캐싱: 자주 요청되는 API 응답을 자체 캐시에 저장해 두어 백엔드 호출 없이 빠르게 응답(지연 시간 감소 및 비용 절감)
  4. 보안 및 인증: API Key, AWS Cognito User Pool, IAM 권한 및 AWS WAF와 연동하여 무단 API 접근을 차단함

- 시험에 나오는 전형적인 정답 키워드
  1. Serverless API / AWS Lambda Integration
     - Lambda 함수와 연동하여 서버리스 API 엔드포인트를 노출하고 싶다
  2. API Management / Rate Limiting / Throttling
     - 백엔드 서버 보호를 위해 API 요청 수나 트래픽을 제어하고 관리해야 한다
  3. RESTful APIs & WebSocket APIs
     - 웹/모바일 어플리케이션을 위한 HTTP/REST 또는 실시간 양방향 통신 API를 구축한다
    
# Identity and Access Management(IAM)***
- 시험 대비 핵심 정리
  1. Root User vs IAM User
     - Root User: 계정을 생성할 때 만들어지는 최상위 사용자. 모드나 권한을 가짐
       - 시험 포인트: 일상적인 작업에 절대 사용하지 말고, 생성 직후 MFA 설정 + Root Access Key 삭제/미생성이 모범 사례
     - IAM User: 계정 내의 사람 또는 어플리케이션을 위한 개별 체제. 기본 권한은 Deny(모두 거부) 상태
  2. IAM Group vs IAM Role
     - IAM Group: 여러 사용자들의 집합체(중첩 불가, 자격 증명 없음, 계층 구조 형성 불가)
     - IAM role:
       - 임시 권한을 부여하는 핵심 매커니즘
       - 사용 주체: EC2 인스턴스, Lambda 함수 등 AWS 서비스가 다른 AWS 서비스에 접근할 때 또는 외부 연동 사용자가 접근할 때 사용
       - 시험 포인트: EC2에 Access Key를 하드코딩하지 않고 S3에 접근하게 하려면 -> IAM Role을 EC2에 연결
  3. IAM Policy(정책) & 최소 권한의 원칙
     - JSON 문서 형태: Effect, Action, Resource로 구성(Effect, Action은 필수 요소)
     - Principle of Least Privilege(최소 권한의 원칙):
       사용자나 서비스에게 업무에 딱 필요한 최소한의 권한만 부여해야 한다는 보안 대원칙
     - 명시적 거부 우선 법칙:
       Allow와 Deny가 충돌할 경우 Deny 우선 적용
  4. 자격 증명 방식(Credentials)
     - Console Password: AWS Management Console 웹 로그인용
     - Access Key ID & Serect Access Key: CLI(명령줄) 또는 SDK/API를 통합 접근용 -> 프로그래밍적 접근.(웹 콘솔 로그인용이 아님)
  5. Multi-Factor Authentication(MFA)
     - Password 입력 외에 추가 인증을 거치는 보안 레이어
     - 시험 포인트: Root User 및 모든 관리자 계정에 MFA 적용 필수
    
