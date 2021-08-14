#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2
import os
import glob
import shutil
import matplotlib.pyplot as plt


# In[11]:


dir_tree = os.walk('DATA/train')
base_outpth = 'FilteredData/train'
os.makedirs(base_outpth,exist_ok=True)
see_mods = ['FLAIR','T1W','T2W','T1WCE']
see_label = 1
limit = 15*len(see_mods)
with open('train_labels.csv') as f:
    data = f.readlines()[1:] #ignore header
print('Data:',len(data))
view_ids = []
for line in data:
    pid,lbl = line.split(',')
    if int(lbl) == see_label:
        view_ids.append(pid)


# In[12]:


dir_seen = 0
for dir_num,(root,dirs,files) in enumerate(dir_tree):
    pat_id_dir = 1
    root = root.replace('\\','/')
    items = root.split('/')
    if len(items) >= 4: 
        pat_id = items[2]
        modality = items[3]
        if modality.upper() not in see_mods:
            continue
        if pat_id not in view_ids:
            continue
        dir_seen +=1
        if dir_seen >= limit+1:
            break

        outpath = os.path.join(base_outpth,pat_id,modality)
        if os.path.exists(outpath):
            continue
        
        nontumorpath = os.path.join(base_outpth,pat_id, 'nontumor')
        os.makedirs(nontumorpath,exist_ok=True)
        print('PATIENT:',pat_id,'Modality',modality)
    files = sorted(files)
    for i,file in enumerate(files):
        if pat_id_dir:
            os.makedirs(outpath,exist_ok=True)
            pat_id_dir = 0
            
        outfile = os.path.join(outpath,file)
        fullpath = os.path.join(root,file)
        #print('fullpath:',fullpath)
        img = cv2.imread(fullpath)
        cv2.namedWindow('inp',0)
        cv2.imshow('inp',img)
        k = cv2.waitKey(0)
        if k == ord('s'):
            shutil.copyfile(fullpath,outfile)
        if k == ord('q'):
            dir_seen = limit
            break
        if k == ord('n'):
            outfile = os.path.join(nontumorpath,file.replace('Image',f'Image-{modality}'))
            shutil.copyfile(fullpath,outfile)
            

cv2.destroyAllWindows()
        



