# 최댓값 만들기(2)
'''
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 
최댓값을 return하도록 solution 함수를 완성해주세요.
'''


def solution(numbers):
    answer = 1
    sorted_num = sorted(numbers, reverse=True)
    if sorted_num[0] * sorted_num[1] > sorted_num[-1] * sorted_num[-2]:
        answer = sorted_num[0] * sorted_num[1]
    else:
        answer = sorted_num[-1] * sorted_num[-2]
    
    return answer


print(solution([1, 2, -3, 4, -5]))