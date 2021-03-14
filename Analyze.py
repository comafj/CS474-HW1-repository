from konlpy.tag import Okt
from Collect import bscrawling

okt = Okt()
news_articles = bscrawling(["태풍", "마이삭", "피해"])
test_article = news_articles[0]

# Extract only nouns from the article
noun_extract = okt.nouns(test_article)
# Extract morphemes from the article
morph_extract = okt.morphs(test_article)
# Tag POS(Part-Of-Speech) to the article
pos_tag = okt.pos(test_article)


# print(pos_tag)