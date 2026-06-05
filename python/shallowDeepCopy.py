rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba) # reference same object i.e True
rgba.append("Alpha")
print(rgb) # ['Red', 'Green', 'Blue', 'Alpha']

correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba) # ['Red', 'Green', 'Blue', 'Alpha']
print(rgb) # ['Red', 'Green', 'Blue', 'Alpha']


rgba
