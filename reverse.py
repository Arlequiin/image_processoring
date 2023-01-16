from PIL import Image
duck=Image.open("img/duck.jpg")
duck=duck.convert("RGB")
pixels=duck.load()
width, height=duck.size
other_side=False
out=Image.new("RGB",(width, height))
pixels_out=out.load()
matrix=[]
matrix2=[]
for y in range(height):
    matrix.append([pixels[x,y] for x in range(width)])
for i in range(len(matrix)):
    matrix2.append(matrix[-i])
for y in range(height):
    for x in range(width):
        pixels_out[x,y]=matrix2[y][x]
out.save("output.jpg")
out.show()