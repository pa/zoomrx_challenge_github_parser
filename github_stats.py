from github3 import login
import csv
import os

repository_name = []
clone_url = []
latest_commit_date = []
latest_commited_author = []
counter = 0

def github_status():
    """
    Creates Github_stats.csv in local filesyastem and calls github_status_parser function.
    """
    github_user_name = os.environ['GITHUB_USERNAME']
    github_password = os.environ['GITHUB_PASSWORD']
    github_connect = login(username=github_user_name, password=github_password)
    try:
        with open('Github_stats.csv', 'w', newline='') as csvfile:
            csvfile.truncate(0)
            fieldnames = ['Repository_Name', 'Clone_Url', 'Latest_Commit_Date', 'Latest_Commited_Author']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            github_status_parser(github_connect, writer)


        csvfile.close()

    except PermissionError as pe:
        print("\nPlease close the CSV file to rewrite")
    except NameError as Ne:
        print("\nEntered orgname/repositoryname is not available")
    except Exception as e:
        print(e)

def github_status_parser(github_connect, writer):
    """
    Retrives specific information from Github and write it to the CSV file.
    :param writer: Module object
    :param github_connect: Github connection object
    """

    try:
        orgname_repo = []
        repository_list = []
        orgname_index = 0
        repo_index = 1

        print("\nPlease enter a list of public Github repositories and type 'quit' to proceed\n")
        while True:
            user_input = input()
            if user_input == "quit":
                break
            repository_list.append(user_input)
        print("\nPlease wait parsing...")

        for line in repository_list:
            orgname_repo = line.split("/")
            orgname = orgname_repo[orgname_index]
            repository_name = orgname_repo[repo_index].rstrip('\n')
            repository = github_connect.repository(orgname, repository_name)
            for repo_commit in repository.commits():
                latest_commit_date = repo_commit._json_data['commit']['committer']['date']
                writer.writerow({'Repository_Name': repository.name,'Clone_Url': repository.clone_url, 'Latest_Commit_Date': latest_commit_date[0:10], 'Latest_Commited_Author':repo_commit.author})
                break
        print("\nParsed to Github_stats.csv file in path :  " + os.getcwd() + "\n")
    except IndexError as Ie:
        print("\nPlease enter a valid orgname/repositoryname")
    except NotFoundError as Ne:
        print("\nEntered orgname/repositoryname is not available")
    except Exception as e:
        print(e)
github_status()
