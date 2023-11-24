from PIL import Image 
from PIL.ExifTags import TAGS 
  
image = Image.open("ch1.png") 
  
exifdata = image.getexif() 
  
for tagid in exifdata: 
      
    
    tagname = TAGS.get(tagid, tagid) 
  
    
    value = exifdata.get(tagid) 
    
    
    print(f"{tagname:25}: {value}") 