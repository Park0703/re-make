def solution(a, b):
	answer = 0
	instead = 0 #compare = [a, b], if compare.max() == a :  //// if a > b:
	# print(c, d)
	if a > b:   #   정렬하기
		# global c, b
		instead = a
		a = b
		b = instead

    #a와 b 사이에 속한 모든 정수의 합을 리턴 
	for num in range(a, b+1) : 
		answer += num
	print(answer)
# print(   )
  
    

# solution(3, 5)
# solution(3, 3)
solution(-5, 3)
solution(-1, 1)