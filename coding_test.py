# 프로그래머스 코딩테스트 입문
from numpy import array


# 24.08.28

# <1> 배열 두 배 만들기
# map + lambda 사용하여 코딩  --> ( lambda 인자 : 표현식 , 반복할 객체)
# map + lambda가 생각보다 느리다.
# map > list comprehension > map + lambda > for loop

def test01(numbers):
    return list(map(lambda x : x * 2 ,numbers))

## list comprehension ==> [수행문1/ if 조건문/ else 수행문2/ for 변수 /in 리스트]
def test01_1(numbers):
    return [i * 2 for i in numbers ]

# <2> 나머지 구하기
def test02(num1, num2):
    return num1 % num2

# 24.08.29
# <3> 중앙값 구하기
def test03(array):
    array01 = sorted(array)
    len_number = len(array)
    middle_index = len_number // 2
    middle_value = array01[middle_index]
    return middle_value

def test03_1(array):
    value_arange = sorted(array)
    middle_index = len(value_arange) // 2
    middle_value = value_arange[middle_index]
    return middle_value

''''
1. 정렬
2. 인덱스 구하기
3. 중앙값 출력
'''

# 24.08.31 - 24.09.01
# 최빈값 구하기
import statistics
def test04_1(array):
    mode_value = statistics.mode(array)
    return mode_value
 # -> -1을 리턴하지 못한다.

def test04(array):
    count = [0] * (max(array) + 1)
    # [0]을 곱하는 이유는 모든 요소가 카운드 초기값을 0으로 맞추기 위함
    # max(array) + 1는 예를들어 [0, 1, 2, 3 ,4]가 있다고 한다면 max값은 4인데 총 숫자 개수는 5칸이다.
    # 따라서 0의 자리를 만들기 위해 +1을 넣는다.
    # print(count) 현재까지 결과 [0, 0, 0, 0, 0]

    for i in array:
        count[i] += 1
    # 반복문을 통해 실제 각 요소의 개수가 들어오면 카운트가 올라가는 코딩을 작성한다.


    m = 0
    for j in count:
        if j == max(count):
            m = m + 1

    if m > 1:
        return -1
    else:
        return count.index(max(count))

# 거의 보다싶이 했다. 어떤 식으로 접근은 해야할지 알겠으나 코드로 구현 자체가 안된다.
# 다양한 코드를 활용해보고 익숙해지는 개념을 토대로 사고하는게 중요하다고 판단된다.


# 24.09.01
# 짝수는 싫어요
'''
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요
'''
import numpy as np
def test05(n):
    result = np.arange(1,n+1,2)
    return result.tolist()
# 넘파이를 이용한 풀이 방법

def test05_1(n):
    return list(range(1,n+1,2))


# 24.09.02
def test06(n):
    return (n+6) // 7

def test06_1(n):
    return (n - 1) // 7 + 1


# 24.09.03 - 피자 나눠 먹기 (2)
def test07(n):
    pizza = 1

    while True:
        if(pizza * 6) % n == 0:
            return pizza
        pizza += 1


# 24.09.04

# 복습 두 수의 합
'''정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요 '''
def test08(num1, num2):
    return num1 + num2

# 두 수의 차
'''정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.'''
def test08_1(num1, num2):
    return num1 - num2

# 두 수의 곱
'''정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.'''
def test08_2(num1, num2):
    return num1 * num2

# 몫 구하기
'''정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.'''
def test08_3(num1, num2):
    return num1 // num2

# 두 수의 나눗셈
'''정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요'''
def test08_4(num1, num2):
    return int((num1 / num2) * 1000)

# 숫자 비교하기
'''정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요'''
def test08_5(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1

# 분수의 덧셈
'''
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''
import math
def test08_6(numer1, denom1, numer2, denom2):
    numer = denom1 * numer2 + numer1 * denom2
    denom = denom1 * denom2
    gcd = math.gcd(numer,denom)
    return [numer//gcd, denom//gcd ]

# 배열 두배 만들기
'''
정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
'''
def test08_7(numbers):
    res = list(map(lambda x : x*2, numbers))
    return res

# 24.09-05 복습
#나머지 구하기
def test09_1(num1, num2):
    return num1 % num2

#중앙값 구하기
def test09_2(array):
    sorted_value = sorted(array)
    index_value = len(array) // 2
    middle_value = sorted_value[index_value]
    return middle_value

#최빈값 구하기
def test09_3(array):
    count = [0] * (max(array) + 1)

    for i in array:
        count[i] += 1

    m = 0
    for j in count:
        if j == max(count):
            m += 1

    if m >= 2:
        return -1
    else:
        return count.index(max(count))

# 짝수는 싫어요
def test09_4(n):
    return list(range(1, n+1, 2))

# 피자 나눠먹기
def test09_5(n):
     return (n+6)// 7

# 24.09-07 복습
# 피자 나눠 먹기 (2)

def test09_6(n):
    pizza = 1

    while True:
       if (pizza * 6) % n == 0:
           return pizza
       else:
           pizza += 1

# 24.09-08
# 버블정렬 - k번째 수
def solution(array, commands):
    value_return = []


    for i, j, k in commands:
        commands_list = sorted(array[i-1 : j])  # 5,2,6,3을 뽑아낸 값
        res = commands_list[k-1]

        value_return.append(res)

    return value_return




if __name__ == '__main__':
    res = solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]])
    print(res)

