#가까운 수
'''
정수 배열 array와 정수 n이 매개변수로 주어질 때, 
array에 들어있는 정수 중 n과 가장 가까운 수를 
return 하도록 solution 함수를 완성해주세요.
'''


def solution(array, n):
    
    sub_array = [] 
    for i in array:
        sub = n-i
        sub_array.append(abs(sub))
    min_res = min(sub_array)

    res = sub_array.index(min_res)
    
    answer = array[res]
    return answer



print(solution([3, 10, 28], 28))


