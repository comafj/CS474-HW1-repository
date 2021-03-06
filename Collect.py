from urllib.parse import quote
import urllib.request
import requests as req
import json
from bs4 import BeautifulSoup as bs


# Function get_news(url) :
# A function that extracts the body by searching for news articles
# on the corresponding link based on URL parameter.
def get_news(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    news_req = req.get(url, headers=headers)
    news_bs = bs(news_req.content, 'html.parser')

    _text = news_bs.select('#articleBodyContents')[0].get_text().replace('\n', " ")
    btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")
    return btext.strip()


# Function bscrawling(keywords, max_news):
# Based on the parameter keywords in the form of a list
# to be used as a search keyword,
# it obtains the body of up to max_news news articles
def bscrawling(keywords, max_news=10):
    search_query = " ".join(s for s in keywords)
    search_query = quote(search_query, safe=':/?-=')

    url = 'https://openapi.naver.com/v1/search/' + 'news' + '?query=' + search_query + "&display=" + str(
        max_news) + "&sort=sim"
    client_id = 'CVbcjoXB1ftbVlrp7T2C'
    client_secret = 'XpEq9FDjlm'
    request = urllib.request.Request(url)
    request.add_header("X-Naver-client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
    else:
        print("Error Code:" + rescode)
        return "Error Occured"

    data = json.loads(response_body)
    urllist = []
    for single_data in data["items"]:
        if single_data["link"].startswith("https://news.naver.com/"):
            urllist.append(single_data["link"])

    body_list = []
    for single_url in urllist:
        body_list.append(get_news(single_url))
    return body_list


# print(bscrawling(["태풍", "마이삭", "피해"]))