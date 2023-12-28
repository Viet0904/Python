import colorgram

colors = colorgram.extract("day18/174/download.webp", 6)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)


# [ (198, 162, 101), (63, 90, 126)]
