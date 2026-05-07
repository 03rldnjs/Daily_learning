# Class

class안에 함수들이 들어있는 구조 / class includes several functions

1. class 선언 방법
   - class 클래스 이름:    /    class name of the class:
       변수나 메소드(함수)  /      variables or method(functions)
   - 메소드(함수)의 첫번째 매개변수는 반드시 'self'여야 함 / method's(function's) first parameter should be 'self'
   - ex) class examples:
           def example(self):
             ...

2. 객체 만들기 / create instance
   - class를 선언한 다음 해당 클래스 밖에서 클래스의 이름을 불러주면 객체가 생성됨 / after declare class, you can create instance by write class's name out of the class
   - ex) e1 = examples()
   - class를 선언할 때에는 ()가 붙지 않지만 객체를 만들때에는 ()를 붙여줘야함 / you should put () when you are creating instance
   - 객체를 만들지 않으면 class내부의 함수를 호출해도 소용없음 / functions in class are not gonna work if you didn't create the instance
  
3. __init__
   - __init__을 활용하면 객체를 만드는 순간 변수를 만들고 초기화할 수 있음 / you can create instance and variables and lnitialize the variables at the same time
   - ex) class examples:
           def __init(self, n, a):
             self.name = n
             self.age = a
     e1 = examples('홍길동', 20)  // create instance and variables, initialize the variables at the same time
     print(f'name: {e1.name}, age: {e1.age}')
     출력 결과: name: 홍길동, age: 20
   - __init__ 도 함수의 일종 / __init__ is also kind of functions

          
