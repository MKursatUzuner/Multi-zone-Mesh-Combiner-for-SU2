# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:48:20 2022

@author: M. Kursat Uzuner
"""
import numpy as np
import os

print('Please enter the zone number\n')
zone_num = int(input());
zones = str(np.zeros(zone_num))
print('Please enter the name for the combined mesh file with its extension.\nIf it does not exist, it will be created\n')
totalName = input()
total = open("%s"%totalName,"w+")
total.write("NZONE= %d\n"%zone_num)
for i in range(zone_num):
    print('\nPlease enter the name of the Zone %d mesh file with its extension;\n'%(i+1))
    current_zone = 1 + i
    zoneTempName = input()
    if os.path.isfile(zoneTempName):
        zoneTemp = open("%s"%zoneTempName,"r")
        total.write("\nIZONE= %d\n"%current_zone)
        total.write(zoneTemp.read())
        zoneTemp.close()
    else:
        print('\nYou have entered a file name that does not exist.')
        break
if i == (zone_num-1):
    print('\nCombined mesh file creation is SUCCESFUL!')
else:
    print('\nCombined mesh file creation is UNSUCCESFUL!')
total.close()
