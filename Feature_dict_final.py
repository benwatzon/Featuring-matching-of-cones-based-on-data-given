import numpy as np
import cv2 
from scipy.spatial import distance

## detection values from different cones.
## here l stands for "left" and r for "right"
## "b" is blue cone and "y" is yellow cone.
## detection map list includes x and y coordinate of the detected cone and height and width of the bounding box
## see image for examples.

detections_map = {'l_1': [1683, 1397, 19, 19, 'b'], 
'l_2': [1216, 1197, 30, 44, 'b'], 
'l_3': [1332, 1141, 21, 32, 'b'], 
'l_4': [1393, 1111, 14, 22, 'b'], 
'l_5': [1425, 1091, 13, 15, 'b'], 
'l_6': [1016, 1083, 16, 9, 'b'], 
'l_7': [1123, 1067, 15, 10, 'b'], 
'l_8': [1098, 1061, 22, 18, 'b'], 
'l_9': [1483, 1056, 18, 15, 'b'], 
'l_10': [1545, 1024, 68, 12, 'b'], 
'l_11': [1903, 1175, 30, 46, 'y'], 
'l_12': [1814, 1128, 21, 33, 'y'], 
'l_13': [1290, 1116, 18, 13, 'y'], 
'l_14': [1759, 1099, 18, 27, 'y'], 
'l_15': [1714, 1082, 15, 22, 'y'], 
'l_16': [1010, 1073, 13, 16, 'y'], 
'l_17': [1688, 1068, 15, 19, 'y'], 
'l_18': [1666, 1060, 13, 16, 'y'], 
'l_19': [1635, 1045, 22, 22, 'y'],
'r_20': [1135, 1194, 32, 43, 'b'], 
'r_21': [1273, 1136, 22, 33, 'b'], 
'r_22': [1347, 1107, 15, 22, 'b'], 
'r_23': [1389, 1088, 11, 17, 'b'], 
'r_24': [1421, 1075, 12, 13, 'b'], 
'r_25': [1015, 1058, 50, 23, 'b'], 
'r_26': [1834, 1043, 16, 11, 'b'], 
'r_27': [1375, 1031, 17, 27, 'b'], 
'r_28': [1502, 1022, 77, 16, 'b'], 
'r_29': [1584, 1021, 31, 16, 'b'], 
'r_30': [1347, 1007, 11, 17, 'b'], 
'r_31': [1984, 1003, 46, 15, 'b'], 
'r_32': [1805, 1161, 25, 37, 'y'], 
'r_33': [1742, 1119, 22, 30, 'y'], 
'r_34': [1286, 1102, 14, 11, 'y'], 
'r_35': [1704, 1094, 18, 28, 'y'], 
'r_36': [1672, 1076, 16, 21, 'y'], 
'r_37': [1653, 1066, 15, 18, 'y'], 
'r_38': [1636, 1059, 13, 14, 'y'], 
'r_39': [1613, 1049, 19, 18, 'y'], 
'r_40': [1595, 1024, 37, 10, 'y'],
'r_41': [1516, 1011, 21, 9, 'y']}

l_blue_cones = {}
l_yellow_cones = {}
r_blue_cones = {}
r_yellow_cones = {}
r_keys = []
l_keys = []

keys = list(detections_map.keys())
values = list(detections_map.values())

def area(dictionary):
    """Finds the area and returns an ouput dictionary with the area appended onto the input dictionary"""

    for key in dictionary:
        areas = (dictionary[key][2]*dictionary[key][3])
        dictionary[key].append(areas)
    
    return dictionary

def get_first_pair(dictionary):
    
    dict_pairs = dictionary.items()
    pairs_iterator = iter(dict_pairs)
    first_pair = next(pairs_iterator)
    
    return first_pair

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

# def SSD(cordinate1, cordinate2):
#     """Find the sum of square distance"""
#     return 

for key in detections_map:
    if 'l' in key:
        if 'b' in detections_map[key]:
            l_blue_cones[key] = detections_map[key]
        else:
            l_yellow_cones[key] = detections_map[key]
            
    else:
        if 'b' in detections_map[key]:
            r_blue_cones[key] = detections_map[key]
        else:
            r_yellow_cones[key] = detections_map[key]


l_blue_final = area(l_blue_cones)
r_blue_final = area(r_blue_cones)
l_yellow_final = area(l_yellow_cones)
r_yellow_final = area(r_yellow_cones)

print(l_blue_final)
print("\n")
print(r_blue_final)
print("\n")
# 
# for key, value in l_blue_cones.items():
#     temp[key] = value

# print(temp)

get_first_pair(l_blue_final)
# temp={}
# temp1={}
pairDict = {}
distanceList =[]
areaList = []
imp_ratio = []

for key,value in l_blue_final.items():
    temp={}
    temp[key] = value
    for key1, value1 in r_blue_final.items():
        trackArea = abs(value[5]-value1[5])
        pair = value[0:2],value1[0:2]
        ratio = trackArea/value[5]
        if ratio<0.20:
            pairDict[key,key1] = pair
        
print(pairDict)
