import requests

username = input("Enter GitHub Username: ")
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
