import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
res = requests.get(url, headers=headers)
# res.raise_for_status()
#   print("문제가 생겼습니다. 에러코드 : ", res.status_code)

with open("nadocoding.html","w", encoding="utf8") as f:
  f.write(res.text)