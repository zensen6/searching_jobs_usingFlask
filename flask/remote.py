"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import requests
from bs4 import BeautifulSoup


URL = "https://remoteok.io/remote-dev+python-jobs"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def get_list(url):
    
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, "html.parser")
    blocks = soup.find_all("td",{"class":"company position company_and_position_mobile"})
    an = soup.find_all("td",{"class":"source"})
    an1 = [i.find("a") for i in an]
    an2 = []
    for i in an1:
        if i != None:
            an2.append(f"https://remoteok.io{i['href']}")
    
    
    link = [i.findAll("a")[0] for i in blocks]
    title = [i.find("h2") for i in link]
    se = [i.findAll("a")[1] for i in blocks]
    company = [i.find("h3") for i in se]
    company1= []
    for i in company:
        if i != None:
            company1.append(i.string)
            
    title1 = []
    for i in title:
        if i != None:
            title1.append(i.text.strip("\t").strip("\xa0").strip('\t'))

    ans = []
    #del an1[0]
    #an2 = [i['href'] for i in an1]
    num = min(len(an2), len(company1), len(title1))
    
    
    for i in range(num):
        ans.append({
            'title':title1[i],
            'company':company1[i],
            'link':an2[i]
        })
    
    return ans
    

    