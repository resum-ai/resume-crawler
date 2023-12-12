from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import jobkorea

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options.add_argument("--headless"),
)

# self_introduction_links = []
#
# f = open("/Users/jang-youngjoon/학교/2023-2학기/졸프/jobkorea_link.txt",'w')
#
# for i in range(1,2):
#     driver.get("https://www.jobkorea.co.kr/starter/PassAssay?schPart=10031&schWork=&schEduLevel=&schCType=&schGroup=&isSaved=1&isFilterChecked=1&OrderBy=0&schTxt=&page="+str(i))
#     # page에 따른 경로
#     paper_list = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[5]/ul")
#     # 자기소개서 목록을 담아놓은 태그
#     driver.implicitly_wait(3)
#     urls = paper_list.find_elements(By.TAG_NAME,'a') # 거기에서 a태그만 가져온다
#     print(urls)
#     for url in urls:
#         if 'selfintroduction' in url.get_attribute('href'):
#         # 가끔씩 이상한 경로가 섞여들어와서 제외하고 진행했다.
#             pass
#         else:
#             self_introduction_links.append(url.get_attribute('href')) # href안에 있는 경로를 array에 추가해준다.
# self_introduction_links = list(set(self_introduction_links))
#
# for content in self_introduction_links:
#     f.write(content + '\n')
# f.close()

# test

jobkorea.link_crawl(driver)
# jobkorea.self_introduction_crawl(driver, "https://www.jobkorea.co.kr/starter/PassAssay/View/241147?Page=1&OrderBy=0&FavorCo_Stat=0&schPart=10031&Pass_An_Stat=0")
