import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.title)
# print(soup.title.get_text())

# print(soup.a.get_text())
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 a element를 찾음.
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class = "Nbtn_upload" 인 어떤 element

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# # print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling

# print(rank1.get_text())
# print(rank2.get_text())
# print(rank3.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank3.a.get_text())
# print(rank1.parent.get_text())

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))


webtoon = soup.find("a", text="프리드로우-제390화 태준 그룹 (5)")

print(webtoon)
