#공지사항

import requests
from bs4 import BeautifulSoup
import json
import requests_cache

def kw_notice():
    
    url = "http://www.kw.ac.kr/ko/life/notice.do"
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    requests_cache.install_cache('notice')

    response = requests.get(url, headers={"USER-AGENT":u_a})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    div_soup = soup.find("div",{"class":"list-box"})
    a_soup = div_soup.find_all("a")

    message=""
    cnt = 1
    
    for ele in a_soup[:30]:
        if "\n" in ele.text:
            text = ele.text.replace("\t","")
            text = text.replace("신규게시글","")
            text = text.replace("\n","")
            
        message += str(cnt)+". " +  text + "\n\n"
        cnt+=1
        
    result = {"text":message}
    
    return result

if __name__ == "__main__":
    kw_notice()

