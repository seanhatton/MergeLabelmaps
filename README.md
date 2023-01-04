# MergeLabelmaps
Merge segmentation label maps with SimpleITK. 

In 3D Slicer (https://www.slicer.org/), it is difficult to review more than 400 objects at a time (e.g. bacteria in an ROI) before memory and performance problems occur. It is straightforward to split labelmaps in Slicer, but merging large labelmaps is very difficult and time consuming. This quick script merges reviewed labelmaps saved as multiple files (seg.nrrd) from Slicer.  

Please note the different options for merging (the last number in the sitk.MergeLabelMap command):

* KEEP (0): MergeLabelMapFilter do its best to keep the label unchanged, but if a label is already used in a previous label map, a new label is assigned. 
* AGGREGATE (1): If the same label is found several times in the label maps, the label objects with the same label are merged. 
* PACK (2): MergeLabelMapFilter relabel all the label objects by order of processing. No conflict can occur. 
* STRICT (3): MergeLabelMapFilter keeps the labels unchanged and raises an exception if the same label is found in several images.

