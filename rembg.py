//python program to remove background
//pip install rembg
from rembg import remove
from PIL import Image
input="input.jpg"
output="input.png"
in=Image.open(input)
out=remove(in)
out.save(output)
