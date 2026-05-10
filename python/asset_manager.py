asset_goal = 0
asset = 0

income_dict = {}
outcome_dict = {}

def print_menu():
  print('1. 수입 내역 추가(날짜, 항목, 금액)')
  print('2. 지출 내역 추가(날짜, 항목, 금액)')
  print('3. 전체 내역 조회')
  print('4. 현재 자산 현황 및 통계 보기')
  print('5. 데이터 저장 및 종료')

def income_note(asset):
  while True:
    try:
      date = input('날짜를 입력하세요(ex. 20260510): ')
      item = input('항목을 입력하세요(ex. 월급, 이자 등): ')
      amount = int(input('금액을 입력하세요: '))
      income_dict[date] = [item, amount]
      asset += amount
      print(f'현재 자산: {asset}')
      print(f'추가된 수입 내역: {income_dict[date]}')
      return asset
    except ValueError:
      print('잘못된 입력입니다. 다시 입력하세요.')

def outcome_note(asset):
  while True:
    try:
      date = input('날짜를 입력하세요(ex. 20260510): ')
      item = input('항목을 입력하세요(ex. 월세, 통신비 등): ')
      amount = int(input('금액을 입력하세요: '))
      outcome_dict[date] = [item, amount]
      asset -= amount
      print(f'현재 자산: {asset}')
      print(f'추가된 지출 내역: {outcome_dict[date]}')
      return asset
    except ValueError:
      print('잘못된 입력입니다. 다시 입력하세요.')
      
def print_income_outcome():
  print('=== 수입 내역 ===')
  print(income_dict)
  print()
  print('=== 지출 내역 ===')
  print(outcome_dict)

def print_stats():
  print(f'현재 자산: {asset}원')
  print(f'목표 자산: {asset_goal}원')
  if asset >= asset_goal:
    print('목표 자산에 도달했습니다.')
  else:
    print(f'목표 자산까지 남은 금액: {asset_goal - asset}원')

while True:
  try:
    first_asset = int(input('초기 자본을 입력하세요: '))
    asset = first_asset
    break
  except ValueError:
    print('잘못된 입력입니다. 다시 입력하세요.')

while True:
  try:
    asset_goal = int(input('목표 자산을 입력하세요: '))
    break
  except ValueError:
    print('잘못된 입력입니다. 다시 입력하세요.')

while True:
  print_menu()
  try:
    menu = int(input('원하시는 서비스의 번호를 입력하세요: '))
    if menu == 1:
      asset = income_note(asset)
    elif menu == 2:
      asset = outcome_note(asset)
    elif menu == 3:
      print_income_outcome()
    elif menu == 4:
      print_stats()
    elif menu == 5:
      print('프로그램을 종료합니다.')
      break
    else:
      print('잘못된 입력입니다. 다시 입력하세요')
      continue

  except ValueError:
    print('잘못된 입력입니다. 다시 입력하세요.')
    continue
