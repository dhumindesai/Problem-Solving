import requests


def getTopicCount(topic):
    url = "https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=" + topic

    response = requests.request("GET", url)

    text = response.json()["parse"]["text"]["*"]

    return text.count(topic)

print(getTopicCount("pizza"))