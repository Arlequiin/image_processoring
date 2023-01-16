from PIL import Image
import urllib.request
from data import data_en
def get_image_from_link(url):
      with urllib.request.urlopen(url) as url:
          image_data = url.read()
      with open('temp.png', 'wb') as f:
          f.write(image_data)
      return "temp.png"
def removebg(url,pokemon):
    get_image_from_link(url)
    im = Image.open("temp.png")
    im = im.convert('RGBA')
    pixels = im.load()
    width, height = im.size
    t=pixels[0,0]
    l=[]
    d={}
    for j in range(height):
        for i in range(width):
            if pixels[i,j]!=t:
                #pixels[i,j]=(255,0,0)
                l.append(j)
                d[j]=(i,j)
                break
            else:
                pass
                #pixels[i,j]=(10*j,255,0)
    highest=d[max(l)]
    lowest=d[min(l)]
    for j in range(height):
        for i in range(width):
            if pixels[i,j]!=t and (i,j)==highest or (i,j)==lowest:
                pixels[i,j]=(255,0,0)
                #break
            else:
                if j==highest[1] or j==lowest[1]:
                 pixels[i,j]=(255,255,0)
    im.save("output.png")
    Image.open("output.png").show()
    return f"SPECIES_{el.upper()} : MAX{highest} ; MIN{lowest}\n"
with open("output.txt",'w') as f:
    pass
for el in data_en.keys():
  el=el.lower().replace("♀","_f").replace("♂","_m").replace("’","").replace(" ","_").replace(".","").replace("-","_").replace("castform","castform/normal").replace("cherrim","cherrim/normal").replace("flabébé","flabebe").replace(":","")
  with open("output.txt",'a') as f:
    print(f"https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{el}/front.png\n---------")
    f.write(removebg(f"https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{el}/front.png",el.upper()))