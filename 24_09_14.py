# 개미군단
'''
개미 군단이 사냥을 나가려고 합니다.
개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다.
장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다.
예를 들어 체력 23의 여치를 사냥하려고 할 때,
일개미 23마리를 데리고 가도 되지만,
장군개미 네 마리와 병정개미 한 마리를 데리고 간다면
더 적은 병력으로 사냥할 수 있습니다. 사냥감의 체력 hp가 매개변수로 주어질 때,
사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면
몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.
'''

def solution01(hp):
    answer = 0

    a = hp // 5
    answer += a

    b = (hp % 5)// 3
    answer += b

    c = ((hp % 5) % 3) // 1
    answer += c
    return answer

# 모스부호
'''
머쓱이는 친구에게 모스부호를 이용한 편지를 받았습니다. 
그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 합니다. 
문자열 letter가 매개변수로 주어질 때, 
letter를 영어 소문자로 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
모스부호는 다음과 같습니다.
'''
def solution(letter):
    morse = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }
    answer = []

    for i in letter.split():
        answer += morse[i]

    return ''.join([morse[i] for i in letter.split()])
    # return ''.join(answer)

# 가위 바위 보
'''
가위는 2 바위는 0 보는 5로 표현합니다. 
가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, 
rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 
나타낸 문자열을 return하도록 solution 함수를 완성해보세요.
'''

def solution03(rsp):
    answer = ''
    list_rsp = list(str(rsp))
    for i in list_rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        elif i == '5':
            answer += '2'
        else:
            pass
    return answer

# 구슬을 나누는 경우의 수
'''
머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 
구슬은 모두 다르게 생겼습니다. 
머쓱이가 갖고 있는 구슬의 개수 balls와 
친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, 
balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 
return 하는 solution 함수를 완성해주세요.
'''

def solution04(ball, share):
    res_ball = 1
    res_share = 1
    res_ball_share = 1

    for i in range(1, ball + 1):
        res_ball *= i

    for j in range(1, share + 1):
        res_share *= j

    for k in range(1, ball-share + 1):
        res_ball_share *= k

    return res_ball // (res_ball_share * res_share)

if __name__ == '__main__':
    res = solution(".... . .-.. .-.. ---")
    print(res)