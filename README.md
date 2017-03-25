# UPHUB
Replaces screenshots taken by Hubstaff, on custom screenshots taken from your collection folder in real time

# Usage
### create_collection.py
Creates a collection folder with screenshots and thumbnails from the target folder with custom screenshots.

Installing dependencies:
```
pip install -r requirements.txt
```

Flags:
- **-c** - path to the collection folder where the collection will be created (by default *collection*)
- **-t** - path to the folder with custom screenshots (by default *temp*)
- **-s** - size of a thumbnail (by default *256x144*)

Example:
```
python create_collection.py -c /path/to/collection/ -t /path/to/temp/ -s 256x144
```

### uphub.ps1

Replaces screenshots taken by Hubstaff, on custom screenshots taken from your collection folder in real time.

Variables:

- **$path_to_hscreen** - path to folder in which Hubstaff saves screenshots
- **$pat_to_gallery** - path to the folder created with *create_collection.py*

### one_line_uphub.ps1
same as *uphub.ps1* can be run as a shell command in the PowerShell terminal
