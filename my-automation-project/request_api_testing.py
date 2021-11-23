import requests

response = requests.get("https://gitlab.com/api/v4/user/nanuchi/projects")
project = response.json()
print(type(project))
