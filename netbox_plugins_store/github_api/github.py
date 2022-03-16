import requests
import re
import json
import math


class GitHubAPI():
    def get_netbox_repos(self):
        github_url = self.url
        github_api_url = self.api_url

        # Get Github topics/netbox-plugin page
        page = requests.get(f'{github_url}/topics/netbox-plugin')
        text = page.text

        # Look through page content for the number of public repositories
        repos_number = re.findall(r'\d{2} public repositories', text)
        repos_number = re.findall(r'\d{2}', repos_number[0])[0]

        # Define number of pages that should be fetched
        number_of_pages = int(math.ceil(int(repos_number) / 30))
        if number_of_pages == 0:
            number_of_pages = 1

        # Create empty array to received repositories found on page
        repos = []

        # Loop until fetch all pages needed to match the number of repos (30 repos per page)
        i = 1
        while number_of_pages >= i:

            # If not first page (results are already acccessable from the first request), fetch i'th page
            if not i == 1:
                page = requests.get(
                    f'https://github.com/topics/netbox-plugin?page={i}')
                text = page.text

            # Search for this regex match on page results
            regex_match = re.findall(
                r'Explore, go to repository, location:explore feed" href="\/[\w,\d\-]*\/[\w,\d\-]*"', text)

            # Loop through every result, separating regular text from repo /author/name
            for item in regex_match:
                item = re.findall(r'\/[\w,\d\-]*\/[\w,\d\-]*', item)
                repos.append(item[0])

            i += 1

        repositories = []
        for repo in repos:
            # HTTP Request
            data = requests.get(
                f'http://api.github.com/repos{repo}',
                headers={
                    "Authorization": f"token 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"
                }
            )

            # Convert HTTP Response to JSON
            data = data.json()

            if data.get('message') == 'Bad credentials':
                print("Token is wrong.")
                return

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

        return repositories

    def __init__(self, url, api_url):

        # GitHub Parameters to run API
        self.url = url
        self.api_url = api_url


def write_json_file(repos_json):
    # Open file
    f = open('repositories_fixed.json', 'w')

    # Write returned JSON to file
    f.write(repos_json)


def check_for_json_file():
    '''If JSON file exists, return it. Else creates it and save to file.'''

    try:
        f = open('repositories_fixed.json')
        print('File found.')

        # Read file
        repositories = f.read()

        # Convert 'str' to 'dict'
        repositories = json.loads(repositories)

    except FileNotFoundError:
        print('File not Found. Creating it.')

        # Calls GitHubAPI's get_netbox_repos() method
        repositories = GitHubAPI(
            'https://github.com',
            'http://api.github.com',
        ).get_netbox_repos()

        # Save retured JSON from GitHub to 'repositories_fixed.json' file
        write_file = write_json_file(json.dumps(repositories))

    return repositories


# JSON returned from GitHub
repositories = check_for_json_file()
