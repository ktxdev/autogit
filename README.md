# autogit
Autogit provides a command line interface to create a new project on local machine and GitHub, add the git remote url 
to the local machine git repository, attach a README.md file and push an initial commit
## Requirements
___
- Ubuntu Linux
- Python 3.10
- Python 3.10-venv
## Installtion
___
Download the installation file from GitHub
```shell
curl -H "Accept: application/vnd.github.VERSION.raw" https://raw.githubusercontent.com/ktxdev/autogit/main/install.sh > install.sh
```
Make file executable
```shell
chmod +x install.sh
```
Run the script
```shell
sudo ./install.sh
```
Check if installation was successful
```shell
autogit --version # Or -v
```
## Basic  Commands
___
Show available actions and a short description of what they do
```shell
autogit --help
```
Configure the new projects creation directory
```shell
autogit config projects.dir <projects-dir-path>
```
Create a new project
```shell
autogit create <project-name>
```
___
> **NB:** Your can type --help on every command to check available options and what they do