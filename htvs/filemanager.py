#!/usr/bin/python3

import json
import os
import shutil
import hashlib
#import tarfile
#from Crypto.Cipher import AES
#from Crypto.Random import get_random_bytes

class FileManager:
    def __init__(self):
        self.json_cfg = set ()
        self.files = set ()

    def read_json(self, file_name):

        '''
        Load the json file
        '''
        with open(file_name) as f:
            self.json_cfg = json.load(f)


    def enumerate_files(self, folder_path):
        self.files = []

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.files.append(file_path)

    def writefiles(self, jsonlist, folder_out, debug, password=""):
        #Crea la cartella per i file malevoli
        os.makedirs(folder_out + "malicious/",mode=0o744,exist_ok=True)
        
        #Crea la cartella per i file ritenuti non malevoli
        os.makedirs(folder_out + "non-malicious/",mode=0o744,exist_ok=True)
        
        for file in jsonlist:
            if file["response_code"] == 0:
                folder = folder_out + "non-malicious/"
            else:
                folder = folder_out + "malicious/"

            if not (debug):
                os.rename(file["filename"], folder + hashlib.md5(open(file["filename"], 'rb').read()).hexdigest())
            else:
                shutil.copyfile(file["filename"], folder + hashlib.md5(open(file["filename"], 'rb').read()).hexdigest())

        #if len(password) > 0:
        #    create_encrypted_tar_gz(folder_out, folder_out + "malwarecollect", password)


# def create_encrypted_tar_gz(source_folder, output_file, password):
#     # Generate a random initialization vector (IV)
#     iv = get_random_bytes(16)

#     # Create the AES cipher with Cipher Block Chaining (CBC) mode
#     cipher = AES.new(password.encode("utf-8"), AES.MODE_CBC, iv)

#     with tarfile.open(output_file, "w:gz") as tar:
#         # Add the source folder contents to the tar archive
#         tar.add(source_folder, arcname="")

#     # Encrypt the tar archive file
#     with open(output_file, "rb") as file:
#         data = file.read()

#     encrypted_data = cipher.encrypt(data)

#     with open(output_file, "wb") as file:
#         file.write(iv + encrypted_data)
