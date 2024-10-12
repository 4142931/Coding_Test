#컨트롤 제트
'''
숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 
문자열에 있는 숫자를 차례대로 더하려고 합니다. 
이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 
숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 
머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(s):
    res = list(s.replace(' ','')) # 매개변수 s에 담긴 공백을 제거 후 list로 변경
    Z_index = res.index('Z') if 'Z' in res else None # "Z"를 "Z" 앞에 수의 -로 만들기 위한 인덱스 찾기

    if Z_index is not None: # Z_index에 Z가 있으면 실행 
        res[Z_index] = '-' + res[Z_index - 1] # 'Z'가 있는 경우 앞의 인덱스의 -를 붙인 수로 변경
    
    anwser = list(map(lambda x : int(x), res))


    return sum(anwser)


print(solution("-1 -2 -3 Z")) 