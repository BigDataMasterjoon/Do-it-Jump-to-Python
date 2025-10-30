### 숫자형 자료형
# 정수형 integer
a = 123
a = -178
a = 0

# 실수형 floating
a = 1.2
a = -3.45
a = 4.24E10 # 지수 표현
a = 4.24e-10

# 8진수
a = 0o177
print(a)

# 16진수
a = 0x8ff
b = 0xABC
print(b)

a = 3
b = 4
a+b #7
a-b # -1
a*b # 12
a/b # 0.75

a**b # 81
# **은 제곱

# 예습
10*18**2+2*11 # 3262

7 % 3
3 % 7

7//3
2/4
7%3

14//3
14%3

### 문자열 자료형
food = "Python's favorite food is perl"
food
food = 'Python's favorite food is perl' # 에러

say = '"Python is very easy." he says'

# 역슬래시를 사용해서 작은 따옴표와 큰 따옴표를 문자열에 포함하기
food = 'Python\'s favorite food is perl'

# 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"
print(multiline)

multiline = '''
life is too short
you need python
'''
print(multiline)

a = "\000"
print(a)
a = "\a 아아아"
print(a)

head = "Python"
tail = " is fun!"
head + tail

a = "Python"
a * 2

a = "Life is too short"
len(a)
b = "You need python"
len(b)

# 문자열 인덱싱
a = "Life is too short, You need python"
a[3]

"""
파이썬은 0부터 숫자를 센다.
"""

a[0]
a[12]
a[-1]


# 응용하여 내가 만든 코드
my_string = "Life is too short, You need python"

reverse_string = ""
for i in range(len(my_string)):
    reverse_index = len(my_string) - 1 - i
    string_piece = my_string[reverse_index]
    reverse_string = reverse_string + string_piece
print(reverse_string)

a = "Life is too short, You need python"
b = a[0]+a[1]+a[2]+a[3]
b

a[0:4]
a[12:17]
a[19:]
a[:17]

# 자주 사용하는 슬라이싱 기법
a = "20250701Sunny"
date = a[:8]
weather = a[8:]

year = a[:4]
day = a[4:8]

# 문자열을 지정하면 바꿀 수 없다.
a = "Pithon"
a[1]
a[1] = 'y'
# 고로 문자열 하나를 바꾸고 싶다면 새로 출력해야됨.
a[:1]+"y"+a[2:]

# 문자열 포매팅
# 1. 숫자 바로 대입
"I eat %d apples." %3

# 2. 문자열 바로 대입
"I eat %s apples." %"five"

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number

# 두 개 이상의 값 넣기
number = 10
day = 'three'
"I ate %d apples. so I was sick for %s days." %(number, day)

"I have %s apples" % 3
"rate is %s" % 3.234

"Erros is %d%%" %98

# 포맷 코드와 숫자 함께 사용하기
"%10s" % "hi" # 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽을 ㅗ정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 것.

"%-10sjane." % "hi"

# 소수점 표현하기
"%0.4f" % 3.42134234

"%10.4f" %3.42134234

#### format 함수 사용
"I eat {0} apples".format(3)
# 'I eat 3 apples'
"I eat {0} apples".format("five")
# 'I eat five apples'

# 숫자 값을 가진 변수로 대입하기
number = 3
"I eat {0} apples".format(number)
# 'I eat 3 apples'

number = 10
day = 'three'
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

"I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = 3)

# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)

# 왼쪽 정렬
"{0:<10}".format("hi")

# 오른 쪽 정렬
"{0:>10}".format("hi")

# 가운데 정렬
"{0:^10}".format("hi")

# 공백 채우기
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")

# 소숫점 표현하기
y = 3.42134234
"{0:0.4f}".format(y)

# {} 문자 표현하기
# 두 번 쓰면 됨
"{{and}}".format()

# f문자열 포매팅
name = '홍길동'
age = 30
f'나으 이름은 {name}입니다. 나이는 {age}입니다.'

f'나는 내년이면 {age+1}살이 된다'

d = {'name' : '홍길동',
     'age' : 30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

# 정렬
f'{"hi":<10}'
f'{"hi":^10}'
f'{"hi":>10}'

# 공백 채우기
f'{"hi":=^10}'
f'{"hi":!^10}'
f'{"hi":!<10}'

# 소숫점 표현
y = 3.42134234
f"{y:0.4f}"
f"{y:10.4f}"


f'{"python":!^12}'

# 문자 갯수 세기-count
a = "hobby"
a.count('b') # 2

# 위치 알려주기 1-find
a = "Python is the best choice"
a.find('b') # 14
# 문자열에서 b가 처음 나온 위치

a.find('k') # 찾는 문자나 문자열이 존재하지 않는다면 -1 반환함.

# 위치 알려주기 2-index
a = "Life is too short"
a.index('t')
a.index('k') # 에러

# 문자열 삽입 - join
",".join('abcd')
#↳'a,b,c,d'

# 소문자를 대문자로 바꾸기 - upper
a = "hi"
a.upper()

# 대문자를 소문자로 - lower
b = "HI"
b.lower()

# 왼쪽 공백 지우기-lstrip
a = " hi "
a.lstrip()

# 오른쪽 공백 지우기-rstrip
a = " hi "
a.rstrip()

# 양쪽 공백 지우기-strip
a = " hi "
a.strip()

# 문자열 바꾸기-replace
a = "Life is too short"
a.replace("Life", "Your leg")

# 문자열 나누기-split
a = "Life is too short"
a.split() # 공백을 기준으로 문자열 나눔.

b = "a:b:c:d"
b.split(':') # :를 기준으로 문자열 나눔.

############## 리스트 자료형

odd = [1, 3, 5, 7, 9]
print(odd)

# 리스트 부터는 인터렉티브로 진행함.

