import requests
from send_email import send_email

API_KEY = "8982b46221af4410ba4a67eb9a0a71a9"

url = ("https://newsapi.org/v2/everything?q=spacex&from="
       "2024-04-17&sortBy=popularity&apiKey="
       "8982b46221af4410ba4a67eb9a0a71a9")

# Send request
response = requests.get(url)

# Get the dictionary of data
content = response.json()


# Access to the article titles and descriptions
msg = ""
for article in content["articles"]:
    if article["title"] and article["title"] != "[Removed]":
        msg += f"{article['title']}\n{article['description']}\n{article['url']}\n\n"

msg = msg.encode("utf-8")
send_email(msg)
