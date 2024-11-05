#문자열 안에 문자열 

'''
문자열 str1, str2가 매개변수로 주어집니다. 
str1 안에 str2가 있다면 1을 없다면 2를 
return하도록 solution 함수를 완성해주세요.
'''


def solution(str1, str2):
    answer = 0
    if str2 in str1:
        answer += 1
    else:
        answer += 2
    return answer


print(solution("ppprrrogrammers", "pppp"))



#제곱수 판별하기
'''
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를
return하도록 solution 함수를 완성해주세요.
'''


def solution(n):
    res = int(n ** 0.5)
    return 1 if res ** 2 == n else 2