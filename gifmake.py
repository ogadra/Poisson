from PIL import Image

images = []

for i in range(1,51):
    dirname = './pics/poisson' + str(i).zfill(2) + '.png'
    im = Image.open(dirname)
    images.append(im)

images[0].save('Poisson.gif', save_all=True, append_images=images[1:], loop=0, duration=150)