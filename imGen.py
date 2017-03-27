"""Tree like image generator.

You need Pillow to be installed for this to work.

"""

AUTHOR = "mtech0 https://github.com/mtech0"
LICENSE = "TBC"
VERSION = "0.0.0"
STATUS = "Dev"
SKU = "Main"
URL = "n/a"


from PIL import Image
from random import random
from os import system

class ImGen():
    """The main class."""
    
    def __init__(self):
        """Stuffs."""
        pass
    
    def randomGen(self, iseeds=[], hight=1366, width=768, path="test.jpg", ext="JPEG", open=True):
        """Randomly generate an image."""
        
        # Seeds 0, 1, 2 are for positive colour.
        # Seeds 3, 4, 5 are for negative colour.
        totalSeeds = 8
        im = Image.new("RGB", (hight, width))
        pix = im.load()
        seeds = []
        for seed in iseeds:
            while seed > 1:
                seed = seed / 10
            seeds.append(seed)
        if len(seeds) < totalSeeds:
            seeds += [random() for x in range(totalSeeds - len(seeds))]
        seedsRGB = [round(256*seed) for seed in seeds]
        print(seedsRGB)
        for x in range(hight):
            for y in range(width):
                # u: up | l: left | c: centre | d: down
                # These cover the pixels already generated.
                pixs = {}
                try:
                    pixs["ul"] = pix[x-1, y-1]
                except IndexError:
                    pixs["ul"] = False
                try:
                    pixs["cl"] = pix[x-1, y]
                except IndexError:
                    pixs["cl"] = False
                try:
                    pixs["dl"] = pix[x-1, y+1]
                except IndexError:
                    pixs["dl"] = False
                try:
                    pixs["cu"] = pix[x, y-1]
                except IndexError:
                    pixs["cu"] = False
                colours = {}
                for value in pixs:
                    if not pixs[value]:
                        r = random()
                        if r < 1/8:
                            pixs[value] = (seedsRGB[0], seedsRGB[1], seedsRGB[2])
                        elif r < 2/8:
                            pixs[value] = (seedsRGB[1], seedsRGB[2], seedsRGB[3])
                        elif r < 3/8:
                            pixs[value] = (seedsRGB[2], seedsRGB[3], seedsRGB[4])
                        elif r < 4/8:
                            pixs[value] = (seedsRGB[3], seedsRGB[4], seedsRGB[5])
                        elif r < 5/8:
                            pixs[value] = (seedsRGB[4], seedsRGB[5], seedsRGB[6])
                        elif r < 6/8:
                            pixs[value] = (seedsRGB[5], seedsRGB[6], seedsRGB[7])
                        elif r < 7/8:
                            pixs[value] = (seedsRGB[6], seedsRGB[7], seedsRGB[0])
                        elif r < 8/8:
                            pixs[value] = (seedsRGB[7], seedsRGB[0], seedsRGB[1])
                    try:
                        colours[pixs[value]] += 0.25
                    except KeyError:
                        colours[pixs[value]] = 0.25
                total = 0
                for value in colours:
                    colours[value] += total
                    total = colours[value]
                place = random()
                for value in colours:
                    if place <= colours[value]:
                        pix[x,y] = value
                        print(value)
                        
        im.save(path, ext)
        system(path)
        