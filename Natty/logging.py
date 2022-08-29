import logging

import coloredlogs

from Natty import config

log = logging.getLogger(__name__)
coloredlogs.install(level='INFO')
if not config.config["bot"]["debug"]:
    logging.getLogger("nextcord.gateway").setLevel(logging.WARNING)
