from PIL import Image, ImageColor
import random, os, sys

settings = {

    # Canvas configuration, every size/position is in pixels, adjust them for your device's screen size
    "canvas_size": (1366, 768),
    "canvas_background_color": "#16161D", # Needs to be in HEX.

    # Icon configuration
    "icon_position": (583, 284),
    "icon_size": (200, 200),

    # Border configuration
    "border": True, # Enable or disable the border
    "border_color": "#DCD7BA", # Needs to be in HEX.
    "border_size": 1,

    # Output configuration
    "output_filename": "bg.png"

}

# Gets a random filename from the assets folder and also the directory for this file
# In the case that an argument is provided via the command line, use said argument instead of selecting randomly.
path = sys.path[0]
icon_random = sys.argv[1] if len(sys.argv) > 1 else random.choice(os.listdir(path + "/assets/"))

print("Selected file: " + icon_random)

# Creates a new image with #16161D as the background color.
image = Image.new(mode="RGBA", size=settings["canvas_size"], color=settings["canvas_background_color"])

# opens the image for the item/trinket icon to add, resizes and converts it to RGBA.
icon_to_add = Image.open(path + "/assets/" + icon_random)
icon_to_add = icon_to_add.resize(settings["icon_size"])
icon_to_add = icon_to_add.convert("RGBA")

# Creates a border around the icon. sometimes the border is displayed incorrectly but im using this while i come around with a proper solution.

if settings["border"]:
    
    # Converts every color pixel on an image to settings[border_color].
    def toColor(img):
        px = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if px[i, j] != (0, 0, 0, 0):

                    img.putpixel((i, j), ImageColor.getcolor(settings["border_color"], "RGBA"))
        return img

    icon_border = icon_to_add
    icon_border = icon_border.resize(
        (
            settings["icon_size"][0] + (settings["border_size"] * 2),
            settings["icon_size"][1] + (settings["border_size"] * 2)
        )
    )

    icon_border = toColor(icon_border)

# Adds the icon border and then the icon to the image.
if settings["border"]:
    image.paste(icon_border, (
            settings["icon_position"][0] - (settings["border_size"]),
            settings["icon_position"][1] - (settings["border_size"])
    ), icon_border)

image.paste(icon_to_add, settings["icon_position"], icon_to_add)


# Saves the image.
image.save(path + "/bg.png")
print("Done.")