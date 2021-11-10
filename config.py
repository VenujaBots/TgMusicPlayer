from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQCzsuXwrGOtlF7CcoNO-WZTp1FVuIi_W7-2ZCShKj0nz7fFfXJMPDgnchpmqSMsNiJJoDsNLqRbGenptmdY52L72WCQLqNBnku8Wf-24X9hGfNy3Sbm3gneTyZ24svIX9lt8CYdBgQGMAkwZVSDAEEz7q8nRyd6NAC7Z2azw3ffDmVhqQmCw8NakaD0Zsylrv1WTlqN_uHbPHJdsonwwyEP1EPie-5SFWCBfe_31djSET3x2WjRB0xmefxPGkxCybJLUEUPv9ouP0hytTaBZzVS3Pj_Vog3CuowJW2DTvIphaAZiW0Eykr2wg3ePqHvCgCEwTNdm7wP1rfhpdGrKZvKbN33ZwA")
BOT_TOKEN = getenv("2056447071:AAGakeL_LqhxnmQZsTSeK2vWc28Lr6GZ5zc")

API_ID = int(getenv(7395896))
API_HASH = getenv("cd3998ddf318dad74d7c506731bc0abc")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("1826486119").split()))

