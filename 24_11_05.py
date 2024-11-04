#OX퀴즈 
'''
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 
형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 
return하도록 solution 함수를 완성해주세요.
'''

def solution(quiz):
    answer = []
    for i in quiz:

        #요소로 나누기 
        divide = i.split()
        operation = divide[1]

        # operation에 조건에 따라 계산한 값을 answer에 담기 
        if operation == "-":
            if int(divide[0]) - int(divide[2]) == int(divide[4]):
                answer.append("O")
            else:
                answer.append("X")
        
        elif operation == "+":
            if int(divide[0]) + int(divide[2]) == int(divide[4]):
                answer.append("O")
            else:
                answer.append("X")   

    return answer

print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
