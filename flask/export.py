import csv

def export_to_csv(jobs):
  f = open("jobs.csv", mode="w")
  writer = csv.writer(f)
  writer.writerow(["Title","Company","Link"])
  for job in jobs:
    writer.writerow(list(job.values())) 