from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQA2ZgFURf-jAd8BuYNNdpbTT_4olywuFHu5TgaDGOq5OBIh4z_k03uKeuGNlURTKrgrdUCv6gawpBq5oQyJ6qxZI8E-mknhK17ZXZFKozz0eevrNWcMwBWEmM0CtPtp9zzW0lD9V9gIDaH0gDqoz02KKzqydIn0XPkv2qgEYid_5HKdEhejPiZAxtbHBOW27J0B93li7_zzlmM3IF9dU2cLAxouPqeSjVzorcbvi5yuq7ZMOiURH-63fyCmpcbd0I-ZOf_X3HHihQZMVzMjzXO9aezRRXaNdxk2TsJ-I5M5t3Z84BnDaXalcrOzp3hu1vGySZAZAZa2cdQuxyhx3V2obN33ZwA")
BOT_TOKEN = getenv("2056447071:AAGakeL_LqhxnmQZsTSeK2vWc28Lr6GZ5zc")

API_ID = int(getenv(7395896))
API_HASH = getenv("cd3998ddf318dad74d7c506731bc0abc")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("1826486119").split()))

