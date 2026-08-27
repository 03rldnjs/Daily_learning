# AWS Config
AWS의 설정 상태를 지속적으로 기록하고, 변경 이력을 추적하며, 사전 정의된 규칙에 부합하는지 준수 여부를 평가하는 관리 서비스
-> AWS 리소스 상태 전용 cctv 및 감사관
- 핵심 기능
  - 설정 이력 기록: 특정 리소스가 시간에 따라 어떻게 변경되었는지 타임라인 형태로 기록함
  - 규정 준수 평가: S3, 보안 그룹 등에 대한 규칙을 정해두고, 이를 위반하면 위반 상태로 표시해 줌
  - 자동 수정: 위반 사항이 발견되면 Systems Manager Automation 등을 연결해 자동으로 설정을 올바르게 복구
  - 리소스간 관계 파악: 보안 그룹이 어떤 EC2 인스턴스나 EBS와 연결되어 있는지 등 리소스간의 연관관계를 시각적으로 보여줌

- 출제 포인트
  - Configuration History(설정 이력 추적)
  - Compliance Check(규정/정책 준수 평가)
  - Auditing/Change Management(감사 및 변경 관리)
  - Resource Relationships(리소스 간 관계 추적)

- 헷갈리기 쉬운 서비스
  1. CloudTrail vs Config
  - CloudTrail: 누가 무슨 API를 호출했는지 행위를 기록
  - Config: 그 행위의 결과로 리소스의 설정 상태가 어떻게 변했는지 기록

  2. Inspector vs Config
  - Inspector: EC2 내부, 컨테이너, Lambda등의 취약점 주기적 자동 진단
  - Config: 리소스의 설정 규칙 위반을 모니터링

  3. Trusted Advisor vs Config
  - Trusted Advisor: AWS 모범 사례를 기반으로 한 종합적인 가이드(비용, 성능, 보안 등) 제공
  - Config: 사용자가 정의한 맞춤형 컴플라이언스 규칙에 맞춰 커스텀 모니터링 가능

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
CloudFront, Elastic IPs(EC2), ALB/ELB, Route 53, Global Accelerator
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
    - 공식 정의: "Amazon SQS decouples application components so that they can <run independently>"
(Amazon SQS는 애플리케이션 구성 요소를 분리하여 독립적으로 실행될 수 있도록 합니다.)
    - 버퍼를 통한 시간적 디커플링
    - 생산자가 메시지를 던져두면 소비자가 자기 속도에 맞춰 메시지를 가져옴 -> 소비자가 잠시 다운되어도 메시지는 안전하게 쌓여있음
    - 수신 측이 복구된 후 원하는 시점에 꺼내어 처리하면 되므로 <Run Independently> 달성 / 수시ㅏㄴ측의 상태와 완전히 무관
      
  - Amazon SNS(Pub/Sub방식)
    - "Amazon SNS is a fully managed <pub/sub> messaging service for decoupling microservices, distributed systems, and serverless applications."
(Amazon SNS는 마이크로서비스 간 Pub/Sub 메시징을 통해 결합을 해제하는 서비스입니다.)
    - Fan-out을 통한 1:N 디커플링
    - 하나의 이벤트 발생 시 이메일, SMS, Lambda, SQS 등 여러 수신처에 동시에 즉시 Push하여 전달
    - 수신 측이 가동 상태여야 문제없이 기능 수행 가능
      
  - Amazon EventBridge(Event Bus 방식)
    - 컨텐츠 패턴 규칙 기반의 스마트 디커플링
    - 이벤트의 내용을 읽어서 조건에 따라 정교하게 라우팅해줌. AWS 서비스 및 타사와의 연동에 특화되어 있음

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
  3. Updating Operation System
     - Underlying 없이 단순히 Updating Operation System이라고만 적혀있으면 기본적으로 고객이 직접 관리하는 EC2(IaaS)의 Guest OS를 의미함. 관리형 서비스일 경우에만 AWS의 책임이므로 특정 유즈케이스가 제시된 것이 아니라면 고객의 책임으로 보는 것이 더 타당함
  4. Host / Physical 단어의 법칙
     - Host, Physical, Infrastructure, Data Center 같은 단어가 포함되어 있다면 고객이 물리적으로 접근할 수 없는 영역이므로 100% AWS의 책임임(Host는 자주 등장하지 않지만 나오면 치명적일 수 있으므로 꼭 기억하기)
  + Virtualization Layer = 하이퍼바이저 및 관련 관리 소프트웨어 계층(순수 인프라 영역) -> 전적으로 AWS의 책임
    
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
    
# Identity and Access Management(IAM)*** - 출제 가능성 매우 높음
- 기본 통제 단위: 단일 계정 내부(해당 IAM이 존재하는 그 계정 안에서만 권한을 제어함), 다른 멤버 계정들이 존재하는 사용자나 역할의 API 접근 제한을 중앙에서 일괄 제어하는 통제는 Organizations의 역할
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
+ IAM 헷갈리는 개념
  - IAM Role을 IAM Group에 부여/연결(Attach) -> 기술적으로 불가능
  - IAM Policy(정책)을 IAM Group이나 IAM User에게 연결 -> 이건 가능
  - IAM Role을 EC2, Lambda 등 서비스나 사용자에게 위임하는 것 -> 이것도 가능

+ IAM 주요 함정 패턴
  1. EC2에서 S3에 접근할 때 Access Key를 저장/하드코딩한다(X)
     - Access Key를 저장하거나 하드코딩하는 행위는 심각한 보안상의 문제를 초래할 수 있음
     -> IAM Role을 생성하여 EC2 인스턴스에 연결해야 함
  2. IAM은 리전별로 생성해야 한다(X)
     - IAM은 글로벌 서비스이므로 글로벌 단위로 관리됨 -> 리전별로 생성할 필요 없음
  3. IAM Group에 다른 Group을 중첩시키거나 Role을 할당한다(X)
     - 그룹 중첩은 불가능, Role은 Group에 붙일 수 없음(Policy만 Group에 Attach 가능)
  4. 웹 콘솔 로그인을 위해 Access Key를 사용한다(X)
     - ACcess Key는 프로그래밍적 접근(CLI, SDK, API) 접근 전용, 콘솔 로그인은 비밀번호 + MFA를 사용
  5. 고객 관리형 정책 대신 인라인 정책을 사용해라
     - 인라인 정책은 권한 수정 시 사용자마다 일일이 찾아가서 수정해야 함. 이렇게 되면 상당한 관리 부담이 생김. AWS는 재사용이 가능한 Managed policy 사용을 강력히 권장

+ 빈출 키워드 매칭
  - Least Privilege (최소 권한의 원칙)
    -> 업무에 필요한 최소한의 권한만 IAM Policy로 부여
  - Temporary Credentials (임시 자격 증명)
    -> IAM Role
  - Cross-Account Access (타 계정 접근 권한 부여)
    -> IAM Role을 활용해 다른 AWS 계정에 안전하게 접근
  - Root User Security (루트 사용자 보안)
    -> MFA 활성화 + Access Key 삭제 + 일상적 사용 X
  - Explicit Deny (명시적 거부)
    -> Allow 정책과 Deny가 충돌하는 경우 Deny 우선
  - Federated Identity / SSO
    -> 기존 기업 계정과 연동하여 IAM Role 할당
  - Create Individual IAM Users
    -> 계정 하나를 여러 사람이 공유하지 말고, 사람마다 개인 ID를 하나씩 생성, 그래야 누가 서비스에서 무슨 활동을 했는지 개별 추적할 수 있음
  - Use groups to assign permissions to IAM users
    -> 사용자 개개인에게 일일히 권한을 부여하지 말고, 그룹을 만들어 권한을 붙인 뒤 사용자를 그 그룹에 넣음

-> 사람마다 개인 ID(Individual IAM Users)를 만들어주고, 권한은 그룹(Group)으로 묶어서 주는 것이 IAM의 핵심

# AWS Data Exchange
- AWS 클라우드용 외부 데이터 마켓 플레이스
- 기업이 비즈니스 분석이나 인공지능 학습에 필요한 외부 3rd-party 데이터를 AWS 콘솔 내에서 손쉽게 검색하고, 구매/구독하여 곧바로 S3나 Redshift로 가져올 수 있게 해주는 데이터 거래 플랫폼
- AWS Marketplace처럼 거래 플랫폼의 형태이지만, 거래 대상이 완전히 다름
  - AWS Marketplace: 3rd-party 소프트웨어, 라이선스, SaaS, AMI를 사고파는 곳
  - AWS Data Exchange: 3rd-party 순수 데이터세트를 사고파는 곳(ex. 금융 주가 데이터, 기상 정보, 인구 통계 데이터 등)
- 키워드: Find and subsciribe to third-party data, Exchange or sell datasets in AWS Cloud

# AWS Software Development Kit(SDK)
- 개발자가 자기가 작성하는 프로그래밍 언어의 코드 안에서 AWS 서비스를 제어할 수 있게 해주는 라이브러리/도구 모음
- AWS 상호작용 3대 접근 방식 비교
  1. AWS Management Console
    - 방식: Web GUI 화면
    - 대상: 일반 사용자 / 초보자
    - 인증: ID + Password(+ MFA)
  2. AWS CLI(Command Line Interface)
    - 방식: 터미널/커맨드 라인(명령어)
    - 대상: 시스템 관리자
    - 인증: Access Key + Secret Access Key
  3. AWS SDK(Software Development Kit)
    - 방식: 소스 코드 라이브러리
    - 대상: 어플리케이션 개발자
    - 인증: Access Key + Secret Access Key(또는 IAM Role)
 
# AWS Elastic Load Balancer(ELB)
- 어플리케이션으로 들어오는 트래픽을 여러 대상(EC2, 컨테이너, IP 주소 등)으로 자동으로 분산해주는 서비스
- 서버의 부하를 줄여주고, 특정 서버가 고장나더라도 정상적인 서버로만 트래픽을 보내 서비스가 중단되지 않도록 만드는 고가용성(High Availability)의 핵심
- ELB의 핵심 특징
  1. 자동 확장성
     - 트래픽이 급증하거나 급감해도 ELB 자체가 알아서 성능을 늘리거나 줄임
  2. 헬스 체크
     - 연결된 EC2 인스턴스들이 정상 동작 중인지 주기적으로 상태를 점검함
     - 비정상 상태인 인스턴스가 발생하면 트래픽 전달을 즉시 중단하고 정상 인스턴스로만 전달함
  3. 단일 리전 / 멀티 AZ 단위 서비스
     - 1개의 ELB는 동일 리전 내 여러 AZ에 나뉘어 있는 EC2에 트래픽을 분산할 수 있음(단, 타 리전은 불가)
  4. 보안 통합
     - SSL/TLS 암호화 certificates(증명서)를 ELB 단에서 처리해 개별 EC2의 암호화 부담을 줄여주는 SSL Offloading 기능을 제공함
      
- ELB의 4가지 유형
  1. Application Load Balancer
     - Layer 7(HTTP/HTTPS)
     - 웹 기반 어플리케이션 특화, URL 경로 기반 및 호스트 기반 라우팅, 컨테이너(ECS) 연동
     - HTTP/HTTPS, Path-based routing, Web application
  2. Network Load Balancer
     - Layer 4 (TCP/UDP)
     - 초고성능/극초저지연, 초당 수백만건의 트래픽 처리, 고정 IP 제공
     - Ultra-low latency, High performance, TCP/UDP, Static IP needed
  3. Gateway Load Balancer
     - Layer 3
     - 타사 방화벽 및 침입 탐지 등의 가상 네트워크 어플라이언스를 배포/관리할 때 사용
     - Third-party virtual appliances, Firewall inspection
  4. Classic Load Balancer
     - Layer 4/7
     - 구형 로드밸런서(시험에서는 이전 세대 키워드로만 언급되며 새로 사용하는 것은 비권장)
    
# AWS Outposts
- 온프레미스 환경에 AWS의 물리적 렉 서버 하드웨어를 직접 설치하여 사용하는 하이브리드 클라우드 서비스
- 온프레미스 물리 공간에 설치되지만, 서버 운영, 관리, 패치 등은 AWS가 알아서 처리하며, 기존 AWS Cloud 콘솔 및 API와 100% 동일한 방식으로 사용할 수 있음
- 사용 목적:
  - 극초저지연: 온프레미스 장비나 공장 설비 바로 옆에서 데이터 처리 필요시
  - 데이터 로컬 처리 및 규제: 법적/규제상의 이유로 데이터를 반드시 자체 데이터센터에 보관해야 할 때
- 주요 특징:
  - AWS 물리 하드웨어가 내 데이터 센터로 들어오는 구조이지만, 서비스의 기본 정체성은 '내 데이터 센터로 확장된 AWS 리전의 일부'로 동작
 - 주요 키워드:
   - Hybrid Cloud + On-premises data center + AWS Infrastructure
   - Ultra-low latency to local systems
   - Run AWS services on-premises
   - Extend VPC to on-premises(Connect와 Extend가 전혀 다름, Connect는 AWS Direct Connect나 AWS site-to-site VPN이, Extend는 Outposts가 담당함)

# Amazon MSK(Managed Streaming for Apache Kafka) - 출제 가능성 낮음, 알아만 두기
- 약자 그대로 AWS가 알아서 서버를 관리해주는 Apache Kafka 서비스
- 기존에 오픈소스 Apache Kafka로 작성된 어플리케이션 코드를 전혀 수정하지 않고 그대로 가져와 쓸 수 있도록, AWS가 Kafka 클러스터의 생성, 패치, 유지 보수를 완전히 대신해주는 서비스
- 비교 (Amazon Kinesis vs Amazon MSK)
  - Amazon Kinesis: AWS의 자체(Native) 실시간 스트리밍 데이터 처리 서비스
    - AWS 전용 API와 SDK를 사용해서 개발해야 함. Apache Kafka 기반으로 작성된 오픈소스 코드나 생태계에 대한 직접적인 호환성은 없음
  - Amazon MSK: 오픈소스 Apache Kafka 기반의 실시간 스트리밍 데이터 처리 서비스
    - 오픈소스 Apache Kafka를 쓰건 기업이 코드 수정 없이 AWS 클라우드로 그대로 옮겨와 사용할 수 있음
- 키워드: Apache Kafka + Managed Service / Avoid infrastructure overhead

# AWS Developer Tools
- 개발자가 코드를 저장하고, 빌드하고, 서버에 배포하고, 전체 과정을 자동화하는 CI/CD(지속적 통합/지속적 배포) 흐름을 담당함
- CodeCommit -> CodeBuilt -> CodeDeploy -> CodePipeline
1. CodeCommit
   - 코드 저장소(AWS판 GitHub/Git)
   - 키워드: Source control, Version control system, Git repository, Code stroage
2. CodeBuild
   - 코드 컴파일 & 검수 (빌드 및 테스트)
   - 키워드: Compile source code, Run tests, Produces build artifacts
3. CodeDeploy
   - 서버 배포 도구(EC2, Lambda 등에 배포)
   - 키워드: Automate code deployment, Deploy to EC2/Lambda/On-premises
4. CodePipeline
   - 전체 파이프라인 관리자(CI/CD 자동화)
   - 키워드: Workflow automation, CI/CD pipeline, Orchestrate build, test and deploy

- 코드 작성 및 저장(CodeCommit) -> 코드 빌드(실행) 및 검수(CodeBuild) -> 코드 배포(CodeDeploy)
- 전체 워크플로우 하나로 묶어 자동화(CodePipeline)
- CodePipeline 자체는 코드를 저장하거나 빌드/배포를 직접 수행하는 주체가 아니라, 각 단계들의 연결 및 흐름을 제어하는 역할만 수행함


# Amazon RDS Custom
- Amazon RDS는 AWS가 제공하는 완전 관리형 관계형 데이터베이스로, 완전 관리형이라 OS에 대한 Root/SSH 접근 권한을 제공하지 않지만, OS 루트 권한이나 사용자 지정 OS 패치가 필수적인 특정 기업 환경을 위해 RDS Custom을 만들었음
- 밀리초 수준의 충분히 빠른 응답 속도를 제공하지만, 밀리초 미만 단위의 속도를 제공하지는 못함
  (+ 밀리초 미만 단위의 속도를 제공하는 기술은 In-Memeory 스토리지임)
- 관리형 서비스이지만, OS root Access가 가능함
- 일반 RDS -> OS 접근 불가 / OS 접근이 필요한 경우 = EC2 or RDS Custom

# 보안 그룹(Security Group)과 NetworkACL에 대한 보안 책임
- AWS의 책임: VPC, subnet, NetworkACL, Security Group이라는 방화벽 기능과 네트워크 인프라 틀 자체를 만들고 제공
- 고객 책임: AWS가 만들어둔 방화벽의 규칙을 어떻게 설정하고 업데이트할지 결정
-> Configuring ~ (설정하기), Updating rules ~ (규칙 업데이트하기)처럼 설정 작업이 들어가면 무조건 고객의 책임
-> 즉, AWS는 인프라 틀 자체만 제공하고, 설정하고 업데이트 등의 관리 책임은 전적으로 고객에게 있음
+ 선지에 Underlying이 적혀있으면 고민없이 AWS의 책임이라고 생각하면 됨

# JSON 정책 문서의 5대 구성 요소 - 출제 가능성 낮음
- Principal(누구에게, 사람/주체)
  - 권한을 부여받거나 거부당하는 주체(IAM User, Role, AWS Account, Service)를 지정
- Effect(허용/거부)
  - Allow 또는 Deny로 권한 행사 여부 결정
- Action (무엇을 할 수 있는가)
  - 허용하거나 거부할 작업 명시
- Resource(어느 대상에, 물건/대상)
  - 작업이 적용될 대상 AWS 리소스 ARN을 명시
- Condition(어떤 조건에서)
  - MFA 인증 여부, 특정 IP 대역 등의 제약 조건 지정
[Principal]이 [Resource]에 대해 [Action]을 수행하는 것을 [Effect]한다

+ IAM Identity Policy와 다른 점
IAM User나 Role에 직접 붙이는 아이덴티티 정책(Identity-based Policy)은 '누구에게' 적용되는지 이미 결정되어 있어서 Principal 요소가 필요 없음. 반면 S3 Bucket Policy처럼 리소스 쪽에 붙이는 리소스 기반 정책(Resource-based Policy)은 외부의 '누가' 접근하는지 명시해야 하므로 Principal이 필수임.

+ Principal vs Resource
- Principal 키워드:
  - User, Account, Role, Group, Who is granted access, Identity
- Resource 키워드:
  - S3 Bucket, ARN (Amazon Resource Name), Target, Database table

# AWS Elastic Beanstalk가 compute 서비스인 이유
- 컴퓨팅 환경을 자동으로 배포하고 관리해주는 컴퓨팅 전용 PaaS 서비스
- 본질은 'EC2 기반 프로비저닝'
  - Beanstalk는 새로운 별개의 시스템을 만드는 것이 아니라, 앱 코드를 실행할 EC2 인스턴스, ALB, Auto Scaling Group을 대신 구축해주는 서비스임
- OS 및 연산 자원 실행
  - 결국 코드가 실제로 작동하고 연산이 일어나는 공간이 EC2(AWS의 대표적 compute 서비스) 기반 환경이므로 AWS에서 공식적으로 Compute 카테고리로 분류함

# AWS Batch
- 수천~수십만 개의 Batch 작업을 효율적으로 실행할 수 있도록 컴퓨팅 자원을 자동으로 스케줄링하고 배포해 주는 서비스
- Batch = 일괄 처리 작업 (ex. 매일 밤 12시에 대용량 데이터 1000만 건을 분석하라)
- 작동 방식
  - 개발자가 연산 작업을 제출하면, Batch가 알아서 필요한 만큼의 EC2 인스턴스나 Spot 인스턴스를 띄워 연산(Compute)을 수행하고 작업이 끝나면 인스턴스를 자동으로 종료함
- 시험 키워드: Batch computing, Run hundreds of thousands of batch jobs, Dynamically provisions compute resources

# CLF-C02 필수 Compute 서비스
- AWS에서 'Compute'카테고리는 가상 서버, 컨테이너, 서버리스 코드 등 사용자의 어플리케이션/연산 코드를 실행해주는 서비스들을 모두 포함함
1. Amazon EC2: 가장 기본적인 가상 서버(IaaS)
2. AWS Lambda: 서버 관리 없이 코드만 실행하는 서버리스
3. 컨테이너 기반 컴퓨팅: Amazon ECS, Amazon EKS, AWS Fargate 
4. AWS Elastic Beanstalk: 코드를 올리면 EC2/ALB 등을 자동 구축해 주는 웹 앱 배포 도구(PaaS)
5. AWS Batch: 대규모 일괄 처리 '연산' 작업을 위한 자동 컴퓨팅 스케줄러

# Trusted Advisor의 5대 핵심 점검 영역
Cost Optimization (비용 최적화): 사용률이 낮은 EC2 인스턴스 탐지
Performance (성능): EBS 성능 병목 탐지
Security (보안): S3 버킷의 공공 열람 권한, MFA 미설정 탐지
Fault Tolerance (결함 허용): Multi-AZ 미적용, 백업 부재 탐지
Service Limits (서비스 제한):
현재 사용 중인 리소스가 AWS 기본 제한 한도(Limit)의 80% 이상에 도달했는지 실시간 모니터링해 줌 
(ex. 80%에 도달하면 경고를 띄워 한도 증가 요청을 하라고 알려줌)

# Amazon ElastiCache
- 일반 DB가 서재 책상에 책을 보관하는 것이라면, ElastiCache는 책상 위에 자주 읽는 책을 꺼내두는 것(RAM 메모리 저장)과 같음. Disk 기반의 DB보다 검색 속도가 월등히 빠름
- 지원 엔진: Redis 및 Memcached
- 주요 사용 목적:
  1. 데이터베이스 부하 감소: 자주 조회되는 Query 결과를 메모리에 저장하여 데이터베이스의 부담을 완화
  2. 읽기 성능 극대화: 캐시 메모리로 저장하여 초고속 응답 속도 제공
  3. 세션 관리: 웹 어플리케이션 로그인 세션 정보 저장
- 주요 출제 키워드
  - In-memory cache / In-memory data store
  - Redis / Memcached
  - Improve database read performance (DB 읽기 성능 향상)
  - Sub-millisecond latency (초저지연 응답)
 
# AWS Management Console
- AWS 클라우드의 모든 서비스를 시각적으로 관리하고 제어(리소스 배포/생성도 가능)할 수 있는 웹 기반 GUI(Graphical User Interface)
  
- 자주 출제되는 핵심 특징
  - 모바일 앱 지원: AWS Console Mobile Application을 제공하여 이동 중에도 리소스 상태 모니터링 및 알람 확인 가능
  - AWS CloudShell 통합: 브라우저 내 콘솔 화면에서 별도 설치 없이 바로 터미널을 열어 CLI 명령어를 실행할 수 있는 CloudShell 환경 제공
  - 모든 웹 브라우저 지원: 별도의 소프트웨어 설치 없이 웹 브라우저만 있으면 접속 가능
    
- 주요 출제 키워드
  - Web-based user interface / GUI
  - Access via Username and Password
    
+ 주요 함정
  - Console에 접속하기 위해 Access Key를 사용한다 -> X
    - Access Key는 CLI/SDK(프로그래밍적 접근)를 위한 것이지 Console 웹 로그인을 위한 용도가 아님
  - 개발자가 앱 코드 내에서 S3에 파일을 올리기 위해 Console을 사용한다 -> X
    - 코드 내부 연동은 AWS SDK의 역할(애초에 코드와 관련된 언급이 있으면 Console이 아니라고 생각하면 됨)
  - 반복적이 관리 작업을 자동화 스크립트로 만들 때 Console을 사용한다 -> X
    - 스크립트 자동화는 AWS CLI의 역할
   
# Amazon Athena
- Amazon S3에 저장된 데이터를 서버를 띄우지 않고 표준 SQL문으로 즉시 조회/분석할 수 있게 해주는 서버리스 서비스
  
- 핵심 기능
  - 보통 S3에 있는 파일 데이터를 분석하려면 DB나 데이터 웨어하우스로 옮기는 작업이 필요하지만, Athena는 S3에 있는 파일 그 자체에 쿼리를 날릴 수 있음
    
- 특징
  - 서버리스: DB 인스턴스를 관리하거나 인프라를 프로비저닝할 필요가 전혀 없음
  - Pay-per-query: 실행한 SQL 쿼리가 스캔한 데이터 용량만큼만 비용을 지불함
    
- 주요 출제 키워드
  - Analyze Data directly in Amazon S3 using standard SQL(S3 데이터를 표준 SQL로 직접 분석)
  - Serverless query service (서버리스 쿼리 서비스)
  - No infrastructure to manage / pay per query (쿼리당 과금)

# AWS Glue
- 다양한 출처의 데이터를 통합, 정리, 변환하여 분석 및 데이터 웨어하우스로 전송해주는 완전 관리형 서버리스 ETL(Extract, Transform, Load) 서비스

- ETL(Extract, Transform, Load)
  - Extract(추출): 여러 장소(S3, RDS, DynamoDB 등)에서 원시 데이터를 가져옴
  - Transform(변환): 쓸모없는 데이터를 잘라내고 분석하기 적합한 형태로 가공
  - Load(적재): 분석용 DB(Amazon Redshift, S3 등)로 정돈된 데이터를 밀어 넣음
    
- 핵심 기능
  - Glue Data Catalog: 데이터의 메타데이터를 한 곳에 저장하는 Central Repository 역할 수행
  - Crawler(크롤러): S3나 DB를 자동으로 훑어보고 데이터 구조를 파악해 Data Catalog 테이블을 자동 생성해 줌
  - Serverless: 인프라 관리가 필요 없으며, ETL 작업이 실행될 때 사용한 컴퓨팅 자원에 대해서만 과금됨
  
- 주요 출제 키워드
  - ETL(Extract, Transform, Load) service
  - Serverless data integration service
  - Prepare and transform data for analytics(분석을 위한 데이터 준비 및 변환)
  - Data Catalog / Discover and catalog metadata
  
- Glue vs Athena vs Redshift
  1. AWS Glue: 데이터를 가져와 변환하고 정돈하는 'ETL' 도구(Data Catalog 관리)
  2. Amazon Athena: S3에 저장된 데이터에 대고 즉시 SQL 쿼리를 날려 분석하는 도구(별도의 수정 작업 불필요)
  3. Amazon Redshift: 대규모 복합 데이터 분석을 위해 데이터를 저장하는 데이터 웨어하우스
-> ETL이 보이거나 데이터 변환/통합(Transfer/Integrate) 얘기가 나오면 Glue를 선택

# AWS Billing and Cost Management vs AWS Billing Conductor - 출제 가능성 낮음
1. AWS Billing and Cost Management
   - 역할: 청구서 확인, 결제 수단 관리, 비용 분석, 예산 설정 등의 메뉴로 들어가는 중앙 통합 콘솔
   - 특징: AWS가 실제로 청구하는 원래 가격을 기반으로 단순 모니터링 및 결제 처리
   
2. AWS Billing Conductor
   - 역할: 여러 AWS 계정을 그룹화하여, 자체적인 내부 정산 로직이나 내부 마진/할인율을 적용한 맞춤형 청구서를 따로 만들어 줌
   - 비유: AWS에서 받은 원본 영수증을 가져와서, 회사 내부 부서별 정산 규칙에 맞게 내부용 맞춤 영수증으로 다시 출력해주는 계산기

-> AWS 기본 영수증 확인은 Billing & Cost management, 내부 정산용 맞춤 영수증 재발급은 Billing conductor

# AWS Snowball & Snowball Edge
- AWS Snowball: 대용량 데이터베이스를 이전할 때, 이전하려는 데이터베이스가 격오지에 위치하거나, 대용량 데이터를 인터넷으로 전송하기에는 네트워크 트래픽이 너무 느리거나 불안정한 경우, AWS가 자체 하드웨어를 배송하여 해당 하드웨어를 통해 오프라인으로 안전하게 데이터베이스를 이전하도록하는 하드웨어 마이그레이션 서비스.

- AWS Snow Family
- 물리 데이터 전송 장비 라인업
  1. AWS Snowcone
     - 용량/크기: 약 8TB
     - 용도: 소규모 데이터 이동 및 공간이 제한된 환경
  2. AWS Snowball(기본/Edge)
     - 용량/크기: 50TB ~ 210TB
     - 종류:
       - Storage Optimized: 순수 데이터 대용량 이동에 최적화
       - Compute Optimized: EC2/Lambda 등을 장비 자체에서 실행하는 엣지 컴퓨팅 탑재
  3. AWS Snowmobile
     - 용량/크기: 최대 100PB
     - 용도: 데이터 센터 전체를 이전하는 초대형 프로젝트

- Snowball의 주요 특징 및 보안
  - 강력한 내구성: 충격, 먼지, 방수 기능이 완비된 특수 케이스로 제작되어 어떠한 거친 환경에서도 견딤
  - 자동 암호화: 장비에 저장되는 모든 데이터는 KMS 256비트 암호화 키로 자동 암호화됨
  - E-Ink 배송 라벨: 장비 표면에 전자식 배송 라벨이 달려 있어서, 데이터 복사가 완료되면 택배 주소가 자동으로 AWS 데이터 센터 목적지로 변경됨
 
- Snowball Edge
  - 그냥 Snowball처럼 단순히 파일만 담는 장비가 아니라, 데이터 센터나 통신이 잘 안터지는 오지에서 장비 자체적으로 컴퓨팅 연산을 수행할 수 있게 만들어짐
  - EC2 지원: 장비 내부에 Amazon EC2 AMI 및 AWS Lambda 기능을 기본 탑재하고 있음. 따라서 인터넷이 없는 상태에서도 장비 안에서 직접 가상 서버를 띄워 데이터를 실시간 처리/분석할 수 있음
 
-> Snowball Standard: 오직 데이터 전송/이동, Snowball Edge: 데이터 전송 + 현장 연산 처리(EC2 & Lambda 지원)

# AWS Budgets
- 핵심 역할: 예산 설정 및 경고 알림(임계치 도달시 알림/액션 실행)
- AWS Budgets의 4가지 유형
  1. Cost Budget(비용 예산): 추적 대상액을 정해놓고 비용 모니터링
  2. Usage Budget(사용량 예산): EC2 작동 시간이나 Data Transfer 용량 등 사용량 모니터링
  3. RI / Savings Plans Utilization Budget(사용률 예산): 내가 구매한 예약 인스턴스/Savings Plans를 목표치만큼 충분히 활용하고 있는지 모니터링(목표치 아래로 떨어지면 알림)
  4. RI / Savings Plans Coverage Budget(보장 범위 예산): 전체 EC2 작업 중 할인 혜택을 받고 있는 비중이 얼마나 되는지 모니터링
 
- 알림 기준: 실제값 vs 예측값
  - 실제값(Actual): 이미 발생한 비용이 설정한 임계치에 도달했을 때 알림
  - 예측값(Forecasted): 현재 사용 추세대로 가면 월말에 설정한 임계치를 초과할 것으로 예상될 때 사전에 알림

- AWS Budgets Actions (자동화 조치)
  - 기본 동작: 이메일 전달 또는 Amazon SNS를 통한 알림 전송
  - Budgets Actions 기능: 예산 초과 시 미리 설정한 액션을 자동 실행하거나 승인 후 실행 가능
    - 특정 IAM 정책/SCP 적용(ex. 새로운 EC2 생성 권한 차단)
    - 특정 EC2 또는 RDS 인스턴스 자동 중지
   
+ AWS Budgets vs AWS Service Quotas (알림 vs 제한)
  - AWS Budgets
    - 기능: 예산 설정 및 경고
    - 특징: 임계치 도달 시 알림/액션 실행
    - 대표 키워드: Set target, Alert, Threshold
      
  - AWS Service Quotas
    - 리소스 생성 최대 한도 관리/제한
    - 계정당 EC2 갯수 제한 등 물리적 한도 설정
    - Limits, Quota increase request

# AWS Secrets Manager
- '애플리케이션이 사용하는 DB 암호'나 'API 키' 등 시스템 자격 증명을 코드 하드코딩 없이 안전하게 저장하고 자동으로 교체(Rotation)해 주는 서비스
- 주요 관리 대상:
  - Database Credentials (RDS/Aurora등의 DB 접속 아이디 및 비밀번호)
  - API Keys (외부 결제 모듈, 외부 서비스 연동용 API 키)
- 핵심 기능
  - 소프트웨어 개발 시 코드 안에 DB 비밀번호를 하드코딩하지 않고, 코드(SDK)가 실행될 때 Secrets Manager에서 비밀번호를 안전하게 가져와 접속하게 만듦

+ 주의 사항
  - Management Console은 Secrets Manager의 적용 대상이 아님
    - 사람이 AWS Management Console에 로그인할 때 사용하는 계정 정보(IAM/Root Password)는 IAM 영역에서 통합 관리됨
    - 따라서 Management Console은 IAM Password Policy와 AWS MFA에 의해 보안을 유지함

- 키워드 요약
- Database credentials / API Keys / Automatic Rotation / Avoid hardcoding in app code
-> AWS Secrets Manager

- Console Login Security / IAM Password complexity / Multi-Factor Authentication
-> Strong Password Policies & AWS MFA

+ 프로그래밍적 접근의 기본 자격 증명과 Secrets Manager의 역할 분담
  - 사람의 콘솔 접근 보안: IAM Password Policy(강력한 비밀번호 정책) + MFA
  - 사람/시스템의 프로그래밍적(CLI,SDK) 접근 보안: IAM Access Key / Secret Access Key(또는 IAM Role)
  - 어플리케이션이 외부 시스템에 접근할 때의 보안: AWS Secrets Manager(DB 비밀번호, API 등을 하드코딩하지 않고 안전하게 로테이션하며 불러옴)
 
-> 프로그래밍적 AWS 접근 자체는 IAM Access Key/Role이 담당하고, 그 코드 내부에서 쓰는 DB 암호나 외부 API 키를 안전하게 관리하는 게 Secrets Manager

# Amazon Simple Email Service(SES)
- 개념: 마케터나 개발자가 고객에게 대규모 이메일을 안전하고 신뢰성있게 발송하기 위한 전용 이메일 플랫폼 서비스
- 주요 용도
  - Transactional Emails: 주문 확인서, 비밀번호 재설정, 결제 영수증 등 사용자 행동에 따라 1:1로 자동 발송되는 이메일
  + 주문 확인서, 비밀번호 재설정, 결제 영수증 등에 Transactional이라는 이름이 붙은 이유
    -> Transactional의 2가지 의미
      - 비즈니스/금융적 의미: 돈을 송금하거나 제품을 구매하는 1:1 거래를 의미
      - 컴퓨터 공학적 의미: 원인이 발생하면 그에 따른 결과가 한 세트로 확실하게 처리되어야하는 일련의 작업
      - 원인-결과 1:1 매칭: 사용자가 버튼을 누르거나 주문을 하는 등 특정 행동(Trigger Event)을 일으켰을 때만 1:1로 즉각 응답해서 발송되는 메일
  - Marketing Emails: 뉴스레터, 프로모션 행사 메일 등 대량 발송

- Amazon SES vs Amazon SNS
  - Amazon SES: 이메일 전용 서비스. 주문 확인서나 비밀번호 재설정 링크처럼 복잡하고 규격화된 메일을 높은 도달률(스팸함으로 빠지지 않게)로 보내는데 최적화되어 있음
  - Amazon SNS: Pub/Sub(발행/구독) 기반의 알림 서비스. SNS도 이메일을 보낼 수는 있지만, 주로 짧은 경고 메시지, SMS(문자), Moblie Push 알림을 보낼 때 사용. 시스템 경고나 간단한 텍스트 알림을 여러 구독자에게 뿌리는 용도이지, 예쁘고 복잡한 템플릿의 이메일 전송 도구가 아님
 
# AWS Activate for Startups - 출제 가능성 낮음
- 기술 스타트업 기업이 AWS 위에서 빠르게 비즈니스를 시작하고 성장할 수 있도록 돕는 스타트업 전용 지원 프로그램
- 주요 혜택
  - AWS Promotional Credits: 인프라 비용 부담을 줄여주기 위해 무료로 사용할 수 있는 크레딧 제공
  - Technical Support: AWS Developer/Business Support 플랜 무료 이용 혜택
  - Training & Resource: 전문가 1:1 상담, 교육 자원 및 멘토링 프로그램 제공

# Service Control Policy(SCP)
- '조직' 내 여러 AWS 계정들이 사용할 수 있는 최대 권한의 한계선을 설정하는 정책
- 적용 대상: 개별 IAM 사용자나 그룹이 아니라, 'AWS Organizations' 단에서 조직 전체, 조직 단위, 또는 특정 AWS 계정에 연결되어 작동
- 시험에 나오는 'SCP = AWS Organizations' 출제 패턴 3개
  - SCP가 무엇과 연결되는가?
    ➔ 정답: AWS Organizations (Root, OU, Member Account)
  - 여러 AWS 계정(Multi-account)의 "최대 권한 한계(Maximum permissions)"를 설정/제한하고 싶다.
    ➔ 정답: SCP (Service Control Policy)
  - 계정의 루트 사용자(Root user)조차도 무시할 수 없는 가드레일(Deny 정책)을 치고 싶다.
    ➔ 정답: SCP

-> SCP가 보이면 걍 Organizations를 찾으면 됨
-> Member Account나 Multi-account + 계정 간 통제 = AWS Organizations & SCP

# Amazon S3
- 객체 스토리지로서 무제한 용량과 99.9999999의 내구성을 가진 AWS의 대표적인 스토리지
- 대표 출제 패턴
  1. 데이터 레이크 및 대규모 저장
     - 출제 형태: 정형/비정형 데이터를 구분 없이 원본 상태로 중앙에 모아두고 빅데이터 분석을 수행하는 기본 저장소를 물어볼 때
     - 포인트: Data Lake 기반(Core)의 스토리지 역할이라는 언급이 있으면 무조건 S3가 담당
     - 키워드: Data Lake, Unstructured Data, Central Repository, Analytics

  2. 아카이브(Archive) 및 백업/복구
     - 출제 형태: 데이터 백업을 장기 보관하거나, 자주 접근하지 않는 데이터를 저렴하게 저장하려 할 때
     - 포인트:
       - S3 Lifecycle Rules(수명 주기 규칙)을 통해 일정 시간이 지나면 자동으로 S3 Glacier로 이관
       - 높은 내구성으로 데이터 손실 우려 없는 백업 저장소 제공
      - 키워드: Backup & Restore, Archive, Glacier, Lifecycle Rules

  3. 정적 웹사이트 호스팅
     - 출제 형태: EC2 서버를 생성하지 않고, HTML/Images 등 정적 컨텐츠만으로 구성된 웹사이트를 호스팅하려 할 때
     - 포인트: S3 버킷 자체에 정적 웹 사이트 호스팅 기능을 켜서 서버리스로 웹사이트 구동 가능
     - 키워드: Static Website, HTML/CSS/JS, Serverless Hosting, No Server required

  4. 객체 스토리지 고유의 특징
     - 출제 형태: 파일 시스템(EFS)이나 가상 하드디스크(EBS)가 아닌, 인터넷을 통해 어디서나 접근 가능한 객체 스토리지
     - 포인트: 파일 단위 저장이 아니라 데이터 + 메타데이터 형태의 '객체'로 관리되며, 인터넷 URL을 통해 직접 접근 가능, 객체 단위로 저장하므로 일부 수정이 불가하고 전체를 덮어써야 함 -> 따라서 수정이 EFS나 EBS에 비해 원활하지 못함
     - 키워드: Object Storage, Key-Value Store, Scalable Storage, Access via HTTP/HTTPS

  5. 보안 및 정적 데이터 암호화
     - 출제 형태: 저장 데이터의 암호화나 리소스 기반의 접근 통제를 적용해야 하는 스토리지 문제를 다룰 때
     - 키워드: Encrypting Data at Rest, Bucket Policy, Public Access Block

  + S3가 정답이 될 수 없는 함정들
    1. 자주 변경되는 데이터
       - 자주 업데이트되거나 수정되는 파일을 저장하려고 함 -> S3는 객체 스토리지의 특성상 원활하게 수정하기 어려움
       - 자주 변경되는 데이터나 DB 파일 저장은 S3가 아닌 EBS나 RDS를 선택해야 함

    2. EC2 인스턴스의 부팅 볼륨(OS 전용 스토리지)
       - EC2의 운영체제를 설치하고 부팅할 스토리지로 S3를 사용 -> EBS 사용 필수
       - OS나 데이터베이스처럼 파일의 특정 블록 단위로 읽기/쓰기가 실시간으로 일어나는 영역에서는 S3를 사용할 수 없음 -> 반드시 EBS를 사용해야 함

    3. 일관성 모델 및 파일 수정 방식
       - S3에 저장된 파일에서 단 몇 줄의 텍스트만 수정하려고 하는 경우 -> 부분 수정(Partial Update) 불가
       - S3는 PUT/DELETE 기반의 객체 스토리지이기 때문에 파일 내 일부만 수정하는 것이 불가능함 -> 파일 전체를 다시 덮어써야하므로 부분 수정과 S3가 엮어 사용되면 오답 선지임
      
-> S3는 한 번 써두고 자주 읽는 정적 데이터에 최적화되어 있음

# Amazon WorkSpace
- AWS에서 제공하는 완전 관리형 VDI(가상 데스크톱 인프라, Virtual Desktop Infrastructure) 및 DaaS(Desktop as a Service) 솔루션
- 복잡한 온프레미스 가상 데스크톱 서버 구축 없이 클릭 몇 번으로 Cloud 상에 Windows나 Linux 기반의 개인용 가상 PC 환경을 생성하고 인터넷이 연결된 어디서나 접속할 수 있게 해 줌
- 핵심 특징
  - 어디서나 접속
    - 노트북, 태블릿, 스마트폰, 웹 브라우저 등 다양한 기기에서 전용 앱이나 브라우저로 Workspace 가상 데스크톱에 접속 가능
  - 고급 데이터 보안
    - 데이터가 사용자의 로컬 기기에 저장되지 않고, 오직 AWS 클라우드 내부에 안전하게 암호화되어 저장됨
  - 관리 편의성 & 확장성
    - 직원들에게 개별 사양의 PC를 순식간에 할당하거나 회수할 수 있으며, 소프트웨어 설치 및 패치를 중앙에서 제어 가능
  - 유연한 요금제
    - 시간제: 접속해서 사용한 시간만큼 정산(파트타임)
    - 월정액: 고정 월 비용 납부(전업 근무자용)
- 주요 Use-Case
  - 재택 근무 및 원격 근무: 직원들에게 사내망 접근이 가능한 가상 PC 환경을 안전하게 제공
  - 외주 개발자 및 계약직: 외부 인력에게 회사 소유의 실제 노트북을 지급하지 않고, 권한이 제한된 가상 데스크톱만 부여하여 보안 유지
  - BYOD 정책: 직원이 개인 소유 기기를 사용하되, 업무용 작업은 독립된 가상 PC인 WorkSpaces 안에서만 처리하도록 분리

-> 재택근무나 외주 개발자에게 안전한 원격 윈도우/리눅스 PC 전체를 빌려줄 때는 Amazon WorkSpace 떠올리

# VPC Gateway 3대장 키워드 정리
1. Internet -> Internet Gateway(IGW)
   - 키워드: Public Internet, Inbound & Outbound, Public Subnet
   - 원리: VPC와 퍼블릭 인터넷 간의 양방향 통신 관문
2. Private Subnet + Outbound Only -> NAT Gateway
   - 키워드: Private Subnet, Outbound Interent, Block Inbound
   - 원리: 외부에서 들어오는 연결은 막고, 내부에서 패치나 업데이트를 위해 밖으로 나가는 통신만 일방통행으로 허용
3. VPN / On-premises -> Virtual Private Gateway(VGW)
   - 키워드: Site-to-Site VPN, On- premises, Encrypted Tunnel
   - 원리: 인터넷이 아닌 회사 데이터센터와 암호화된 VPN 연결을 할 때 AWS 쪽에 달아두는 관문
+ VPN의 구성요소: Virtual Private Gateway(AWS 쪽 관문) & Customer Gateway(고객 쪽 관문)

# AWS Control Tower - 출제 가능성 30% 정도 
- 여러 개의 AWS 계정을 사용하는 기업 환경에서 AWS Best practice에 맞는 안전한 기본 인프라를 자동으로 구축하고 통제해 주는 거버넌스 관리 서비스
- 핵심 역할과 특징
  1. Landing Zone 자동 생성:
     - 기업이 AWS를 처음 사용할 때, 각종 서비스들을 수동으로 세팅할 필요 없이, 클릭 몇 번으로 완벽하게 보안 설정이 끝난 표준 멀티 계정 환경을 만들어 줌
  2. Guardrails
     - 필수 및 권장 보안 규칙을 자동으로 적용
     - ex. S3 버킷의 퍼블릭 접근을 절대 허용하지 않는다, MFA를 설정하지 않은 계정 생성을 차단한다 등의 정책을 중앙에서 강제함
  3. Account Factory:
     - 개발팀, 재무팀 등 새로운 팀이 들어왔을 때, 보안 및 규정 정책이 이미 완벽히 세팅된 표준 AWS 계정을 몇 분 만에 뚝딱 찍어내듯 생성해 줌
    
+ Multi-account environment, Set up a Landing Zone, Enforce Guardrails 같은 문구가 대놓고 나올 때만 Control Tower가 정답임. 보안 규칙 검사나 계정 생성만 보고 판단하면 AWS Config나 AWS Organizations와 헷갈릴 수 있으니 주의가 필요함

# AWS IAM Access Analyzer
- 역할: S3 버킷, KMS 키, IAM Role 등 내 계정의 리소스 중 외부 조직이나 다른 계정(External Principals)에 접근 권한이 열려 있는 리소스를 자동으로 분석해서 알려주는 IAM의 세부 기능
- 핵심 원리: 논리적 수학 검증을 통해 퍼블릭 또는 교차 계정으로 접근 가능한 리소스를 감지
-> 외부로 공유된 리소스 탐지 등장 = IAM Access Analyzer

# AWS Fargate
- Amazon ECS 및 EKS와 함께 작동하는 컨테이너용 서버리스 컴퓨팅 엔진
- 핵심 특징
  1. 서버리스 방식
     - EC2 가상 머신을 프로비저닝하거나 관리할 필요가 전혀 없음
     - 가상 머신 크기 선택, 클러스터 스케일링, OS 패치 및 보안 업데이트를 AWS가 알아서 처리함
  2. 유연한 리소스 및 요금 모델
     - 컨테이너가 필요로 하는 vCPU와 메모리의 양만 지정하면 됨(서버리스)
     - 실행된 컨테이너가 사용한 vCPU 및 메모리 자원 사용과 실행 시간에 대해서만 비용을 지불함
  3. 격리된 보안 환경
     - 고유한 격리된 VM 경계 내에서 실행되어서 다른 어플리케이션과의 리소스 공유로 인한 보안 리스크가 차단됨

# Edge Location 관련 핵심 AWS 서비스
1. Amazon CloudFront
   - 역할: CDN(Content Delivery Network). Edge Location에 컨텐츠(이미지, 동영상)를 캐싱하여 빠르게 제공/전달
2. AWS Shield(및 AWS AWF)
   - 역할: DDoS 방어 및 웹 어플리케이션 방화벽(WAF). Edge Location 단에서 트래픽을 미리 검사하고 차단
3. Amazon Route 53
   - 역할: DNS(Domain Name Service) 서비스. Edge Location을 통해 사용자와 가장 가까운 위치에서 지연시간이 적은 DNS 응답 제공
4. AWS Global Accelerator
   - 역할: AWS의 글로벌 백본 네트워크를 이용해 트래픽을 최단 경로로 라우팅하여 어플리케이션 성능 향상

# 보안 그룹 vs NetworkACL(NACL)
- 보안 그룹(Security Group)/인스턴스 바로 앞 개별 문지기
  - 적용 수준: 인스턴스 레벨
  - 지원 규칙: Allow만 가능(서버는 허용된 안전한 트래픽 외에는 전부 닫아두는 것이 가장 안전함)
  - 상태 유지: Stateful(인바운드 허용 시 응답 자동 허용)
- NetworkACL(서브넷 전체를 아우르는 울타리)
  - 적용 수준: subnet 레벨
  - 지원 규칙: Allow/Deny 모두 가능
  - 상태 유지: Stateless(인바운드/아웃바운드 각각 설정)
    - 이유: 서브넷 레벨에는 수많은 인스턴스가 존재하는데, 이 연결 상태를 모두 기억하면 메모리와 성능에 과부하가 유발됨. 따라서 상태를 기억하지 않는 stateless로 설계되었음
-> 선지에 Block이나 Explicitly Deny가 등장하면 Deny가 가능한 NetworkACL이 무조건 정답에 해당하게 됨

# Amazon MemoryDB - 출제 가능성 낮음
- Redis(또는 Valkey)와 호환되는 In-memory 기반의 초고속 데이터베이스 서비스
- ElastiCache와의 결정적 차이점
  - ElastiCache: 단순 캐시 용도로 메모리가 꺼지면 데이터가 휘발될 수 있음
  - MemoroyDB: 메모리 기반으로 마이크로초 수준의 읽기/쓰기 속도를 제공하면서도, 3개 AZ로 영구 저장해주기 때문에 메인 데이터베이스로 직접 사용할 수도 있음
  
# AWS VPC Flow Logs
- VPC 내 네트워크 인터페이스를 오고 가는 IP 트래픽을 모니터링/기록하는 서비스
- VPC Flow Logs vs CloudTrail
  1. VPC Flow Logs
     - 기록 대상: VPC 내 네트워크 인터페이스를 오고 가는 IP 트래픽
     - 네트워크 수준의 인바운드/아웃바운드 IP 흐름을 캡처하는 전용 기능
  2. CloudTrail
     - 기록 대상: 누가, 언제, 어떤 AWS API를 호출했는지
     - 네트워크를 오고 가는 실제 IP 트래픽 데이터는 기록하지 못함
- 핵심 키워드
  - IP traffic (인바운드/아웃바운드 IP 트래픽)
  - Network Interface(ENI) / Subnet / VPC
  - Accept / Reject (보안 그룹이나 NACL에서 트래픽이 허용되었는지 거부되었는지 문제 해결 용도)

 # AWS Amplify
 - 역할: 웹 및 모바일 앱을 빠르게 개발/배포할 수 있도록 인증, 백엔드 연결, 프론트엔드 호스팅 등을 하나로 제공하는 개발 플랫폼 프레임워크
 - mobile and web applications 개발 지칭 시 가장 대표적으로 등장하는 서비스
 - 모바일/웹 앱 신속 개발 및 호스팅

# AWS AppSync - 출제 가능성 낮음
- 역할: GraphQL API를 활용하여 여러 데이터 소스의 데이터를 쉽게 연결하고 동기화해주는 관리형 서비스
- real-time updates(GraphQL Subscription 기반 실시간 데이터 업데이트) 및 offline functionalities(네트워크 중단 시 로컬 캐시를 사용하다 재연결 시 자동 동기화)가 핵심 키워드
- GraphQL 기반 실시간 데이터 동기화

# AWS Systems Manager -> 운영 자동화 + 통합 사용자 인터페이스/대시보드
- AWS 환경 뿐만 아니라 온프레미스 및 타사 클라우드 서버까지 하나의 대시보드에서 일괄 관리 및 자동화할 수 있도록 지원하는 통합 운영 관리 서비스
- 핵심 기능
  1. Session Manager
     - 웹 콘솔만을 통해 EC2 인스턴스에 안전하게 원격 접속하는 기능
     - 시험 포인트: '키 페어 관리 없이 안전한 인스턴스 접속', '22번 포트 차단'
  2. Parameter Store
     - 암호, DB 연결 문자열, 라이센스 코드 등의 설정 데이터를 중앙에서 안전하게 저장하고 관리하는 서비스
     - 특징: AWS KMS와 연동되어 암호화가 지원되며, 소스코드 안에 비밀번호를 하드코딩하지 않고 불러와 사용할 수 있게 해줌
  3. *Automation(자동화)*
     - 미리 정의된 Runbook 스크립트를 이용해 반복적인 IT 운영 작업(EC2 백업, AMI 생성 등)을 자동화하는 기능
  4. Patch Manager & Maintenance Windows
     - OS 및 어플리케이션의 보안 패치를 자동화하고, 정해진 점검 시간에만 패치가 수행되도록 스케줄링하는 기능
-> 시험에는 '운영 자동화'와 Session Manager를 통한 안전한 접속'이 주로 등장

# AWS Cognito
- 웹 및 모바일 어플리케이션에 회원가입, 로그인, 접근 제어 기능을 손쉽게 붙일 수 있게 해주는 서버리스 자격 증명 관리 서비스
- 2가지 핵심 구성 요소
  1. User Pools (사용자 풀) - 인증 담당(너 누구니?/신원 검증)
     - 역할: 사용자 로그인/회원가입 디렉터리 관리
     - 기능:
       1. 이메일, 아이디/비밀번호 기반 로그인 처리
       2. 소셜 로그인 연동(google, facebook, apple 등) 및 SAML/OIDC 지원
       3. MFA 및 비밀번호 재설정 기능 자동 제공
      - 인증 성공 시 어플리케이션에 JWT 토큰을 발급해 줌
  2. Identity Pools (자격 증명 풀) - 인가 담당(너 뭐 할 수 있니?/임시 접근 권한 부여)
     - 역할: 사용자가 AWS 리소스에 직접 접근할 수 있는 임시 권한 부여
     - 기능: User Pools나 소셜 로그인을 거친 사용자에서 임시 AWS IAM 자격 증명을 발급
     - 앱 사용자가 백엔드 서버를 거치지 않고 S3에 직접 사진을 업로드하는 등의 작업이 가능해짐
  - IAM과의 구분
  -> AWS 계정 내 직원/개발자 권한 관리는 IAM, 웹/모바일 앱의 일반 고객 로그인 관리는 Cognito

- 주요 키워드
  - Web and Mobile App Sign-Up / Sign-In (웹 및 모바일 앱 회원가입/로그인)
  - Social Identity Providers (구글, 페이스북 등 소셜 로그인 연동)
  - User Pools & Identity Pools
  - Temporary AWS Credentials for app users (앱 사용자용 임시 AWS 자격 증명)

# 비동기 통합(Asynchronous Integration)
- 개념: 어플리케이션의 여러 구성 요소(component)들이 통신할 때, 요청을 보낸 쪽이 상대방의 작업 처리가 끝날 때가지 기다리지 않고 곧바로 자신의 다음 작업을 진행하는 방식
- 구성 요소들이 서로 직접 엮여있지 않도록하여 한 쪽에 장애가 생기거나 병목 현상이 일어나도 전체 시스템에 영향이 없도록 함(Decoupling)
- 비동기 통합(Asynchronous Integration)을 통해 Decoupling을 이루어낸다고 생각하면 됨
- 키워드
  - Decouple application conponents (앱 구성요소 결합도 낮추기)
  - Asynchronous Integration(비동기 통합)
  - Loose coupling (느슨한 결합)
- 비동기 통합(Asynchronous Integration) & Decoupling 지원 서비스
  - SNS, SQS, Step Functions, EventBridge

# AWS Application Discovery Service
- 역할: 온프레미스 데이터센터의 서버 성능 데이터, 서버 간의 의존성, 하드웨어 사양 등을 자동으로 탐지/수집하는 서비스
- 목적: 수집한 데이터를 기반으로 AWS 마이그레이션 계획을 수립 및 적절한 인스턴스 스펙 및 비용 예측
- 키워드: On-premises data centers, Planning a migration, Collect server data
- 서비스 이름에 Application이 들어가는 이유
  -> 단순히 물리 하드웨어나 OS 정보만 긁어오는 것이 아니라, 어플리케이션 단위의 연관 관계를 파악하기 위한 서비스이기 때문
  -> 서버들 간의 관계를 분석하여 어플리케이션 그룹핑 및 의존성 지도를 그림
  -> 이를 바탕으로 마이그레이션할 때 '어플리케이션' 단위로 함께 클라우드로 옮길 수 있도록 그룹화함

# AWS AI/ML Services 요약
- 이미지/영상 속 얼굴/물체 찾기 ➔ Rekognition
- 글자(Text)를 목소리(Speech)로 읽기 ➔ Polly
- 목소리(Audio)를 글자(Text)로 받아쓰기 ➔ Transcribe
- 음성/텍스트 대화형 챗봇 만들기 ➔ Lex
- 텍스트의 긍정/부정 감정 분석하기 ➔ Comprehend
- 문서 모음집에서 자연어로 검색하기 ➔ Kendra
- 개발자가 직접 ML 모델을 구축/학습/배포하기 ➔ SageMaker

# AWS Support Plan 등급별 최대 심각도 & 응답 시간 비교
(Basic Plan은 기술 지원(Technical Support Case)자체가 아예 제공되지 않으므로 생략)
1. Developer Plan
   - 지원 최상위 심각도: 시스템 손상(System Impaired)
   - 목표 응답 시간: 12시간 이내
   - TAM 유무: 무
2. Business Plan
   - 지원 최상위 심각도: 운영 시스템 중단(Production system down)
   - 목표 응답 시간: 1시간 이내
   - TAM 유무: 무
3. Enterprise On-Ramp
   - 지원 최상위 심각도: Business-critical system down
   - 목표 응답 시간: 30분 이내
   - TAM 유무: 전담 TAM이 아닌 TAM Pool 지원
   - Concierge 팀 지원(결제 및 계정 문의 전담 처리반)
4. Enterprise
   - 지원 최상위 심각도: Business-critical system down
   - 목표 응답 시간: 15분 이내
   - TAM 유무: 전담 TAM 배정
   - Concierge 팀 지원(결제 및 계정 문의 전담 처리반)
  
# AWS PrivateLink
- 개념: 퍼블릭 인터넷에 노출시키지 않고, AWS 내부 네트워크(Direct Connect, VPC Endpoint 등)을 통해 특정 서비스/어플리케이션에 1:1 사설 IP로 안전하게 접근하게 해주는 기술
- 작동 방식
  - 내 VPC 안에 인터페이스 VPC 엔드포인트라는 사설 가상 랜카드 생성
  - 온프레미스 데이터센터에서 Direct Connect 등을 타고 들어와 퍼블릭 인터넷을 거치지 않고 오직 내부 사설 IP로만 타사 SaaS 앱이나 다른 VPC의 특정 서비스에 연결하게 해 줌
- 유사 서비스 키워드 요약
  1. Site-to-Site VPN
     - On-premises to VPC + Encrypted IPsec tunnel
  2. AWS Direct Connect
     - On-premises to VPC + Private Dedicated Connection
  3. AWS PrivateLink
     - No Public Internet + Private IP access to services/SaaS + VPC Endpoint

# VPC Endpoint
- AWS 내부 네트워크 망을 이용해 VPC와 다른 AWS 서비스 또는 외부 SaaS 서비스를 안전하게 연결해 주는 가상 장치
- 인터넷 게이트웨이, NAT 게이트웨이, VPN, Direct Connect 같은 통로를 거치지 않고 퍼블릭 인터넷 노출 없이 AWS 백본망 내부에서만 통신할 수 있게 해 줌
- VPC Endpoint가 필요한 이유
  - S3, DynamoDB 같은 AWS 서비스들은 퍼블릭 IP를 가진 퍼블릭 엔드포인트 형태로 제공됨
  -> VPC Endpoint가 없다면 퍼블릭 인터넷 구간을 거쳐야하므로 보안 위험과 NAT gateway 비용이 발생함
  -> VPC Endpoint를 사용하면 외부 인터넷 사용 없이 AWS 내부 사설 망으로 직접 꽂혀서 통신하므로 최고의 보안성을 확보할 수 있고 NAT 비용도 절감할 수 있음
- VPC Endpoint의 핵심 유형 2가지
  1. Gateway Endpoint
    - 작동 방식: VPC 라우팅 테이블에 타겟으로 등록하여 트래픽 라우팅
    - 지원 서비스: Amazon S3, DynamoDB
    - 비용: 무료
  2. Interface Endpoint
    - 작동 방식: 서브넷 안에 사설 IP를 가진 가상 랜카드를 생성하여 1:1통신
    - 지원 서비스: S3, DynamoDB를 제외한 대부분의 AWS 서비스 + 타 사 SaaS 서비스
    - 비용: 유료(시간당 요금 + 데이터 처리량 요금)
 
# 글로벌 서비스 vs 리전 서비스
1. 글로벌 서비스
   : IAM, Route 53, CloudFront, AWS WAF, AWS Organizations, AWS Shield, AWS Global Accelerator
2. 리전 서비스
   : EC2, VPC, RDS, EBS, S3(S3는 네임페이스는 글로벌(전세계에 같은 이름이 2개 있으면 안됨)이지만 버킷 생성 위치는 리전 단위)
