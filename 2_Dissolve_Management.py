#Code for Dissolve Management
#Developer: Sagar Chougule
#Contact : 92chougulesagar@gmail.com, https://github.com/92sagarchougule

import arcpy

from arcpy import env

env.workspace = r'D:\ClassData'

arcpy.Dissolve_management("Buffer_Road","Poly_Road")

