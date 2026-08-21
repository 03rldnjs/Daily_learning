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

- Amazon EC2
  가장 표준적인 RI 모델로, 가상 서버 용량을 미리 예약하고 최대 72~75%의 할인을 받음
  표준 RI와 사양 변경이 가능한 Convertible RI로 나뉨
- Amazon RDS
  관계형 데이터베이스 인스턴스용 예약 요금제
  Reserved DB Instance라고 부르며, 24시간 계속 구동되는 DB 인프라 특성상 RI 사용시 할인 효과가 매우 큼
- Amazon DynamoDB
  NoSQL(비관계형) 데이터베이스. 스키마가 엄격하지 않으며 Key-Value 모델과 Document 모델을 지원함
  읽기/쓰기 용량 단위에 대해 미리 예약하여 할인을 받는 Reserved Capacity 방식을 지원함
- Amazon ElastiCache/MemoryDB
  Redis/Memcached 기반의 인메모리 캐시 및 데이터베이스 서비스
  Reserved Nodes 형태로 1년/3년 약정을 통해 노드 비용 할인을 받음
- Amazon Redshift
  대규모 데이터 웨어하우스 서비스로 데이터 분석도 제공함
  Reserved Nodes 개념으로 노드 비용을 크게 절감할 수 있음
  
---

# AWS Oranizations의 통합 결제 기능

- 4대 핵심 규칙
  1. 단일 결제 주체: 조직의 관리 계정이 모든 연결된 계정의 비용을 일괄 지불함
  2. 볼륨 할인 공유: AWS의 대부분의 리소스는 사용량이 늘어날수록 GB당 단가가 낮아지는데, 계정을 통합하면서 할인 구간이 상승하여 더 저렴한 단가로 서비스 이용이 가능함
  3. RI 및 Savings Plans 혜택 공유: 한 멤버 계정에서 구매한 RI나 Savings Plans를 해당 계정이 다 쓰지 못해 남는 경우, 조직 내 다른 멤버 계정의 온디맨드 사용량으로 할인이 자동으로 넘어감
  4. 무료 티어 합산: 무료 티어 혜택은 계정마다 적용되는 것이 아니라, 조직 전체를 통틀어 1개 계정 분량만 통합 합산되어 적용됨

- RI / Savings Plans 할인 공유 조건 및 주의사항
  1. 조건 일치 필수: 인스턴스 타입, 리전, AZ 등의 사양이 일치해야 할인이 공유됨
  2. 비활성화 옵션: 조직 관리자는 필요에 따라 특정 계정 간에 RI/Savings Plans 할인이 공유되지 않도록 비활성화할 수 있음





