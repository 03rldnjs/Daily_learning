# Amazon Virtual Private Cloud(VPC)
# AWS Global Infrastructure
- 전 세계에 분산된 AWS 인프라를 통해 고가용성, 낮은 지연 시간, 재해 복구 및 글로벌 서비스 제공을 가능하게 하는 기반
1. Region과 AZ(SAA를 위한 추가 지식)
  1. Region 선택 고려 사항
    1. 데이터 주권 및 규정 준수
    2. 사용자와의 지리적 거리 및 지연 시간
    3. 서비스 및 기능의 제공 여부
    4. 비용
    5. 재해 복구 및 가용성 요구사항
    -> 특정 AWS 서비스가 특정 Region에서 제공되지 않는 상황이라면, 다른 Region을 선택하거나 해당 리전에서 지원하는 대체 아키텍처를 고려해야 함
  2. AZ ID와 AZ Name의 차이
    - AZ Name: ap-northeast-2a처럼 표시되는 AZ 이름
    - AZ ID: apne2-az1처럼 표시되는 AZ의 고유 식별자
    - AZ Name은 AWS 계정마다 동일한 AZ를 다른 Name으로 표기될 수 있지만, AZ ID는 계정 간에도 동일한 물리적 AZ를 식별함
    - 즉, 두 계정에서 ap-northeast-2a라는 이름(AZ Name)이 같더라도 실제 물리적 AZ는 각각 apne2-az1, apne-az2로 다를 수 있음
    - AZ Name을 계정마다 달리 표현하여 특정 AZ에 트래픽이 몰리지 않도록 하고, 보안성을 향상시킴
  3. Multi-AZ와 Multi-Region은 해결하는 장애 범위가 다름
    - Multi-AZ는 하나의 리전 내에서 AZ 규모로 발생하는 장애에 대한 대응을 함(Region 내 사설 네트워크를 통해 AZ간 연결)
    - Multi-Region은 서로 다른 Region에 리소스나 서비스를 배치하여 Region 전체 규모의 장애에 대한 대응을 함(Region간 연결)

2. AWS Outposts
   - AWS의 인프라와 서비스를 고객의 온프레미스 환경으로 확장하는 서비스
   - AWS가 제공하는 하드웨어를 고객의 데이터센터나 사내 서버실에 설치하고, 그곳에서 AWS 서비스를 실행할 수 있도록 하는 것
   - 즉, AWS 클라우드의 운영 방식과 API를 유지하면서도 물리적인 실행 장소를 고객의 온프레미스 환경에 두는 서비스
   - Outposts를 사용하는 이유
     1. Low Latency(낮은 지연 시간)
        - 일반 AWS Region에 애플리케이션을 배치하면 온프레미스 시스템에서 AWS Region까지 네트워크를 통해 통신해야 함
        - 하지만 Outposts를 사용하면 애플리케이션을 온프레미스 시스템과 가까운 곳에서 실행할 수 있으므로 네트워크 지연 시간이 감소됨
     2. 데이터 로컬 처리
        - 기업의 데이터가 외부 AWS 데이터센터로 이동하기 전에 로컬 데이터센터 내부에서 처리되어야 하는 경우, 해당 데이터를 현장의 로컬에서 처리한 후, 이외의 데이터만 AWS Region으로 전달하여 처리할 수 있음
     3. 온프레미스 의존성 애플리케이션 Manage 가능
        - 기존 기업 시스템 중에서는 물리적 서버, 네트워크 장비, 데이터베이스 등 온프레미스 인프라에 강하게 의존하는 애플리케이션이 있음
        - 이 시스템들을 완전히 클라우드로 이전하기 어려운 경우 Outposts를 활용할 수 있음
    - Outposts의 구조
      - Outposts(On-premise)와 AWS Region이 연결되어있는 구조
      - 주요 개념 두가지
        1. Service Link(Home Region <-> Outposts)
           - **Outposts와 해당 Outposts의 Home Region을 연결**하는 암호화된 VPN(Virtual Private Network) 연결
           - 용도
             - Outposts의 관리 및 모니터링
             - 펌웨어 및 소프트웨어 업데이트
             - Region과 Outposts 간 VPC 트래픽 전달
             - Region의 AWS 서비스와 연동
           - 즉, Outposts는 고객 데이터 센터에 설치되어 있지만, AWS Region과 지속적으로 연결되어 운영되는 구조
           - 시험 point
             - Outposts는 Region과의 연결이 중요한 서비스
             - Service Link가 끊어지면 관리 및 Region 의존 작업에 영향을 미칠 수 있으므로 연결의 가용성을 고려해야 함.
        2. Local Gateway(On-premise <-> Outposts)
           - **Outposts와 고객의 온프레미스 네트워크를 연결**하는 네트워크 구성 요소
           - 사내 네트워크와 데이터 통신을 주 목적으로 함
           - Local Gateway는 Outposts Rack의 네트워크 구성 요소이며, Outposts Server에서는 Local Network Interface 등 다른 연결 방식을 사용함
      - Outposts는 Region과 AZ 중 어디에 속할까?
        - Outposts는 또다른 하나의 독립적 Region이 아님
        - 각 Outposts는 특정 리전의 특정 AZ에 연결되며, 해당 AZ의 확장으로 동작함(데이터센터가 해당 AZ에 존재하는 것은 아니지만, 해당 AZ에 존재하는 것처럼 동작)
        - VPC는 리전에 생성하지만, Outposts에 리소스를 배치하려면 해당 VPC에 Outpost Subnet을 생성해야 함
        - 이 Subnet에 EC2 인스턴스를 배치하면 실제 컴퓨팅은 고객 데이터센터에 설치된 Outposts 하드웨어서 처리 및 실행됨
      - Outposts의 하드웨어 관리
        - AWS가 하드웨어를 설치하고 관리하는 Fully Managed Service
        - 다만 고객의 시설에 설치되는 것이므로 고객도 전력, 공간, 냉각, 네트워크 연결 등 설치 환경을 준비해야 함
        - 모든 AWS 서비스가 Outposts에서 지원된다고 단정할 수 없음. Outposts의 형태와 Home Region에 따라 차이가 있으므로 사전에 확인하여야 함

3. AWS Local Zones
   - AWS Region의 인프라를 주요 대도시와 같은 특정 지역으로 확장하여, 최종 사용자와 가까운 곳에서 AWS 리소스를 실행할 수 있도록 하는 서비스
   - AWS Region의 데이터센터가 사용자와 멀리 떨어져 있어 지연 시간이 발생하는 경우, 사용자와 가까운 지역에 일부 AWS 인프라를 제공
     - ex. 미국의 주요 도시에서 사용자가 실시간 영상 편집 서비스를 제공한다고 가정
        - 사용자가 AWS Region까지 멀리 이동하지 않고 도시 인근의 Local Zone에서 실행되는 EC2 인스턴스에 접근하도록 구성하면 지연 시간을 단축시킬 수 있음
    - 핵심 특징
      1. 사용자와 가까운 곳에서 컴퓨팅 및 스토리지 제공
         - Local Zones는 지연 시간에 민감한 작업에 적합
           - 실시간 게임
           - 미디어 콘텐츠 제작 및 렌더링
           - 가상 데스트톰
           - 실시간 영상 처리
           - 지연 시간에 민감한 애플리케이션
      2. Parent Region과 연결
         - Local Zone 역시 독립적인 Region이 아님
         - 특정 AWS Region에 연결된 확장 인프라
         - 연결된 특정 리전을 Parent Region이라고 부름
      3. 역시 모든 AWS 서비스를 제공하는 것은 아님
         - AZ와 비교할 때 중요한 포인트
         - AZ는 리전의 핵심 인프라로서 폭넓은 AWS 서비스를 제공하지만, Local Zone은 지연 시간에 민감한 워크로드에 필요한 일부 서비스 중심으로 구성됨
         - 따라서 경우에 따라 사용할 수 없는 AWS 서비스가 존재할 수 있음 -> 지원 서비스 확인 필요
         - Local Zone에서 컴퓨팅을 실행하면서 다른 서비스는 Parent Region에서 이용하는 형태로 설계할 수 있음
         - 즉, 별도의 독립적인 VPC를 새로 만드는 것이 아니라 기존 VPC를 Local Zone까지 확장하는 방식
      
4. AWS Wavelength Zones
   - AWS Wavelength
     - 통신 사업자의 5G 네트워크 내부에 AWS 컴퓨팅 및 스토리지 인프라를 배치하여, 5G 모바일 기기와 사용자에게 초저지연 서비스를 제공
     - Local Zones와 마찬가지로 사용자와 가까운 곳에서 AWS 리소스를 실행한다는 공통점이 있음
     - 하지만 Wavelength는 특히 통신 사업자의 5G 네트워크와 연결된다는 점이 핵심적 차이
   - Wavelength를 사용하는 이유
     - 일반적인 5G 모바일 서비스의 통신 구조
       - 스마트폰에서 실시간 게임을 실행하고 있다고 가정할 때, 기존의 구조에서는 스마트폰의 요청이 통신 사업자의 네트워크를 거쳐 AWS Region까지 이동해야 할 수 있음
       - 이 과정에서 물리적인 거리오아 네트워크 경로로 인한 지연시간이 발생함
       - Wavelength를 사용하면 통신 사업자의 5G 네트워크 내부에 AWS 인프라를 배치할 수 있음
       - 대표적 활용 사례
         - 5G 기반 클라우드 게임
         - 자율주행 차량 및 커넥티드 카
         - 실시간 영상 스트리밍 및 처리
         - IoT 및 산업용 모바일 장치
         - AR/VR 서비스
    - Wavelength의 구조
      - AWS Parent Region <-> Wavelength Zone(통신 사업자 데이터 센터 내부) <-> 5G 스마트폰 및 모바일 기기
      - 중요 구성 요소 2가지
        1. Wavelength Zone
           - 통신 사업자(SKT, KT, U+ 등)의 데이터센터에 배치된 AWS 인프라
           - 일반적인 AWS Region과 달리 통신 사업자의 5G 네트워크에 직접 연결되는 위치에 배치
           - Wavelength Zone은 Parent Region의 논리적 확장. 따라서 VPC를 Parent Region에서 생성한 후 Wavelength Zone에 Subnet을 생성하여 EC2 등의 리소스를 배치해야 함
        2. **Carrier Gateway**
           - 주요 역할
             - 특정 위치의 통신 사업자 네트워크에서 들어오는 트래픽 허용
             - 통신 사업자 네트워크로 나가는 트래픽 전달
             - 인터넷으로 나가는 아웃바운드 트래픽 전달
           - Wavelength와 통신 사업자 간 네트워크 연결
