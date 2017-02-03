import requests
from bs4 import BeautifulSoup
import json

#취업정보

def kw_jobinfo():

    initial_text =[]
    result_text = []
    
    url = "http://www.kw.ac.kr/ko/life/job.do"
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    response = requests.get(url, headers={"USER-AGENT":u_a})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    div_soup = soup.find("div",{"class":"list-box"})
    a_soup = div_soup.find_all("a")

    for a_tag in a_soup:
        initial_text.append(a_tag.text)
    
    for text in initial_text:
        for filter in ["\n","\t","신규게시글","Attachment"]:
            if filter in text:
                text = text.replace(filter,"")
        result_text.append(text)

    cnt = 1
    message = "취업정보 게시판 보기 : http://www.kw.ac.kr/ko/life/job.do\n\n"
    for a in result_text:
        message += str(cnt)+". " +  a + "\n\n"
        cnt+=1
        
    result = {"text":message}

    return result

if __name__ == "__main__":
    kw_jobinfo()
