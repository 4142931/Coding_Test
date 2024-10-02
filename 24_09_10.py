# 배열의 평균값
'''
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
'''

def solution01(numbers):
    answer = sum(numbers) / len(numbers)
    return answer


# 옷가게 할인 받기
'''
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
'''

def solution02(price):
    def solution(price):
        if 100000 <= price < 300000:
            return int(price * 0.95)
        elif 300000 <= price < 500000:
            return int(price * 0.9)
        elif price >= 500000:
            return int(price * 0.8)
        else:
            return int(price)

# 배열 뒤집기
'''
정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. 
num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution03(num_list):
    return num_list[::-1]

# 아이스 아메리카노
'''
머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 
아이스 아메리카노는 한잔에 5,500원입니다. 
머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 
머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 
남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(money):
    # answer = []
    #
    # res01 = money // 5500
    # res02 = money % 5500
    # answer.append(res01)
    # answer.append(res02)
    #
    # return answer

    return [money // 5500, money % 5500]



if __name__ == '__main__':
    res = solution(15000)
    print(res)