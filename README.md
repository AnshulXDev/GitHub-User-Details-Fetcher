# GitHub User Details Fetcher v2.1

A Python-based tool that fetches and displays GitHub user information using the GitHub API.

## 🚀 What's New in v2.1?

Version **2.1** improves the project structure and output:

- 📁 Split the project into **3 Python files** instead of keeping everything in `main.py`
- ▶️ `main.py` controls the main program
- 🔌 `api.py` handles GitHub API requests
- 🖥️ `output.py` handles displaying the fetched information
- 🔢 Added **index numbers** before followers
- 🌿 Added **index numbers** before branches
- 🧹 Improved code organization and readability

## 📂 Project Structure

```text
GitHub-User-Details-Fetcher/
│
├── main.py       # Main program / entry point
├── api.py        # GitHub API functions
├── output.py     # Output and display functions
└── README.md     # Project documentation
```

## 🔧 How It Works

The program asks for a GitHub username and uses the **GitHub REST API** to fetch information about that user.

It can display details such as:

- 👤 Username
- 📝 Name
- 📖 Bio
- 📦 Public repositories
- 👥 Followers
- 🌿 Repository branches
- 🔗 GitHub profile information
- And other available GitHub details

Followers and branches are displayed with index numbers to make the output easier to read.

Example:

```text
Followers:
1. user_one
2. user_two
3. user_three

Branches:
1. main
2. development
3. testing
```

## 🛠️ Technologies Used

- **Python**
- **GitHub REST API**
- **Requests library**

## 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd GitHub-User-Details-Fetcher
```

Install the required dependency:

```bash
pip install requests
```

## ▶️ Running the Project

Run:

```bash
python main.py
```

Then enter the GitHub username when prompted.

## 🧩 File Responsibilities

### `main.py`

The entry point of the application.

It handles the main program flow and connects the API and output modules.

### `api.py`

Contains functions responsible for communicating with the GitHub API and retrieving user/repository information.

### `output.py`

Contains functions responsible for formatting and displaying the fetched information to the user.

This separation keeps the project cleaner and makes it easier to modify individual parts.

## 👨‍💻 Author

**Anshul**

---

⭐ If you find this project useful, consider giving the repository a star!

📢 Notice: This project is **not simply copy-pasted from AI or another source**. The project was **created by me**, with the code, structure, features, and improvements developed and understood by me. AI may have been used as a learning/helping tool, but the project itself is my own work.
