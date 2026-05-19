1. 리스트 컴프리헨션(List comprehesion)
   - style : [x for y in data]
   - 대괄호 [] 사용 (use [])
   - 결과를 한꺼번에 다 만들어서 메모리에 올림 (create all results instantly)
   - 메모리 차지(memory) : 데이터의 양만큼 메모리를 차지함 (occupy memory by the amount of memory)
   - 속도(speed) : 소량의 데이터일 경우에만 빠름 (fast only when the amount of memory is small)
   - 재사용성(reusablilty) : 여러 번 다시 사용 가능 (high reusablilty)

2. 제너레이터 표현식(Generator expression)
   - style : (x for y in data)
   - 괄호 () 사용 (use ())
   - 결과를 미리 만들지 않고 필요할 때마다 전달 (create results only if it needs)
   - 메모리 차지(memory) : 필요할 때만 결과가 나오므로 적은 메모리 차지 (occupy only small amount of memory)
   - 속도(speed) : 매우 빠른 편, 대량의 데이터를 처리할 때 유리 (very fast, very useful when you have to process huge amount of data)
   - 재사용성(reusablilty) : 일회용 (can use it only once)

왜 [student_management_advanced.py]에서 제너레이터 표현식을 사용했는가?
(Why did I use generator expression in [student_management_advanced.py]?)
- 성적의 합계만 알면 됐지, 성적들을 따로 리스트로 모아둘 필요가 없었기 때문 (because I didn't have to make list of grades. all I need was just total of grades)
- 리스트 컴프리헨션에 비해 메모리를 아끼면서 같은 결과를 낼 수 있었음 (Can make same result while saving memorys)
