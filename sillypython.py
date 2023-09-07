import random
import sys
import os

def sillyfy(python_code: str):
    unique_characters = list(set(python_code))
    new_character_meanings = dict()
    for character in unique_characters:
        random_character = random.choice(unique_characters)
        while random_character in new_character_meanings:
            random_character = random.choice(unique_characters)
        new_character_meanings[character] = random_character
    new_python_code = python_code
    for character, new_character in new_character_meanings.items():
        new_python_code = new_python_code.replace(character, new_character)
    return new_python_code, new_character_meanings

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
███████╗██╗██╗     ██╗  ██╗   ██╗    ██████╗ ██╗   ██╗
██╔════╝██║██║     ██║  ╚██╗ ██╔╝    ██╔══██╗╚██╗ ██╔╝
███████╗██║██║     ██║   ╚████╔╝     ██████╔╝ ╚████╔╝ 
╚════██║██║██║     ██║    ╚██╔╝      ██╔═══╝   ╚██╔╝  
███████║██║███████╗███████╗██║       ██║        ██║   
╚══════╝╚═╝╚══════╝╚══════╝╚═╝       ╚═╝        ╚═╝   """)
    if len(sys.argv) < 2:
        print("[Error] No args given, use -h or --help to get a help menu with all commands displayed.")
    elif "-a" in sys.argv or "--about" in sys.argv:
        print("Programmed by TN3W\nMake your Python code look silly")
        print("- https://github.com/tn3w/sillypython -")
    elif "-h" in sys.argv or "--help" in sys.argv:
        print("Use the following command arguments:")
        print("-a, --about               > Displays an About menu with information about the software")
        print("-h, --help                > Displays this help menu")
        print("-f, --file <filename>     > Define the file which should look silly")
        print("-i, --iterations <number> > How many layers of sillyity there should be. (Default: 10000)")
    input("Enter: ")
    exit()
            
            
        
