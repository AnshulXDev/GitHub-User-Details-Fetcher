# @codedrust

import requests

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
        print("\nPlease enter a valid number!")
        continue

    if choice == 1:

        username = input("\nEnter GitHub Username: ")
        url = f"https://api.github.com/users/{username}"

        response = requests.get(url)
        data = response.json()

        fetch_username = data["login"] 
        id = data["id"] 
        nodeID = data["node_id"] 
        avtarURL = data["avatar_url"] 
        account_type = data["user_view_type"] 
        is_admin = data["site_admin"] 
        name = data["name"] 
        company = data["company"] 
        blog = data["blog"] 
        location = data["location"] 
        email = data["email"] 
        hireable = data["hireable"] 
        bio = data["bio"] 
        x_username = data["twitter_username"] 
        pub_repos = data["public_repos"]
        pub_gists = data["public_gists"]
        followers = data["followers"] 
        following = data["following"] 


        print(f"\nProfile Avtar link: {avtarURL}")
        print(f"\nUsername: {fetch_username}")
        print(f"ID: {id}")
        print(f"NodeID: {nodeID}")
        print(f"Name: {name}")
        print(f"Followers: {followers}")
        print(f"Following: {following}")
        print(f"Bio: {bio}")

        print(f"\nEmail: {email}")
        print(f"Twiteer(X) username: {x_username}")
        print(f"Company: {company}")
        print(f"Blog: {blog}")
        print(f"Hireable: {hireable}")
        print(f"Location: {location}")

        print(f"\nAccount Type: {account_type}")
        print(f"Is admin: {is_admin}")

        print(f"\nPublic Repostory: {pub_repos}")
        print(f"Public Gists: {pub_gists}")

    elif choice == 2:

        username = input("\nEnter Username: ")
        url = f"https://api.github.com/users/{username}/repos"

        response = requests.get(url)
        data = response.json()

        print("\n")
        for repos in data:
            print(repos["name"])

    elif choice == 3:

        repos = input("Enter Repository: ")
        url = f"https://api.github.com/search/repositories?q={repos}"

        response = requests.get(url)
        data = response.json()

        print("\n")
        for repos in data["items"]:
            print("Repository name: "+ repos["name"])
            print("Username: "+ repos["owner"]["login"])
            print("##-----------------------------------------------##")

    elif choice == 4:
        username = input("Enter Username: ")
        url = f"https://api.github.com/users/{username}/followers"

        response = requests.get(url)
        data = response.json()

        print()
        for userFollowers in data:
            print(userFollowers["login"])

    elif choice == 5:
        ownerID = input("Enter owner's username: ")
        repoName = input("Enter Repository name: ")

        url = f"https://api.github.com/repos/{ownerID}/{repoName}/pulls"

        response = requests.get(url)
        data = response.json()

        print()
        for pulls in data:
            print("PR Number: #"+ str(pulls["number"]))
            print("Title: "+ pulls["title"])
            print()

    elif choice == 6:
        username = input("Enter username: ")
        repo = input("Enter Repository name: ")

        url = f"https://api.github.com/repos/{username}/{repo}/branches"

        response = requests.get(url)
        data = response.json()

        print()
        for branch in data:
            print(branch["name"])

    elif choice == 7:
        break

    else:
        print("Invalid choice!")
