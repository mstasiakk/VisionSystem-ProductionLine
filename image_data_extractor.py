import json
from pathlib import Path
import os
from PIL import Image

Image_Folder_Path = "TestImages"  # <--- Provide root directory

SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}

def is_image_file(file_path):
    return Path(file_path).suffix.lower() in SUPPORTED_EXTENSIONS

def get_image_metadata(root_dir):
    image_metadata = []

    for current_dir, subdirs, files in os.walk(root_dir):
        for file_name in files:
            full_file_path = os.path.join(current_dir, file_name)
            
            if is_image_file(full_file_path):
                file_size = os.path.getsize(full_file_path)
                
                try:
                    # With Pillow open img
                    with Image.open(full_file_path) as img:
                        width, height = img.size  # .size gives ->(width, height)
                except Exception as e:

                    print(f"Error while trying to open directory: {full_file_path}: {e}")
                    width, height = None, None  # None dimension in case of exception being caught


                metadata_entry = {
                    "file_path": full_file_path,
                    "file_size_bytes": file_size,
                    "dimensions": {  # Nested dictionary
                        "width": width,
                        "height": height
                    }
                }
                image_metadata.append(metadata_entry)
                
                print(f"Found: {full_file_path} ({width}x{height})")

    return image_metadata

def main():
    
    if not os.path.isdir(Image_Folder_Path): 
        print(f"Error: '{Image_Folder_Path}' is not a correct directory")
        return

    # Collect metadata
    print(f"Searching in: {Image_Folder_Path}...")
    all_metadata = get_image_metadata(Image_Folder_Path) 
    print(f"found {len(all_metadata)} images.")

    # Save to JSON file
    output_file = "images_metadata.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_metadata, f, indent=2, ensure_ascii=False)
    print(f"Data saved: {output_file}")

if __name__ == "__main__":
    main()