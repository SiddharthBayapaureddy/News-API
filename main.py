import requests
from send_mail import send_mail

api_key = '3b319c643ace403e9d87dbd08f2fb587'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-12-20&sortBy=publishedAt&apiKey=3b319c643ace403e9d87dbd08f2fb587'

# Making a request
request = requests.get(url)

# Getting a dictionary with news data
content = request.json()

# Accessing the articles and discription 
for article in content['articles']:
    print(article['title'])
    print(article['description'])
    print('\n')

# Making the text for mail

text = ""
for article in content['articles']:
    if article['title'] != None and article['description'] != None:
        text = text + article['title'] + '\n' + article['description'] + '\n' + '\n'

text = text.encode('utf-8')
send_mail(text)