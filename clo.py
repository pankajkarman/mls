#!/usr/bin/env python
# coding: utf-8

from mls import MLSDownload

odir = '/home/pankaj/phd/code/hole/antarctic/data/mls/'
filename = "/home/pankaj/phd/code/hole/antarctic/data/links/subset_ML2CLO_005_20210201_115601.txt"
mls = MLSDownload(filename)
mls.download(odir)

