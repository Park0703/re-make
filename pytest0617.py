# # 1
# poem = """흔들리며 피는 꽃
# 도종환
# 흔들리지 않고 피는 꽃이 어디 있으랴
# 이 세상 그 어떤 아름다운 꽃들도
# 다 흔들리면서 피었나니
# 흔들리면서 줄기를 곧게 세웠나니
# 흔들리지 않고 가는 사랑이 어디 있으랴
# 젖지 않고 피는 꽃이 어디 있으랴
# 이 세상 그 어떤 빛나는 꽃들도
# 다 젖으며 젖으며 피었나니
# 바람과 비에 젖으며
# 꽃잎 따뜻하게 피웠나니
# 젖지 않고 가는 삶이 어디 있으랴
# """
# # 1)
# print(poem[:50]+'\n'+'...중략...')
# # 2)
# poem_split = poem.split()
# sear = input('검색할 단어 입력 :') # 꽃
# cnt = [s for s in poem_split if sear in s]
# print("'꽃'이 사용된 횟수 =", len(cnt))
# # 3) 
# poem_split = poem.split()
# print('전체 단어수 :', len(poem_split))

# # 2
# code = {'A':'.-', 'B':'-....', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.',
# 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
# 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
# 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}
# words = input('모스부호로 표시할 단어(알파벳 대문자) :').upper()
# for word in words :
#     print(word,':',code[word])
# # 3
# slist = "A python is a large snak".split()
# nlist = []
# for ss in slist :
#     nlist.append(ss.capitalize())
# print(' '.join(nlist))


# 1
# TypeError: %d format: a number is required, not str
# %d 는 숫자를 받고, %s 문자를 받는다
# print("%s는 %d개 있고, %s는 없습니다." % ("사과", 3, '포도'))

# # 2
# phonebook = {'hong':'010-1234-0909', 'lee':'010-4321-8989', 'kim':'031-555-3333', 'park':'02-1234-5678', 'song':'032-222-5555'}
# name_keys = input('이름 입력 :')
# cnt = 0 
# for k in phonebook :
#     if k == name_keys :
#         cnt += 1
#         print('연락처 :', phonebook[k])
# if cnt == 0 :
#     print('연락처에 없는 이름입니다.')

# # 3
# import operator
# list1 = sorted(phonebook.items(), key=operator.itemgetter(0))
# print(list1)

# # 4
# import operator
# list2 = sorted(phonebook.items(), key=operator.itemgetter(1))
# print(list2)

# # 5
# import re
# data= 'hong:90,lee:80,kim:75,park:50,song:60'.split(',')
# list3 = re.findall('\d+', str(data))
# list3 = list(map(int, list3))
# print('점수 합계 :', sum(list3))



































