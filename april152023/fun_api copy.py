import requests
import datetime
import urllib.parse
import json

params = {
    "q": "covid",
    "apiKey": "b39fbe8fcbdf44e8a16489ce95cfacf3",
    "from": "",
    "to": "",
}

today = datetime.datetime.now().date()
daily_articles = {}

for i in range(14):
    end = today - datetime.timedelta(days=i)
    start = today - datetime.timedelta(days=i + 1)
    params["from"] = start.isoformat()
    params["to"] = end.isoformat()

    print(urllib.parse.urlencode(params))

    res = json.loads(
        requests.get(
            "https://newsapi.org/v2/everything?" + urllib.parse.urlencode(params)
        ).content
    )
    daily_articles[start] = res["totalResults"]
