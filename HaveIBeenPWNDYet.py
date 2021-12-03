import requests
import time
import random
import string
import getpass

def main() -> None:
    Welcome = '''haveibeenpwnd api script by pro WIP'''
    count = 0
    r = requests.session()
    with open('Emails.txt') as f:
       for line in f:
        print(line +" Results:")
        url = "https://haveibeenpwned.com/api/v3/breachedaccount/" + line.rstrip()
        headers = {
        "hibp-api-key": "<YOUR_KEY_HERE>"
        }
        count+=1
        b = r.get(url=url, headers=headers)
        brl = "Reported"
        ETA = "time:"
        ReportCount = "count:"
        file_object = open(line + '.txt', 'wb')
        file_object.write(b.content)
        file_object.close()
        print(brl,b.status_code, b.content, ETA, b.elapsed, ReportCount, count)
        time.sleep(2)
if __name__ == '__main__':
    main()
