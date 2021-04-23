import yaml

def config():
    with open("config.yaml", "r") as ymlfile:
        config = yaml.load(ymlfile)
    return config