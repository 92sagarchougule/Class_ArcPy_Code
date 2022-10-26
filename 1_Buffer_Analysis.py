#Code for Buffer_Analysis
#Developer: Sagar Chougule
#Contact : 92chougulesagar@gmail.com, https://github.com/92sagarchougule

import arcpy

from arcpy import env

env.workspace = r'D:\ClassData'

arcpy.Buffer_analysis("Roads","Buffer_Road",'10 Meters',"FULL")

