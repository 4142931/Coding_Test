# 숨어있는 숫자의 덧셈

'''
문자열 my_string이 매개변수로 주어집니다. 
my_string안의 모든 자연수들의 합을 return하도록 
solution 함수를 완성해주세요.
'''

def solution(my_string):
    
    res = list(map(int,filter(lambda x : x in '123456789', my_string)))
    anwser = sum(res)

    return anwser


print(solution("1a2b3c4d123"))


# 소인수분해
'''
소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 
예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 
따라서 12의 소인수는 2와 3입니다. 
자연수 n이 매개변수로 주어질 때 
n의 소인수를 오름차순으로 담은 배열을 
return하도록 solution 함수를 완성해주세요.
'''

def solution01(n):
    res = []
    num = 2
    while n > 1:
        while n % num == 0:
            res.append(num)
            n = n // num
        num += 1
    anwser = sorted(set(res))
    return anwser

print(solution01(420))