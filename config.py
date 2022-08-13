from pathlib import Path, PurePath


class Config:

    def __init__(self):
        self.projects_directory_key = 'projects.dir'
        self.available_config_options = ['projects.dir']
        self.config_file = Path.joinpath(Path.home(), '.autogitconfig')
        self.projects_directory = PurePath.joinpath(Path.home(), 'Projects')
        self.config_help_text = 'Usage: autogit config [--help] <key> <value> \
            \nThese are common Autogit commands used in various situations: \
            \n\tprojects.dir - Get and set projects directory'

        self.setup()

    def setup(self):
        if not self.config_file.exists():
            self.config_file.touch()

            default_configs = {}
            for option in self.available_config_options:
                if option == self.projects_directory_key:
                    default_configs[option] = self.projects_directory
                else:
                    default_configs[option] = ''

            self.write_configs(default_configs)

    def write_configs(self, configs: dict) -> None:
        with open(self.config_file, 'w') as file:

            for config in configs:
                file.write(f'{config}={configs[config]}\n')

    def get_configs(self) -> dict:
        configs = {}

        if not self.config_file.exists():
            return configs

        with open(self.config_file, 'r') as file:

            for line in file:
                config = line.split("=")
                configs[config[0]] = config[1].strip("\n")

        return configs
