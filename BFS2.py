def solution (arr) :
    visit = []
    for k in range(0, len(arr)) :
        visit.append(False)
    print(visit)
    queue = [1]    
    answer = []
    
    while queue != [] :   
        # cur = queue[0]
        cur = queue.pop(0)
        visit[cur] = True
        answer.append(cur)
        
        for i in range(0, len(visit)) :
            if visit[i] :
                continue 
            if arr[cur][i] == 1 :
                queue.append(i)
        
    print(visit) 
    print(answer)
    return answer
# 1 4 6 3 5 7 2 8 
solution([
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 1, 0, 0, 1, 0, 1, 0, 0 ], 
  [ 0, 0, 1, 0, 0, 1, 0, 0, 0 ],
  [ 0, 0, 0, 1, 1, 0, 0, 0, 0 ], 
  [ 0, 1, 0, 1, 1, 1, 0, 0, 0 ],
  [ 0, 0, 1, 0, 1, 1, 0, 0, 1 ],
  [ 0, 1, 0, 0, 0, 0, 1, 1, 0 ], 
  [ 0, 0, 0, 0, 0, 0, 1, 1, 0 ], 
  [ 0, 0, 0, 0, 0, 1, 0, 0, 1 ] 
])

'''
[ # 0  1  2  3  4  5  6  7  8
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # 0
  [ 0, 1, 0, 0, 1, 0, 1, 0, 0 ], # 1
  [ 0, 0, 1, 0, 0, 1, 0, 0, 0 ], # 2
  [ 0, 0, 0, 1, 1, 0, 0, 0, 0 ], # 3
  [ 0, 1, 0, 1, 1, 1, 0, 0, 0 ], # 4
  [ 0, 0, 1, 0, 1, 1, 0, 0, 1 ], # 5
  [ 0, 1, 0, 0, 0, 0, 1, 1, 0 ], # 6
  [ 0, 0, 0, 0, 0, 0, 1, 1, 0 ], # 7
  [ 0, 0, 0, 0, 0, 1, 0, 0, 1 ]  # 8
]'''
