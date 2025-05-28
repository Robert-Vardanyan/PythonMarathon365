import re
from colorama import init, Fore, Style

init(autoreset=True)

emoji_dict = {
    "happy": "😄",
    "sad": "😢",
    "love": "❤️",
    "dog": "🐶",
    "cat": "🐱",
    "sun": "☀️",
    "moon": "🌙",
    "fire": "🔥",
    "cool": "😎",
    "ok": "👌",
    "pizza": "🍕",
    "sleep": "😴",
    "party": "🎉",
    "coffee": "☕",
    "car": "🚗",
    "book": "📚",
    "computer": "💻",
    "money": "💰"
}

def translate_to_emoji(text):
    words = re.findall(r"\w+|\W+", text.lower())  # сохраняем пробелы и знаки препинания
    translated = ""
    for word in words:
        if word.strip().isalnum() and word in emoji_dict:
            translated += emoji_dict[word] + " "
        else:
            translated += word
    return translated.strip()

def main():
    print(Fore.LIGHTBLUE_EX + "💬 Welcome to the Emoji Translator!\n" + Style.RESET_ALL)
    while True:
        user_input = input(Fore.LIGHTWHITE_EX + "Enter your text: ")
        translation = translate_to_emoji(user_input)
        print(Fore.YELLOW + "🔤 Translated: " + Fore.GREEN + translation + Style.RESET_ALL)

        again = input(Fore.CYAN + "\nTranslate another? (y/n): ").strip().lower()
        if again != 'y':
            print(Fore.LIGHTRED_EX + "👋 Bye! Stay expressive!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
