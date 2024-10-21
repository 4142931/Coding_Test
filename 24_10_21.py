#한 번만 등장한 문자
'''
문자열 s가 매개변수로 주어집니다. 
s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 
한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
'''

def solution(s):
    # 중복을 제거하고 정렬하기
    s_set = sorted(set(s))
   
    # 각 문자의 등장 횟수 카운트하기
    count = {char: s.count(char) for char in s_set}
   
    # 한 번만 등장하는 문자 필터링
    single_chars = [char for char, cnt in count.items() if cnt == 1]
    
    # 결과 문자열 반환
    return ''.join(single_chars)

print(solution("abcabcadc"))


