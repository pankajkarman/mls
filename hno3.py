#!/usr/bin/env python
# coding: utf-8

from mls import MLSDownload

odir = '/home/pankaj/phd/code/hole/antarctic/data/mls/'
filename = "/home/pankaj/phd/code/hole/antarctic/data/links/subset_ML2HNO3_005_20210201_115946.txt"
mls = MLSDownload(filename)
mls.download(odir)

