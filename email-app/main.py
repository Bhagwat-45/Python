import requests

api_key = "7e7ee3ea72bb4c7c92b4c7caac552ec5"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-13&sortBy=publishedAt&apiKey=7e7ee3ea72bb4c7c92b4c7caac552ec5"
    
#Make Request
request = requests.get(url,)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])