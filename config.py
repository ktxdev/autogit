from pathlib import Path, PurePath

PROJECTS_DIR_KEY = 'projects.dir'
AVAILABLE_CONFIG_OPTIONS = ['projects.dir']
DEFAULT_PROJECTS_DIR = PurePath.joinpath(Path.home(), "Projects")
CONFIG_FILE = Path.joinpath(Path.home(), ".autogitconfig")
CONFIG_HELP_TEXT = "Usage: autogit config [--help] <key> <value> \
    \nThese are common Autogit commands used in various situations: \
    \n\tprojects.dir - Get and set projects directory"


def setup() -> None:
    if not CONFIG_FILE.exists():
        CONFIG_FILE.touch()

        default_configs = {}
        for option in AVAILABLE_CONFIG_OPTIONS:
            if option == PROJECTS_DIR_KEY:
                default_configs[option] = DEFAULT_PROJECTS_DIR
            else:
                default_configs[option] = ''

        write_configs(default_configs)


def write_configs(configs: dict) -> None:
    with open(CONFIG_FILE, 'w') as file:

        for config in configs:
            file.write(f'{config}={configs[config]}\n')


def get_configs() -> dict:
    configs = {}

    if not CONFIG_FILE.exists():
        return configs

    with open(CONFIG_FILE, 'r') as file:

        for line in file:
            config = line.split("=")
            configs[config[0]] = config[1].strip("\n")

    return configs
