# 배열 자르기

'''
정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때,
numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을
return 하도록 solution 함수를 완성해보세요.
'''

def solution01(numbers, num1, num2):
    return numbers[num1 : num2 + 1]


# 외계행성의 나이
'''
우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 
입국심사에서 나이를 말해야 하는데, 
PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. 
a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 
나이 age가 매개변수로 주어질 때 
PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.
'''

def solution02(age):
    anwser = ""
    ABC = "abcdefghij"
    result = [int(i) for i in str(age)]

    for i in result:
        anwser += ABC[i]

    return anwser

# 진료 순서 정하기
'''
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다.
정수 배열 emergency가 매개변수로 주어질 때 
응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.
'''
# def solution(emergency):
#     anwser = []
#     sorted_emergency = sorted(emergency, reverse=True)
#     return [sorted_emergency.index(i)+1 for i in emergency]

def solution(emergency):
    sorted_emergency = sorted(emergency, reverse= True)
    return [sorted_emergency.index(i) + 1 for i in emergency]






def solution04(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += 1
    return answer



if __name__ == '__main__':
    res = solution([3, 76, 24])
    print(res)