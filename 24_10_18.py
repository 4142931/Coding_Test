#암호해독 
'''
군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.
암호화된 문자열 cipher를 주고받습니다.
그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
문자열 cipher와 정수 code가 매개변수로 주어질 때 
해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(cipher, code):
    answer = []
    list_cipher = list(cipher)
    res = list_cipher[code-1::code]
    answer = ''.join(res)
    return answer

#str에 바로 슬라이싱 가능했다! 
def solution(cipher, code):
    print(cipher[0:1])
    return None

print(solution("dfjardstddetckdaccccdegk", 4))



#대문자와 소문자
'''
문자열 my_string이 매개변수로 주어질 때, 
대문자는 소문자로 소문자는 대문자로 변환한 
문자열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(my_string):
    answer = my_string.swapcase()
    return answer

print(solution("cccCCC"))
