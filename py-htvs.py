#!/usr/bin/python3

import os
import sys
import htvs.filemanager as mf
import htvs.getopt as og
import htvs.vscheck as csv


def main():
    #Get run folder
    prj_folder = os.path.dirname(os.path.realpath(__file__))
    
    #inizialize the objects
    fm = mf.FileManager()
    go = og.GgetArgs()
    
    go.process_arguments(sys.argv[1:])

    #check the settings file, if doesn't exist the script exits
    try:
        fm.read_json(prj_folder + "/settings/setting.json")
        if go.debug : print("File json delle configurazioni {}".format(fm.json_cfg))

    except Exception as e:
        print("Errore durante la lettura del file di setting")
        sys.exit(0)
    vsc = csv.VsCheck(fm.json_cfg["api_key"])
    tmplist = []
    if (len(go.file) > 0) and (len(go.folderin) == 0):
        tmplist.append(go.file)

    elif (len(go.file) == 0) and (len(go.folderin) > 0):
        fm.enumerate_files(go.folderin)
        tmplist = fm.files

    else :
        print("Opzioni -f e -r non possono essere passate insieme")
        sys.exit(0)

    vsc.check_hash_in_virustotal(tmplist,fm.json_cfg["url"])
    vsc.printresult()
    if len(go.folderout) > 0:
        fm.writefiles(vsc.file_checked, go.folderout, go.debug, go.compress)
    else:
        print(os.getcwd())
        fm.writefiles(vsc.file_checked, os.getcwd() + "/", go.debug)

    

if __name__== "__main__":
    main()