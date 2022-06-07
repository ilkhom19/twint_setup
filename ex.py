import os
from datetime import timedelta, date,datetime
import subprocess as sp

os.system("mkdir logs")
os.system("mkdir json-files")
start_date = date(2022, 2, 1)
end_date = date(2022, 6, 1)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)+2):
        yield start_date + timedelta(n)

dates = []

for single_date in daterange(start_date, end_date):
    dates.append(single_date.strftime("%Y-%m-%d"))

for i in range(1,len(dates)):

    text_file = open("logs/"+str(dates[i - 1])+"-logs.txt", "a")

    start_time = str("Start: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    output = sp.getoutput("twint -s 'Ukraine' --lang 'en' --since " + str(dates[i - 1]) + " --until " + str(dates[i]) + " -o " + "json-files/"+str(dates[i - 1]) + ".json --json")
    end_time = str(" - Finish: " + datetime.now().strftime("%H:%M:%S"))
    text_file.write("\n <***> Day: " + str(dates[i - 1]) + " ->  " + start_time + end_time + " with code: "+output)

    text_file.close()
