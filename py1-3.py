def solution(s):
    answer = True
    s = s.lower()
    if s.count('p') == s.count('y') :
      return True
    elif  s.count('p') == 0 and s.count('y') == 0 :
      return True
    elif s.count('p') != s.count('y') :
      return False

    
solution("pPoooyY")
solution("Pyy")