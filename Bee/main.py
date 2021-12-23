import os
import config
import time

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()[0]
        words = text.split()
    return words

def send_message(phone_number, message): 
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    words = get_words('bee.txt')
    for word in words:
        time.sleep(1)
        send_message(config.poorPerson, word)