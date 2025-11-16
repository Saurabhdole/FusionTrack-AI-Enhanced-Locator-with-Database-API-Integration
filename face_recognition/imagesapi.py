from PIL import Image
from io import BytesIO
import requests
import json
from images_update import makenew
import numpy as np

# Using API to add all photos from the database to the folder for encoding and matching 
def getimages():
    url = "http://localhost:5000/api/missingpeople/getallpersons"
    mydata = requests.get(url)
    finaldata = mydata.json()
    
    # Delete all previous photos using makenew function
    makenew()
    
    for i in range(len(finaldata)):
        fdata = finaldata[i]['image']['data']['data']
        
        # Convert fdata (byte data) into a NumPy array of type uint8 (valid for image data)
        newobj = np.array(fdata, dtype=np.uint8)
        
        # The name of the image is followed by (name_adhaarnumber) as there may be multiple people with the same Aadhaar number
        newname = finaldata[i]['name'] + '_' + finaldata[i]['adhaar_number']
        
        # Create the image from byte data
        img = Image.open(BytesIO(newobj))
        
        # Save the image in the desired folder
        img.save(f"./images/{newname}.png")
