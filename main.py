from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

print("WOW")

image = Image.new("RGB", (800, 400), "white")
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

draw.text((50, 50), "Test!", fill="black", font=font)

image.save("output/output.png")

answer = input("Do you want to delete the output picture? (y/n)")

if answer == "y":
    print("Deleted!")
    os.remove("output/output.png")