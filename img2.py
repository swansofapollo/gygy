class Editor:
  def return_palette(self):
    from colorthief import ColorThief
    color_thief = ColorThief('fire.png')
# get the dominant color
    dominant_color = color_thief.get_color(quality=6)
    return (color_thief.get_palette(color_count=6))
