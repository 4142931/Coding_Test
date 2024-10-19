
#영어가 싫어요  
'''
영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 
문자열 numbers가 매개변수로 주어질 때,
 numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
'''
def solution(numbers):
    #numbers에 해당하는 숫자 dict
    number_dict = {"one" : 1, "two" : 2, "three" : 3, "four":4, "five":5, "six" :6,"seven":7 ,"eight":8 ,"nine":9}
    
    #리턴할 답을 받을 변수
    answer = ""

    #반복문의 결과를 담을 변수
    res = ""

    for i in numbers:
        res += i
    print(res)

        

print(solution("onetwothreefourfivesixseveneightnine"))




# 인덱스 바꾸기

'''
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
 my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를
바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(my_string, num1, num2):
    #문자열 list로 변환
    str_list = list(my_string)

    #인덱스 변환하기 
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    
    #리스트 문자열로 변환
    answer = ''.join(str_list)
    return answer
    

print(solution("hello",1,2))


