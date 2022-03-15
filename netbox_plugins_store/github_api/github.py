import requests
import re
import json
import time

github_url = 'https://github.com'
github_api_url = 'http://api.github.com'

page = requests.get(f'{github_url}/topics/netbox-plugin')
text = page.text

regex_match = re.findall(
    r'Explore, go to repository, location:explore feed" href="\/[\w,\d\-]*\/[\w,\d\-]*"', text)

# print(regex_match)
repos = []
for item in regex_match:
    item = re.findall(r'\/[\w,\d\-]*\/[\w,\d\-]*', item)
    repos.append(item[0])


repositories = []
f = open('repositories.json', 'w')
for repo in repos:
    data = requests.get(f'{github_api_url}/repos{repo}', headers={
        "Authorization": f"token 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"
    })
    data = data.json()

    info = {
        "id": data["id"],
        "name": data["name"],
        "full_name": repo,
        "owner": {
            "login": data["owner"]["login"],
            "id": data["owner"]["id"],
            "url": data["owner"]["html_url"],
            "type": data["owner"]["type"]
        },
        "url": data["html_url"],
        "description": data["description"],
        "git_url": data["git_url"],
        "clone_url": data["clone_url"],
        "created_at": data["created_at"],
        "updated_at": data["updated_at"],
        "pushed_at": data["pushed_at"],
        "stargazers_count": data["stargazers_count"],
        "watchers_count": data["watchers_count"],
        "language": data["language"],
        "forks": data["forks"],
        "open_issues": data["open_issues"],
        "topics": data["topics"]
    }

    repositories.append(info)

f.write(json.dumps(repositories))
