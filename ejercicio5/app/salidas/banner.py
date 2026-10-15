import pyfiglet
from colorama import Fore, Style


def mostrar(evento):
    print(Fore.CYAN + pyfiglet.figlet_format(evento, font="slant") + Style.RESET_ALL)
    print(Fore.YELLOW + "   ¡Te esperamos! Inscripciones abiertas." + Style.RESET_ALL)
