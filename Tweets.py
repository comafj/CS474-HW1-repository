import twitter

twitter_consumer_key = "ZQ0JhUksP8EFPYOTxZL5r5oer"
twitter_consumer_secret = "1msCHW4E1XqRxCHo6L9GW3wKjwMTLTQfYbaCvrNKRUKvNuIzBp"
twitter_access_token = "1370962200173506562-aqRMb87VV8Ojk8LhphmBmDJg1M83Io"
twitter_access_secret = "KpBGOtLoOcGHVO6y8meKRKNxMBpE8sdR30TDzPDny9mUk"
twit_API = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret,
                       access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)


def t_search(query, count=10):
    elems = twit_API.GetSearch(term=query, count=count)
    text_list = [elem.text for elem in elems]
    return text_list


# print(t_search("태풍 하이선"))