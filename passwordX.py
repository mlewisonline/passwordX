import pyperclip as pc
import random
import string
import hashlib
import requests
import getpass
import csv


class Menu_system:
    '''
    Class for the main menu of the program.
    keeps track of the user's choice and calls the appropriate functions.
    '''
    def __init__(self) -> None:
        self._main_title = """
 ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · ▄▄▌ ▐ ▄▌      ▄▄▄  ·▄▄▄▄      ▐▄• ▄ 
▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. ██· █▌▐█▪     ▀▄ █·██▪ ██      █▌█▌▪
 ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌     ·██· 
▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█▐█▌██▐█▌▐█▌.▐▌▐█•█▌██. ██     ▪▐█·█▌
.▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀•     •▀▀ ▀▀
                            By Matthew Lewis 2023
"""

        self._main_options = """
    Main Menu
        
        1: Generate Password
        2: Generate Passphrase
        3: Test Password (HaveIBeenPwnd)
        4: Exit
"""

        self._pass_options = """
    Password Menu:
    ------------------------------------------------------
    Length recommended between 8 - 128 characters

    Character set options:
        1: Upper, Lower, Numbers
        2: Upper, Lower, Numbers and Symbols
        3: Upper, Lower and Symbols
        B: Back to main menu\n
"""

        self._word_options = """
    Memorable Password Generator:
    ------------------------------------------------------
    multi-word passwords are much better than 
    hard-to-remember “complex” passwords.

    Create a multi word password:
    Enter the number of words required
    Capitalize the First Letter ? y/n
    Have the words in UPPERCASE ?  y/n
    Select a separator ( - * ^ space)
    B: Back to main menu\n
"""

        self._pwnd_options = """
    Have I been Pwned Password Check:
    ------------------------------------------------------
    check if your current password has been involved in
    any breaches. The tool will display the number of times
    your password has been seen in a breach.
    
    If your password is in any breaches change it.
    FYI: you password wont display on screen when you type\n
"""

    @property
    def main_title(self):
        return self._main_title

    @property
    def main_options(self):
        return self._main_options

    @property
    def pass_options(self):
        return self._pass_options

    @property
    def word_options(self):
        return self._word_options

    @property
    def pwnd_options(self):
        return self._pwnd_options

    def clear_screen(self):
        print("\033c", end="")

    def start_menu(self):
        while True:
            self.clear_screen()
            print(self.main_title, end="")
            print(self.main_options)
            response = input("What would you like to do? ").strip()
            match response:
                case "1":
                    self.password_menu()
                case "2":
                    self.words_menu()
                case "3":
                    self.pwnd_check()
                case "4":
                    quit()

    def password_menu(self):
        while True:
            self.clear_screen()
            print(self.main_title, end="")
            print(self.pass_options)
            try:
                length = int(input("Required length: "))
                char_set = int(input("Required character set: "))
                if char_set not in range(1, 4):
                    continue
            except ValueError:
                return
            else:
                password = generate_random_password(length, char_set)
                print(f"Your new password: {password} --> copied to clipboard")
                pc.copy(password)
                input("\n<--Press enter to return")
                return

    def words_menu(self):
        while True:
            self.clear_screen()
            print(self.main_title, end="")
            print(self.word_options)
            try:
                num_words = int(input("How many words: ").strip())
            except:
                return
            else:
                is_caps = input("Capitalized words: ").strip().lower()
                if is_caps == "yes" or is_caps == "y":
                    is_caps = True
                else:
                    is_caps = False
                is_upper = input("Uppercase words: ").strip().lower()
                if is_upper == "yes" or is_upper == "y":
                    is_upper = True
                else:
                    is_upper = False
                sep = input("Enter a Separator: ")
                passphrase = multi_word_password(num_words, is_caps, is_upper, sep)
                print(f"Your new password: {passphrase} --> copied to clipboard")
                pc.copy(passphrase)
                input("\n<--Press enter to return")
                return

    def pwnd_check(self):
        while True:
            self.clear_screen()
            print(self.main_title, end="")
            print(self.pwnd_options)
            result = check_password(getpass.getpass("Enter your password: "))
            if result > 0:
                print(
                    f"FAIL - This password has been seen in {result} of breaches.\nDO NOT USE THIS PASSWORD"
                )
            else:
                print(f"{result} breaches seen.")
            input("\n<--Press enter to return")
            return


def main():
    menu = Menu_system()
    menu.start_menu()


def generate_random_password(length: int = 8, character_set: int = 2) -> str:
    """
    Generate a random password s using the supplied parameters.

    Parameters
    ----------
    length : int default = `8`
    supply a s length from 8 to 128

    character_set : int default = `2`
        1: character_set (upper, lower, numbers)
        2: character_set (upper, lower, numbers, symbols)
        3: character_set (upper, lower, symbols)

        Allowed symbols are !@#$%^&*

    Returns
    -------
    s : str
    a value in string format
    """
    symbols = "!@#$%^&*"
    s = str()
    match character_set:
        case 1:
            # Default set of characters (upper, lower, numbers)
            while not all(
                (
                    any(map(lambda x: x in string.ascii_uppercase, s)),
                    any(map(lambda x: x in string.ascii_lowercase, s)),
                    any(map(lambda x: x in string.digits, s)),
                )
            ):
                s = ""
                for _ in range(length):
                    s += random.choice(
                        string.ascii_uppercase + string.ascii_lowercase + string.digits
                    )
            return s
        case 2:
            # Set of characters (upper, lower, numbers, symbols)
            while not all(
                (
                    any(map(lambda x: x in string.ascii_uppercase, s)),
                    any(map(lambda x: x in string.ascii_lowercase, s)),
                    any(map(lambda x: x in string.digits, s)),
                    any(map(lambda x: x in symbols, s)),
                )
            ):
                s = ""
                for _ in range(length):
                    s += random.choice(
                        string.ascii_uppercase
                        + string.ascii_lowercase
                        + string.digits
                        + symbols
                    )
            return s
        case 3:
            # Set of characters (upper, lower, symbols)
            while not all(
                (
                    any(map(lambda x: x in string.ascii_uppercase, s)),
                    any(map(lambda x: x in string.ascii_lowercase, s)),
                    any(map(lambda x: x in symbols, s)),
                )
            ):
                s = ""
                for _ in range(length):
                    s += random.choice(
                        string.ascii_uppercase + string.ascii_lowercase + symbols
                    )
            return s


def check_password(password: str) -> int:
    """
    Check Password against Have I been Pwned.

    Parameters
    ----------
    string password : str
    This plain text is converted to a SHA1 hash using
    a support function.

    Returns
    -------
    count : int
    The number of times the password has been seen.
    """
    headers = {"user-agent": "passwordX", "api-version": 2}
    range_url = "https://api.pwnedpasswords.com/range/{}"

    hashed_password = get_sha1_hash(password)

    prefix = hashed_password[:5]
    suffix = hashed_password[5:]

    response = requests.get(range_url.format(prefix), headers).text

    for line in iter(response.splitlines()):
        hex, _, count = line.partition(":")
        if hex == suffix.upper():
            return int(count)
    return 0


def multi_word_password(  
    num_words: int = 3,
    capitalization: bool = False,
    upper_case: bool = False,
    sep: str = " ",
) -> str:
    """
    Random word combinations are strong but easy to remember, 
    which means it hits the sweet spot for being a good password. 
    function will return a random combination of words.
    using the word list from a CSV file.

    Parameters
    ----------
    num_words : int default = `3`
    capitalization : bool default = `False`
    upper_case : bool default = `False`
    sep : str default = ` " "`

    Returns
    -------
    random_word : str
    """

    wordDB = load_word_data()
    l = list()
    for i in range(num_words):
        word = random.choice(wordDB[0])
        if word not in l:
            l.append(word)
    if capitalization:
        l = [word.capitalize() for word in l]
    if upper_case:
        l = [word.upper() for word in l]
    return sep.join(l)


def get_sha1_hash(str: str):
    """
    Support function to generate a SHA1 hash from a
    string.

    Parameters
    ----------
     plaintext string : str

    Returns
    -------
    hash : str
    """
    hash_obj = hashlib.sha1(str.encode())
    return hash_obj.hexdigest()


def load_word_data():
    """
    Support function to load the word list from a CSV file.

    Parameters
    ----------
    None

    Returns
    -------
    wordDB : list
    """
    try:
        with open("words.csv") as f:
            reader = csv.reader(f)
            return [words for words in reader]
    except FileNotFoundError:
        print("words.csv not found.")


if __name__ == "__main__":
    main()