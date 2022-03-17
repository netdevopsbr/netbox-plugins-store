import requests
import re
import json
import math

class GitHubAPI():
    def get_netbox_json(self, **kwargs):
        '''
            Get JSON from "https://github.com/emersonfelipesp/netbox-plugins-store/blob/develop/repositories.json"
        '''

        json_type = kwargs.get('json_type', 'summary')

        # Define JSON to retrieve from GitHub emersonfelipesp/netbox-plugins-store
        if json_type == 'all':
            github_file_name = 'repositories.json'
        elif json_type == 'summary':
            github_file_name = 'repositories_github.json'
        else:
            return


        ### GitHub Data
        github_user = 'emersonfelipesp'
        github_repo_name = 'netbox-plugins-store'
        github_api_url = self.api_url
        github_read_token = self.read_token


        # HTTP Request
        get_response = requests.get(
            f'{github_api_url}/repos/{github_user}/{github_repo_name}/contents/{github_file_name}',
            headers = {
                "Accept": "application/vnd.github.v3+json",
                "Authorization": f"token {github_read_token}"
            }
        ).json()

        raw_content_url = get_response.get('download_url')

        # Get Raw Content of 'repositories.json' file from GitHub 'emersonfelipesp/netbox-plugins-store' repo
        get_json_file = requests.get(
            raw_content_url,
            headers = {
                "Authorization": f"token {github_read_token}"
            }
        )
        return

        # Convert HTTP response to 'dict'
        repositories = json.loads(get_json_file.text)
        return repositories


    def get_repos_name(self):
        '''
            Look for Netbox Repositories names going to:
            "github.com/topics/netbox-plugin"
        '''

        github_url = self.url
        github_read_token = self.read_token

        # Get Github topics/netbox-plugin page
        page = requests.get(
            f'{github_url}/topics/netbox-plugin',
            headers = {
                "Authorization": f"token {github_read_token}"
            }
        )
        text = page.text

        # Look through page content for the number of public repositories
        repos_number = re.findall(r'\d{2} public repositories', text)
        repos_number = re.findall(r'\d{2}', repos_number[0])[0]

        # Define number of pages that should be fetched
        number_of_pages = int(math.ceil(int(repos_number) / 30))
        if number_of_pages == 0:
            number_of_pages = 1

        # Create empty array to received repositories found on page
        repos_name = []

        # Loop until fetch all pages needed to match the number of repos (30 repos per page)
        i = 1
        while number_of_pages >= i:

            # If not first page (results are already acccessable from the first request), fetch i'th page
            if not i == 1:
                page = requests.get(
                    f'{github_url}/topics/netbox-plugin?page={i}',
                    headers = {
                        "Authorization": f"token {github_read_token}"
                    }
                )
                    
                text = page.text

            # Search for this regex match on page results
            regex_match = re.findall(
                r'Explore, go to repository, location:explore feed" href="\/[\w,\d\-]*\/[\w,\d\-]*"', text)

            # Loop through every result, separating regular text from repo /author/name
            for item in regex_match:
                item = re.findall(r'\/[\w,\d\-]*\/[\w,\d\-]*', item)
                repos_name.append(item[0])

            i += 1
        
        return repos_name
    

    def get_repo_json(self, repository_name):
        '''Based on repository name, returns JSON from GitHub API'''

        github_api_url = self.api_url
        github_read_token = self.read_token

        # HTTP Request
        data = requests.get(
            f'{github_api_url}/repos{repository_name}',
            headers = {
                "Accept": "application/vnd.github.v3+json",
                "Authorization": f"token {github_read_token}"
            }
        )

        # Convert HTTP Response to JSON
        data = data.json()

        # Check for TOKEN error
        if data.get('message') == 'Bad credentials':
            print("Token is wrong.")
            return

        # Return GitHub API Repository JSON
        return data


    def get_repos_all(self):
        '''Saves GitHub API (Repos Endpoint) to list without treating JSON'''
        repos = self.get_repos_name()

        repositories = []

        for repo in repos:
            data = self.get_repo_json(repo)
            repositories.append(info)

        return repositories


    def get_repos_summary(self):
        repos = self.get_repos_name()

        repositories = []

        for repo in repos:
            data = self.get_repo_json(repo)

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


    def __init__(self, github_url, github_api_url, github_read_token):

        # GitHub Parameters to run API
        self.url = github_url
        self.api_url = github_api_url
        self.read_token = github_read_token


def write_json_file(repos_json, **file_params):
    '''
        Write JSON passed to file using FILENAME provided or default "repositories.json"
    '''
    filename = str(file_params.get('filename', 'repositories_fixed.json'))

    # Open file
    f = open(f'{filename}', 'w')

    # Write returned JSON to file
    f.write(json.dumps(repos_json))


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

        # Calls GitHubAPI's create_netbox_repos() method
        repositories = GitHubAPI(
            'https://github.com',
            'http://api.github.com',
        ).create_netbox_repos()

        # Save retured JSON from GitHub to 'repositories_fixed.json' file
        write_file = write_json_file(json.dumps(repositories))

    return repositories


# JSON returned from GitHub
github_object = GitHubAPI(
    'https://github.com',
    'http://api.github.com',
    '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',
)

# Useful functions
repos_json_all = github_object.get_netbox_json(json_type = 'all')
repos_json_summary = github_object.get_netbox_json(json_type = 'summary')
repos_name = github_object.get_repos_name()


def search_github_json(plugin_name):
    # Check if NAME provided in URL is Plugin
    for repo_name in repos_name:
        # If Plugin name found, look for JSON
        if plugin_name in repo_name:
            for json in repos_json_all:
                # If GitHub JSON of Plugin found, return it.
                json_r = json.get('name')
                if json_r == plugin_name:
                    return json

                
        
        