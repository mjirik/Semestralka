# -*- coding: utf-8 -*-
"""
Created on Mon May 26 12:07:13 2014

@author: TheLosPavlos
"""

import ZDO2014juna_rak_hejdova_hog as ss
import skimage

zn = ss.Znacky()
img = skimage.io.imread('cesta_ke_zjistovane_znacce')
print zn.rozpoznejZnacku(img)