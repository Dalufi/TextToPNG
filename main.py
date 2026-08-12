print("Starting...")
print("")

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pathlib import Path
import os
import sys
import shutil

outputFolder = Path("output")
outputFolder.mkdir(exist_ok=True)

os.system("title TextToPNG - Terminal interface v0.2.0")

# ANSI-Codes presets
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Critical error codes
def Err1():
    print(f"{RED}[CRITICAL ERROR] No fonts or font type is not supported.{RESET}")
    sys.exit(f"{YELLOW}[WARNING] Program was ended forcefully{RESET}")

# Startup checks
if not any(file.suffix.lower() in [".ttf"] for file in Path("fonts").iterdir()):
    Err1()
for file in Path("fonts").iterdir():
    if not file.name ==  "Roboto.ttf":
        source = Path("assets/mainFont/Roboto.ttf")
        destination = Path("fonts/Roboto.ttf")

        shutil.copy(source, destination)

settings = {
    "fontSize": 500,
    "HSize": 1800,
    "VSize": 1200,
    "font": "Roboto"
}

COMMANDLIST = {
    "run": {
        "description": "Starts the program",
        "usage": "run"
    },
    "set": {
        "description": "Can change the default settings for the program",
        "usage": "set [setting] [value]"
    },
    "delete": {
        "description": "Deletes the latest created file",
        "usage": "delete"
    },
    "exit": {
        "description": "Exits the program",
        "usage": "exit"
    },
    "help": {
        "description": "Shows you this page",
        "usage": "help ([specific command])"
    }
}

SPECHELP = {
    "set": {
        "fontSize": "[fontSize] Allows you to change the size of the font. Use reset to put this setting back to default.",
        "HSize": "[HSize] Allows you to change the horizontal size of the picture (in px)",
        "VSize": "[VSize] Allows you to change the vertical size of the picture (in px)",
        "font": "[font] Allows you to change the font of the text. You can even add your own fonts in the 'fonts' folder of this program. Use reset to put the font back to default."
    }
}

# Some variables
sizeEdited = False

def CreateImage():
    image = Image.new("RGB", (settings["HSize"], settings["VSize"]), "white")
    draw = ImageDraw.Draw(image)
    ImageWidth = image.width
    ImageHeight = image.height

    UserText = input("Enter Text: ")
    fontSize = settings["fontSize"]
    showWarning = False

    if sizeEdited == True:
        showWarning = True

    while True:
        font = ImageFont.truetype("fonts/" + settings["font"] + ".ttf", fontSize)
        bbox = draw.textbbox((0, 0), UserText, font=font)
        TextWidth = bbox[2] - bbox[0]

        if TextWidth <= image.width:
            break

        if showWarning == True:
            print(f"{YELLOW}[WARNING] Your chosen font size is too big for you text. The result will be cropped.{RESET}")
            showWarning = False
        
        fontSize -= 1

    x = ImageWidth / 2
    y = ImageHeight / 2

    draw.text((x, y), UserText, fill="black", font=font, anchor="mm")

    image.save("output/output.png")
    image.show()

def SetFont(userFont):
    Folder = Path("fonts")
    Failed = True

    if userFont == "reset":
        settings["font"] = "Roboto"
        print(f"{CYAN}[INFO] Success! Font has been reset to Roboto.{RESET}")
    else:
        for file in Folder.iterdir():
            if file.name == userFont + ".ttf":
                settings["font"] = userFont
                Failed = False
                print(f"{CYAN}[INFO] Success! Font is set to {settings["font"]} now.{RESET}")
                
        if Failed == True:
            print(f"{RED}[ERROR] Font not found. Please check if you've spelled it correctly.{RESET}")

print("v0.2.0 TextToPNG")
print(f"{GREEN}Welcome to the TextToPNG terminal! Use 'help' for the list of the currently available commands.{RESET}")

while True:

    ProgramCommand = input("> ")
    CommandPart = ProgramCommand.split()

    if len(CommandPart) > 0:
        if CommandPart[0] == "run":
            CreateImage()

        elif CommandPart[0] == "help":
            if len(CommandPart) == 2:
                if CommandPart[1] == "set":
                    print("Properties of 'set': \n")

                    for command, description in SPECHELP["set"].items():
                        print(command)
                        print(f"{YELLOW}" + description + f"{RESET} \n")
                else:
                    print(f"{RED}[ERROR] Command not found or command has no arguments")
            else:
                print("Available commands:\n")
                    
                for command, info in COMMANDLIST.items():
                    print(f"{command}")
                    print(f"  {info['description']}")
                    print(f"  Usage: {info['usage']}\n")

        elif CommandPart[0] == "set":
            if len(CommandPart) < 3:
                print(f"{RED}[ERROR] Argument missing. Command use: set [setting] [value]{RESET}")
            else:
                if CommandPart[1] == "fontSize":
                    if CommandPart[2] == "reset":
                        if sizeEdited == True:
                            settings["fontSize"] = 500
                            sizeEdited = False
                            print(f"{CYAN}[INFO] Success! Font size has been reset.{RESET}")
                        else:
                            print(f"{RED}[ERROR] The font size wasn't changed by user.{RESET}")
                    elif int(CommandPart[2]) > 0:
                        settings["fontSize"] = int(CommandPart[2])
                        print(f"{CYAN}[INFO] Success! Font size is {settings["fontSize"]} now.{RESET}")
                        if sizeEdited == False:
                            sizeEdited = True
                    else:
                        print(f"{RED}[ERROR] Value cannot be 0 or negative.{RESET}")
                elif CommandPart[1] == "HSize":
                    if CommandPart[2] == "reset":
                        settings["HSize"] = 1800
                        print(f"{CYAN}[INFO] Success! Horizontal size has been reset.{RESET}")
                    elif int(CommandPart[2]) > 0:
                        settings["HSize"] = int(CommandPart[2])
                        print(f"{CYAN}[INFO] Success! Horizontal size is {settings["HSize"]} now.{RESET}")
                    else:
                        print(f"{RED}[ERROR] Value cannot be 0 or negative.{RESET}")
                elif CommandPart[1] == "VSize":
                    if CommandPart[2] == "reset":
                        settings["VSize"] = 1200
                        print(f"{CYAN}[INFO] Success! Vertical size has been reset.{RESET}")
                    elif int(CommandPart[2]) > 0:
                        settings["VSize"] = int(CommandPart[2])
                        print(f"{CYAN}[INFO] Success! Vertical size is {settings["VSize"]} now.{RESET}")
                    else:
                        print(f"{RED}[ERROR] Value cannot be 0 or negative.{RESET}")
                elif CommandPart[1] == "font":
                    SetFont(CommandPart[2])
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
    else:
         print(f"{RED}[ERROR] Command not found. Please enter a valid command.{RESET}")



print(f"{CYAN}[INFO] Ending Program{RESET}")