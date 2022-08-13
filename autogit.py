from lib2to3.pgen2 import driver
import os
import subprocess

from sys import argv
from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from git import Git
from config import Config
from github import Github

GITHUB_LOGIN_URL = "https://github.com/login"
NEW_REPO_GITHUB_URL = "https://github.com/new"
AVAILABLE_ACTIONS = ['config', 'create', '--help']
ACTIONS_HELP_TEXT = "Usage: autogit [--help] <command> [<args>]\
    \n\nThese are common Autogit commands used in various situations:\
    \n\n\tconfig - Get or set congifurations\
    \n\tcreate - Creates new project"


def main():
    config = Config()
    
    action = argv[1]

    if len(argv) < 2:
        print("Invalid number of arguments for action:", action)
        return

    if action == '--help':
        print(ACTIONS_HELP_TEXT)
        return

    if not AVAILABLE_ACTIONS.__contains__(action):
        print("Cannont perform unknown action:", action)
        return

    if len(argv) < 3:
        print("Invalid number of arguments for action:", action)
        return

    match action:
        case 'config':
            command = argv[2]

            if not config.available_config_options.__contains__(command) and not command == '--help':
                print(
                    "Invalid configuration option. Please type `config --help` to see valid options")

            if command == "--help":
                print(config.config_help_text)
                return

            configs = config.get_configs()
            if (len(argv) == 3):
                if not configs.__contains__(command):
                    print(command, "config is not been set")
                else:
                    print(configs[argv[2]])
                return

            if len(argv) != 4:
                print(
                    "Invalid number of arguments, type `config --help` to see valid options")
                return

            configs[command] = argv[3]

            config.write_configs(configs)
        case 'create':
            configs = config.get_configs()

            projects_dir = Path(configs[config.projects_directory_key])
            if not projects_dir.exists():
                Path.mkdir(projects_dir)
            # Move to the configured projects dir
            os.chdir(configs[config.projects_directory_key])
            # Create the project dir
            project_name = argv[len(argv) - 1]
            project_dir = Path.joinpath(projects_dir, project_name)

            if project_dir.exists():
                if argv.__contains__("-f"):
                    subprocess.call(["rm", "-r", project_dir])
                else:
                    print("Another project with same name already exists")
                    return

            project_dir.mkdir()
            # Move to the project dir
            os.chdir(project_dir)
            # Initialize a git repository
            Git.initialize_repo()
            # Create a repo on github
            username = input('GitHub username:')
            password = input('GitHub password:')
            Github(username, password).create_repo(project_name)
            # Add the remote to local project
            Git.add_remote(username, project_name)
            # Create a ReadMe.md file
            readme_file = Path.joinpath(project_dir, "README.md")
            readme_file.touch()
            readme_file.write_text('# ' + project_name)
            # Make initial commit
            Git.commit("Initial commit")
            # Push to github
            Git.push()


if __name__ == '__main__':
    main()
