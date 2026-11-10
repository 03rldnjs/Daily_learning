# 🚀 AWS Certified Solutions Architect – Associate (SAA-C03) Study Notes

AWS SAA-C03 자격증 취득 및 실무 수준의 클라우드 아키텍처 설계 능력을 함양하기 위해, 탄력성(Resiliency), 고성능(Performance), 보안(Security), 그리고 비용 최적화(Cost-Optimization) 관점의 설계 원칙과 패턴을 기록하는 학습 폴더입니다.  
A comprehensive architecture-focused study archive for the AWS Certified Solutions Architect – Associate (SAA-C03) exam, covering resilient, high-performing, secure, and cost-optimized design patterns.

---

## 💡 주요 학습 및 아키텍처 설계 목표 (Core Architecture Domains)

### 1. 회복력 있는(Resilient) 아키텍처 설계
- **VPC 네트워킹 심화**: 
  - 퍼블릭 서브넷(Public Subnet)과 프라이빗 서브넷(Private Subnet) 분리 설계.
  - 인터넷 가이트웨이(IGW), NAT 게이트웨이(NAT Gateway), 라우팅 테이블(Routing Table)의 유기적 연동.
- **고가용성 및 결함 허용 (High Availability & Fault Tolerance)**:
  - 멀티 AZ(Multi-AZ) 기반의 ALB(Application Load Balancer)와 Auto Scaling Group(ASG) 연동.
  - Route 53을 활용한 글로벌 트래픽 라우팅 및 페일오버(Failover) 전략.

### 2. 고성능(High-Performing) 아키텍처 설계
- **컴퓨팅 및 스토리지 최적화**: 
  - EC2 인스턴스 패밀리별 특성 파악 (Compute, Memory, Storage Optimized).
  - EBS 볼륨 타입(gp3, io2 등) 및 S3 스토리지 클래스(Standard, Intelligent-Tiering, Glacier)의 적재적소 선택.
- **캐싱 및 데이터베이스 확장**:
  - Amazon ElastiCache(Redis/Memcached)를 통한 데이터베이스 부하 분산 및 응답 속도 가속.
  - Aurora Read Replica 및 DynamoDB 글로벌 테이블 활용 방안.

### 3. 보안(Secure) 응용 프로그램 및 아키텍처 설계
- **접근 제어 및 권한 관리**:
  - IAM 정책(Policy), 역할(Role), 크로스 계정(Cross-Account) 접근 제어 및 최소 권한의 원칙(Principle of Least Privilege).
- **네트워크 보안**:
  - 보안 그룹(Security Groups, SG)과 네트워크 ACL(NACL)의 차이점 및 상태 비저장(Stateless) vs 상태 저장(Stateful) 필터링 구조.
  - AWS KMS(Key Management Service)를 통한 데이터 암호화 및 WAF/Shield를 통한 웹 취약점 방어.

### 4. 비용 최적화된(Cost-Optimized) 아키텍처 설계
- **구매 옵션 및 스토리지 수명 주기**:
  - EC2 스팟 인스턴스(Spot Instances), 절감형 플랜(Savings Plans), 예약 인스턴스(RI)의 비용 효율적 조합.
  - S3 수명 주기 정책(Lifecycle Policy)을 통한 장기 데이터 자동 아카이빙.

---

## 🛠️ 실무 및 시험 대비 핵심 아키텍처 패턴 (Key Design Patterns)
- **3계층 웹 애플리케이션 아키텍처 (3-Tier Web Architecture)**:
  `Client ➡️ CloudFront ➡️ Route 53 ➡️ ALB ➡️ Public/Private EC2 (Auto Scaling) ➡️ Multi-AZ RDS` 구조의 End-to-End 데이터 흐름 이해 및 병목 구간 해소 전략.
- **서버리스 이벤트 기반 아키텍처 (Serverless Event-Driven Architecture)**:
  `API Gateway ➡️ Lambda ➡️ DynamoDB / SQS / SNS`를 활용한 확장성 높고 유지보수 비용이 없는 구조 설계.

---

> 🔄 **Work in Progress**: 본 폴더는 SAA-C03 합격 및 실무 역량 강화를 위해 실시간으로 업데이트 및 보강되고 있습니다.
