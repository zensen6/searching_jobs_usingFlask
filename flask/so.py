"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import requests
from bs4 import BeautifulSoup


URL = "https://stackoverflow.com/jobs?r=true&q=python"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def get_last_page(url):
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
  span = [i.find("span") for i in pages]
  last_page = span[-2].get_text(strip=True)
  return int(last_page)


def get_list(url):
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  jobs = soup.find("div",{"class":"listResults"}).find_all("div")
  h2 = []
  h3 = []
  link = []
    
  for i in jobs:
    if i != None:
      h2.append(i.find("h2",{"class":"mb4 fc-black-800 fs-body3"}))
      h3.append(i.find("h3",{"class":"fc-black-700 fs-body1 mb4"}))
        
  a = []
  company = []
  ans = []
  company_ans = []
    
  for i in h2:
    if i != None:
      a.append(i.find("a")["title"])
      link.append(i.find("a"))
  for i in h3:
    if i != None:
      company.append(i.find("span").get_text(strip=True)) 
 
  
  company_ans = [company[i] for i in range(0,len(company),3)]
  ans = [a[i] for i in range(0,len(a),3)]
  link_ans = [link[i] for i in range(0, len(link),3)]
  link_ans = [f"https://stackoverflow.com/{i['href']}" for i in link_ans]

  return company_ans, ans, link_ans


def get_each_pages(url):
    ans = []
    company = []
    link = []

    pages = get_last_page(url)
    for i in range(1,pages+1):
        
        c, a, l = get_list(url)
        ans += a
        company += c
        link += l
    
    d = []
    for i in range(len(ans)):
        d.append({
            'title':ans[i],
            'company':company[i],
            'link':link[i]
        })
    return d
    
