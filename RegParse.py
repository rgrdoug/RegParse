

import argparse                         # Python Standard Library - Parser for command-line options, arguments
import sys                              # Allows python to interact with system
import os                               # So we can get to the OS on the computer for stuff
from prettytable import PrettyTable     # To create a pretty table

from regipy.registry import RegistryHive # Python library to convert offline registry files to readable format 

class RegParser: 
    def __init__(self, hiveFilePath, regFolder):
        self.hiveFilePath = hiveFilePath
        self.regFolder = regFolder
        self.keyPaths = []
        self.parseHiveFile()
        
    def parseHiveFile(self):
        with open(self.hiveFilePath, 'r') as hiveFile:
            for line in hiveFile:
                self.keyPaths.append(line.strip())
                
    def parse(self):
        pass
    
    
        
        
def main():
    if len(sys.argv) !=3:
        print("Usage: python RegParse.py hiveFilePath regFolder")
        print("\t hiveFilePath: ")                          #
        print("\t regFolder: ")
        exit(1)                                             #exits with an error code of 1 to indicate not being run correctly
    hiveFilePath = sys.argv[1]                                  #A list of command line arguments, and used to have user input data into program
    regFolder = sys.argv[2]
     
    regParser = RegParser(hiveFilePath, regFolder)
    regParser.parse()
    
    print(regParser.regFolder)
    print(regParser.hiveFilePath)    
    
    
if __name__ == "__main__":
    main()

