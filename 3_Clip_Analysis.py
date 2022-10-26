#Code for Clip Analysis
#Developer: Sagar Chougule
#Contact : 92chougulesagar@gmail.com, https://github.com/92sagarchougule

import arcpy

arcpy.env.workspace = r'D:\ClassData'

arcpy.Clip_analysis("Roads","Sector","Clip_Road")

