import colorama
from colorama import Fore, Back, Style

colorama.init()

# dir(colorama) - shows all attributes and methods of the module
print("Attributes of colorama:", dir(colorama))

# Fore - changes text color
# contains constants like RED, GREEN, BLUE, YELLOW, RESET etc.
# used to colorize text output in terminal
print(Fore.RED + "This text is red")
print(Fore.GREEN + "This text is green")
print(Fore.BLUE + "This text is blue")

# Back - changes background color
# same constants as Fore but for background
print(Back.YELLOW + "This has yellow background" + Back.RESET)

# Style - changes text style
# BRIGHT - bold text, DIM - dim text, RESET_ALL - reset everything
print(Style.BRIGHT + "This is bright text")
print(Style.DIM + "This is dim text")
print(Style.RESET_ALL + "This is normal text")

# init(autoreset=True) - automatically resets style after each print
# deinit() - restores terminal to original state
