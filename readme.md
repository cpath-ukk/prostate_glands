Reference of provided code

NB! We provide raw working scripts used for the development and implementation.
Upon publication we will annotate and prepare code for end users.

NB! Most of the experiments and scripts were run in anaconda environment
using Ubuntu 22.04. We recommend using this setup.

## 01_qupath_patch_extraction
This a Groovy script for use with QuPath v. > 0.3 for extraction of training
or validation/test patches and associated segmentation masks (ground truth
from annotations).

## 02_train_pixel_wise_segmentation
train_script.py: This is a training script.
It was used with the Python v.3.9
and pytorch v.1.10.
Segmentation-models-pytorch v.0.3.1 library (or any other version) is
used for model construction.
pytorch_toolbelt is used for construction of some of the loss functions (v.0.6.3)

dataset_v2.py: Helper script for dataset construction and data augmentation.
Albumentations package (v1.3.0) was used for data augmentation.

## 03_Patch_level_validation_testing
This is a Python script for additional validation or test of the trained checkpoints
using patch-level metrics of segmentation accuracy (Dice score and IoU).
