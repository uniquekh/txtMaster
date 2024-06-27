import os

API_ID = API_ID = 21179966

API_HASH = os.environ.get("API_HASH", "d97919fb0a3c725e8bb2a25bbb37d57c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7158015873:AAFNXF3OEfexth-SAnpQ6Foa9XGhY6HeqAU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7326397503))

LOG = -1002159061590

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7326397503").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
