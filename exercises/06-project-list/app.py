import requests
import pandas as pd

# Your code here
url = 'https://assets.breatheco.de/apis/fake/sample/project_list.php'

response = requests.get(url)

data = response.json()
coursera = data[1]

print(coursera['name'])

