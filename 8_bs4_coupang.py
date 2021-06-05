import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?rocketAll=true&q=%EB%85%B8%ED%8A%B8%EB%B6%81&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=rocket_wow%2Ccoupang_global&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&component=&rating=0&sorter=scoreDesc&listSize=36"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:

  # 광고 제품 제외
  # ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
  # if ad_badge:
  #   print("광고 상품 제외")
  #   continue
  name = item.find("div", attrs={"class":"name"}).get_text() # 제품명 애플 제외
  if "Apple" in name:
    print("<애플 상품 제외>")
    continue
  price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격

  #리뷰 100개이상 , 평점 4.5 이상 되는 것만 조회
  rate = item.find("em", attrs={"class":"rating"}) # 평점
  if rate:
    rate = rate.get_text()
  else:
    print(" <평점없는 상품 제외합니다.>")
    continue
  rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 리뷰 수
  if rate_cnt:
    rate_cnt = rate_cnt.get_text() # 예 : (26)
    rate_cnt = rate_cnt[1:-1]
  else:
    print(" <리뷰 없는 상품제외>")
    continue

  link = "https://www.coupang.com/"+item.a["href"]

  if float(rate) >= 4.5 and int(rate_cnt) > 300:
    print("=================================")
    print("이름: ", name)
    print("가격: ", price,"원")
    print("평점: ", rate)
    print("리뷰수: ", rate_cnt)
    print("링크: ", link)
    print("=================================")