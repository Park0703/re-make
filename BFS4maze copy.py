# 미로 상하좌우, 얼마나 걸리는지 출구 몇개, 
# 줄세우기, n명, n번째 경우
# 주사위1~6. n번 , n개
# dfs 속도 연산 횟수  vs bfs 최단경로 


def solution(maze) :
    
    # 0. visit
    visit = []
    for i in range(len(maze)) :
        visit.append([])
    for i in range(len(maze)) :
        for j in range(len(maze[0])) :
            visit[i].append(False)    
            
    # # 1. 현위치 (시작점) 
    # curx = 0 # 세로 상하 
    # cury = 1 # 가로 좌우

    # 2. 동작 키
        # 0상,1하,2좌,3우
    dx = [ -1, 1, 0, 0 ]
    dy = [ 0, 0, -1, 1 ]

    # queue
    queue = [ [0, 1, 0] ]
    
    # 3. 동작 시작
    while len(queue) != 0 :
        print(queue)
        cur = queue.pop(0)
        visit[cur[0]][cur[1]] = True
        
        # 동작 키 작동 0 ~ 3
        for i in range(0, 4) :
            # 1) 미로프레임 확인 // 맵 안 인지
            #    상                하                                  좌                 우
            if cur[0] + dx[i] < 0 or cur[0] + dx[i] > len(maze)-1 or cur[1] + dy[i] < 0 or cur[1] + dy[i] > len(maze[0])-1 :
                continue
        
            # 2) visit == true인지 확인 // 중복인지
            if visit[ cur[0] + dx[i] ][ cur[1] + dy[i] ] == True :
                continue 
            
            # 3) 0 인지 확인 // 정해진 경로인지 
            # maze cur + xy좌표 == 0 이면
            if maze[ cur[0] + dx[i] ][ cur[1] + dy[i] ] == 0 : 
                continue
            
            # 현위치 true
            queue.append([cur[0] + dx[i] , cur[1] + dy[i], cur[2] + 1])            
    print(visit)    

#호출
solution (
    [
        [ 0, 1, 0, 0, 0, 0, 0, 0 ], # [0][1] 출발지   x 0
        [ 0, 1, 0, 1, 1, 0, 1, 0 ],
        [ 0, 1, 0, 0, 1, 0, 1, 0 ],
        [ 0, 1, 1, 1, 1, 1, 1, 0 ],
        [ 0, 0, 1, 0, 0, 0, 1, 0 ],
        [ 0, 1, 1, 0, 1, 1, 1, 0 ],
        [ 0, 0, 0, 0, 1, 0, 0, 0 ]  #[6][4] 도착지    x 6 idx니깐 6이다
    ]    
    )    # y 0                y 7
