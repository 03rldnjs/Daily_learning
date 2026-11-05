# AWS Organizations & Control Tower
# AWS Organizations
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
          - Root(조직의 최상위 컨테이너 - K8s나 Docker같은 컨테이너가 아니라 단순히 여러 구성 요소를 담아두고 관리하는 논리적 최상위 공간 혹은 집합체를 의미)
            - Management Account는 조직을 관리하는 AWS 계정이고, Root는 조직 내 모든 OU와 계정을 포함하는 최상위 컨테이너임
            - Management Account는 SCP의 영향을 받지 않지만, Root에는 SCP를 연결하여 권한을 제한할 수 있음
            - Management Account도 Root라는 컨테이너에 포함되지만, SCP가 적용되지 않음
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
        - 기본 구성에서 자주 사용되는 방식
        - 기본적으로 AWS 서비스 사용을 허용하면서, 특정 서비스나 작업만 제한하는 방식
        - ex. 다음과 같은 정책을 설정한다고 가정
          - EC2 사용 가능
          - S3 사용 가능
          - RDS 사용 가능
          - CloudTrail 비활성화 금지
            -> 이 경우 CloudTrail을 비활성화하는 작업만 명시적으로 거부하면 됨
          - 나머지 AWS 서비스와 작업은 SCP에서 별도로 금지하지 않는 한 기존 권한 정책에 따라 사용 여부가 결정됨
          - Deny List Strategy의 장점
            - 새로운 AWS 서비스가 추가되어도 별도의 허용 정책을 계속 추가할 필요가 적음
            - 특정 보안 위반 행위만 제한 가능
            - 정책 관리가 상대적으로 간단
           
      - 4-2. Allow List Strategy
        - 엄격한 서비스 통제 방식
        - 명시적으로 허용한 서비스와 작업만 사용할 수 있도록 제한하는 방식
        - ex. 다음과 같은 정책을 설정한다고 가정
          - EC2 사용 허용
          - S3 사용 허용
          - RDS 사용 허용
          - 그 외 서비스는 기본적으로 허용하지 않음
          -> 이 정책 전략을 적용하면 명시적으로 허용한 EC2, S3, RDS만 SCP의 허용 범위에 들어감
          - 다만 이 정책 하나만 계정에 연결되었다고 해당 서비스들에 대한 접근 권한이 생기는 것은 아니며, Root부터 대상 계정까지 모든 계층에서 해당 서비스에 대한 작업이 허용되어야 권한이 생김
        - Allow List Strategey의 장단점
          - 장점
            - 조직에서 사용할 수 있는 서비스를 엄격하게 통제할 수 있음
            - 승인되지 않은 AWS 서비스의 사용을 사전에 차단할 수 있음
            - 규제가 엄격한 기업 환경에 적합
          - 단점
            - 새로운 AWS 서비스를 사용하려면 SCP를 수정해야 함
            - 서비스별로 필요한 작업을 빠짐없이 허용해야 함
            - 정책 관리가 복잡해질 수 있음
           
      + AWS는 기본적으로 FullAWSAccess라는 AWS 관리형 SCP를 Root, OU, 계정에 연결함. 이 정책은 모든 서비스와 작업을 허용하는 정책
      -> 따라서 기본 설정에서는 Deny List방식으로 SCP를 활용하기 쉬움
      -> Allow List 전략을 사용하려면 FullAWSAccess를 제거하고 필요한 권한만 허용하는 SCP로 대체해야 함

    - 5. SCP Inheritance: 정책 상속 구조
      - 상위 계층에 연결된 SCP가 하위 계층에도 적용되는 구조
      - ex. Root(SCP A): EC2 허용 -> Development OU(SCP B): S3 허용 -> Account A(SCP C): RDS 허용
      - 위와 같은 경우, Account A는 EC2, S3, RDS에 대한 SCP상의 허용 범위를 가짐
      - 5-1. Allow의 상속
        - Allow list 전략에서 특정 작업을 수행하려면 Root부터 해당 계정까지 모든 계층에서 명시적으로 허용되어야 함
        - 즉, Root와 Account A에서는 S3에 대한 접근 권한이 허용되어있더라도, 중간 단계인 Development OU에서 Allow가 명시되어있지 않다면 Account A는 S3에 대한 접근 권한을 가질 수 없음
      - 5-2. Deny 상속
        - 상위 계층 중 어느 한 곳에서라도 특정 작업을 명시적으로 거부하면 하위 계정에서도 해당 작업을 수행할 수 없음
        - 즉, Root와 Account A에서는 EC2에 대한 접근 권한이 Allow 상태여도, 중간 단계인 Development OU에서 Deny인 경우 Account A는 EC2에 대한 접근 권한이 없음
      - 5-3. 상속 구조 기본 원칙
        1. 상위 OU의 SCP는 하위 OU와 계정에 적용됨
        2. Allow는 대상 계정까지 이어지는 모든 계층에서 허용되어야 함
        3. Deny는 경로 상 어느 한 계층에서라도 Deny되면 하위 계정의 해당 작업을 차단함
        - 명시적 Deny는 항상 다른 어떤 것보다 우선권을 가짐
   - 6. AWS Organizations와 AWS Control Tower
     - 6-1. AWS Control Tower란?
       - 여러 AWS 계정을 안전하고 일관된 방식으로 운영할 수 있도록 다중 계정 환경을 자동으로 구성하고 관리하는 서비스
       - Organizations가 여러 계정을 관리하는 기본적인 틀을 제공한다면, Control Tower는 그 틀을 활용하여 기업에 필요한 보안 및 운영 환경을 자동으로 구축해 줌
       - Landing Zone: 기업이 AWS를 사용하기 위해 마련하는 기본적인 다중 계정 운영 환경
       - Control Tower가 지원하는 작업
         - 다중 계정 환경 자동 구성
         - 권장 OU 및 계정 구조 생성
         - 보안 및 감사 환경 구성
         - AWS CloudTrail 및 AWS Config 등 보안 서비스 통합
         - Guardrails를 통한 보안 정책 적용
         - Account Factory를 통한 신규 계정 생성 및 등록
         - 환경의 설정 이탈(Drift) 감지
      - 6-2. Guardrails란?
        - AWS계정들이 기업의 보안 및 운영 규칙을 준수하도록 통제하는 기능
        - ex.
          - Preventive Control: 위반 행위 사전 차단(ex. 특정 리전에서 리소스 생성 금지)
          - Detective Control: 위반 상태 감지(ex. CloudTrail 설정이 비활성화된 계정 탐지)
          - Proactive Control: 리소스 생성 전 규칙 검증(ex. 규정을 위반하는 CloudFormation 리소스 생성 방지)
        - Guardtails는 SCP와 동일한 개념이 아님
        - SCP는 Organizations의 정책 기능 중 하나이고, Guardrails는 Control Tower가 제공하는 보다 포괄적인 통제 체계
      - 6-3. Organizations와 Control Tower의 차이
        1. Organizations
           - 핵심 역할: 다중 계정 중앙 관리
           - 계정 관리: 계정 생성/초대/이동
           - OU 관리: 직접 구성
           - 정책 관리: SCP, RCP 등
           - 보안 관리: 정책 중심의 통제
           - 설정 자동화: API 등을 통한 자동화
           - 설정 이탈 감지: 직접 다른 서비스와 조합
        2. Control Tower
           - 핵심 역할: 다중 계정 환경 자동 구축 및 통제
           - 계정 관리: Account Factory로 계정 프로비저닝
           - OU 관리: 권장 구조를 자동으로 구성하고 관리
           - 정책 관리: Guardrails를 통해 정책 및 규칙 적용
           - 보안 관리: 예방/탐지/사전 검증 통제
           - 설정 자동화: Landing Zone 자동 구성
           - 설정 이탈 감지: Drift Detection 제공
        - 즉, Control Tower는 Organizations를 대체하는 서비스가 아니라 Organizations를 기반으로 더 높은 수준의 자동화와 거버넌스 기능을 제공하는 서비스

+ IAM Policy vs Permission Boundary vs SCP
  - 모두 AWS 리소스에 대한 접근 권한을 통제한다는 공통점을 지님. 하지만 통제하는 대상과 목적에서 차이가 있음
  - 핵심 정리
    1. IAM Policy: 사용자가 실제로 어떤 작업을 수행할 수 있는지에 대한 권한 부여
    2. Permission Boundary: IAM 사용자 또는 역할이 가질 수 있는 최대 권한 제한
    3. SCP: AWS Organizations에 속한 계정에서 가질 수 있는 최대 권한을 조직 차원에서 제한
  - 간단한 비유
    1. IAM Policy: 직원에게 실제 업무 권한을 부여하는 것
    2. Permission Boundary: 직원이 가질 수 있는 업무 권한의 상한선을 정하는 것
    3. SCP: 회사 전체에서 금지하거나 허용할 수 있는 업무 범위를 정하는 것
   
  1. IAM Policy
     - IAM User, IAM Group, IAM Role 등에 연결하여 AWS 서비스와 리소스에 대한 접근 권한을 부여하거나 제한하는 정책
     - 실제 권한을 부여하는 역할 수행
     - 단, IAM Policy에 Allow가 있다고 반드시 접근 권한이 있다고 단정할 수 있는 것은 아님
     - Permission Boundary, SCP, 명시적 Deny 등 다른 권한 통제 조건도 함께 평가해야 함
  2. Permission Boundary
     - IAM User 또는 IAM Role이 가질 수 있는 최대 권한을 설정하는 정책
     - IAM Policy가 실제 권한을 부여한다면, Permission Boundary는 해당 IAM 주체가 그 권한을 어디까지 가질 수 있는지 제한함
     - Effective Permissoins = IAM Policy와 Permission Boundary의 교집합
     - 2-1. 대표적 활용 사례
       - 관리자: 개발팀의 IAM 사용자 생성을 허용
       - 개발팀 관리자: 직접 IAM 사용자를 생성하고 권한 부여
       - 보안팀: 개발팀 관리자가 부여할 수 있는 최대 권한을 제한
       - 개발팀 관리자가 자신이 생성한 IAM 사용자에게 어떤 IAM Policy를 연결하더라도, 사전에 설정된 Permission Boundary를 초과하는 권한을 사용할 수 없음
       - Permission Boundary는 다른 사람에게 IAM 권한 관리 업무를 위임하면서도, 권한이 무분별하게 확대되는 것을 방지하는데 유용
     - 2-2. 시험에서 기억할 표현
       - Delegate(위임하다) IAM permission management safely
       - Prevent privilege escalation
       - Set the maximum permission for IAM users or roles   
  3. SCP
     - Permission Boundary와 비슷하게 최대 권한을 제한하지만, 적용 대상이 다름
       - Permission Boundary: 특정 IAM User 또는 Role
       - SCP: Organizations에 속한 Member Account의 IAM User, Role 및 Root User
     - ex. 한 기업이 다음과 같은 계정을 운영한다고 가정
       - 개발 계정
       - 운영 계정
       - 테스트 계정
       - 기업 보안팀은 모든 계정에서 특정 리전 이외의 AWS 사용을 금지하려고 함
       - 이때, 각 계정의 IAM 사용자에게 일일이 정책을 설정할 필요 없이, Organizations의 Root 또는 OU에 SCP를 연결하면 간단히 처리 가능

# AWS Control Tower
1. Landing Zone
   - Control Tower가 구축하는 기본 환경
   - 조직이 AWS를 안전하고 일관된 방식으로 사용하기 위해 미리 구성해 놓은 멀티 계정 기반 환경
   - 단순히 AWS 계정을 여러 개 모아놓은 것이 아니라, 계정 구조, 보안, 접근 권한, 로그 수집, 감사 체계까지 담당하는 관리 환경
   - Control Tower에서 Landing Zone을 설정하면 AWS Organizations를 기반으로 여러 AWS 서비스가 연동됨
   - Landing Zone의 주요 구성 요소
     - AWS Organizations: 계정 및 OU의 계층적 관리
     - AWS IAM Identity Center: 사용자와 그룹의 중앙 집중식 계정 접근 관리
     - AWS CloudTrail: AWS 계정에서 발생한 API 활동 기록
     - AWS Config: AWS 리소스 구성 및 변경 사항 추적
     - AWS Control Tower Controls: 조직의 보안 및 운영 규칙 적용
     - AWS Account Factory: 표준화된 신규 AWS 계정 생성
2. Shared Accounts: 세 가지 핵심 계정
   1. Management Account
      - AWS Control Tower를 설정하고 조직 전체를 관리하는 중심 계정
