import requests
from settings.settings import settings
from send_email import send_email

topic = "tesla"

api_key = "7e7ee3ea72bb4c7c92b4c7caac552ec5"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2025-12-13&sortBy=publishedAt&apiKey={api_key}&language=en&"
    
#Make Request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n" 

#Send the email
body = body.encode("utf-8")
send_email(message=body)