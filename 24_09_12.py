# 특정 문자 제거하기

'''
문자열 my_string과 문자 letter이 매개변수로 주어집니다.
my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
'''

def solution01(my_string, letter):
    return my_string.replace(letter,'')


# 각도기

'''
각에서 0도 초과 90도 미만은 예각, 90도는 직각, 
90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다.
각 angle이 매개변수로 주어질 때  예각일 때 1, 직각일 때 2, 
둔각일 때 3, 평각일 때 4를  return하도록  solution 함수를 완성해주세요.
'''

def solution02(angle):
   if 0 < angle <90:
       return 1
   elif angle == 90:
       return 2
   elif 90 < angle < 180:
       return 3
   elif angle == 180:
       return 4
   else:
       pass

# 양꼬치
'''
머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 
양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 
정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 
총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.
'''


def solution03(n, k):

  B = n // 10

  bill = 12000 * n + 2000 * k
  service = 2000 * B

  answer = bill - service
  return answer

def solution04(n, k):
    return (12000 * n) + (2000 * k - n//10)

#짝수의 합
'''
정수 n이 주어질 때, n
이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
'''
def solution(n):
    return sum(list(range(n+1))[2::2])




if __name__ == '__main__':
    res = solution(4)
    print(res)