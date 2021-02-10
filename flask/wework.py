"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import requests
from bs4 import BeautifulSoup


URL = "https://weworkremotely.com/remote-jobs/search?term=python"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def get_list_w(url):
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  list_jobs = soup.find("section",{"id":"category-2"}).find_all("li")
  link = [i.find("a", recursive=False) for i in list_jobs]
  del link[-1]
  company = [i.find("span",{"class":"company"}).string for i in link]
  title = [i.find("span",{"class":"title"}).string for i in link]
  link = [f"https://weworkremotely.com/{i['href']}" for i in link]
  ans = []
  num = min(len(title), len(company), len(link))
  for i in range(num):
    ans.append({
        'title':title[i],
        'company':company[i],
        'link':link[i]
    })
    
    
  return ans
