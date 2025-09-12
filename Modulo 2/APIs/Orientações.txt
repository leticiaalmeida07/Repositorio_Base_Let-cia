import requests

postar = "http://172.25.253.124:5000/alunos"
leticinha= requests.get(postar)

print("leticinha:", leticinha.json())

dados = { 
    "nome":"Leticia",
    "email":"leticiaalmeida@gmail.com"
}
leticinha_postar= requests.post(postar, json=dados)

print("\n Bem-sucedido!!")
print(leticinha_postar.json())
