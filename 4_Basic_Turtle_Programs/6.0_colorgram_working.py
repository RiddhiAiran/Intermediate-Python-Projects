import colorgram

# Extract 40 colors from the dot painting image.
colors = colorgram.extract('image.jpg', 40)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
    
print(rgb_colors)
# Remove Background Whiter Shades Manually
