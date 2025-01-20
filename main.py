import requests
from send_mail import send_mail

api_key = '3b319c643ace403e9d87dbd08f2fb587'

topic = 'tesla'

url =   "https://newsapi.org/v2/everything?" \
        f"q={topic}&" \
        "from=2024-12-20&" \
        "sortBy=publishedAt&" \
        "language=en&" \
        "apiKey=3b319c643ace403e9d87dbd08f2fb587" \

# Making a request
request = requests.get(url)

# Getting a dictionary with news data
content = request.json()

# Accessing the articles and discription 
# for article in content['articles']:
#     print(article['title'])
#     print(article['description'])
#     print('\n')


# Making the text for mail
text = "Subject: Today's news " + '\n'
for article in content['articles'][:15]:
    if article['title'] != None and article['description'] != None:
        text = text + article['title'] + '\n' + article['description'] + '\n' + article['url'] + '\n' + '\n'

# Encoding to UTF-8
text = text.encode('utf-8')

# Bringing the function
send_mail(text)