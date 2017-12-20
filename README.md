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
  
  
### Experiment

Used a pretrained GooleNet (Inception V3) model and retrained the fianl layer for the new two categories. 
Inception v3 paper: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44903.pdf

Instructions: https://www.tensorflow.org/tutorials/image_retraining

Commands: 
Training and testing:
```{r, engine='bash', count_lines}
python -m scripts.retrain \
    --bottleneck_dir=tf_files/bottlenecks \
    --model_dir=tf_files/models/"inception_v3" \
    --summaries_dir=tf_files/training_summaries/"inception_v3" \
    --output_graph=tf_files/retrained_graph.pb \
    --output_labels=tf_files/retrained_labels.txt \
    --architecture="inception_v3" \
    --image_dir=tf_files/flower_photos 
```

Only Training so you can run a custom test script:
```{r, engine='bash', count_lines}
python -m scripts.retrain \
    --bottleneck_dir=tf_files/bottlenecks \
    --model_dir=tf_files/models/"inception_v3" \
    --summaries_dir=tf_files/training_summaries/"inception_v3" \
    --output_graph=tf_files/retrained_graph.pb \
    --output_labels=tf_files/retrained_labels.txt \
    --architecture="inception_v3" \
    --image_dir=tf_files/flower_photos  \
    --testing_percentage = 0
```

| Experiment        | Description               | Accuracy  |
| ----------------- |:-------------------------:| -----:|
| Horizontal Concatenation      | We wanted to make use of as much information available as possible. Inception v3 uses a 299 x 299 image as the input vector. Since our input is an image of size 3200px x 480px , padding and reducing the size causes the image to get blurry | 67.05 % |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |


