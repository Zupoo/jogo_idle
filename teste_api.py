import requests
import json

status = requests.get("http://127.0.0.1:5001/status").json()
print(status)

upgrade = requests.post("http://127.0.0.1:5001/upgrade")
if upgrade.status_code == 200:
    print(upgrade.json())
else:
    print('Deu erro:', upgrade.status_code, upgrade.text)
      
