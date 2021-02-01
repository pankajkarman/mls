#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests, os
from tqdm import tqdm


# In[2]:


class MLSDownload:
    def __init__(self, filename, skiprows=2):
        self.filename = filename
        self.skiprows = skiprows
        with open(filename, "r") as f:
            lines = f.readlines()[skiprows:]
            lines = [line.strip() for line in lines]
        self.links = lines

    def download(self, odir="./data/mls/"):
        for infile in tqdm(self.links):
            fname = infile.split("/")[-1]
            species = fname.split("-")[2].split("_")[0].lower()
            filename = odir + species + "/" + fname
            if not os.path.exists(filename):
                resp = requests.get(infile)
                with open(filename, "wb+") as f:
                    f.write(resp.content)


# In[ ]:

odir = '/home/pankaj/phd/code/hole/antarctic/data/mls/'
filename = "/home/pankaj/phd/code/hole/antarctic/data/links/subset_ML2HNO3_005_20210201_115946.txt"
mls = MLSDownload(filename)
mls.download(odir)

