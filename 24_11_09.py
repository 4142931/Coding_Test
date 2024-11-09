# 잘라서 배열로 저장하기 
'''
문자열 my_str과 n이 매개변수로 주어질 때, 
my_str을 길이 n씩 잘라서 저장한 배열을 
return하도록 solution 함수를 완성해주세요.
'''

def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer

print(solution("abcdef123", 3))



# 중복된 숫자 개수
'''
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, 
array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
'''

def solution(array, n):
   return array.count(n) 


print(solution([1, 1, 2, 3, 4, 5], 1))


