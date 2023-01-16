from PIL import Image
duck=Image.open("img/duck.jpg")
duck=duck.convert("RGB")
pixels=duck.load()
width, height=duck.size
for j in range(height):
    for i in range(width):
        pixels[i,j]=tuple(sum(pixels[i,j])//len(pixels[i,j]) for z in range(3))
duck.save("output.jpg")
duck.show()