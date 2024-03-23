from bs4 import BeautifulSoup
import requests

# with open("website.html", encoding="utf-8") as file:
#     file_new = file.read()
#
#
# soup = BeautifulSoup(file_new, "html.parser")
# print(soup.prettify())
#
# print(soup.a)
# anchor_tags = soup.findAll(name="a")
# print(anchor_tags)
# for tag in anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3",class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)



article_link = soup.find_all(name="a")
article_texts = [link.text for link in article_link]
article_links = [links.get("href") for links in article_link]


article_score = soup.find_all(class_="score")
article_scores = [score.text.split()[0] for score in article_score]
print(article_scores)
print(article_links)
print(article_texts)

largest = max(article_scores)
print(largest)
print(largest.index(largest))