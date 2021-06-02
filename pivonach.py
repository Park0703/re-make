def solution (rab_this, month) :
    rab_last = 0
    rab_son = 0
    for i in range(1, month + 1):
        if i == 12 :
            rab_this = rab_this//2
            # rab_last = rab_last//2
            if rab_this%2 == 1 : 
                rab_this = rab_this - 1
                # rab_last = rab_last - 1 
        rab_last = rab_this # 이번 어른 토끼를 저번 어른 토끼로
        rab_this = rab_son + rab_last # 이번 어른토끼는 전달 어른토끼, 아이 를 더함
        rab_son = rab_last # 이번 아이토끼는 전달 어른 토끼
        print("{}번째 달".format(i))
        print("이번 어른토끼: {} , 아기토끼: {} , 총: {}".format(rab_this, rab_son, rab_this+rab_son))
        
    return rab_this
# solution(1, 4)
solution(6, 12)
# solution(2, 18)    
# 한쌍 토끼 매달 한쌍 토끼낳는다
# 새로 태어난 토낀느 한달지나야 낳기 가능
# 12개월 에 한번 토끼의 반이 죽음 // 30 => 15이면 14가 됨    


# 1 어른 2 아이 0
# 2 어른 2 (저번어른 2 + 아이0) 아이 2
# 3 어른 4 (저번어른 2 + 아이2) 아이 2(저번어른)
# 4 어른 10 (저번 2 + 아이0) 아이 6
# 5 어른 16 (저번 2 + 아이0) 아이 10
# 6 어른 26 (저번 2 + 아이0) 아이 16


# 3 이번 어른 = 2 저번 어른 + 2 저번아이
# 3 이번 아이 = 2 저번 어른
# 2 저번 어른 = 2 이번 어른