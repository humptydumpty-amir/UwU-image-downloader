import requests
import wget
import sys
from bs4 import BeautifulSoup

print("--- UwU image downloader ---")

if len(sys.argv) < 3:
    print("usage:")
    print(sys.argv[0] + " <url> <destination path>")
    exit()

url = sys.argv[1]
dst = sys.argv[2]
status = requests.get(url)
if status.status_code == 200:
    print("connection: ok")
else:
    print("url not found :(")
    exit()

soup =  BeautifulSoup(status.text,"html.parser")
images = soup.findAll('img')

for img in images:
    print("\ndowloafing: " + img['src'])
    wget.download(img['src'],dst)


