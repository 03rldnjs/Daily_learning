# ☁️ AWS Certified Cloud Practitioner (CLF-C02) Study Notes

AWS CLF-C02 자격증 취득을 목표로 클라우드 컴퓨팅의 기초 개념부터 핵심 아키텍처 서비스, 보안, 요금 체계, 그리고 실전 시험에서 자주 출제되는 함정 선지 및 오답 노트를 체계적으로 기록한 학습 폴더입니다.  
A comprehensive study archive for the AWS Certified Cloud Practitioner (CLF-C02) exam, covering core cloud concepts, AWS services, security, billing models, and exam-focused troubleshooting notes.

---


## 💡 주요 학습 및 정리 내용 (Core Study Topics)

### 1. 클라우드 컴퓨팅 개론 및 경제적 이점 (Cloud Concepts & Benefits)
- **가변 비용 모델 (Variable Expense)**: 선행 투자 비용(IDC 구축 등)을 가변 비용으로 전환하여 자원 효율성 극대화.
- **규모의 경제 (Economies of Scale)**: 대규모 인프라 운영을 통한 비용 절감 효과.
- **용량 추정 불필요**: 트래픽 예측에 따른 과잉/과소 투자 위험 방지 및 민첩성(Agility) 확보.

### 2. AWS 글로벌 인프라 및 핵심 아키텍처 (Global Infrastructure)
- **리전 (Region) & 가용 영역 (Availability Zones, AZ)**: 물리적으로 격리된 데이터센터의 집합과 고가용성(High Availability) 설계.
- **Multi-AZ 배포**: 단일 장애 지점(Single Point of Failure, SPOF) 방지 및 애플리케이션 가용성 향상.
- **Amazon CloudFront (CDN)**: 전 세계 엣지 로케이션(Edge Location)을 활용한 글로벌 지연 시간(Latency) 감소 및 S3 정적 웹 호스팅 가속.

### 3. 주요 AWS 서비스 및 아키텍처 매칭 (Core Services & Matching)
- **컴퓨팅 (Compute)**: 
  - `Amazon EC2`: 온디맨드, 예약 인스턴스, 스팟 인스턴스 등 워크로드별 최적화된 구매 옵션.
  - `AWS Lambda`: 서버리스(Serverless) 이벤트 기반 컴퓨팅, 실행 시간(Duration) 및 요청 수(Requests) 기준 과금.
- **데이터베이스 (Database)**:
  - `관계형 데이터베이스 (RDBMS)`: Amazon RDS, Amazon Aurora (엄격한 스키마, ACID 트랜잭션 보장, 금융/주문 시스템).
  - `비관계형 데이터베이스 (NoSQL)`: Amazon DynamoDB (유연한 스키마, 수평적 확장성, 실시간 게임/SNS 타임라인).
- **메시징 및 마이그레이션**:
  - `Amazon SNS` (알림 브로드캐스트) vs `Amazon SQS` (대기열 및 결합 해제).
  - `AWS MGN` (서버 전체 통째로 EC2 Lift-and-Shift 마이그레이션) vs `AWS DMS` (데이터베이스 내 데이터만 이전).

### 4. 보안, 컴플라이언스 및 요금/지원 플랜 (Security & Billing)
- **AWS 공동 책임 모델 (Shared Responsibility Model)**: 클라우드 *의* 보안(AWS 책임)과 클라우드 *내부*의 보안(고객 책임).
- **지원 플랜 (Support Plans)**: Basic, Developer, Business, Enterprise On-Ramp, Enterprise별 응답 시간 및 기술 지원 범위 비교.
- **비용 관리 도구**: AWS Budgets, Cost Explorer, AWS Pricing Calculator를 통한 효율적인 비용 통제.

---

## 🔍 실전 오답 노트 및 함정 선지 분석 (Troubleshooting & Exam Tips)
- 서비스 이름이나 기능이 헷갈리기 쉬운 대표적인 함정 선지(예: `DAX` vs `CloudFront`, `DMS` vs `MGN`, `SQS` vs `SNS`)를 비교 분석하여 명확한 유스케이스(Use-Case)를 정립했습니다.
- 공식 문서 및 실전 모의고사에서 틀린 문제를 바탕으로 원인을 분석하고, AWS가 요구하는 아키텍처 설계 철학을 코멘트로 남겼습니다.
