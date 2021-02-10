from remote import get_list
from so import get_each_pages
from wework import get_list_w

'''
https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs
'''

def parsing(language):
  jobs = []
  url1 = f"https://stackoverflow.com/jobs?r=true&q={language}"
  url2 = f"https://weworkremotely.com/remote-jobs/search?term={language}"
  url3 = f"https://remoteok.io/remote-dev+{language}-jobs"

  jobs += get_each_pages(url1)
  jobs += get_list_w(url2)
  jobs += get_list(url3)
  return jobs

