import numpy as np
from PIL import Image

def gen_html_icon(i, coords, bg_shape):
    x,y = coords
    x = x / bg_shape[0] * 100
    y = y / bg_shape[1] * 100
    return f'<img class="icon-skull" style="top: {y:.4f}%; left: {x:.4f}%;">'

paths = [
    "imgs/raw/skulls-downtown.png",
    "imgs/raw/skulls-little_havana.png",
    "imgs/raw/skulls-north_beach.png",
    "imgs/raw/skulls-south_beach.png",
]

out = "var html_maps = {"
for path in paths:
    name = path.split('-')[1].split('.')[0]

    with Image.open(path) as img:
        arr = np.array(img.convert("RGB")).transpose(1, 0, 2)
        mask = np.all(arr == [255, 0, 0], axis=-1)
        idxs = np.argwhere(mask)

        out += f'{name}: `<div class="image-container">'
        out += f'<img id="map-bg" src="imgs/{name}.jpg" alt="">'
        for i,idx in enumerate(idxs):
            out += gen_html_icon(i, idx, img.size)
        out += '</div>`,'

out += "};"

with open("skulls.temp.js", "w") as file:
    file.write(out)
