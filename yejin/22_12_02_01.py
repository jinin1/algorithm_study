# 짝수 홀수 개수

#방법1
# even, odd 변수를 만들어 반복문에서 나머지를 구해 하나씩 카운트 해준다.
def solution(num_list):
    even, odd = 0, 0
    for i in num_list:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]
  
# ////////////////위가 내 찐풀이//////////////////////
# ////////////////밑은 다른 사람 참고(그저 연습이다. 무시할 것.)/////////////////

# 방법2
# 변수를 even 하나만 만들고, 홀수값은 전체길이에서 even 값을 빼준다.
def solution(num_list):
    even = 0
    for i in num_list:
        if i%2 == 0:
            even += 1
    return [even, len(num_list)-even]

# 방법3
# answer[0,0]의 배열을 만들어서 
#짝수일 경우 answer[0]에 +1, 
#홀수일 경우 answer[1]에 +1 해주기
def solution(num_list):
    answer = [0,0]
    for i in num_list:
        answer[i%2]+=1
    return answer
