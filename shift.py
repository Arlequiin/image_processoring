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
#=---------------------
deca=100 #changer cette valeur pour faire varier les pixels de decalage
#----------------------
for x in range(width):
    matrix.append([pixels[x,y] for y in range(height)])
for i in range(deca,len(matrix),1):
    matrix2.append(matrix[i])
for i in range(0,deca,1):
    matrix2.append(matrix[i])
for x in range(width):
    for y in range(height):
        pixels_out[x,y]=matrix2[x][y]
out.save("output.jpg")
out.show()