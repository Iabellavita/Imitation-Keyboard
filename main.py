from pyfiglet import Figlet
import random
import keyboard

TIME_SLEEP = ['0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09', '0.1']


def insert_imitation_text():
    try:
        with open('text.txt', encoding='utf-8') as f:
            text = f.readlines()

        for word in text:
            keyboard.write(word, float(random.choice(TIME_SLEEP)))
    except:
        print("\033[31m\033[4mOOPS, Error...\033[0m")


if __name__ == "__main__":
    preview_text = Figlet(font="small", width=300)
    text = preview_text.renderText('KEYBOARD  IMITATION')
    print(f'\033[35m\033[1m{text}\033[0m')
    print(
        "\033[33m\033[1m\033[4m#1\033[0m---\033[32m\033[1mINPUT YOUR TEXT TO \033[31m\033[4mtext.txt\033[0m \033[32m\033[1mFILE\033[0m\n"
        "\033[33m\033[1m\033[4m#2\033[0m---\033[32m\033[1mDEFINE MOUSE CURSOR ON AREA AND CLICK LEFT BUTTON\033[0m\n"
        "\033[33m\033[1m\033[4m#3\033[0m---\033[32m\033[1mPRESS \033[31m\033[4mCtrl+Q\033[0m \033[32m\033[1mFOR START IMITATION\033[0m\n"
        "\033[33m\033[1m\033[4m#4\033[0m---\033[32m\033[1mPRESS \033[31m\033[4mCtrl+C\033[0m \033[32m\033[1mFOR STOP IMITATION\033[0m\n")

try:
    while True:
        keyboard.add_hotkey("ctrl+q", insert_imitation_text)
except KeyboardInterrupt:
    print("\n\033[31m\033[1m[ERROR]\033[0m PROGRAM STOPPED BY USER\n")

keyboard.release("ctrl+q")
