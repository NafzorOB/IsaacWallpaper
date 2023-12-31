from PIL import Image, ImageFilter, ImageDraw
import random, os, pathlib

# converts every color pixel on an image to #DCD7BA.
def toWhite(img):
    px = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if px[i, j] != (0, 0, 0, 0):
                img.putpixel((i, j), (220, 215, 186, 255))
    
    return img

# gets a random filename from the assets folder and also the directory for this file
path = str(pathlib.Path(__file__).parent.absolute())
icon_random = random.choice(os.listdir(path + "/assets/"))

# creates a new image with #16161D as the background color
image = Image.new(mode="RGB", size=(1366, 768), color="#16161D")

# opens the image for the item/trinket icon to add, resizes and converts it to RGBA.
icon_to_add = Image.open(path + "/assets/" + icon_random)
icon_to_add = icon_to_add.resize((200, 200))
icon_to_add = icon_to_add.convert("RGBA")

# creates a border around the icon. sometimes the border is displayed incorrectly
# but im using this while i come around with an actual solution.
icon_border = icon_to_add
icon_border = icon_border.resize((204, 204))
icon_border = toWhite(icon_border)

# adds the icon border and then the icon to the image.
image.paste(icon_border, (581, 282), icon_border)
image.paste(icon_to_add, (583, 284), icon_to_add)

# saves the image
image.save(path + "/bg.png")