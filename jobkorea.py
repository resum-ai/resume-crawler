from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import json
import requests

with open('secrets.json', 'r') as file:
    secrets = json.load(file)

jobkorea_id = secrets['ID']
jobkorea_password = secrets['PASSWORD']

def link_crawl(driver):
    self_introduction_links = []
    f = open("/Users/jang-youngjoon/학교/2023-2학기/졸프/jobkorea_link.txt",'w')
    # 전체 page 개수 - 여기서는 49개
    for i in range(1,49):
        driver.get("https://www.jobkorea.co.kr/starter/PassAssay?schPart=10031&schWork=&schEduLevel=&schCType=&schGroup=&isSaved=1&isFilterChecked=1&OrderBy=0&schTxt=&page=" + str(i))
        paper_list = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[5]/ul")
        driver.implicitly_wait(3)
        urls = paper_list.find_elements(By.TAG_NAME,'a')
        print(urls)
        for url in urls:
            if 'selfintroduction' in url.get_attribute('href'):
                pass
            else:
                self_introduction_links.append(url.get_attribute('href'))
    self_introduction_links = list(set(self_introduction_links))
    for content in self_introduction_links:
        f.write(content+'\n')
    f.close()

def self_introduction_crawl(driver:webdriver.Chrome,file_url):
    question_list = []
    answer_list = []

    driver.get(file_url)

    user_info = driver.find_element(By.XPATH,'//*[@id="container"]/div[2]/div[1]/div[1]/h2')
    company = user_info.find_element(By.TAG_NAME,'a')
    print("지원 회사: ", company.text) # 지원회사
    season= user_info.find_element(By.TAG_NAME,'em')
    print("지원 시기: ", season.text) # 지원시기
    specification=driver.find_element(By.CLASS_NAME,'specLists')
    spec_array = specification.text.split('\n')
    print("지원 스펙: ", spec_array[:-2]) #스펙
    paper = driver.find_element(By.CLASS_NAME,"qnaLists")
    questions = paper.find_elements(By.TAG_NAME,'dt')
    print("회사 질문")
    for index in questions:
        question = index.find_element(By.CLASS_NAME,'tx')
        if question.text=="":
            index.find_element(By.TAG_NAME,'button').click()
            question = index.find_element(By.CLASS_NAME,'tx')
            question_list.append(question.text)
            # print(question.text)
        else:
            question_list.append(question.text)
            # print(question.text) # 자소서 질문 모아놓은 리스트
    print(question_list)
    driver.implicitly_wait(3)

    answers = paper.find_elements(By.TAG_NAME,'dd')
    driver.implicitly_wait(3)
    print('답변')
    for index in range(len(answers)):
        answer =answers[index].find_element(By.CLASS_NAME,'tx')
        if answer.text == "":
            questions[index].find_element(By.TAG_NAME,'button').click()
            answer =answers[index].find_element(By.CLASS_NAME,'tx')
        answer_list.append(answer.text)
    print(answer_list)
    # print(answer.text) # 자소서 답변 모아놓은 리스트