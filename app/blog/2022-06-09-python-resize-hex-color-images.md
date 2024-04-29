Python is by far one of the easiest programming languages to use. Writing functions are intuitive and so is reading the code itself. When dealing with images I found Python to be easier to use compared to NodeJS and PHP.

## Use Case
Let’s say you were building a website that’s similar to Unsplash. Users are uploading 10MB images to your website from their DLSR camera. Displaying these images on the front-end is asking for a terrible page load. So how do you resize images with Python?

## Get Started
[[youtube_1]]
1. Locate your image
2. Open as an Image
3. Resize Save

### Install Dependencies
- [webcolor](https://pypi.org/project/webcolors/) 
- [python-resize-image](https://pypi.org/project/python-resize-image/)
- [colorthief](https://pypi.org/project/python-resize-image/)

```
pip3 install webcolors python-resize-image colorthief
```


### Resize Image

```
from resizeimage import resizeimage 
from PIL import Image

image_path = './dog.jpeg'
new_max_width = 1800
new_filename = './dog-1800.jpeg'

with open(image_path, 'r+b') as f:
  with Image.open(f) as image:

  # Resize
  smaller_image = resizeimage.resize_width(image, new_max_width)
  smaller_image.save(new_filename, image.format)
```

Your image needs to be open as bytes and readable. image.format re-saves the image as the correct type (dog.jpeg is saved back as a jpeg). If you run the code above you just resized an image. The height is auto-calculated based on width keeping the ratio. The PIL package stands for “Pillow” and is installed with “python-resize-image”. Pillow is the ultimate package for dealing with an image. A quick way to get the current height and width plus other metadata.

With the same **open(image_path, ‘r+b’)** using ColorThief a palette of colors are found.


### Get the HEX color value from image


```
from resizeimage import resizeimage
from PIL import Image
import webcolors
from colorthief import ColorThief

image_path = './dog.jpeg'
new_max_width = 1800
new_filename = './dog-1800.jpeg'
image_colors = []

with open(image_path, 'r+b') as f:
  with Image.open(f) as image:

        # Resize
        smaller_image = resizeimage.resize_width(image, max_width)
        smaller_image.save(new_image_path, image.format)

        # Get Colors
        color_thief = ColorThief(new_image_path)
        color_palette = color_thief.get_palette(color_count=10, quality=10)
        for color in color_palette:
            print(webcolors.rgb_to_hex(color))
```

color_palette = returns an array tuples of RGB values then, webcolors.rgb_to_hex converts each tuple in to a hex value.


### RBG to HEX

```
import webcolors
print(webcolors.rgb_to_hex((255, 255, 255)))
```

### Get color by name

```
import webcolors
print(webcolors.rgb_to_name((255, 255, 255)))
```

Sample Code — [https://github.com/terrillo/learn-python](https://github.com/terrillo/learn-python)