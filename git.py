import subprocess


class Git:
    @staticmethod
    def initialize_repo():
        subprocess.call(["git", "init"])

    @staticmethod
    def add_remote(username, repo_name):
        subprocess.call(["git", "remote", "add", "origin",
                        f"git@github.com:{username}/{repo_name}.git"])
        subprocess.call(["git", "branch", "-M", "main"])

    @staticmethod
    def commit(message):
        subprocess.call(["git", "add", "."])
        subprocess.call(["git", "commit", "-m", message])

    @staticmethod
    def push():
        subprocess.call(["git", "push", "-u", "origin", "main"])
