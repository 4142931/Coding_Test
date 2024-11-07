#세균 증식
'''
어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 
처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 
t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
'''

def solution(n, t):
    num = [2] * t
    answer = n
    for i in num:
        answer *= i
    return answer



print(solution(7, 15))


#문자열 정렬하기(2)
'''
영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때,
my_string을 모두 소문자로 바꾸고 알파벳 순서대로 
정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(my_string):
    return ''.join(sorted(my_string.lower()))


print(solution("Bcad"))