from colorama import init
from pyfiglet import Figlet
import secrets
import keyboard
import random
import string
import time

init()
TIME_SLEEP = ['0.04', '0.05', '0.06', '0.07', '0.08', '0.09', '0.1', '0.2', '0.3']


def insert_imitation_text(count: int = 0):
    try:
        with open('text.txt', encoding='utf-8') as f:
            text = f.read()
    except:
        print("\n\033[31m\033[1m[ERROR]\033[0m FILE \033[31m\033[4mtext.txt\033[0m does not EXIST!\n")

    counter = []
    positions_for_errors = tuple(random.randint(0, len(text)) for position in range(6))

    for word in text[count:]:
        keyboard.write(word, float(random.choice(TIME_SLEEP)))
        counter.append(word)

        if random.randint(0, len(text)) in positions_for_errors:
            error_str = ''.join(secrets.choice([x for x in string.printable if x not in string.whitespace]) for _ in
                                range(random.randint(1, 2)))
            keyboard.write(error_str, float(random.choice(TIME_SLEEP)))
            for _ in range(len(error_str)):
                time.sleep(0.3)
                keyboard.send('backspace')
                time.sleep(0.3)

        if keyboard.is_pressed('f2'):
            break
    return len(counter) + count


if __name__ == "__main__":
    preview_text = Figlet(font="small", width=300)
    text = preview_text.renderText('KEYBOARD  IMITATION')
    print(f'\033[35m\033[1m{text}\033[0m')
    print(
        "\033[33m\033[1m\033[4m[WARNING]\033[0m---\033[32m\033[1mINPUT YOUR TEXT TO \033[31m\033[4mtext.txt\033[0m \033[32m\033[1mFILE\033[0m\n")

    print(
        "\033[33m\033[1m\033[4m[INFO]\033[0m---\033[32m\033[1mPRESS \033[31m\033[4mF1\033[0m \033[32m\033[1mFOR START \U000025B6 IMITATION\033[0m\n"
        "\033[33m\033[1m\033[4m[INFO]\033[0m---\033[32m\033[1mPRESS \033[31m\033[4mF2\033[0m \033[32m\033[1mFOR PAUSE \U000023F8 IMITATION\033[0m\n"
        "\033[33m\033[1m\033[4m[INFO]\033[0m---\033[32m\033[1mPRESS \033[31m\033[4mF3\033[0m \033[32m\033[1mFOR CONTINUE \U000023E9 IMITATION\033[0m\n"
        "\033[33m\033[1m\033[4m[INFO]\033[0m---\033[32m\033[1mPRESS \033[31m\033[4mF4\033[0m \033[32m\033[1mFOR CLEAR \U0001F9F9 IMITATION TEXT\033[0m\n"
        "\033[33m\033[1m\033[4m[INFO]\033[0m---\033[32m\033[1mPRESS \033[31m\033[4mF5\033[0m \033[32m\033[1mFOR STOP \U000023FA IMITATION TEXT\033[0m")
    try:
        while True:
            if keyboard.is_pressed('f1'):
                count = insert_imitation_text()
            if keyboard.is_pressed('f3'):
                count = insert_imitation_text(count)
            if keyboard.is_pressed('f4'):
                for i in range(count):
                    keyboard.send('backspace')
                    time.sleep(0.05)
            if keyboard.is_pressed('f5'):
                exit()
    except:
        print("\n\033[31m\033[1m[ERROR]\033[0m PROGRAM STOPPED BY USER\n")
