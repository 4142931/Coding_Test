# def solution(my_string):
#     anwser = list(my_string)
#     anwser.reverse()
#     anwer02 = ''.join(anwser)
#     return anwer02
def solution(my_string):
    return my_string[::-1]

if __name__ == '__main__':
    res = solution("jaron")
    print(res)