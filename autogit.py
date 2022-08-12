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

from config import setup, get_configs, write_configs, CONFIG_HELP_TEXT, AVAILABLE_CONFIG_OPTIONS, PROJECTS_DIR_KEY

GITHUB_LOGIN_URL = "https://github.com/login"
NEW_REPO_GITHUB_URL = "https://github.com/new"
AVAILABLE_ACTIONS = ['config', 'create', '--help']
ACTIONS_HELP_TEXT = "Usage: autogit [--help] <command> [<args>]\
    \n\nThese are common Autogit commands used in various situations:\
    \n\n\tconfig - Get or set congifurations\
    \n\tcreate - Creates new project"


def main():
    if len(argv) < 2:
        print("Invalid number of arguments for action:", action)
        return

    action = argv[1]

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

            if not AVAILABLE_CONFIG_OPTIONS.__contains__(command) and not command == '--help':
                print(
                    "Invalid configuration option. Please type `config --help` to see valid options")

            if command == "--help":
                print(CONFIG_HELP_TEXT)
                return

            configs = get_configs()
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

            write_configs(configs)
        case 'create':
            configs = get_configs()

            projects_dir = Path(configs[PROJECTS_DIR_KEY])
            if not projects_dir.exists():
                Path.mkdir(projects_dir)
            # Move to the configured projects dir
            os.chdir(configs[PROJECTS_DIR_KEY])
            # Create the project dir
            project_name = argv[len(argv) - 1]
            project_dir = Path.joinpath(projects_dir, project_name)

            if project_dir.exists():
                if argv.__contains__("-f"):
                    subprocess.call(["rm","-r",project_dir])
                else:
                    print("Another project with same name already exists")
                    return

            project_dir.mkdir()
            # Move to the project dir
            os.chdir(project_dir)
            # Initialize a git repository
            subprocess.call(["git", "init"])
            # Create a repo on github
            username = input('GitHub username:')
            password = input('GitHub password:')
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(GITHUB_LOGIN_URL)
            element = driver.find_element(By.ID, "login_field")
            element.clear()
            element.send_keys(username)
            element = driver.find_element(By.ID, 'password')
            element.clear()
            element.send_keys(password)
            element.send_keys(Keys.ENTER)

            driver.get(NEW_REPO_GITHUB_URL)
            element = driver.find_element(By.ID, 'repository_name')
            element.clear()
            element.send_keys(project_name)

            # element = driver.find_element(By.CLASS_NAME, 'btn')
            element.submit()
            driver.close()

            # Create a ReadMe.md file
            readme_file = Path.joinpath(project_dir, "README.md")
            readme_file.touch()
            readme_file.write_text('# ' + project_name)

            # Add the remote to local project
            subprocess.call(["git", "remote", "add", "origin", f"git@github.com:{username}/{project_name}.git"])
            subprocess.call(["git", "branch", "-M", "main"])
            # Make initial commit
            subprocess.call(["git", "add", "."])
            subprocess.call(["git", "commit", "-m", "Initial commit"])
            # Push to github
            subprocess.call(["git", "push", "-u", "origin", "main"])


if __name__ == '__main__':
    setup()
    main()
