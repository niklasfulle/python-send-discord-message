"""
-
"""

# pylint: disable-msg=W0603,W0718,E1101,C0209,E0401,E0611,W0105,R0903,R0913,W0622,W0719,C0301,W0621,W0602,C0103,W3101
import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")

payload = {"content": sys.argv[1]}
headers = {"Authorization": os.getenv("AUTH")}

res = requests.post(url, payload, headers=headers)
