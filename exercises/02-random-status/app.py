import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")

if response.status_code == 404:
    print(f"The URL you asked for is not found. Error {response.status_code}")
elif response.status_code == 503:
    print(f"Unavailable right now. Error {response.status_code}")
elif response.status_code == 200:
    print(f"Everything went perfect. Error {response.status_code}")
elif response.status_code == 400:
    print(f"Something is wrong with the request params. Error {response.status_code}")
else:
    print(f"Unkown status code. Error {response.status_code}")
