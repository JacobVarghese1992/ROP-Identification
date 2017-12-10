import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import os
from shutil import copyfile

cats_df = pd.read_csv('categories.csv')
images = os.listdir("./output")
for image in images:
    set_id = image.split("_")[2]
    set_id = set_id.replace('OS-','')
    set_id = set_id.replace('OD-','')
    df_tmp = cats_df.loc[cats_df['set_id'].astype(str) == set_id]
    if(len(df_tmp) <1):
        continue
    if(df_tmp.iloc[0]['has_rop'] == 1.0):
        print("./output_has_rop/" + image)
        copyfile("./output/" + image, "./output_has_rop/" + image)
        
    else:
        print("./output_no_rop/" + image)
        copyfile("./output/" + image, "./output_no_rop/" + image)
        
