import os
import json
from notion.client import NotionClient
from notion.block import *
TOKEN_V2 = "5b1c9c57c88f3762e33bc5d15f8488b48360feb113af61facbd99c5f916ed8af1fef5c9a9592bb6787436a8c4aa564559902f8e7c989e50eba5fa9c840df1112794e25e0ab31d8f99bc4e8b13300"
# os.environ["TOKEN_V2"]
WORKSPACE_URL = "https://www.notion.so/MusaForum-TOP-39d9909ed59d4e129c6b1eccb87627d5"
# os.environ["WORKSPACE_URL"]
BLOCK_URL = "https://www.notion.so/5a2a9358771247f686d2cf5de9ff2e66?v=8673d0796123493181d4ab41e220822d"
# os.environ["BLOCK_URL"]


collectionlist = ["球状コンクリーション", "縞状鉄鉱層", "ヒスイ", "ラピスラズリ","ウミユリ","放散虫","アノマロカリス","青色LEDのもと：GaN結晶","タンパク質の結晶化の原理","X線で結晶の構造が分かる！","雪の結晶","カニ"]



def permission(emailad,row):
    # Obtain the `token_v2'value by inspecting your browser cookies on a logged-in (non-guest)
    client = NotionClient(token_v2=TOKEN_V2)
    # Replace this URL with the URL of the page you want to edit
    link = WORKSPACE_URL
    page = client.get_block(link)# print("The old title is:", page.title)
    page.children
    link2 = BLOCK_URL
    page2 = client.get_block(link2)
    # Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
    cv = client.get_collection_view(BLOCK_URL)

    #emailからidを取得
    email = "%s" % emailad
    uid_from_email = client.post('findUser', data={"email": email}).json()['value'] #idを外すと詳細情報が見える

    user_permissions_dict = { 
        'role': 'reader',
        'type': 'user_permission',
        'user_id': uid_from_email['value']['id'] # put the actual user id in here
    }
    
    #全体ページ
    pagenum = len(page.get()['permissions'])
    pageid = []
    for i in range(pagenum):
        pageid.append(page.get()['permissions'][i]['user_id'])
    if(uid_from_email['value']['id'] not in pageid):
        page.get()['permissions'].append(user_permissions_dict)

    #コレクション一覧
    page2num=len(page2.get()['permissions'])
    page2id = []
    for i in range(page2num):
        page2id.append(page2.get()['permissions'][i]['user_id'])
    if(uid_from_email['value']['id'] not in page2id):
        page2.get()['permissions'].append(user_permissions_dict)

    #コレクション
    #for row in collectionlist:
    sample_text = "%s" % collectionlist[row]
    permission_row_ = cv.collection.get_rows(search=sample_text) #権限を与える行を選択 (ブロックの中で)
    permission_row= permission_row_[0]    

    num = len(permission_row.get()['permissions'])
    col = []
    for i in range(num):
        if(permission_row.get()['permissions'][i]['type']=='user_permission'):
            col.append(permission_row.get()['permissions'][i]['user_id'])

    if(uid_from_email['value']['id'] not in col):
        permission_row.get()['permissions'].append(user_permissions_dict)
        break
        
    # append the user permissions to the local cached dictionary object
    # append で追記されるので、もとの権限はそのまま残ってしまう→配列内で旧データの削除必要か？
    
    # share to web をオフにしていないと、permissionが取得できない
    
    permission_row.set(path=['permissions'], value=permission_row.get()['permissions'])
    page.set(path=['permissions'], value=page.get()['permissions'])
    page2.set(path=['permissions'], value=page2.get()['permissions'])

    # clientまではOK
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }

