from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pathlib import Path
import os

outputFolder = Path("output")
outputFolder.mkdir(exist_ok=True)

# ANSI-Codes presets
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

settings = {
    "fontSize": 500,
    "HSize": 1800,
    "VSize": 1200
}

def CreateImage():
    image = Image.new("RGB", (settings["HSize"], settings["VSize"]), "white")
    draw = ImageDraw.Draw(image)
    ImageWidth = image.width
    ImageHeight = image.height

    UserText = input("Enter Text: ")
    fontSize = settings["fontSize"]

    while True:
        font = ImageFont.truetype("fonts/arial.ttf", fontSize)
        bbox = draw.textbbox((0, 0), UserText, font=font)
        TextWidth = bbox[2] - bbox[0]

        if TextWidth <= image.width:
            break
        
        fontSize -= 1

    x = ImageWidth / 2
    y = ImageHeight / 2

    draw.text((x, y), UserText, fill="black", font=font, anchor="mm")

    image.save("output/output.png")
    image.show()



while True:

    ProgrammCommand = input("> ")
    CommandPart = ProgrammCommand.split()

    if CommandPart[0] == "run":
        CreateImage()

    elif CommandPart[0] == "set":
        if len(CommandPart) < 3:
            print(f"{RED}[ERROR] Parameter missing. Command use: set [setting] [value]{RESET}")
        else:
            if CommandPart[1] == "fontSize":
                if int(CommandPart[2]) > 0:
                    settings["fontSize"] = int(CommandPart[2])
                    print(f"{CYAN}[INFO] Success! Font size is {settings["fontSize"]} now.{RESET}")
                else:
                    print(f"{RED}[ERROR] Value cannot be 0 or negative.{RESET}")
            elif CommandPart[1] == "HSize":
                if int(CommandPart[2]) > 0:
                    settings["HSize"] = int(CommandPart[2])
                    print(f"{CYAN}[INFO] Success! Horizontal size is {settings["HSize"]} now.{RESET}")
                else:
                    print(f"{RED}[ERROR] Value cannot be 0 or negative.{RESET}")
            elif CommandPart[1] == "VSize":
                if int(CommandPart[2]) > 0:
                    settings["VSize"] = int(CommandPart[2])
                    print(f"{CYAN}[INFO] Success! Vertical size is {settings["VSize"]} now.{RESET}")
                else:
                    print(f"{RED}[ERROR] Value cannot be 0 or negative.{RESET}")
            else:
                print(f"{RED}[ERROR] Invalid setting. Please use 'help' for more info.{RESET}")

    elif CommandPart[0] == "delete":
        confirm = input("Are you sure you want to delete the latest output image? (y/n)")
        if confirm == "y":
            if Path("output/output.png").exists():
                os.remove("output/output.png")
                print(f"{CYAN}[INFO] Latest output image has been deleted.{RESET}")
            else:
                print(f"{RED}[ERROR] There is no output image to delete.{RESET}")
        else:
            print(f"{CYAN}[INFO] Deletion cancelled.{RESET}")
    elif CommandPart[0] == "exit":
        break
    else:
        print(f"{RED}[ERROR] Command not found. Please enter a valid command.{RESET}")




print(f"{CYAN}[INFO] Ending Programm{RESET}")