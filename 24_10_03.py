
# 최댓값 만들기(1)

'''
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
'''


def solution(numbers):
    # 주어진 배열을 오름차순으로 정렬 
    numbers.sort()
    # 맨 뒤의 두 수를 곱한 값을 반환
    answer = numbers[-2] * numbers [-1]
    return answer



print(solution([0, 31, 24, 10, 1, 9]))



