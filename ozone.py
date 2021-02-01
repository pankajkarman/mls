#!/usr/bin/env python
from mls import MLSDownload

odir = '/home/pankaj/phd/code/hole/antarctic/data/mls/'
filename = "/home/pankaj/phd/code/hole/antarctic/data/links/subset_ML2O3_005_20210201_115401.txt"
mls = MLSDownload(filename)
mls.download(odir)

