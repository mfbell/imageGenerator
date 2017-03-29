"""Tree like image generator.

In development and I don't know how it works either...

You need Python Pillow to be installed for this to work.

"""

AUTHOR = "mtech0 https://github.com/mtech0"
LICENSE = "To be comfirmed, all rights reserved."
VERSION = "0.4.1"
STATUS = "Dev"
SKU = "Main"
URL = "n/a"

from PIL import Image
from random import random, randint, shuffle
from os import system
import sys
        
        
class TreeGen():
    """Generate a image in a tree growth like way.
    - Or was the intention."""
   
    def __init__(self, colours=[], hight=512, width=512, bg=True, fgcc=0.005, bgcc=0.004, path="test.jpg", ext="JPEG", open=True, rl=None, xy=None):
        """Main stuff.
        
        See README.md for documentation.
        
        """
        colourCount = 2
        if xy == "c":
            startxy = (round(width/2), round(hight/2))
        elif xy:
            if not isinstance(xy, tuple) or len(xy) != 2:
                raise InvalidArg("{0} is not a valid XY turple.".format(xy))
            elif not isinstance(xy[0], int) or not isinstance(xy[1], int):
                raise InvalidArg("A value in {0} is not an interger.".format(xy))
            elif xy[0] < 0 or xy[1] < 0 or xy[0] > width or xy[1] > hight:
                raise InvalidArg("{0} out of range.".format(xy))
            else:
                startxy = xy
        else:
            startxy = (randint(0,width-1), randint(0, hight-1))
        for colour in colours:
            if not isinstance(colour, tuple) or len(colour) != 3:
                raise InvalidArg("{0} is not a valid RGB turple.".format(colour))
            for value in colour:
                if not isinstance(value, int):
                    raise InvalidArg("{0} in {1} is not an interger.".format(value, colour))
                if value < 0 or value > 255:
                    raise InvalidArg("{0} in {1} out of colour range.".format(value, colour))
        while len(colours) < colourCount:
            colours.append((randint(0,255), randint(0,255), randint(0,255)))
        self.im = Image.new("RGB", (hight, width))
        self.pix = self.im.load()
        self.colours = colours
        self.hight = hight
        self.width = width
        self.FGColourChance = fgcc
        self.BGColourChance = bgcc
        if rl:
            self.recursionlimit = rl # I got stack overflow at 2581.
            sys.setrecursionlimit(self.recursionlimit)
        else:
            self.recursionlimit = sys.getrecursionlimit()
        self.tree(startxy)
        if bg:
            for x in range(hight):
                for y in range(width):
                    if self.pix[x,y] == (0,0,0):
                        self.pix[x,y] = self.colours[1]
        self.im.save(path, ext)
        if open:
            system(path)
        print(startxy)
        return None
      
           
    def pick(self, xy):
        """Picks the colour for xy."""
        SColourChance = 1-self.FGColourChance-self.BGColourChance
        takefrom = [(xy[0]-1, xy[1]-1), (xy[0], xy[1]-1), (xy[0]+1, xy[1]-1), (xy[0]-1, xy[1]), (xy[0]+1, xy[1]), (xy[0]-1, xy[1]+1), (xy[0], xy[1]+1), (xy[0]+1, xy[1]+1)]
        scolours = {self.colours[0]: self.FGColourChance, self.colours[1]: self.BGColourChance}
        for _xy in takefrom:
            try:
                pixColour = self.pix[_xy]
                try:
                    scolours[pixColour] += SColourChance/len(takefrom)
                except KeyError:
                    scolours[pixColour] = SColourChance/len(takefrom)
            except IndexError:
                #if random() < 1/(self.FGColourChance+self.BGColourChance)*self.FGColourChance:
                #    pixColour = self.colours[0]
                #else:
                #    pixColour = self.colours[1]"""
                pass 
                # Not counted for. 
                # To have it randomly choose based on fgcc and bgcc uncomment the above.
                # And move the nested try bellow and inline this one.
            
        if (not (0,0,0) in self.colours) and (0,0,0) in scolours:
            # Does not help if one of the colours is black.
            del scolours[(0,0,0)]
        rtotal = 0
        for colour in scolours:
            rtotal += scolours[colour]
        if rtotal != 1:
            for colour in scolours:
                scolours[colour] = 1/rtotal*scolours[colour]
        rtotal = 0
        rand = random()
        for colour in scolours:
            scolours[colour] += rtotal
            rtotal = scolours[colour]
            if rand < scolours[colour]:
                self.pix[xy] = colour
                break
        return None
            
    def tree(self, xy, lvl=0):
        """Grow from the xy."""
        try:
            if self.pix[xy] == (0, 0, 0):
                self.pick(xy)
                grow = [(xy[0], xy[1]-1), (xy[0]-1, xy[1]), (xy[0]+1, xy[1]), (xy[0], xy[1]+1)]
                shuffle(grow)
                if not lvl >= self.recursionlimit-20: 
                # -10 seems to get it to not RecursionError out, just stack overflow crash when recursionlimit is above 2581.?
                    for item in grow:
                        self.tree(item, lvl+1)
                return None
            else:
                return None
        except IndexError:
            return None
       
class Error(Exception):
    """General error class."""
    
    def __init__(self, msg=None):
        """Stuffs."""
        if not msg:
            msg = self.__doc__
        super(Error, self).__init__(msg)
        self.msg = msg

class InvalidArg(Error):
    """An invalid arg was passed to a function or method."""
        
if __name__ == "__main__":
    info = ["imGen, import to use.",
            "Version {0}, {1}".format(VERSION, STATUS),
            "Written by {0}".format(AUTHOR),
            "Licensed under {0}".format(LICENSE),
            "SKU: {0}".format(SKU),
            "URL: {0}".format(URL)]
    for line in info:
        print(line)