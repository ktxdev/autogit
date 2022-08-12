from ast import arg
from asyncio import subprocess
import os
from pathlib import Path
from sys import argv
from config import setup, get_configs, write_configs, CONFIG_HELP_TEXT, AVAILABLE_CONFIG_OPTIONS, PROJECTS_DIR_KEY

GITHUB_LOGIN_URL = "https://github.com/login"
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
            project_dir = Path.joinpath(projects_dir, argv[len(argv) - 1])

            if project_dir.exists():
                if argv.__contains__("-f"):
                    project_dir.rmdir()
                else:
                    print("Another project with same name already exists")
                    return

            project_dir.mkdir()
            # Move to the project dir
            os.chdir(project_dir)
            # Create a ReadMe.md file
            readme_file = Path.joinpath(project_dir, "README.md")
            readme_file.touch()
            # Initialize a git repository
            # Create a repo on github
            # Add the remote to local project
            # Make initial commit
            # Push to github


if __name__ == '__main__':
    setup()
    main()
