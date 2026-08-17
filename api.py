import requests

class GitHubAPI:
    mainURL = "https://api.github.com/"
    def getUser(self, username):
        response = requests.get(f"{self.mainURL}users/{username}")
        
        if response.status_code == 200:
            return response.json()
        else:
            print("Error occured :(")

class RepoExplore:
    def repos(self, username):
        response = requests.get(f"{GitHubAPI.mainURL}users/{username}/repos")

        if response.status_code == 200:
            return response.json()
        else:
            print("Error occured :(")

class RepoSearch:
    def search(self, search):
        response = requests.get(f"{GitHubAPI.mainURL}search/repositories?q={search}")

        if response.status_code == 200:
            return response.json()
        else:
            print("Error occured :(")

class Follower:
    def followers(self, username):
        response = requests.get(f"{GitHubAPI.mainURL}users/{username}/followers")

        if response.status_code == 200:
            return response.json()
        else:
            print("Error occured :(")

class PullRequest:
    def pullReq(self, username, repoName):
        response = requests.get(f"{GitHubAPI.mainURL}repos/{username}/{repoName}/pulls")

        if response.status_code == 200:
            return response.json()
        else:
            print("Error occured :(")

class Branches:
    def branch(self, username, repo):
        response = requests.get(f"{GitHubAPI.mainURL}repos/{username}/{repo}/branches")

        if response.status_code == 200:
            return response.json()
        else:
            print("Error occured :(")