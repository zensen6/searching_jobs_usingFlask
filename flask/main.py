"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
from flask import Flask, render_template, redirect, request, send_file
from merge import parsing
from export import export_to_csv

db = {}

app = Flask("final")
@app.route('/')
def home():
  return render_template("index.html")

@app.route('/search')
def query_s():
  language = request.args.get('term')
  if language:
    language = language.lower()
    word = db.get(language)
    if word:
      jobs = word
    else:
      jobs = parsing(language)
      db[language] = jobs 
    count = len(jobs) 
    return render_template("job.html" ,language = language, count = count, jobs=jobs)
  else:
    return render_template("index.html")
  
@app.route('/export')
def export():
  try:
    language = request.args.get("term")
    if not language:
      raise Exception()
    language = language.lower()
    word = db.get(language)
    if not word:
      raise Exception()
    export_to_csv(word)
    return send_file("jobs.csv")
  except:  
    return redirect('/')


app.run(host="0.0.0.0")