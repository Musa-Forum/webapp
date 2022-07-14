import os
import json
import requests
from pprint import pprint
from notion_client import Client

def test2():
    token: str = os.environ.get("NOTION_TOKEN", "yourToken")
    notion = Client(auth=token)

    list_users_response = notion.users.list()
    pprint(list_users_response)

    ret = notion.databases.retrieve(database_id="62c3856a670e40c6b30ebd9ff945d5d3")
    pprint(ret)
