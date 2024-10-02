# 합성수 찾기
'''
약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
자연수 n이 매개변수로 주어질 때 
n이하의 합성수의 개수를 return하도록 solution 함수 를 완성해주세요.
'''

def solution(n):
    answer = 0
    if n < 4:
        return 0 

    for i in range(4, n+1):
        
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            answer += 1
        else:
            pass
    return answer

print(solution(15))

# 결국 못 풀었다.
# LLM 확인 및 다시 풀어볼 것 

# 에라토스테네스의 체?
# 제곱근까지만 나누어 떨어지는지 
# 소수를 먼저 찾고 나머지를 합성수로 처리 - 위 코드는 5,7의 소수를 포함하기 때문에 작동이 안된다.
# 생각이 부족한 점 약수의 개수를 구하는 코딩을 구현을 못했다. 
def solution(n): 
    count = 0  # 합성수 개수를 담을 변수 
    for num in range(4, n+1): # 1,2,3은 합성수가 아니니 제외
        divisors = 0  #약수를 담을 변수 
        for i in range(1, num+1):
            if num % i == 0:
                divisors += 1
        if divisors >= 3:
            count += 1
    return count

