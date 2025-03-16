import numpy as np
from PIL import Image

def gen_html_icon(coords, bg_shape):
    x,y = coords
    x = x / bg_shape[0] * 100
    y = y / bg_shape[1] * 100
    return f'  <img class="icon" src="maps/skull_off.png" alt="Icon" style="top: {y:.4f}%; left: {x:.4f}%;">\n'

paths = [
    "imgs/raw/skulls-downtown.png",
    "imgs/raw/skulls-little_havana.png",
    "imgs/raw/skulls-north_beach.png",
    "imgs/raw/skulls-south_beach.png",
]

out = ""
for path in paths:
    name = path.split('-')[1].split('.')[0]

    with Image.open(path) as img:
        arr = np.array(img.convert("RGB")).transpose(1, 0, 2)
        mask = np.all(arr == [255, 0, 0], axis=-1)
        idxs = np.argwhere(mask)

        out += '<div class="image-container">\n'
        out += f'  <img src="maps/{name}.jpg" alt="">\n'
        for idx in idxs: out += gen_html_icon(idx, img.size)
        out += '</div>\n\n'

with open("skulls.temp.html", "w") as file:
    file.write(out)
