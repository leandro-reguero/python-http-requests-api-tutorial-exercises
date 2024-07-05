import requests


url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"

response = requests.post(url, json = {"id": 2323, "title": "Very big project"}, headers = {"Content-Type": "application/json"})

print(response.text)

