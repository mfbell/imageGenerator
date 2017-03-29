# imGen: Tree like image generator

Info coming soon...

## Quick Documentation v0.1.0
You need to import this module to use it.
### Classes
#### TreeGen
```
Generate a image in a tree growth like way.
- Or was the intention.
```
Auto runs to generate an image.
##### Args
All args are optional.
`colours=[], hight=512, width=512, bg=True, fgcc=0.005, bgcc=0.004, path="test.jpg", ext="JPEG", open=True, rl=None, xy=None`
###### Colours
colours - A list containing any number of turples, only the first two are used, each containing three intergers which ranging from 0 to 255.
These are the foreground/positive colour and the background/negative colour, in that order.
If not give or only one, the remaining needed are randomly generated.
###### Hight
hight - An interger.
The hight of the image to generate, defaults of 512.
###### Width
width - An interger.
The width of the image to generate, defaults of 512.
###### Background
bg - A boolean.
If to set unset parts of the image to the background colour once the recursion limit is reached.
Default to true, if false unset areas are black (0,0,0).
###### Foreground Colour Chance
fgcc - A float (or int). 
This is used at as the base possibilty of the foreground colour in any pixels generation.
See <Probabilty Cals sections when writen> for more info.
I may change the default at time so sorry if it changes.
(Can be used when IndexErrors in pick(). See comments there for more info.)
###### Background Colour Chance
bgcc - A float (or int)
This is used at as the base possibilty of the background colour in any pixels generation.
See <Probabilty Cals sections when writen> for more info.
I may change the default at time so sorry if it changes.
(Can be used when IndexErrors in pick(). See comments there for more info.)
###### Path
path - String. Save path including file name. Note that ext over writes the file extention as said in the Pillow docs.
Default to "test.jpg".
###### Extention
ext - String. The image file format. Default to JPEG
###### Auto View
open - A boolean. If to automatically open the image once generated. Default to true.
###### Recursion Limit
rl - Interger. Set the system recursion limit to the value. If left to None, default, it will not change it. If you go to high, for me around 2580 depending on the offset <see note>, you get a stack overflow crashing the interpiter.
###### XY
xy - Turple with two intergers. The starting point to the growth. If None, default, it will randomly pick a point. If "c" is passed the point will be the centre, as width/2 and hight/2.