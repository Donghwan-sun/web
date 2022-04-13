from bs4 import BeautifulSoup
import requests

def html_creator(tag, new_tag):
    def text_wrapper(text):
        new_text = text.replace(tag, new_tag)
        print(f"{new_text}")
    return text_wrapper

#star = html_creator("*")
#star(["안녕", "하세요"])

res = requests.get("https://davelee-fun.github.io/blog/crawl_html_css.html")
soup = BeautifulSoup(res.text, "html.parser")
link_titles = soup.select("ul#hobby_course_list > li")
for link_title in link_titles:
    translate_text = html_creator("-", "*")
    text = link_title.get_text()
    translate_text(link_title.get_text())


