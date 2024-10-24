# 편지

'''
머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다. 
할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며, 
편지를 가로로만 적을 때, 
축하 문구 message를 적기 위해 필요한 편지지의 최소 가로길이를 
return 하도록 solution 함수를 완성해주세요.
'''

def solution(message):
    answer = len(message) * 2 
    return answer


print(solution("I love you~"))


#가장 큰 수 찾기
'''
정수 배열 array가 매개변수로 주어질 때, 
가장 큰 수와 그 수의 인덱스를 담은 배열을 
return 하도록 solution 함수를 완성해보세요.
'''

def solution(array):
    answer = []
    answer.append(max(array))
    res = array.index(answer[0])
    answer.append(res)
    return answer

print(solution([9, 10, 11, 8]))


def solution(array):

    return [max(array), array.index(max(array))]

print(solution([9, 10, 11, 8]))



# 문자열 계산하기 
'''
my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 
문자열 my_string이 매개변수로 주어질 때, 
수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
'''

def solution(my_string):
    # 공백으로 분리
    res = my_string.split()
    
    # 숫자와 연산자 추출
    num1, operator, num2 = res
    
    # 연산자에 따라 계산
    if operator == '+':
        answer = int(num1) + int(num2)
    elif operator == '-':
        answer = int(num1) - int(num2)
    
    return answer

print(solution("3 + 4")) 
