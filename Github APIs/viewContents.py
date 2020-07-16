import requests
import os


print("================================")
print("Viewing contents of a Repository")
print("================================")

username = input("Enter you github username:")
repo = input("Enter the repository name:")
token = os.getenv('GIT_TOKEN')
headers = {}
while True:
    ch = int(input("\n1)Private Repo \n2)Public Repo \nEnter your choice:"))
    if(ch == 1):
        if token == None:
            print("You haven't set up TOKEN. Check out how to set up the TOKEN")
            exit()
        headers = {"authorization" : f"token {token}"}
        break
    elif(ch == 2):
        print("Authentication not required")
        break
    else:
        print("Invalid choice...")
        continue

query_url = "https://api.github.com/repos/{username}/{repo}/contents".format(username = username, repo = repo)

content = requests.get(query_url, headers = headers)
data = content.json()

if "message" in data:
    print(data["message"])
else:
    for i in range(len(data)): 
        print(data[i]["name"])