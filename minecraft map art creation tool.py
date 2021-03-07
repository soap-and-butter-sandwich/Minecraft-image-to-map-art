import PIL, math, numpy
from colormap import hex2rgb
from colormap import rgb2hex
from PIL import Image
import xlsxwriter as xl
global colour_map, rgb_pallet

java_colour_map = {
  '#0E0E0F':'north facing black wool',
  '#111112':'black wool',
  '#141416':'south facing black wool',

  '#2B2B2F':'north facing grey wool',
  '#353539':'grey wool',
  '#3E3E43':'south facing grey wool',

  '#323438':'north facing cyan terracota',
  '#3D4145':'cyan terracota',
  '#474B51':'south facing cyan terracota',

  '#414145':'north facing cobblestone',
  '#4F4F54':'cobblestone',
  '#5C5C62':'south facing cobblestone',

  '#59595F':'north facing light grey wool',
  '#6C6C74':'light grey wool',
  '#7D7D86':'south facing light grey wool',

  '#606067':'north facing iron block',
  '#76767E':'iron block',
  '#898993':'south facing iron block',

  '#5E6171':'north facing clay block',
  '#74768B':'clay block',
  '#868AA2':'south facing clay block',

  '#73737B':'north facing mushroom stem',
  '#8C8C96':'mushroom stem',
  '#A3A3AF':'south facing mushroom stem',

  '#949197':'north facing diorite',
  '#B4B2B9':'diorite',
  '#D1CFD7':'south facing diorite',

  '#94949E':'north facing white wool',
  '#B4B4C1':'white wool',
  '#D1D1E0':'south facing white wool',

  '#150C0A':'north facing black terracota',
  '#190F0B':'black terracota',
  '#1E120E':'south facing black terracota',

  '#211715':'north facing grey terracota',
  '#281D1A':'grey terracota',
  '#2F221F':'south facign grey terracota',

  '#2B1D15':'north facing brown terracota',
  '#35231A':'brown terracota',
  '#3E291F':'south facing brown terracota',

  '#4B311E':'north facing spruce wood',
  '#5B3D25':'spruce wood',
  '#6A462B':'south facing spruce wood',

  '#4E3D3D':'north facing light grey terracota',
  '#5F4B4A':'light grey terracota',
  '#6F5856':'south facing light grey terracota',

  '#573E2F':'north facing dirt',
  '#6B4D3A':'dirt',
  '#7C5944':'south facing dirt',

  '#52452C':'north facing oak planks',
  '#655436':'oak planks',
  '#75623F':'south facing oak planks',

  '#786663':'north facing white terracota',
  '#947D79':'white terracota',
  '#AB918D':'south facing white terracota',

  '#5C2C30':'north facing pink terracota',
  '#71363B':'pink terracota',
  '#833F45':'south facing pink terracota',

  '#591E20':'north facing red wool',
  '#6C2427':'red wool',
  '#7D2A2D':'south facing red wool',

  '#52221C':'north facing red terracota',
  '#642A22':'red terracota',
  '#743128':'south facing red terracota',

  '#410100':'north facing netherrack',
  '#4F0100':'netherrack',
  '#5C0200':'south facing netherrack',

  '#940000':'north facing redstone block',
  '#B40000':'redstone block',
  '#D10000':'south facing redstone block',

  '#5C2F16':'north facing orange terracota',
  '#70391B':'orange terracota',
  '#824320':'south facing orange terracota',

  '#7D4920':'north facing acacia planks',
  '#985927':'acacia planks',
  '#B1682D':'south facing acacia planks',

  '#6B4C16':'north facing yellow terracota',
  '#835D1B':'yellow terracota',
  '#986D20':'south facing yellow terracota',

  '#908A2F':'north facing gold block',
  '#B0A83A':'gold block',
  '#CDC344':'south facing gold block',

  '#848420':'north facing yellow wool',
  '#A1A127':'yellow wool',
  '#BCBC2D':'south facing yellow wool',

  '#8F8665':'north facing birch planks',
  '#AFA57B':'birch planks',
  '#CABF8F':'south facing birch planks',

  '#49760F':'north facing lime wool',
  '#599012':'lime wool',
  '#68A716':'south facing lime wool',

  '#496622':'north facing grass block',
  '#597D2A':'grass block',
  '#689231':'south facing grass block',

  '#004700':'north facing saplin',
  '#005700':'saplin',
  '#006600':'south facing saplin',

  '#2B2F19':'north facing green terracota',
  '#353920':'green terracota',
  '#3E4325':'south facing green terracota',

  '#3B4321':'north facing lime terracota',
  '#485228':'lime terracota',
  '#54602F':'south facing lime terracota',

  '#3B4920':'north facing green wool',
  '#485927':'green wool',
  '#54682D':'south facing green wool',

  '#007D23':'north facing emerald block',
  '#00992C':'emerald block',
  '#00B233':'south facing emerald block',

  '#347E84':'north facing prismarine block',
  '#419AA1':'prismarine block',
  '#4BB3BB':'south facing prismarine block',

  '#3B5986':'north facing light blue wool',
  '#486CA3':'light blue wool',
  '#547DBE':'south facing light blue wool',

  '#2B495F':'north facing cyan wool',
  '#355974':'cyan wool',
  '#3E6886':'south facing cyan wool',

  '#1E2B6E':'north facing blue wool',
  '#243586':'blue wool',
  '#2A3E9C':'south facing blue wool',

  '#2B4A9E':'north facing lapis block',
  '#345AC1':'lapis block',
  '#3D69E0':'south facing lapis block',

  '#5C5C9E':'north facing ice',
  '#7171C1':'ice',
  '#8383E0':'south facing ice',

  '#413E55':'noth facing light blue terracota',
  '#7171C1':'light blue terracota',
  '#8383E0':'south facing light blue terracota',

  '#413E55':'north facing magenta wool',
  '#4F4C69':'magenta wool',
  '#5C5979':'south facing magenta wool',

  '#662B86':'north facing purple wool',
  '#7D35A3':'purple wool',
  '#923EBE':'south facing purple wool',

  '#49246E':'north facing blue terracota',
  '#592C86':'blue terracota',
  '#68349C':'south facing blue terracota',

  '#2B2338':'north facing purple terracota',
  '#352B45':'purple terracota',
  '#3E3351':'south facing purple terracota',

  '#563243':'north facing magenta terracota',
  '#693D52':'magenta terracota',
  '#7A475F':'south facing magenta terracota',

  '#8B4966':'north facing pink wool',
  '#AA597D':'pink wool',
  '#C66891':'south facing pink wool',

  '#3B2B20':'north facing dark oak planks',
  '#483527':'dark oak planks',
  '#543E2D':'south facing dark oak planks'
  }

legacy_colour_map = {
  '#666666':'posotive gradient stone',
  '#7C7C7C':'stone',
  '#8D8B8E':'negative gradient stone',

  '#779136':'posotive gradient grass block',
  '#86A849':'grass block',
  '#97BC55':'negative gradient grass block',

  '#986635':'posotive gradient dirt block',
  '#AD7441':'dirt block',
  '#BD8142':'negative gradient dirt block',

 '#B6B18B':'posotive gradient sandstone',
  '#D1CD9E':'sandstone',
  '#E7E0B2':'negative gradient sandstone',

  '#AC7535':'posotive gradient red sandstone',
  '#C2833E':'red sandstone',
  '#D9904C':'negative gradient red sandstone',

  '#BDBCB7':'posotive gradient diorite',
  '#D7D6D1':'diorite',
  '#E9EAE5':'negative gradient diorite',

 '#1A1C1A':'posotive gradient block of coal',
  '#1B1B1A':'block of coal',
  '#2A2C2A':'negative gradient block of coal',

  '#006D00':'posotive gradient dried kelp block',
  '#008300':'dried kelp block',
  '#019200':'negative gradient dried kelp block',

  '#BDB44C':'posotive gradient block of gold',
  '#D1CE5F':'block of gold',
  '#E8E365':'negative gradient block of gold',

  '#8D8B8E':'posotive gradinet block of iron',
  '#A6A4A5':'block of iron',
  '#B6AEb3':'negative gradient block of iron',

  '#B6AEB3':'posotive gradient block of diamonds',
  '#66C2BE':'block of diamonds',
  '#77D5D4':'negative gradient block of diamonds',

  '#02AA43':'posotive gradient block of emerald',
  '#00C24B':'block of emerald',
  '#00D756':'negative gradient block of emerald',

  '#650101':'posotive gradient nether quarkz ore',
  '#7D0001':'nether quarkz ore',
  '#8C0001':'negative gradient nether quarkz ore',

  '#843636':'posotive gradient nether wart block',
  '#9A3E41':'nether wart block',
  '#AC4848':'negative gradient nerther wart block',

  '#645338':'posotive gradient oak planks',
  '#765D40':'oak planks',
  '#7D7043':'negative gradient oak planks',

  '#755337':'posotive gradient spruce planks',
  '#856641':'spruce planks',
  '#956D47':'negative gradient spruce planks',

  '#B7B289':'posotive gradient birch planks',
  '#D3CDA4':'birch planks',
  '#E7E1B1':'negative gradient birch planks',

  '#9A6436':'posotive gradient jungle planks',
  '#AB7540':'jungle planks',
  '#BE8141':'negative gradient jungle planks', 
  
  '#AD7435':'posotive gradient acacia planks',
  '#BF8441':'acacia planks',
  '#D5924D':'negative gradient acacia planks',
  
  '#654936':'posotive gradient dark oak planks',
  '#765C44':'dark oak planks',
  '#7B664B':'negative gradient dark oak planks',

  '#665237':'posotive gradient oak wood',
  '#765C43':'oak wood',
  '#836C4A':'negative gradient oak wood',

  '#843636':'posotive gradient bricks',
  '#9A4040':'bricks',
  '#AB4948':'negative gradient bricks',

  '#8C8B9D':'posotive gradient ice',
  '#A19ED5':'ice',
  '#B4B1E9':'negative gradient ice',

  '#BDBDBF':'posotive gradient snow',
  '#D9D9D8':'snow',
  '#EBE9EA':'negative gradient snow',

  '#644934':'posotive gradient soul sand',
  '#765B40':'soul sand',
  '#7B6649':'negative gradient soul sand',

  '#B6B18B':'posotive gradient glowstone',
  '#D4CDA2':'glowstone',
  '#E7E1B1':'negative gradient glowstone',

  '#4C7485':'posotive gradient prismarine',
  '#5D8396':'prismarine',
  '#6493AF':'negative gradient prismarine',

  '#5EAAA6':'posotive gadient dark prismarine',
  '#67BFBF':'dark prismarine',
  '#74DACF':'negative gradient dark prismarine',

  '#764290':'posotive gradient mycelium',
  '#824AAD':'mycelium',
  '#9255BE':'negative gradient mycelium',

  '#765437':'posotive gradient podzol',
  '#856644':'podzol',
  '#956D4C':'negative gradient podzol',

  '#934BAE':'posotive gradient purpur block',
  '#AA5EC2':'purpur block',
  '#BE66D6':'negative gradient purpur block',

  '#2C0E10':'posotive gradient black terracota',
  '#2B1B0F':'black terracota',
  '#351B1E':'negative gradient black terracota',

  '#4C415B':'posotive gradient blue terracota',
  '#5E4A63':'blue terracota',
  '#655372':'negative gradient blue terracota',

  '#66677C':'posotive gradient light blue terracota',
  '#7E768E':'light blue terracota',
  '#8A84A0':'negative gradient light blue terracota',

  '#545D64':'posotive gradient cyan terracota',
  '#646868':'cyan terracota',
  '#6D7675':'negative gradient cyan terracota',

  '#4B5230':'posotive gradient green terracota',
  '#605C37':'green terracota',
  '#656C43':'negative gradient green terracota',

  '#656D32':'posotive gradient lime terracota',
  '#757D41':'lime terracota',
  '#7C8B49':'negative gradient lime terracota',

  '#8A4A49':'posotive gradient pink terracota',
  '#A25E5F':'pink terracota',
  '#AD6964':'negative gradient pink terracota',

  '#845366':'posotive gradient magenta terracota',
  '#966676':'magenta terracota',
  '#A26E85':'negative gradient magenta terracota',

  '#6E4B55':'posotive gradient purple terracota',
  '#855469':'purple terracota',
  '#916775':'negative gradient purple terracota',

  '#7A4136':'posotive gradient red terracota',
  '#914A36':'red terracota',
  '#9C5446':'negative gradient red terracota',

  '#4C352E':'posotive gradient brown terracota',
  '#5C412E':'brown terracota',
  '#654934':'negative gradient brown terracota',

  '#8B5331':'posotive gradient orange terracota',
  '#A25F29':'orange terracota',
  '#AD6C35':'negative gradient orange terracota',

  '#9A742B':'posotive gradient yellow terracota',
  '#B38B2C':'yellow terracota',
  '#C09837':'negative gradient yellow terracota',

  '#A98F92':'posotive gradient white terracota',
  '#BDAC97':'white terracota',
  '#D2BDB3':'negative gradient white terracota',

  '#75675C':'posotive gradient light grey terracota',
  '#8A766F':'light grey terracota',
  '#97837A':'negative gradient light grey terracota',

  '#402A2D':'posotive gradient grey terracota',
  '#4A362D':'grey terracota',
  '#544034':'negative gradient grey terracota',

  '#1B1B19':'posotive gradient black wool',
  '#1E191C':'black wool',
  '#2E2A27':'negative gradient black wool',

  '#344B91':'posotive gradient blue wool',
  '#435FAD':'blue wool',
  '#4B65C2':'negative gradient blue wool',

  '#6783AA':'posotive gradient light blue wool',
  '#7597C2':'light blue wool',
  '#7CABD8':'negative gradient light blue wool',

  '#4B7585':'posotive gradient cyan wool',
  '#5F8295':'cyan wool',
  '#6991AA':'negative gradinet cyan wool',

  '#667439':'posotive gradient green wool',
  '#768148':'green wool',
  '#7D914F':'negative gradient green wool',

  '#78A31C':'posotive gradient lime wool',
  '#87BA20':'lime wool',
  '#95C937':'negative gradinet lime wool',

  '#B5758C':'posotive gradient pink wool',
  '#D0849E':'pink wool',
  '#E496AA':'negative gradient pink wool',

  '#924BAA':'posotive gradient magenta wool',
  '#AC5BC4':'magenta wool',
  '#B968D9':'negative gradient magenta wool',

  '#764192':'posotive gradient purple wool',
  '#864AAB':'purple wool',
  '#9553BF':'negative gradient purple wool',

  '#B2B133':'posotive gradient yellow wool',
  '#C9C444':'yellow wool',
  '#DEDA46':'negative gradient yellow wool',

  '#828282':'posotive gradient light grey wool',
  '#969696':'light grey wool',
  '#ACADA9':'negative gradient light grey wool',

  '#4A4948':'posotive gradient grey wool',
  '#605C5C':'grey wool',
  '#636768':'negative gradient grey wool',
  
  '#BA0100':'posotive gradinet block of redstone',
  '#D30403':'block of redstone',
  '#E20402':'negative gradient block of redstone'
  }

bedrock_colour_map = {

  '#7C7C7C':'stone',

  '#86A849':'grass block',

  '#AD7441':'dirt block',

  '#D1CD9E':'sandstone',

  '#C2833E':'red sandstone',

  '#D7D6D1':'diorite',

  '#1B1B1A':'block of coal',

  '#008300':'dried kelp block',

  '#D1CE5F':'block of gold',

  '#A6A4A5':'block of iron',

  '#66C2BE':'block of diamonds',

  '#00C24B':'block of emerald',

  '#7D0001':'nether quarkz ore',

  '#9A3E41':'nether wart block',

  '#765D40':'oak planks',

  '#856641':'spruce planks',

  '#D3CDA4':'birch planks',

  '#AB7540':'jungle planks',

  '#BF8441':'acacia planks',

  '#765C44':'dark oak planks',

  '#765C43':'oak wood',

  '#9A4040':'bricks',

  '#A19ED5':'ice',

  '#D9D9D8':'snow',

  '#765B40':'soul sand',

  '#D4CDA2':'glowstone',

  '#5D8396':'prismarine',

  '#67BFBF':'dark prismarine',

  '#824AAD':'mycelium',

  '#856644':'podzol',

  '#AA5EC2':'purpur block',

  '#2B1B0F':'black terracota',

  '#5E4A63':'blue terracota',

  '#7E768E':'light blue terracota',

  '#646868':'cyan terracota',

  '#605C37':'green terracota',

  '#757D41':'lime terracota',

  '#A25E5F':'pink terracota',

  '#966676':'magenta terracota',

  '#855469':'purple terracota',

  '#914A36':'red terracota',

  '#5C412E':'brown terracota',

  '#A25F29':'orange terracota',

  '#B38B2C':'yellow terracota',

  '#BDAC97':'white terracota',

  '#8A766F':'light grey terracota',

  '#4A362D':'grey terracota',

  '#1E191C':'black wool',

  '#435FAD':'blue wool',

  '#7597C2':'light blue wool',

  '#5F8295':'cyan wool',

  '#768148':'green wool',

  '#87BA20':'lime wool',

  '#D0849E':'pink wool',

  '#AC5BC4':'magenta wool',

  '#864AAB':'purple wool',

  '#C9C444':'yellow wool',

  '#969696':'light grey wool',

  '#605C5C':'grey wool',

  '#D30403':'block of redstone',

  }

  
  
colour_map = legacy_colour_map #asign a colour map to be used

rgb_pallete = [] #creates look up table 

for i in range(0,len(list(colour_map))): #loop for the lenght of the dictonary
  rgb_pallete.append(hex2rgb((list(colour_map))[i])) #loops over all the colours and adds them to a look up table
      
def convert_image(path, height, width, file_write):
  if file_write == True : #check if excel file is requeted for creation 
    workbook = xl.Workbook(str(path + '.xlsx')) #creates the work sheet
    worksheet = workbook.add_worksheet() #adds sheet to the excel file where all the data can be writen to 
    
  instructions = [] #create instructions list

  image = Image.open(path) #load image using PIL
  new_image = image.resize((width,height)) #resize image so it is the desired height and width in pixels 
  
  for x in range(width): #loops through all the pixels on the x axis
   for y in range(height): #loops though all the pixels on the y axis
  
       r,g,b = new_image.getpixel((x,y)) #gets r g b colour value for the pixel
       replace_colour = new_colour(r,g,b) #gets the closest colour from the colour map in use
       try : #optimisation so if pixel is already in colour map then it will skip over that pixel
         colour_map[rgb2hex(r,g,b)] #checks if pixel is already in the image so it doesnt have to calculate distances 
         instructions.append(colour_map[rgb2hex(r,g,b)]) #adds the block to the instructions list
       except KeyError : #when pixel is not in the image it can find the closest one
         instructions.append(replace_colour[1]) #adds the block to the instructions list
         new_image.putpixel((x,y), replace_colour[0]) #replaces pixel with new colour
         
       if file_write == True : #check if excel file is requested to be made
         worksheet.write(y,x,str(colour_map[rgb2hex(replace_colour[0][0],replace_colour[0][1],replace_colour[0][2])])) #write the block type to an excel spreadsheet, in the position it would be on the image        
  if file_write == True : #check if excel file is requested to be made 
    workbook.close()# closes excel file once all the pixel block data has been writen 
  
  new_image.show() #shows image
  return instructions
  
def new_colour(r,g,b):
  distance = [] # creates list for all the distances 
  for i in range(0,len(list(colour_map))): # loops through all the colour in the map
    distance.append(calculate_distance(rgb_pallete[i],(r,g,b))) # calcualte the distance to each point
  closest_point = numpy.argmin(distance) # calculates the smallest value
  return rgb_pallete[closest_point],colour_map[rgb2hex(rgb_pallete[closest_point][0],rgb_pallete[closest_point][1],rgb_pallete[closest_point][2])]# returns the RGB value at the index of the charter and the instruction                                

def calculate_distance(c1,c2):
  (r1,g1,b1) = c1
  (r2,g2,b2) = c2
  return math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2) # calculates the distance between the the RGB values
    
def colour(hex_value): #use when you want to colour pick from an image 
  return new_colour(hex2rgb(hex_value)[0],hex2rgb(hex_value)[1],hex2rgb(hex_value)[2]) #return the closest colour and what block it is 
