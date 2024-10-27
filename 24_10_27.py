# 숫자 찾기
'''
정수 num과 k가 매개변수로 주어질 때,
 num을 이루는 숫자 중에 k가 있으면 
 num의 그 숫자가 있는 자리 수를 return하고 없으면 
 -1을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(num, k):
    num_list = list(str(num))
    str_k = str(k)
    answer = 0 

    if str_k in num_list:
        answer = num_list.index(str_k)
        
        return answer +1

    else:
        return -1

    

print(solution(123456, 7))