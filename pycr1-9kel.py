from selenium import webdriver
import time

# 로딩화면 기다리기
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # as 줄임말

browser = webdriver.Chrome('./chromedriver.exe')
browser.maximize_window() # 창 최대화

url = 'https://flight.naver.com/flights/'
browser.get(url) # url로 이동

# 가는 날 선택
browser.find_element_by_link_text('가는날 선택').click()

# 이번 달 27, 28일 선택
# browser.find_elements_by_link_text('27')[0].click() # [0] 이번 달 에서 선택
# browser.find_elements_by_link_text('28')[0].click() # [0] 이번 달 에서 선택

# 다음 달 27, 28일 선택
# browser.find_elements_by_link_text('27')[1].click() # [1] 다음 달 에서 선택
# browser.find_elements_by_link_text('28')[1].click() # [1] 다음 달 에서 선택

# 이번 달 27, 다음 28일 선택
browser.find_elements_by_link_text('27')[0].click() # [0] 이번 달 에서 선택
browser.find_elements_by_link_text('28')[1].click() # [1] 다음 달 에서 선택

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()


# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

#로딩화면 때문에 동작x 1) time.sleep으로 기다리기, 2) 최적화방법? 
try : # 단 10초가 지나도 안나오면 에러가 뜸 // 성공하면 
    elem = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
        # (browser)를 10초 동안 기다리기    ~까지   tuple(xpayh)element가 나올 때까지
    print(elem.text)
finally : # 실패하면 종료
    browser.quit()


# 첫번째 결과 출력
elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
print(elem.text)



# time.sleep(5)
# browser.quit()