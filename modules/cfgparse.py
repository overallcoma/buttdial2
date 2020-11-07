import configparser


def parse_config(config_file_location):
    config = configparser.ConfigParser()
    config.read(config_file_location)
