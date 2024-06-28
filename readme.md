# Prostate Gland Segmentation Algorithm 

We provide the code for our prostate gland segmentation algorithm trained on the [PESO dataset](https://www.wouterbulten.nl/posts/peso-dataset-whole-slide-image-prosate-cancer/) used in our publication "Enhancing prostate cancer diagnosis: AI-driven virtual biopsy for optimal MRI-targeted biopsy approach and Gleason grading strategy".

NB! Most of the experiments and scripts were run in anaconda environment
using Ubuntu 22.04. We recommend using this setup.

## 01_prepare_training_data
#### split_data.py 
For the Peso data annotation masks are only provided for the train split. 
In order to also have a validation split, we split the original training set into a new training and validation split. 
To do so, we move 12 of the training images and their masks to the new "validation" dir.

#### extract_patches.py 
After the data has been split, we extract training patches with a given patch size (PS) and microns-per-pixel (MPP) from the WSIs and their masks.
The patches are saved in new directories.
We use [openslide python](https://openslide.org/api/python/) to open the WSIs and extraxt the patches. 

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
