from PIL import Image
import urllib.request
def get_image_from_link(url):
      with urllib.request.urlopen(url) as url:
          image_data = url.read()
      with open('temp.png', 'wb') as f:
          f.write(image_data)
      return "temp.png"
def removebg(url):
    get_image_from_link(url)
    im = Image.open("temp.png")
    im = im.convert('RGBA')
    pixels = im.load()
    width, height = im.size
    t=pixels[0,0]
    for j in range(height):
        for i in range(width):
            if t[0]+30>pixels[i,j][0]>t[0]-30 and t[1]+30>pixels[i,j][1]>t[1]-30 and t[2]+30>pixels[i,j][2]>t[2]-30:#and pixels[i,j][0]==pixels[i,j][1]==pixels[i,j][2]:
                pixels[i,j]=(0,0,0,0)
    im.save("output.png")
    Image.open("output.png").show()
removebg("https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/absol/front.png")