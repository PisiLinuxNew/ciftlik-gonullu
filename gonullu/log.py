from colorama import init, Fore, Style
import sys


class Log:
    def __init__(self):
        init(autoreset=True)

    @staticmethod
    def error(message):
        # burada hata mesajlarımızı yazdıracağız.
        print(Fore.RED + ' [x] Hata: ' + message + Style.RESET_ALL)

    @staticmethod
    def information(message, continued=False, new_line=False):
        # burada bilgi mesajlarımızı yazdıracağız.
        if continued is True:
            print(Fore.LIGHTBLUE_EX + ' [*] Bilgi: ' + message + Style.RESET_ALL, end="\r")
        else:
            if new_line is True:
                print('\n' + Fore.LIGHTBLUE_EX + ' [*] Bilgi: ' + message + Style.RESET_ALL)
            else:
                print(Fore.LIGHTBLUE_EX + ' [*] Bilgi: ' + message + Style.RESET_ALL)

    @staticmethod
    def success(message):
        # burada başlarılı işlem mesajlarımızı yazdıracağız.
        print(Fore.GREEN + ' [+] Başarılı: ' + message + Style.RESET_ALL)

    @staticmethod
    def warning(message):
        # burada uyarı mesajlarımız olacak.
        print(Fore.YELLOW + ' [!] Uyarı: ' + message + Style.RESET_ALL)

    @staticmethod
    def get_exit():
        print(Fore.RED + ' [x] Hata: Programdan çıkılıyor!' +Style.RESET_ALL)
        sys.exit(0)
