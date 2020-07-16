import requests
import os

userName = input("Enter you github username:")
repoName = input("Enter the name of the repository you want to create:")
token = os.getenv('GIT_TOKEN')
description = input("Enter description for your repo:")
private = False

if token == None:
    print("You haven't set up TOKEN. Check out how to set up the TOKEN")
    exit()

while True:
    ch = int(input("1)Private repo 2)Public repo \nEnter your choice:"))
    if ch == 1:
        private = True
        break
    if ch == 2:
        #private = False
        break
    else:
        print("Invalid choice...")
        continue

query_url = "https://api.github.com/user/repos"
headers = {"authorization" : f"token {token}"}
data = {"name" : f"{repoName}",
        "description" : f"{description}",
        "private": private}


response = requests.post(query_url, headers=headers, json= data)
responseJSON = response.json()

try:
    print(responseJSON["html_url"], "- Link to visit your repository")
except:
    print("Report creation error...")
