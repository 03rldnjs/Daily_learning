# AWS Organizations & Control Tower
- AWS Organizations
  - 여러 AWS 계정을 하나의 조직으로 묶어 중앙에서 관리하고, 계정별 권한과 정책을 통제할 수 있도록 해주는 서비스
  - 1. AWS Orgaizations의 구성과 역할
      - 1-1. Oragizations를 사용하는 이유
        - 한 기업이 다음과 같은 AWS 계정을 운영한다고 가정
          - 개발팀: 개발 환경
          - 운영팀: 실제 서비스 운영 환경
          - 보안팀: 보안 및 감사 환경
          - 테스트팀: 실험 및 테스트 환경
        - 이 모든 환경을 하나의 AWS 계정에서 운영하면 권한과 리소스가 뒤섞일 수 있음
        - Organizations를 사용하면 계정을 여러 개 생성하고, 목적에 따라 그룹화한 뒤 중앙에서 관리할 수 있음
      - 1-2. Organizations의 계층 구조
          - Management Account(조직 생성 및 중앙 관리)
          - Root(조직의 최상위 컨테이너)
          - Development OU / Production OU(목적에 따라 AWS 계정을 그룹화하는 단위)
          - Account A, Account B / Account C, Account D(실제 AWS 리소스를 생성하고 운영하는 계정)
            - OU 안에 다른 OU를 생성할 수 있음
            - ex. Root -> Business OU -> Development OU -> Account A
            - 조직 구조를 계층적으로 설계하면 상위 OU에 설정한 정책을 하위 OU와 계정에 적용할 수 있음
      - 1-3. Management Account와 Member Account
          - Management Account
            - 조직을 생성하는 계정
            - 새로운 AWS 계정을 생성하거나 기존 계정을 조직에 초대할 권한을 가짐
            - OU를 생성하고 계정을 이동할 수 있음
            - 조직 전체에 정책 연결
            - 통합 결제(Consolidated Billing) 관리
          - Member Account
            - 조직에 소속된 일반 AWS 계정
            - EC2, S3, RDS 등 실제 워크로드 운영
            - Organizations에서 설정한 정책의 통제를 받음
          + SCP는 Management Account에는 적용되지 않음 -> Management Account에는 실제 워크로드를 가급적 배치하지 않는 것이 AWS의 권장 보안 방향
   - 2. Organizations API
        - 2-1. Organizations API란?
          - AWS Organizations의 계정과 조직 구조를 프로그래밍 방식으로 관리하기 위한 인터페이스
          - 즉, AWS Management Console에서 직접 클릭해서 수행하던 작업을 CLI/SDK 또는 API 호출을 통해 자동화할 수 있음
          - 기업이 새로운 개발팀을 구성할 때 다음 과정을 자동화할 수 있음
            1. 새로운 AWS 계정 생성
            2. 개발팀 OU 생성
            3. 생성한 계정을 개발팀 OU에 배치
            4. 해당 OU에 SCP 연결
        - 2-2. 주요 Organizations API
          - CreateOrganization: 새로운 조직 생성
          - CreateAccount: 새로운 AWS 계정 생성
          - InviteAccountToOrganization: 기존 AWS 계정을 조직에 초대
          - CreateOrganizationalUnit: OU 생성
          - AttachPolicy: 정책을 Root, OU 또는 계정에 연결
          - CreatePolicy: 새로운 조직 정책 생성
          - RegisterDelegatedAdministrator: 멤버 계정을 위임 관리자로 등록
          - ex. 기업에서 새로운 개발팀이 만들어진 경우
            - CreateAccount로 개발팀 계정 생성
            - CreateOrganizationalUnit으로 개발팀 OU 생성
            - MoveAccount로 해당 계정을 개발팀 OU에 배치
            - AttachPolicy로 개발팀에 적합한 SCP를 연결
        + Organizations API는 여러 AWS 계정의 생성, 초대, 이동, 정책 연결 등을 자동화하는 수단이지, EC2나 S3 등의 서비스 자체를 생성하는 기능은 아님
       
    - 3. SCP(Service Control Policy)
      - 3-1. SCP란?
        - AWS Organizations에서 제공하는 정책으로, 조직에 속한 계정의 IAM 사용자와 IAM 역할이 사용할 수 있는 최대 권한의 범위를 제한함
        - 즉, 기업의 중앙 관리자가 각 계정의 상한선을 설정하는 것
      - 3-2. SCP는 권한을 부여하는 정책이 아니다!
        - SCP는 권한을 부여하는 정책이 아니라 **권한을 제한하는 정책**임
        - ex. 상황: 개발팀 계정의 S3 접근
          - IAM Policy: S3에 접근할 수 있는 권한 부여(Allow)
          - SCP: S3 접근 금지(Deny)
          - 최종 결과: SCP에서 S3에 대한 접근을 금지했으므로 접근 불가
            + 반대로 SCP에서 S3 접근에 대한 금지를 하지 않았더라고 IAM Policy에서 권한이 부여되지 않았다면 접근 불가
          - > 최종적으로 사용할 수 있는 권한은 IAM 정책 등 실제 권한 부여 정책과 SCP가 허용하는 범위의 교집합
      - 3-3. SCP 적용 대상과 예외
        - SCP는 조직의 Root, OU, Member Account에 연결할 수 있음
        - SCP가 적용되는 대상은 Member Account의 IAM User, IAM Role, Root User가 있음
        - 단, **Management Account에는 SCP가 적용되지 않고, AWS 서비스 연결 역할(Service-linked role)은 SCP의 제한을 받지 않음**
    - 4. SCP의 Strategies: Deny List와 Allow List
      - 4-1. Deny List Strategy
        - 
