#!/usr/bin/env python3
#
# Merge Label Maps
# Version: 04 Jan 2023  

import os
import SimpleITK as sitk

#%% Functions
def number_of_objects(df):
    stats = sitk.LabelShapeStatisticsImageFilter()
    stats.Execute(df)
    num = stats.GetNumberOfLabels()
    return num

#%% Pipeline
wkdir=os.getcwd()

seg_1 = sitk.ReadImage(f'{wkdir}/eb1-399.seg.nrrd', imageIO='NrrdImageIO')
seg_1 = sitk.Cast(seg_1, sitk.sitkUInt64)
num = number_of_objects(seg_1)
print(f'Label Map 1 has {num} number of objects')
seg_1 = sitk.LabelImageToLabelMap(seg_1)

seg_2 = sitk.ReadImage(f'{wkdir}/eb400-999.seg.nrrd', imageIO='NrrdImageIO')
seg_2 = sitk.Cast(seg_2, sitk.sitkUInt64)
num = number_of_objects(seg_2)
print(f'Label Map 2 has {num} number of objects')
seg_2 = sitk.LabelImageToLabelMap(seg_2)

seg_3 = sitk.ReadImage(f'{wkdir}/eb1000-1399.seg.nrrd', imageIO='NrrdImageIO')
seg_3 = sitk.Cast(seg_3, sitk.sitkUInt64)
num = number_of_objects(seg_3)
print(f'Label Map 3 has {num} number of objects')
seg_3 = sitk.LabelImageToLabelMap(seg_3)

seg_4 = sitk.ReadImage(f'{wkdir}/eb1400-1799.seg.nrrd', imageIO='NrrdImageIO')
seg_4 = sitk.Cast(seg_4, sitk.sitkUInt64)
num = number_of_objects(seg_4)
print(f'Label Map 4 has {num} number of objects')
seg_4 = sitk.LabelImageToLabelMap(seg_4)

seg_5 = sitk.ReadImage(f'{wkdir}/eb1800-end.seg.nrrd', imageIO='NrrdImageIO')
seg_5 = sitk.Cast(seg_5, sitk.sitkUInt64)
num = number_of_objects(seg_5)
print(f'Label Map 5 has {num} number of objects')
seg_5 = sitk.LabelImageToLabelMap(seg_5)

final_image = sitk.MergeLabelMap(seg_1,seg_2,seg_3,seg_4,seg_5, 2)
final_image = sitk.Cast(final_image, sitk.sitkUInt64)
num = number_of_objects(final_image)
print(f'Final Label Map has {num} number of objects')
outfile = (f'{wkdir}/outfile.seg.nrrd')
sitk.WriteImage(final_image, outfile, imageIO='NrrdImageIO', useCompression=True)
print(f'Merged Label Maps saved to {outfile}')
