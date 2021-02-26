from colorthief import ColorThief
color_thief = ColorThief('fire.png')
# get the dominant color
dominant_color = color_thief.get_color(quality=6)
print(color_thief.get_palette(color_count=6))