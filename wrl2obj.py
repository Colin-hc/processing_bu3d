# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:23:59 2019
@author: DSY
"""

import numpy as np

import glob
import os
# from re import *
import re
import json
# import linecache
# %%
# points
# wrls = glob.glob(os.path.join('E:\\3Dface\ZZ_3D', '*.wrl'))
wrls = ['data/F0001_AN01WH_F3D.wrl']
wrl = json.loads('data/F0001_AN01WH_F3D.wrl')
outpath = ""
wrls.sort()
for wrl in wrls:
    f = open(wrl, "r")
    lines = f.readlines()
    f.close()
    keywords = "coord Coordinate"
    for i in range(0, len(lines)):
        i += 1
        if re.search(keywords, lines[i]):
            break
    # skip point[
    i = i + 2
    points = []
    keywords2 = 'coordIndex'
    for i in range(i, len(lines)):
        if re.search(keywords2, lines[i]):
            break
        points.append(lines[i].split(',')[0].split())
    points = points[0:-2]

    # %%
    faces = []
    i = i + 2
    keywords3 = 'texCoord TextureCoordinate'
    for i in range(i, len(lines)):
        if re.search(keywords3, lines[i]):
            break
        faces.append(lines[i].split(',')[0].split()[0:3])
    faces = faces[0:-1]
    faces = np.array(faces, dtype=int) + 1
    # +1来符合obj的face格式

    # %%
    a = np.zeros((len(points), 1), dtype='str')
    a[:] = 'v'
    points = np.hstack((a, points))
    a = np.zeros((len(faces), 1), dtype='str')
    a[:] = 'f'
    faces = np.hstack((a, faces))
    files = np.vstack((points, faces))
    np.savetxt(outpath + wrl.split("\\")[-1].split(".")[0] + '.obj', files, delimiter=' ', fmt='%s')
