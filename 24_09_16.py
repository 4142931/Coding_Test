# 공 던지기
'''
머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 
공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 
친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, 
k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.
'''

def solution(numbers, k):
    len_numbers = len(numbers)

    while len(numbers) < 2*k:
        numbers += numbers
        
    return numbers[::2][k-1]
        
# 순환하면 좋겠다고 생각했는데 순환하는 방법을 코드로 구현이 어려워서 리스틀 확장했다.
# % 나머지 개념을 사용하면 굳이 리스트를 늘리지 않고 구현이 가능하다.