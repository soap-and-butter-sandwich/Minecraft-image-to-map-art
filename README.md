# Minecraft-image-to-map-art
convert any image into a minecraft map art on any version

to change between different pallete go into the source code and switch out the palette in the line of code that says :
colour_map = 

when creating the image use the command 'convert_image' to do so.

convert_image take ins multiple arrguments the first being the path to the image the 2nd and 3rd being the height and the width of the image this is given in pixels so a 1 by 1 map art would be 128,128 pixels the final argument is whether or not you want an excel file to be created that stores all the block and in what place you will need to put them.

you will need to pip install the following modules :
-PIL
-xlsxwriter
-colourmap
-numpy
