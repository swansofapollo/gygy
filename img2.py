class Editor:
    def return_palette(self, im):
        from colorthief import ColorThief
        color_thief = ColorThief(im)
        # get the dominant color
        dominant_color = color_thief.get_color(quality=6)
        res = (color_thief.get_palette(color_count=6))
        return res
