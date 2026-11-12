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
      - AWS Parent Region <-> Wavelength Zone(통신 사업자 데이터 센터 내부 <-> 5G 스마트폰 및 모바일 기기)
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
           - Wavelength와 통신 사업자 간 네트워크 연결이 가장 큰 역할임

5. Amazon CloudFront
   - CloudFront는 CDN(Content Delivery Network) 서비스로, 전 세계에 분산된 Edge Location을 이용해 사용자에게 콘텐츠를 빠르고 효율적으로 전달함
   - ex. 학국, 미국, 독일에 사용자가 있는 글로벌 쇼핑몰을 운영한다고 가정
     - 쇼핑몰의 이미지와 동영상이 미국의 AWS Region에 있는 S3 버킷에 저장되어 있다면, 한국 사용자가 이미지를 요청할 때 미국까지 데이터를 요청해 가져오느라 지연 시간이 발생하게 됨
     - 이때 CloudFront를 사용하면 사용자가 **자주 요청하는 콘텐츠**를 가까운 Edge Location에 미리 캐싱하여 빠르게 전달할 수 있음
   - CloudFront의 핵심 구성 요소
     1. Origin
        - CloudFront가 사용자에게 전달할 원본 콘텐츠를 가져오는 서버 또는 저장소
        - 대표적 Origin
          - Amazon S3 Bucket
          - Amazon EC2에서 실행되는 웹 서버
          - ALB
          - MediaPackage
          - 외부 HTTP 서버
     2. Distribution
        - CloudFront의 콘텐츠 배포 설정 단위
        - CloudFront를 통해 어떤 콘텐츠를 어디서 가져와 어떻게 사용자에게 전달할 것인지 정의하는 설정
        - Distribution 생성 시 설정 사항
          - Origin 서버
          - Cache Behavior
          - Viewer Protocol Policy
          - Cache Policy
          - HTTPS 인증서
          - 접근 제어 설정
        - CloudFront의 Distribution은 글로벌 서비스로, 특정 리전에 종속되는 일반적 리소스와 다름
     3. Edge Location
        - CloudFront가 사용자에게 콘텐츠를 전달하기 위해 사용하는 전 세계의 분산된 네트워크 거점
        - 사용자가 CloudFront Distribution에 접속하면 DNS가 해당 요청을 적절한 Edge Location으로 연결
        - 무조건 물리적 거리가 가까운 Edge Location으로 연결되는 것은 아니며, 일반적으로 지연 시간 등을 고려해 적절한 Edge Location이 선택됨
     4. Regional Edge Cache
        - Edge Location과 Origin 사이에 위치하는 중간 캐시 계층
        - ex. 특정 이미지가 한국의 Edge Location에서 한동안 요청되지 않아 캐시에서 제거됨
          - 다시 같은 이미지가 요청된 경우, Regional Edge Cache에 해당 콘텐츠가 남아 있다면 Origin까지 가지 않고 Regional Edge Cache에서 콘텐츠를 가져올 수 있음
        - Regional Edge Cache는 일반적인 Edge Location보다 더 큰 캐시 용량을 가지며, 인기 콘텐츠가 아닌 콘텐츠도 매번 Origin에 접근하지 않고 제공될 수 있도록 도움

   - CloudFront의 콘텐츠 전달 과정
     - ex. 상황 가정
       - Origin: 미국 리전의 S3 Bucket
       - 사용자: 대한민국
       - Edge Location: 한국의 CloudFront 거점
       - 동작 순서
         1. 사용자가 콘텐츠 요청
         2. DNS가 적절한 CloudFront Edge Location으로 요청 연결
         3. Edge Location이 캐시에 요청한 콘텐츠가 있는지 확인
         4. 콘텐츠가 있다면(Cache Hit) 바로 사용자에게 전달
         5. 콘텐츠가 없다면(Cache Miss) Regional Edge Cache를 확인하고, 거기에도 없다면 Origin에 요청
         6. **가져온 콘텐츠를 캐시에 저장**하고 사용자에게 전달
       - Regional Edge Cache는 모든 콘텐츠 요청에 반드시 거쳐야 하는 것은 아님, 캐시 계층의 실제 동작은 콘텐츠와 배포 설정에 따라 달라짐

   - TTL과 Cache Policy
     - TTL(Time To Live): 콘텐츠를 캐시에 보관할 시간
       - 웹사이트의 로고 이미지가 자주 변동되지 않는다면 오랜 시간 캐싱해도 됨
       - 반면 실시간 가격 정보처럼 자주 변경되는 데이터는 짧은 시간만 캐싱하거나 캐싱하지 않는 것이 적절
     - CloudFront Cache Policy
       - 세가지 TTL 설정
         1. Minimum TTL: 캐시할 최소 시간
         2. Default TTL: Origin이 별도의 캐시 지시자를 제공하지 않을 때 적용되는 기본 시간
         3. Maximum TTL: 캐시할 수 있는 최대 시간
       - 중요 주의 사항
         - Origin이 Cache-Control: no-cache 또는 no-store를 보내더라도 Min TTL이 0보다 크다면 CloudFront는 TTL 동안 캐싱할 수 있음
         - 즉, 캐싱을 완전히 방지하려면 Cache Policy의 Min TTL을 0으로 설정해야 함
         - 콘텐츠를 변경했는데, 기존 캐시가 계속 전달되는 상황에서는 Invalidation을 사용할 수 있음
         - 그러면 CloudFront가 해당 객체를 기존 캐시에서 무효화하여 다음 요청에서 최신 콘텐츠를 가져오도록 할 수 있음
   - CloudFront의 보안 기능
     - CloudFront는 콘텐츠에 대한 접근 제어 및 보안 기능도 제공함
       1. HTTPS
          - CloudFront는 Viewer와 CloudFront 간 HTTPS 통신을 지원함
          - 또한 Origin과 CloudFront 사이의 통신도 HTTPS로 설정할 수 있음
          - 사용자와 CloudFront 간 연결, CloudFront와 Origin 간 연결은 별개의 통신 구간임
       2.Origin Access Control(OAC)
          - 사용자가 CloudFront를 거치지 않고 S3의 직접 URL로 접근할 수 있다면 CloudFront에서 설정한 접근 제어를 우회할 수 있는 위험이 존재
          - 이를 방지하지 위해 OAC를 사용할 수 있음
          - OAC를 설정하면 지정된 CloudFront Distribution이 S3 객체를 읽도록 권한을 구성할 수 있음
          - 즉, 사용자가 CloudFront를 통해서만 콘텐츠에 접근할 수 있도록 할 수 있음
          - 기존 OAI보다 OAC가 더 권장되며, OAC는 SSE-KMS 암호화와 PUT/DELETE 요청 등의 기능도 지원함
       3. Signed URL과 Signed Cookie
          - 특정 사용자에게만 콘텐츠를 제공해야 한다면 Signed URL 또는 Signed Cookie를 사용할 수 있음
          - ex. 유료 동영상 서비스를 운영한다고 가정
            - Signed URL: **특정 파일 하나**에 대한 접근 권한을 제한할 때 적합(ex. 특정 유료 파일 하나를 다운로드하도록 허용해야하는 경우)
            - Signed Cookie: **여러 파일**에 대한 접근 권한을 한 번에 제공할 때 적합(ex. 동영상 강의의 여러 영상 파일을 재생해야 하는 경우)
   - CloudFront와 Global Accelerator의 차이
     - CloudFront
       - 핵심 목적: 콘텐츠 전송 가속
       - 주요 방식: 콘텐츠 **캐싱**
       - 캐싱: O
       - 프로토콜: 주로 HTTP/HTTPS(Layer 7, 애플리케이션 레이어)
       - 주요 기능: Edge Location, CDN
       - 대표 사례: 이미지, 동영상, 웹 콘텐츠
     - Global Accerlerator
       - 핵심 목적: 애플리케이션 네트워크 연결 최적화
       - 주요 방식: AWS 글로벌 네트워크를 통한 트래픽 라우팅
       - 캐싱: X
       - 프로토콜: TCP/UDP (Layer 3/4, 네트워크 레이어)
       - 주요 기능: 고정 Anycast IP, Endpoint 장애 조치
       - 대표 사례: 게임 서버, API, 글로벌 애플리케이션
    - 구분 방법
      - 전 세계 사용자에게 이미지와 동영상을 빠르게 제공하고 싶다 -> CloudFront
      - 전 세계 사용자의 TCP/UDP 트래픽을 가장 적절한 AWS 엔드포인트로 전달하고 싶다 -> Global Accelerator
    - 특히, CloudFront는 콘텐츠를 캐싱하지만, Global Accelerator는 콘텐츠를 캐싱하지 않는다는 차이를 기억해야 함

+ Home Region과 Parent Region
  - Parent Region과 Home Region이 서로 다른 개념은 아님, 그러나 AWS 서비스별로 공식 용어가 다른 것은 사실임
  - Outposts -> Home Region(Parent Region으로 표현해도 큰 문제 없음)
  - Local Zones -> Parent Region
  - Wavelength -> Parent Region


# IP Addressing
1. IPv4의 구조
  - IPv4란? 
   - 네트워크에서 장치를 식별하고 통신 경로를 지정하기 위해 사용하는 주소 체계
   - 총 32비트(32 bits)로 구성됨
   - 일반적으로 다음과 같은 10진수 형식으로 표현됨
     - 192.168.1.10(.을 기준으로 각각 8bits -> 8 + 8 + 8 + 8 = 32bits)
     - 각 숫자는 8비트로 구성된 Octet(옥텟)
     - 8비트로 표현할 수 있는 값음 0~255이믜로 IPv4 주소의 각 숫자는 항상 0~255 범위에 존재함
     - ex. 192.168.1.10의 2진수 표현
       - 192 = 11000000
       - 168 = 10101000
       - 1 = 00000001
       - 10 = 00001010
     - 32비트로 표현할 수 있는 전체 주소의 개수 = 2의 32승 = 4,294,967,296(약 43억 개)
  - IPv4주소의 Network와 Host
    - IPv4주소는 크게 두 부분으로 구분됨
      - Network Portion: 해당 IP 주소가 속한 네트워크를 식별
      - Host Portion: 해당 네트워크 내부의 개별 장치를 식별
        - ex. 192.168.1.10/24 -> 앞의 24비트가 Network Portion이라는 의미
        - 즉, 192.168.1은 네트워크 식별을 위한 정보, 10은 호스트 식별의 위한 정보임
        - 따라서 192.168.1.10/24의 의미
          - Network Address: 192.168.1.0
          - Host Address: 2192.168.1.10
          - Broadcast Address: 192.168.1.255
        - 즉, 192.168.1.0/24라는 네트워크 안에 여러 장치가 존재할 수 있으며, 각가의 장치는 서로 다른 Host Address를 할당 받음

2. CIDR과 Subnet Mask
   - CIDR이란?
     - IP 주소에서 Network Portion이 몇 비트인지 나타내는 표기법(ex. 192.168.1.10/24에서 /24부분)
     - 예시에서 설명한 바와 같이, CIDR 숫자가 커질수록 Network Portion이 커지고, Host Portion은 작아짐
   - Subnet Mask란?
     - Network Portion과 Host Portion을 구분하기 위한 **32비트 값**
     - ex. /24의 Subnet Mask는 11111111.11111111.11111111.00000000
     - CIDR과 Subnet Mask는 서로 다른 개념이 아니라 동일한 네트워크 경계를 서로 다른 형식으로 표현한 것.
     - 이해를 위한 추가 예시
       - ex. /25 = 255.255.255.128 -> 총 25비트가 Network Portion이므로 마지막 자리를 2진수로 표현하면 .10000000임. 이를 다시 10진수로 변환하면 128이므로 위와 같은 Subnet Mask가 나타나게 됨.
       - /27도 동일한 방식으로 계산하여 마지막 자리는 128 + 64 + 32 = 224이므로 255.255.255.224가 Subnet Mask가 됨
   - IP 주소 개수 계산
     - IPv4 네트워크의 전체 주소 개수는 다음 공식으로 계산됨
     - 2^(32-CIDR Prefix)
     - ex. /24라면 Host Portion이 8이므로 해당 네트워크의 주소 개수는 2의 8승인 256개임
     - 주의사항 -> 일반적인 IPv4 서브넷에서는 네트워크 주소와 브로드캐스트 주소를 호스트에 할당하지 않으므로, 사용 가능한 주소는 전체 개수에서 2개를 제외함.
     - ex. 일반적인 /24 네트워크는 256개 중 254개를 호스트에서 사용할 수 있음
     - AWS VPC Subnet은 다름. 추후 설명 예정

3. Private IP Address Ranges
   - Public IP와 Private IP
     1. Public IP
        - 사용 범위: 인터넷에서 라우팅 가능
        - 인터넷에서 직접 접근: 가능(보안/라우팅 조건 충족 시)
        - 주소 중복: 전 세계적으로 고유해야 함
        - 주요 사용처: 인터넷 서비스 서버
     2. Private IP
        - 사용 범위: 사설 네트워크 내부
        - 인터넷에서 직접 접근: 불가
        - 주소 중복: 서로 다른 사설 네트워크인 경우 중복 가능
        - 주요 사용처: 내부 서버, DB, 사내 네트워크
   - RFC 1918: Private IPv4 Address Ranges
     - Private IP 주소는 RFC 1918이라는 표준에 정의되어 있음(Class A,B,C는 과거의 Classful Addressing 체계에 따른 범위의 별칭임. 현재 CIDR 기반 네트워크 설계에서는 클래스 자체보다 CIDR Prefix를 기준으로 판단함
       1. Class A: 10.0.0.0/8 (16,777,216개 주소 / 2의 24승)
       2. Class B: 172.16.0.0/12 (1,048,576개 주소 / 2의 20승)
       3. Class C: 192.168.0.0/16 (65,536개 주소 / 2의 16승)
     - 특히, 172번 대역이 자주 등장함
       - 172.16.0.0 ~ 172.31.255.255 -> Private IP
       - 172.15.0.1 -> Private IP 아님
       - 172.32.0.1 -> Private IP 아님
       - 따라서 시험에서는 172.16/12라는 범위를 정확하게 기억하는 것이 중요
   - Private IP의 특징
     - Private IP는 인터넷에 직접 라우팅되지 않음
     - ex. 두 개의 서로 다른 네트워크에서 다음과 같은 주소를 사용한다고 가정
       - 회사 A: 192.168.1.10
       - 회사 B: 192.168.1.10
       - 두 네트워크는 서로 독립된 네트워크이므로 동일한 Private IP를 사용해도 무방함
       - 하지만 두 네트워크를 VPN이나 Direct Connect로 연결하려는 경우에는 IP 주소 범위가 겹치면서 라우팅이 모호해져 문제가 발생할 수 있음
       - 따라서 VPC와 온프레미스 네트워크를 VPN 또는 Direct Connect로 연결하는 시나리오에서는 CIDR Block이 서로 겹치지 않도록 설계해야 함

4. AWS VPC에서의 IP Addressing
   - VPC CIDR Block
     - VPC를 생성할 때 해당 VPC가 사용할 IPv4 CIDR Block을 지정해야 함
     - ex. VPC CIDR: 10.0.0.0/16
     - 이는 VPC에서 총 65,536(2의 (32 - 16)승)개의 IPv4 주소 범위를 확보한다는 의미임
     - AWS VPC의 IPv4 CIDR 크기는 기본적으로 /16부터 /28까지 지정할 수 있음
   - VPC를 Subnet으로 분할하기
     - 하나의 VPC는 여러 Subnet으로 나눌 수 있음
     - ex. 10.0.0.0/16 VPC를 다음과 같이 분할 가능
       - Public Subnet(AZ-A): 10.0.1.0/24
       - Private Subnet(AZ-A): 10.0.2.0/24
       - Private Subnet(AZ-B): 10.0.3.0/24
     - 중요 규칙
       1. Subnet의 CIDR은 VPC의 CIDR 범위 안에 포함되어야 함(10.0.0.0/16이므로 Subnet의 IP는 10.0까지는 동일해야 함)
       2. 동일 VPC 내 Subnet들의 CIDR은 서로 겹치면 안됨
       3. 각 Subnet은 하나의 AZ에 속함
       4. 하나의 VPC는 여러 AZ에 걸쳐 Subnet을 생성할 수 있음
       5. 동일한 VPC 안에 IP 주소가 겹치는 경우가 없어야 함
          - ex. 다음 두 Subnet은 사용할 수 없음
            - Subnet A: 10.0.1.0/24
            - Subnet B: 10.0.1.128/25
          - 두 주소의 범위가 Subnet A의 마지막 8비트 숫자가 128을 넘어가는 순간부터 128개가 겹치므로 불가
   - AWS가 예약하는 5개의 IP 주소
     - 일반적인 네트워크에서는 Network Address와 Broadcast Address를 제외한 주소를 호스트에 사용할 수 있음
     - 그런데 AWS VPC의 IPv4 Subnet에서는 총 5개의 IP 주소를 AWS가 예약함
     - ex. 10.0.1.0/24 Subnet을 생성했다고 가정
       - 10.0.1.0 -> Network Address
       - 10.0.1.1 -> VPC Router
       - 10.0.1.2 -> Amazon 제공 DNS Server
       - 10.0.1.3 -> 향후 사용을 위해 예약
       - 10.0.1.255 -> Broadcast Address
     - 따라서 전체 256개의 주소 중 5개를 제외한 251개만 사용할 수 있음
     - 특히 AWS에서는 Subnet의 /28이 주소 개수의 하한선임. 즉, /27, /24 등은 가능하지만, /31, /30 등은 불가능함. 참고로 /28은 사용 가능한 주소가 11개뿐임(2의 (32-28)승 - 5)

5. Public Subnet과 Private Subnet의 관계
   - AWS에서는 Subnet의 Public/Private 구분이 IP 주소만으로 결정되지 않음
   - Public Subnet
     - 일반적으로 Route Table에 다음 경로가 설정된 Subnet임
     - Internet Gateway를 통해 인터넷과 통신할 수 있도록 라우팅이 설정된 것
     - 단, EC2가 실제로 인터넷과 직접 통신하려면 Public IPv4주소 또는 Elastic IP 등도 필요하며, Security Group과 NACL 등의 조건도 충족해야 함
   - Private Subnet
     - 일반적으로 Internet Gateway로 향하는 직접적인 기본 경로가 없는 Subnet
     - 대신 NAT Gateway를 통해 인터넷으로 나가는 경로를 구성할 수 있음(NAT instance도 가능)
     - NAT Gateway를 활용하면 Private Subnet에 있는 EC2 instance가 인터넷으로 요청을 보낼 수 있지만, 일반적인 NAT Gateway 구성에서는 외부 인터넷이 인스턴스로 접근할 수는 없음


# Amazon VPC
1. Amazon VPC란?
  - VPC의 개념
    - AWS 클라우드 내에 논리적으로 격리된 가상 네트워크를 생성할 수 있도록 해주는 서비스
    - AWS 안에 자신만의 네트워크 공간을 만드는 것
    - VPC를 생성하면 다음과 같은 네트워크 환경을 구성할 수 있음
      - IP Address Range(CIDR Block) 지정
      - Subnet 생성
      - Route Table을 통한 네트워크 경로 설정
      - Internet Gateway를 통한 인터넷 연결
      - NAT Gateway를 통한 아웃바운드 인터넷 연결
      - Security Group 및 Network ACL을 통한 트래픽 제어
  - VPC의 주요 특징
    - Logical Isolation: 다른 VPC와 논리적으로 격리되어있음
    - Regional Resource: 하나의 AWS Region에 생성
    - Multi-AZ: 여러 AZ에 걸쳐 Subnet 구성 가능
    - CIDR Block: VPC가 사용할 IP 주소 범위 지정
    - Custom Network: Route Table, Gateway, Security Group 등으로 네트워크 구성
  - VPC는 Region 단위의 리소스이며, Subnet은 AZ 단위의 리소스임
    - ex. 서울 리전에 VPC를 하나 생성한 다음 서로 다른 AZ에 Subnet을 각각 배치할 수 있음
2. VPC CIDR Blocks
  - VPC CIDR Block이란?
    - 해당 VPC에서 사용할 수 있는 IPv4 주소의 범위를 의미함
    - ex. 10.0.0.0/16으로 CIDR Block을 설정했다고 가정
      - Network Portion: 16bits
      - Host Portion: 16bits
      - 전체 IPv4 주소 개수 = 2의 16승개 = 65,536개
      - 주소 범위: 10.0.0.0 ~ 10.0.255.255
    - AWS VPC의 기본 IPv4 CIDR Block은 /16부터 /28까지 지정할 수 있음
    - AWS에서 VPC CIDR을 설정할 때 고려사항
      - RFC 1918 Private IP 범위를 주로 사용함
      - VPC의 CIDR은 기존 네트워크와 겹치지 않도록 설계하는 것이 좋음
      - VPC에 여러 IPv4 CIDR Block을 연결할 수도 있음
      - 추가 CIDR Block을 연결하면 VPC에서 사용할 수 있는 IP 주소 범위를 확장할 수 있음
    - Primary CIDR과 Secondary CIDR
      - Primary IPv4 CIDR: VPC 생성 시 지정하는 기본 CIDR(기본 IP 주소 범위)
      - Secondary IPv4 CIDR: 이후 VPC에 추가로 연결하는 CIDR(추가로 확보한 IP 주소 범위)
    - VPC CIDR과 Subnet CIDR의 관계
      - VPC CIDR은 전체 네트워크의 주소 범위이고, Subnet CIDR은 그 범위를 더 작은 네트워크로 나눈 것
      - ex. 다음과 같은 설계 가능
        - VPC CIDR: 10.0.0.0/16 -> 65,536개
        - Public Subnet A: 10.0.1.0/24 -> 256개
        - Public Subnet B: 10.0.2.0/24 -> 256개
        - Private Subnet A: 10.0.3.0/24 -> 256개
        - Private Subnet B: 10.0.4.0/24 -> 256개
      - 모든 Subnet CIDR은 반드시 VPC CIDR 안에 포함되어야 하고, Subnet CIDR끼리 겹치는 부분이 존재하면 안 됨.
     
3. Subnet
   - VPC 공간을 더 작은 네트워크로 분할한 것
   - Subnet의 기본 개념
     - VPC CIDR Block의 일부 주소 범위를 할당받아 생성
     - ex. VPC CIDR이 10.0.0.0/16이라면 다음과 같이 Subnet을 구성할 수 있음
       - 10.0.1.0/24
       - 10.0.2.0/24 등
     - 하나의 Subnet은 반드시 하나의 AZ에 속함
     - 따라서 고가용성을 확보하려면 여러 AZ에 Subnet을 분산 배치해야 함
   - Public Subnet과 Private Subnet
     1. Public Subnet
       - Public Subnet은 연결된 Route Table에 Internet Gateway로 향하는 경로가 있는 Subnet임
       - ex. 경로
         - 10.0.0.0/16    타겟: local
         - 0.0.0.0/0      타겟: Internet Gateway
         - 0.0.0.0/0은 모든 IPv4 주소를 의미하는 기본경로(/0이므로 마스킹된 부분도 없음)
         - 따라서 외부 인터넷과 통신할 수 있는 네트워크 경로가 만들어짐
       - 단, Public Subnet에 EC2를 배치했다고 자동으로 인터넷에 접근할 수 있는 것은 아님
       - EC2에 Public IP가 있어야 하고, Security Group과 NACL 등의 조건도 충족해야 함
     2. Private Subnet
       - Internet Gateway로 직접 연결되는 경로가 없는 Subnet
         - 일반적으로 다음과 같이 구성
           - ex.
           - 10.0.0.0/16     타겟: local
           - 0.0.0.0/0       타겟: NAT Gateway
         - 이와 같이 구성하면 Private Subnet에서 NAT Gateway를 통해 인터넷으로 요청을 보낼 수 있음.
         - 하지만 외부 인터넷에서 Private Subnet의 EC2로 직접 새로운 연결을 시작할 수는 없음
   - Public과 Private Subnet 비교
     - Public Subnet
       - Internet Gateway 직접 경로: 있음
       - 인터넷으로 Outbound 통신: 가능
       - 인터넷에서 직접 접근: 조건 충족 시 가능
     - Private Subnet
       - Internet Gateway 직접 경로: 없음
       - 인터넷으로 Outbound 통신: NAT Gateway를 통해 가능
       - 인터넷에서 직접 접근: 일반적으로 불가능
     + Isolated Subnet: 외부 네트워크로 향하는 경로가 아예 없는 Subnet. VPC 내부 통신만 허용하는 형태로 사용 가능
     + VPN-only Subnet: 인터넷 게이트웨이 대신 VPN을 통해 온프레미스 네트워크와 통신하도록 구성 가능
    
4. AWS Public and Private Services
  - Public Service Endpoint: AWS 서비스의 공개된 엔드포인트를 통해 접근
    - ex. Amazon S3, Amazon DynamoDB, Amazon SQS, AWS Systems Manager
  - Private Connectivity: VPC 내부에서 사설 네트워크 경로를 통해 AWS 서비스에 접근 
    - VPC Endpoint
      1. Gateway Endpoint
         - Amazon S3와 Amazon DynamoDB에서 사용가능
         - 특징
           - Route Table에 Endpoint를 대상으로 하는 경로 추가
           - 별도의 ENI를 생성하지 않음
           - NAT Gateway나 Internet Gateway를 거치지 않고 서비스에 사설 경로로 접근 가능(즉, 인터넷을 거치지 않고 리소스에 접근 가능)
           - Gateway Endpoint 자체에는 별도의 시간당 사용 요금이 없음
      2. Interface Endpoint
         - 대부분의 AWS 서비스와 AWS Private Link를 활용하는 서비스에서 사용 가능
           - ex. AWS Systems Manager, Amazon CloudWatch, AWS Secrets Manager, AWS Key Management Service, Amazon SNS
         - 특징
           - Subnet에 ENI를 생성
           - 해당 ENI에 Private IP 할당
           - Private IP를 통해 AWS 서비스에 접근
           - 일반적으로 시간당 요금과 데이터 처리 요금이 발생함
    - Gateway Endpoint vs Interface Endpoint
      - Gateway Endpoint
        - 기반 기술: VPC Endpoint
        - 연결 방식: Route Table
        - ENI 생성: 없음
        - 지원 서비스: S3, DynamoDB
        - 요금: Endpoint 시간당 요금 없음      
        - NAT Gateway: 불필요
        - Internet Gateway: 불필요
      - Interface Endpoint
        - 기반 기술: AWS Private Link
        - 연결 방식: ENI 및 Private IP
        - ENI 생성: 있음
        - 지원서비스: 다양한 AWS 리소스 및 일부 외부 서비스
        - 요금: 시간당 및 데이터 처리 요금 발생
        - NAT Gateway: 불필요
        - Internet Gateway: 불필요   
  - 시험에서의 구분방법
    - S3 또는 DynamoDB에 인터넷 없이 사설 연결 -> Gateway Endpoint
    - Systems Manager, CloudWatch 등 다양한 AWS 서비스에 사설 연결 -> Interface Endpoint
    - 다른 AWS 계정의 서비스나 지원되는 SaaS 서비스에 사설 연결 -> AWS Private Link
    + S3와 DynomoDB도 Interface Endpoint를 지원하는 구성이 있으므로, 두 서비스는 Gateway Endpoint만 사용할 수 있다고 외우면 안됨. 다만 일반적인 비용 효율적인 VPC 접근 문제에서는 Gateway Endpoint를 사용하는 것이 적절함
