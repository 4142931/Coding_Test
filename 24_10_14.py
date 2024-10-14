# 배열 원소의 길이

'''
문자열 배열 strlist가 매개변수로 주어집니다. 
strlist 각 원소의 길이를 담은 배열을 retrun하도록 
solution 함수를 완성해주세요.
'''

def solution(strlist):
    answer = []
    for i in strlist: 
        res = list(i)
        count = len(res)
        answer.append(count)

    return answer


print(solution(["I", "Love", "Programmers."]))


# 중복된 문자 제거

'''
문자열 my_string이 매개변수로 주어집니다. 
my_string에서 중복된 문자를 제거하고 
하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(my_string):
    answer = []
    for i in my_string:
        if i not in answer:
            answer.append(i)

    return ''.join(answer)



print(solution("We are the world"))