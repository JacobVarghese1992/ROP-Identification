import os
import sys
from PIL import Image, ImageFile
from matplotlib.pyplot import imshow
import numpy as np
import multiprocessing


ImageFile.LOAD_TRUNCATED_IMAGES = True

def concat_image(patient, eye_code, eye_number, parent_dir):
    
    dates = os.listdir(parent_dir + "/" + patient)    
    for date in dates:
	print("hi")        
        eyes = os.listdir(parent_dir + "/" + patient + "/" + date + "/")
        print(eyes)
        if len([eye for eye in eyes if (eye.startswith(eye_code))]) == 0:
            print("Missing: " + eye_code + " " + patient + " " + date)
            continue
            
        lent = len([eye for eye in eyes if (eye_code in eye)])
        for ct in range(lent):
            
            file_name = [eye for eye in eyes if (eye.startswith(eye_code))][ct]
            eye_path = parent_dir + "/" + patient + "/" + date + "/" + file_name + "/"
#             print(os.listdir(eye_path))
            eye_files = ['DiscUp.png', 'DiscLeft.png', 'DiscRight.png', 'DiscDown.png', 'DiscCenter.png']
            contains_all =  (set(['DiscUp.png', 'DiscLeft.png', 'DiscRight.png', 'DiscDown.png', 'DiscCenter.png']).issubset(os.listdir(eye_path)))
        
            if contains_all == True:
            
                eye_files_path = list(map(lambda s: eye_path + s, eye_files))
                eye_images = list(map(Image.open, eye_files_path))
                widths, heights = zip(*(i.size for i in eye_images))
                total_width = sum(widths)
                max_height = max(heights)
                new_im = Image.new('RGB', (total_width, max_height))
                x_offset = 0
                for im in eye_images:
                    new_im.paste(im, (x_offset,0))
                    x_offset += im.size[0]
                new_im.save("./output/" + patient + "_" + date + "_" + file_name + "_" + eye_number +".png")
                print("Saved:"+ "./output/" + patient + "_" + date + "_" + file_name + "_" + eye_number +".png")



tasks = []
pool = multiprocessing.Pool()
parent_dir = "./images"
patients   = os.listdir(parent_dir)
i = 0
for patient in patients:
    i = i + 1
    print(i)
#    concat_image(patient, "OD", "0", parent_dir)
#    concat_image(patient, "OS", "1", parent_dir)

    tasks.append( (patient, "OD", "0", parent_dir) )
    tasks.append( (patient, "OS", "1", parent_dir) )

results = [pool.apply_async( concat_image, t ) for t in tasks]
pool.close()
pool.join()










