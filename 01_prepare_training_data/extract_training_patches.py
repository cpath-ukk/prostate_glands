from openslide import open_slide
import os
from PIL import Image

def extract_patches_and_masks(wsi_dir,mask_dir,patch_out_dir,mask_out_dir,final_p_s,final_mpp):
	"""
    Extracts patches and corresponding masks from whole-slide images (WSIs) and saves them to specified directories.

    Args:
        wsi_dir (str): Directory containing the whole-slide images (WSIs).
        mask_dir (str): Directory containing the masks corresponding to the WSIs.
        patch_out_dir (str): Directory to save the extracted image patches.
        mask_out_dir (str): Directory to save the extracted mask patches.
        final_p_s (int): Patch Size.
        final_mpp (float): Microns per pixel (MPP) for the patches.

    Returns:
        None

    This function processes each WSI and its corresponding mask to extract patches with given patch size and MPP.
	The patches in the specified output directories. The patches
    from the WSI are saved as JPEG images, and the patches from the masks are saved as PNG images.
    
    Note:
        The slide MPP is manually set to 0.48 microns per pixel as it is not readable from the data.
        
    Example:
        extract_patches_and_masks('/path/to/wsi_dir', '/path/to/mask_dir', '/path/to/patch_out_dir', '/path/to/mask_out_dir', 256, 0.25)
    """
	wsis = sorted(os.listdir(wsi_dir))

	# As this is not readable from data 
	slide_mpp = 0.48 

	for wsi in wsis:
		print("working with ", wsi)

		#read out wsi
		path_slide = os.path.join(wsi_dir, wsi)
		wsi_work = open_slide(path_slide)

		#with slide_mpp we can calculate the size of patches to be cut out 
		# of the wsi that have final_mpp when resized to final_p_s
		# slide_mpp = float(wsi_work.properties["openslide.mpp-x"])
		slide_p_s = int( (final_mpp/slide_mpp) * final_p_s)
		
		#read out mask 
		path_mask = os.path.join(mask_dir,wsi.replace(".tif","") + "_training_mask.tif")
		mask_work = open_slide(path_mask)
		
		#calculate the number of horizontal and vertical patches given the calculated slide_p_s
		width,height = wsi_work.level_dimensions[0]
		wi = width // slide_p_s
		he = height // slide_p_s
		
		#iterate over the patches and extract them
		for h in range(he):
			for w in range(wi):
				w_str = f"_{w:03d}"
				h_str = f"_{h:03d}"

				#read out patch, resize it to final_p_s (doing so it gets the wanted mpp), convert to RGB and save 
				patch_wsi = wsi_work.read_region((w*slide_p_s,h*slide_p_s), 0, (slide_p_s,slide_p_s))
				patch_wsi = patch_wsi.resize((final_p_s,final_p_s), Image.LANCZOS)
				patch_wsi = patch_wsi.convert('RGB')
				img_patch_save_path = os.path.join(patch_out_dir,wsi.replace(".tif","") + h_str + w_str + ".jpg")
				patch_wsi.save(img_patch_save_path, quality = 90)
				
				#read out mask, resize it to final_p_s (doing so it gets the wanted mpp), convert to greyscale and save 
				patch_mask = mask_work.read_region((w*slide_p_s,h*slide_p_s), 0, (slide_p_s,slide_p_s))
				patch_mask = patch_mask.resize((final_p_s,final_p_s), Image.LANCZOS)
				patch_mask = patch_mask.convert('L')
				mask_patch_save_path = os.path.join(mask_out_dir,wsi.replace(".tif","") + h_str + w_str + ".png")
				patch_mask.save(mask_patch_save_path) 
	
if __name__ == '__main__':
	# Set resolution and size of patches
	FINAL_MPP = 2.0
	FINAL_P_S = 512

	## Set directories for the training data 
	WSI_DIR = os.path.join('DATA','peso','original_data','train','image')
	MASK_DIR = os.path.join('DATA','peso','original_data','train','mask')
	IMG_PATCHES_OUT_DIR = os.path.join('DATA','peso','MPP_2','P_S_512','train','image')
	MASK_PATCHES_OUT_DIR = os.path.join('DATA','peso','MPP_2','P_S_512','train','mask')

	#extract patches for the training data
	extract_patches_and_masks(WSI_DIR,MASK_DIR,IMG_PATCHES_OUT_DIR,MASK_PATCHES_OUT_DIR,FINAL_P_S,FINAL_MPP)


	## Set directories for the validation data 
	WSI_DIR_VAL = os.path.join('DATA','peso','original_data','val','image')
	MASK_DIR_VAL = os.path.join('DATA','peso','original_data','val','mask')
	IMG_PATCHES_OUT_DIR_VAL = os.path.join('DATA','peso','MPP_2','P_S_512','val','image')
	MASK_PATCHES_OUT_DIR_VAL = os.path.join('DATA','peso','MPP_2','P_S_512','val','mask')

	#extract patches for the validation data
	extract_patches_and_masks(WSI_DIR_VAL,MASK_DIR_VAL,IMG_PATCHES_OUT_DIR_VAL,MASK_PATCHES_OUT_DIR_VAL,FINAL_P_S,FINAL_MPP)




	