import requests

API_KEY = "8982b46221af4410ba4a67eb9a0a71a9"

url = ("https://newsapi.org/v2/everything?q=spacex&from="
       "2024-04-17&sortBy=popularity&apiKey="
       "8982b46221af4410ba4a67eb9a0a71a9")

# Send request
response = requests.get(url)

# Get the dictionary of data
content = response.json()

# Access to the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
