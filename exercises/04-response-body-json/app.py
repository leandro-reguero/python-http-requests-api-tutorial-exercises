import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
print(response.text)


data = response.json()
print(data)
hours = data['hours']
minutes = data['minutes']
seconds = data['seconds']

print(f"Current time: {hours} hrs {minutes} min and {seconds} sec")