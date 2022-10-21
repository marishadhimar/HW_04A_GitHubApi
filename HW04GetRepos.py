import requests
import json


def fetchRepos(username):
    """ Fetch repositories and commits"""

    repositoryApi = "https://api.github.com/users/"
    commitsApi = "https://api.github.com/repos/"

    repositoryList = []
    commits = []

    repositoryUrl = repositoryApi + f'{username}/' + 'repos'

    try:
        repo_url = requests.get(repositoryUrl)
    except (TypeError, KeyError, IndexError):
        return "Failed to fetch repository information!"
    repo_url = json.loads(repo_url.text)
    print(repo_url)

    # Get Repository information by github username
    for repo in repo_url:
        try:
            repositoryList.append(repo['name'])
        except (TypeError, KeyError, IndexError):
            return "Repository with name doesn't exist!"

    # Get Number of commits for each repository from repository list
    for repository in repositoryList:
        commitUrl = commitsApi + f'{username}/{repository}/commits'
        try:
            response = requests.get(commitUrl)
        except (TypeError, KeyError, IndexError):
            return "Failed to fetch the commits for repository " + repository
        res_json = json.loads(response.text)
        commits.append(f'Repo: {repository}  Number of commits: {len(res_json)}')
    return commits


def main():
    """ Get user's Github ID as input """

    user = input("Please enter Github username: ")
    result = fetchRepos(user)
    print(result)
    return result

if __name__ == '__main__':
    main()
