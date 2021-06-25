# pip install selenium 설치
# chrome 정보 1) chrome;//version 2) 설정 - 도움말 - chrome 정보
# chromedriver - 크롬에 맞는 버전 설치 - python 폴더에 설치 - chromedriver.exe

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('./chromedriver.exe') # chromedriver.exe가 다른 폴더에 있다면 경로를 적어줘야함(c:/download)

# '''
# browser.get('http://naver.com') # chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다.

# # PS C:\Users\pc\Desktop\PYTHON\PROJECT> python
# # Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
# # DevTools listening on ws://127.0.0.1:49900/devtools/browser/2e8d6818-1154-4813-9ce4-d88821551ec0

# 로그인
# elem = browser.find_element_by_class_name('link_login') # 로그인 가기
# elem
# # <selenium.webdriver.remote.webelement.WebElement (session="cafa46900ea45f7e1e44f4f5fa076ce0", element="5d34dfb8-22c5-4281-a943-7fc15936ba80")>
# # elem.click() # 로그인 클릭
# # browser.back() # 브라우저 뒤로가기
# # browser.forward() # 브라우저 앞으로가기
# # browser.refresh() # 브라우저 새로고침
# # browser.back()

#검색
# elem = browser.find_element_by_id('query')
# elem.send_keys('나도코딩')
# elem.send_keys(Keys.ENTER) # Keys 대문자

# elem = browser.find_element_by_tag_name('a')
# # elem = browser.find_elements_by_tag_name('a') 하면 element를 다 가져옴
# for e in elem :
#     e.get_attribute('href') # a태그의 모든 것들을 가져옴
# '''

 
browser.get('http://daum.net')

elem = browser.find_element_by_name('q')
elem
elem.send_keys('나도코딩')
elem.send_keys(Keys.ENTER)
browser.back()

elem
elem.send_keys('나도코딩')
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()
browser.close() # 탭닫기
browser.quit() # 창닫기
exit() # 파이썬 종료





