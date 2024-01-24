#!/usr/bin/python3

import requests
import hashlib

class VsCheck:
    def __init__(self, api_key):
        self.api_key = api_key
        self.hashfile = set()
        self.file_checked = []

       
    def check_hash_in_virustotal(self, fileslist, url):
        
        for file in fileslist:
            file_hash = hashlib.sha256(open(file, 'rb').read()).hexdigest()
            params = {'apikey': self.api_key, 'resource': file_hash}
            response = requests.get(url, params=params)
            if response.status_code == 200:
                responsetmp = response.json()
                responsetmp["filename"] = file
                self.file_checked.append(responsetmp)
            else:
                print("Error occurred during the request.")


    def printresult(self):
        for json_response in self.file_checked:
            if json_response['response_code'] == 1:
                positives = json_response['positives']
                total = json_response['total']
                print()
                if positives > 0:
                    print(f"The file {json_response['filename']} is considered malicious. Detection ratio: {positives}/{total}")
                else:
                    print(f"The file {json_response['filename']} is not detected as malicious.")
            elif json_response['response_code'] == -2:
                print(f"The file {json_response['filename']} is still queued for analysis.")
            else:
                print(f"No results found for the file {json_response['filename']}.")
