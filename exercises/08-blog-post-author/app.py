import requests

# Your code here

url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
response = requests.get(url)    
data = response.json()
posts = data['posts']
print(posts[0]['author']['name'])



