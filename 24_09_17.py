#배열 회전시키기 
'''
정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 
solution 함수를 완성해주세요
'''

def solution(numbers, direction):

    if direction == "right":
        return [numbers[-1]] + numbers[0:-1]
    elif direction == "left":
        return numbers[1:] + [numbers[0]]
    else:
        return print(f'잘못된 입력입니다 : ', {numbers})
    




res = solution([1, 2, 3], "right")
print(res)