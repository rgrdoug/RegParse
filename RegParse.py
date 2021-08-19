

import argparse                         # Python Standard Library - Parser for command-line options, arguments
import sys                              # Allows python to interact with system
import os                               # So we can get to the OS on the computer for stuff
from prettytable import PrettyTable     # To create a pretty table

from regipy.registry import RegistryHive # Python library to convert offline registry files to readable format 

class RegParser: 
    def __init__(self, hiveFilePath, regFile):
        self.hiveFilePath = hiveFilePath
        self.regFile = regFile
        self.keyPaths = []
        self.parseHiveFile()
        self.reg = RegistryHive(regFile)
          
    def parseHiveFile(self):
        with open(self.hiveFilePath, 'r') as hiveFile:
            for line in hiveFile:
                self.keyPaths.append(line.strip())
              
    def parse(self):
         
    # Iterate over a registry hive recursively:
       # for entry in self.reg.recurse_subkeys(as_json=True):
            #print(entry)
        
        regKey = reg.get_key('HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR').get_values(as_json=True)
        #strregKey = regKey.decode('ascii', 'ignore')
        #print(strregKey)
        print(type(regKey))
        
def main():
    if len(sys.argv) !=3:
        print("Usage: python RegParse.py hiveFilePath regFile")
        print("\t hiveFilePath: Text file containing paths to specific registry keys ")                          #
        print("\t regFile: Location of Windows Registry file ")
        exit(1)                                             #exits with an error code of 1 to indicate not being run correctly
    hiveFilePath = sys.argv[1]                                  #A list of command line arguments, and used to have user input data into program
    regFile = sys.argv[2]
     
    regParser = RegParser(hiveFilePath, regFile)
    regParser.parse()
    
    #print(regParser.regFile)
    #print(regParser.hiveFilePath)    
    
    
if __name__ == "__main__":
    main()

