from requests import get, post


data = input("Data > ")

id = post("http://127.0.0.1:8500/create", data=data).text

url = "http://127.0.0.1:8500/get/" + id

input("Url: " + url)

response = get(url).text

input("Response: " + response)