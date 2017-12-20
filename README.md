# ROP-Identification
### Files and Directories ###

Original Images: are in the folder path, PATIENT_ID -> DATE OF EXAM -> SET_ID -> IMAGES 

* concatnate.py: Python script to concatenate the five views into one horizontal image. This is done per patient per date per exam for each eye. The views that are concatenated are 'DiscUp.png', 'DiscLeft.png', 'DiscRight.png', 'DiscDown.png', 'DiscCenter.png'. If any of these views for an exam are missing the whole examination is dropped and not considered.  
 Input: 'DiscUp.png', 'DiscLeft.png', 'DiscRight.png', 'DiscDown.png', 'DiscCenter.png' images each of size 640px x 480px
 Output: Images of size 3200px x 480px
 
 
* concatenate4sq.py: Python script to concatenate the four views into a square. This is done per patient per date per exam for each eye. The views that are concatenated are 'DiscUp.png', 'DiscLeft.png', 'DiscRight.png', 'DiscDown.png'. If any of these views for an exam are missing the whole examination is dropped and not considered.  
 Input: 'DiscUp.png', 'DiscLeft.png', 'DiscRight.png', 'DiscDown.png' images each of size 640px x 480px
 Output: Images of size 1280px x 960px


* concatenateCenter.py: Python script to extract the center view  per patient per date per exam for each eye.  
 Input: 'DiscCenter.png' images each of size 640px x 480px
  Output: Images of size 640px x 480px
 
 
* split.py: Split all the horizontally concatenated images into categories of "output_has_rop" and "output_no_rop"
  Prerequisits:
  Input: Images of size 3200px x 480px named with the set_id
  Output: Images of size 3200px x 480px separated into it's "output_has_rop" and "output_no_rop" folders
  
* split4sq.py: Split all the horizontally concatenated images into categories of "output_has_rop" and "output_no_rop"
  Prerequisits:
  Input: Images of size 1280px x 960px named with the set_id
  Output: Images of size 1280px x 960px separated into it's "output_has_rop" and "output_no_rop" folders
  

* splitCenter.py: Split all the horizontally concatenated images into categories of "output_has_rop" and "output_no_rop"
  Prerequisits:
  Input: Images of size 640px x 480px named with the set_id
  Output: Images of size 640px x 480px separated into it's "output_has_rop" and "output_no_rop" folders
  
  
  
