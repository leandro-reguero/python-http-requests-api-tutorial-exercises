import requests

# Your code here
url = 'https://assets.breatheco.de/apis/fake/sample/post.php'

my_obj = {"Nombre": "Leandro",
          "Alias": "El Máquina",
          "Apellido": "Reguero",
          "Edad": 22,
          "Sexo": "Cinturón Negro"
          }

post_req = requests.post(url, json = my_obj)
print(post_req.text)

