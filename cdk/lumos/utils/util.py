import zipfile
import os

def zip_dir(folder_path, name_of_zip):
    zip_path = os.path.join(folder_path, name_of_zip)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file != name_of_zip:
                    zipf.write(os.path.join(root, file),
                               os.path.relpath(os.path.join(root, file),
                                               os.path.join(folder_path, '../..')))