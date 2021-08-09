

import argparse                         # Python Standard Library - Parser for command-line options, arguments
import sys                              # Allows python to interact with system
import os                               # So we can get to the OS on the computer for stuff
from prettytable import PrettyTable     # To create a pretty table

from regipy.registry import RegistryHive # Python library to convert offline registry files to readable format 


if len(sys.argv) !=2:
    print("Please enter one file path as command line argument")
    exit(1)                                             #exits with an error code of 1 to indicate not being run correctly

hiveFile = sys.argv[1]                                   #A list of command line arguments, and used to have user input data into program

#Need to argparse this so that the user can input which file they want 


reg = RegistryHive(hiveFile)

# Iterate over a registry hive recursively:
for entry in reg.recurse_subkeys(as_json=True):
    print(entry)

## Iterate over a key and get all subkeys and their modification time:
#for sk in reg.get_key('Software').get_subkeys():
    #print(sk.name, convert_wintime(sk.header.last_modified).isoformat())

## Get values from a specific registry key:
#reg.get_key('Software\Microsoft\Internet Explorer\BrowserEmulation').get_values(as_json=True)

## Use plugins:
#from regipy.plugins.ntuser.ntuser_persistence import NTUserPersistencePlugin
#NTUserPersistencePlugin(reg, as_json=True).run()

## Run all supported plugins on a registry hive:
#run_relevant_plugins(reg, as_json=True)