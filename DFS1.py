def solution (arr) :
    visit = []
    for k in range(0, len(arr)) :
        visit.append(False)
    print(visit)    
    answer = []
    
    def DFS (depth) :
        for i in range(1, len(visit)) :
            if visit[i] :
                continue 
            if arr[depth][i] == 0 :
                continue 
            visit[i] = True
            answer.append(i)
            DFS (i)
                    
        
    
    DFS(1)
    print(visit) 
    print(answer)
    return answer

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
