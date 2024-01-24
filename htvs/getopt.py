#!/usr/bin/python3

import getopt
import sys


class GgetArgs:
    def __init__(self):
        self.file = set ()
        self.debub = set()
        self.folderin = set ()
        self.folderout = set ()
        self.compress = set ()

    def process_arguments(self, argv):
        # Define the expected command-line options
        short_options = "dhf:r:o:c:"
        long_options = ["help", "file=", "recursive=", "output=", "compress=", "debug"]

        try:
            # Parse the command-line arguments
            opts, args = getopt.getopt(argv, short_options, long_options)
        except getopt.GetoptError:
            # Display an error message if the arguments are invalid
            print("Invalid arguments. Usage: " + sys.argv[0] + " -f <file name> -r <input folder> -o <output folder> -c <password for tar.gz archive>")
            sys.exit(2)

        # Process the parsed options and arguments
        self.compress = ""
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                # Display the usage instructions
                print("Usage: " + sys.argv[0] + " -f <file name> -r <folder> -o <output folder> -c <password for tar.gz archive>")
                sys.exit()
            elif opt in ("-f", "--file"):
                # Store the file name value
                self.file = arg[1:]
            elif opt in ("-r", "--recursive"):
                # Store the folder input value
                self.folderin = arg[1:] + "/"
            elif opt in ("-o", "--output"):
                # Store the folder output value
                self.folderout = arg[1:] + "/"
            elif opt in ("-c", "--compress"):
                # Store the compress value
                self.compress = arg[1:]
            elif opt in ("-d", "--debug"):
                # Store the compress value
                self.debug = True
        
    # Call the function with the command-line arguments
    # process_arguments(sys.argv[1:])
