class GitHubUser:
    def __init__(self, data):
        self.avtar = data["avatar_url"]
        self.username = data["login"]
        self.id = data["id"]
        self.nodeID = data["node_id"]
        self.acc_type = data["user_view_type"]
        self.is_admin = data["site_admin"] 
        self.name = data["name"] 
        self.company = data["company"]
        self.blog = data["blog"] 
        self.location = data["location"]  
        self.email = data["email"]  
        self.hireable = data["hireable"] 
        self.bio = data["bio"] 
        self.x_username = data["twitter_username"] 
        self.pub_repos = data["public_repos"]
        self.pub_gists = data["public_gists"]
        self.followers = data["followers"]
        self.following = data["following"]

    def display(self):
        print("\n---Identity---")
        print(f"\nProfilr avatar link: {self.avtar}")
        print(f"\nUsername: {self.username}")
        print(f"ID: {self.id}")
        print(f"Node ID: {self.nodeID}")
        print("\n---Profile Overview---")
        print(f"\nName: {self.name}")
        print(f"Followers: {self.followers}")
        print(f"Following: {self.following}")
        print(f"Bio: {self.bio}")
        print("\n---Contact info---")
        print(f"\nEmail: {self.email}")
        print(f"Twitter(X): @{self.x_username}")
        print(f"Comapany: {self.company}")
        print(f"Blog: {self.blog}")
        print(f"Location: {self.location}")
        print(f"Hireable: {self.hireable}")
        print("\n---Account---")
        print(f"\nAccount type: {self.acc_type}")
        print(f"Site admin: {self.is_admin}")
        print("\n---Repo---")
        print(f"\nPublic Repo: {self.pub_repos}")
        print(f"Public Gists: {self.pub_gists}")

class RepoExplorer:
    def Repos(self, data):
        print()

        for i, repository in enumerate(data, start=1):
            print(f"{i}. {repository['name']}")

class RepositorySearch:
    def user_search(self, SearchResponse):
        print("\n")
        for repo in SearchResponse["items"]:
            print("Repository name: "+ repo["name"])
            print("Username: "+ repo["owner"]["login"])
            print("##-----------------------------------------------##")

class Followers:
    def follower_view(self, fler_num):
        print("\n")
        for i, users in enumerate(fler_num, start=1):
            print(f"{i}. {users['login']}")

class PullReq:
    def showPullReq(self, data):
        print()
        for pulls in data:
            print(" * Pull Request Number: #" + str(pulls["number"]))
            print("   Title: " + pulls["title"])
            print()

class BranchesOut:
    def showBranches(self, data):
        print()
        for branch in data:
            print(branch["name"])
    