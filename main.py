# main.py

import schedule
import time
from actions import label_and_respond_to_issues, close_stale_issues

def job():
    print("Running GitHub AI automation...")
    label_and_respond_to_issues()
    close_stale_issues()

# Schedule every hour
schedule.every(1).hours.do(job)

print("GitHub AI bot running...")
while True:
    schedule.run_pending()
    time.sleep(10)
