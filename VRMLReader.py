# -*- coding: utf-8 -*-
"""
Created on Tues Sep 28 10:23:59 2021
@author: Colin Han
"""

import numpy as np
import re


def VRMLReader(wrlname):
    wrl = wrlname
    f = open(wrl, "r")
    lines = f.readlines()
    f.close()
    i = 0
    keywords = "url"
    for idx in range(i, len(lines)):
        if re.search(keywords, lines[idx]):
            i = idx
            break
    imgname = lines[i].split('"')[1]
    keywords = "coord Coordinate"
    for idx in range(i, len(lines)):
        if re.search(keywords, lines[idx]):
            i = idx
            break
    # skip point[
    i = i + 2
    points = []
    keywords2 = 'coordIndex'
    for idx in range(i, len(lines)):
        if re.search(keywords2, lines[idx]):
            i = idx
            break
        # if lines[idx].split(',')[0].split() == ']' or lines[idx].split(',')[0].split() == '}':
        #     continue
        points.append(lines[idx].split(',')[0].split())
    points = points[0:-2]

    # %%
    faces = []
    i = i + 1
    keywords3 = 'texCoord TextureCoordinate'
    for idx in range(i, len(lines)):
        if re.search(keywords3, lines[idx]):
            i = idx
            break
        data = lines[idx].split(',')[0].split()
        if len(data) == 4:
            faces.append(data[0:3])
        if len(data) == 5:
            faces.append(data[0:3])
            faces.append([data[0], data[2], data[3]])
        if len(data) == 6:
            faces.append(data[0:3])
            faces.append([data[0], data[2], data[3]])
            faces.append([data[0], data[3], data[4]])
        if len(data) == 7:
            faces.append(data[0:3])
            faces.append([data[0], data[2], data[3]])
            faces.append([data[0], data[3], data[4]])
            faces.append([data[0], data[4], data[5]])

    # faces = np.array(faces, dtype=int) + 1
    # +1来符合obj的face格式

    texpoints = []
    i += 2
    keywords4 = 'texCoordIndex'
    for idx in range(i, len(lines)):
        if re.search(keywords4, lines[idx]):
            i = idx
            break
        texpoints.append(lines[idx].split(',')[0].split())
    texpoints = texpoints[0:-2]

    i += 1
    texcoord = []
    keywords5 = 'DEF Tricorder_Camera_Front Viewpoint'
    for idx in range(i, len(lines)):
        if re.search(keywords5, lines[idx]):
            i = idx
            break
        data = lines[idx].split(',')[0].split()
        if len(data) == 4:
            texcoord.append(data[0:3])
        if len(data) == 5:
            texcoord.append(data[0:3])
            texcoord.append([data[0], data[2], data[3]])
        if len(data) == 6:
            texcoord.append(data[0:3])
            texcoord.append([data[0], data[2], data[3]])
            texcoord.append([data[0], data[3], data[4]])
        if len(data) == 7:
            texcoord.append(data[0:3])
            texcoord.append([data[0], data[2], data[3]])
            texcoord.append([data[0], data[3], data[4]])
            texcoord.append([data[0], data[4], data[5]])



    points = np.array(points).astype(float)
    faces = np.array(faces).astype(int) + 1
    texpoints = np.array(texpoints).astype(float)
    texcoord = np.array(texcoord).astype(int) + 1
    return imgname, points, faces, texpoints, texcoord
    # for idx in range(0, len(points)):
    #     for jdx in range(0, len(points[idx])):
    #         points[idx][jdx] = float(points[idx][jdx])
    #
    # for idx in range(0, len(faces)):
    #     for jdx in range(0, len(faces[idx])):
    #         faces[idx][jdx] = int(faces[idx][jdx])
    #
    # for idx in range(0, len(texpoints)):
    #     for jdx in range(0, len(texpoints[idx])):
    #         texpoints[idx][jdx] = float(texpoints[idx][jdx])
    #
    # for idx in range(0, len(texcoord)):
    #     for jdx in range(0, len(texcoord[idx])):
    #         texcoord[idx][jdx] = int(texcoord[idx][jdx])

if __name__ == '__main__':
    wrl = 'data/F0001_AN01WH_F3D.wrl'
    data = VRMLReader(wrl)
    a = 1