from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pathlib import Path
import os

outputFolder = Path("output")
outputFolder.mkdir(exist_ok=True)

image = Image.new("RGB", (1800, 1200), "white")
draw = ImageDraw.Draw(image)
isCropped = False
fontSize = 500
ImageWidth = image.width
ImageHeight = image.height

UserText = input("Write down the Text you want to display on a picture")

while isCropped == False:
    font = ImageFont.truetype("fonts/arial.ttf", fontSize)
    bbox = draw.textbbox((0, 0), UserText, font=font)
    TextWidth = bbox[2] - bbox[0]

    if TextWidth <= image.width:
        isCropped = True
    
    fontSize -= 1

x = ImageWidth / 2
y = ImageHeight / 2

draw.text((x, y), UserText, fill="black", font=font, anchor="mm")

image.save("output/output.png")
image.show()

answer = input("Do you want to delete the output picture? (y)")

if answer == "y":
    print("Deleted!")
    os.remove("output/output.png")