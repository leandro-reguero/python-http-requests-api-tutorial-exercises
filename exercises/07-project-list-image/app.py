import requests
import pandas as pd

# Your code here
url = 'https://assets.breatheco.de/apis/fake/sample/project_list.php'

response = requests.get(url)

data = response.json()

last = data[-1]

print("This is the link for the last image of the last project: ")
print(last['images'][-1])