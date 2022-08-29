import json


with open("config.json") as conf:
    config = json.load(conf)
discord_token   = config["discord"]["token"]
discord_prefix  = config["discord"]["prefix"]
discord_owners  = config["discord"]["owners"]
blacklist       = config["discord"]["blacklist"]
VERSION         = config["bot"]["version"]
