import os
import random
import shutil

def sample_and_move_data(img_path, mask_path, val_img_path, val_mask_path):
    """
    Randomly selects 12 image IDs from the train directory and moves the corresponding image and mask files 
    to the specified destination directories.

    Args:
        img_path (str): Path to the directory containing the image files.
        mask_path (str): Path to the directory containing the mask files.
        val_img_path (str): Destination directory for the selected image files.
        val_mask_path (str): Destination directory for the selected mask files.

    Returns:
        None

    This function scans the directory for image files, extracts unique image IDs, 
    randomly selects 12 of these IDs, and moves the corresponding image and mask files 
    to the specified destination directories.

    Example:
        sample_and_move_data('/path/to/img_path', '/path/to/mask_path', '/path/to/iv_path', '/path/to/mv_path')
    """
    # Get the list of files in the img_path directory
    img_files = os.listdir(img_path)

    # Extract the ids from the image filenames
    ids = [file.split('_')[1].split('.')[0] for file in img_files]

    # Remove duplicates and sort the ids
    ids = sorted(list(set(ids)))
    print(len(ids))

    # Sample 12 ids
    sampled_ids = random.sample(ids, 12)

    # Iterate over the sampled ids
    for id in sampled_ids:
        # Find the corresponding image and mask filenames
        img_filename = 'pds_'+str(id)+'_HE.tif'
        mask_filename = img_filename.replace('.tif', '_training_mask.tif')

        # Construct the source and destination paths
        img_src = os.path.join(img_path, img_filename)
        mask_src = os.path.join(mask_path, mask_filename)
        img_dst = os.path.join(val_img_path, img_filename)
        mask_dst = os.path.join(val_mask_path, mask_filename)

        # Move the image and mask files to the destination paths
        shutil.move(img_src, img_dst)
        shutil.move(mask_src, mask_dst)

        print(f"Moved image: {img_filename} to {img_dst}")
        print(f"Moved mask: {mask_filename} to {mask_dst}")

if __name__ == '__main__':

    # Source directories (= train directories)
    img_path = 'DATA/peso/train/image'  # Directory containing the images
    mask_path = 'DATA/peso/train/mask'  # Directory containing the masks

    # Destination directories
    val_img_path = 'DATA/peso/val/image'  # Destination directory for images
    val_mask_path = 'DATA/peso/val/mask'  # Destination directory for masks

    sample_and_move_data(img_path, mask_path, val_img_path, val_mask_path)
