# 모음 제거 

'''
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
문자열 my_string이 매개변수로 주어질 때 
모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
'''


def solution(my_string):
    return ''.join(filter(lambda x : x not in 'aeiou', my_string))
 # filter 2개의 인자를 받는다 : 첫번째 함수, 두번째 반복가능 객체
 # 반복가능 객체가 함수를 적용했을 때 True일 경우 문자를 조인
 # 람다 -> aeiou가 없으면 True로 반환 

print(solution("nice to meet you"))