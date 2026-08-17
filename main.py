from api import GitHubAPI
from api import RepoExplore
from api import RepoSearch
from api import Follower
from api import PullRequest
from api import Branches
from output import GitHubUser
from output import RepoExplorer
from output import RepositorySearch
from output import Followers
from output import PullReq
from output import BranchesOut

while True:
    print("\n--------------------------")
    print("1. Profile Detail        |")
    print("2. Repository Explorer   |")
    print("3. Search Repository     |")
    print("4. Followers Viewer      |")
    print("5. Pull Requests         |")
    print("6. Branches              |")
    print("7. Quit                  |")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("\nPlease enter a number!")
        continue

    if choice == 1:
        username = input("Enter GitHub username: @")
        api = GitHubAPI()
        data = api.getUser(username)
        if data:
            user = GitHubUser(data)
            user.display()
        else:
            print("User not found!")

    elif choice == 2:
        repo = RepoExplore()
        username = input("Enter GitHub username: @")
        data = repo.repos(username)
        if data:
            reposes = RepoExplorer()
            reposes.Repos(data)
        else:
            print("No repo(s) found!")

    elif choice == 3:
        repoS = RepoSearch()
        search = input("Search Repo: ")
        SearchResponse = repoS.search(search)
        if SearchResponse:
            output = RepositorySearch()
            output.user_search(SearchResponse)
        else:
            print("No repo(s) found!")

    elif choice == 4:
        var = Follower()
        username = input("Enter GitHub username: ")
        fler_num = var.followers(username)
        if fler_num:
            output = Followers()
            output.follower_view(fler_num)
        else:
            print("User not found! :/")

    elif choice == 5:
        var = PullRequest()
        username = input("Enter Username: ")
        repoName = input("Enter Repository name: ")
        data = var.pullReq(username, repoName)
        if data:
            output = PullReq()
            output.showPullReq(data)
        else:
            print("\nUser or Repo not found or there is no pull requests!")

    elif choice == 6:
        var = Branches()
        username = input("Enter username: ")
        repo = input("Enter Repository name: ")
        data = var.branch(username, repo)
        if data:
            output = BranchesOut()
            output.showBranches(data)
        else:
            print("\nUser or Repo not found! Try again.")

    elif choice == 7:
        break

    else:
        print("Invalid choice")