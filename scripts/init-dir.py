# author: @kodedile
# ---
# Call this script from the root directory
#   python script/init-dir.py
# ---
# Initializes folders for each of the dungeons 
# and for each of the paths as provided 
# in the associated game's tsv files
# ---


import os
import csv


# init directory names

dir_game = input("Which game directory? (default: 'Boktai 1') ")
if dir_game == "":
    dir_game = 'Boktai 1'


# init tsv filenames
tsv_dungeons = 'data/' + dir_game + '/dungeons.tsv';
tsv_paths = 'data/' + dir_game + '/paths.tsv';


# ask if we should separate folders into map areas
separate = ""
while not separate.strip():
    separate = input("Group each folder by map area? [y/n] ")
if separate.strip().lower() == "y":
    separate = True
else:
    separate = False


# init directories

dungeons = '/Dungeons'
paths = '/Paths'

dir_dungeons = dir_game + dungeons
dir_paths = dir_game + paths

# init these to be the same as without field group
dir_dungeons_field = dir_dungeons
dir_paths_field = dir_paths


# init row counter
count = 0

# initialize folders for each dungeon
with open(tsv_dungeons, 'r', encoding='utf8') as data:
    data = csv.reader(data, delimiter='\t')
    for row in data:
        # skip first row
        if count > 0:
            name = row[0] + ' - ' + row[4]
            
            # setup field directory if requested
            field = ""
            if separate:
                field = '/Field ' + row[2]
                dir_dungeons_field = dir_game + field + dungeons
                
                if not os.path.exists(dir_game + field):
                    os.mkdir(dir_game + field)
            
            # initialize containing directory
            if not os.path.exists(dir_dungeons_field):
                os.mkdir(dir_dungeons_field)
            
            # setup dungeon directory
            if not os.path.exists(dir_dungeons_field + '/' + name):
                os.mkdir(dir_dungeons_field + '/' + name)
            
            # gitkeep
            outfile = dir_dungeons_field + '/' + name + '/.gitkeep'
            print(outfile)
            if not os.path.exists(outfile):
                with open(outfile, 'w') as fp:
                    pass
            
        count += 1


# reset row counter
count = 0

# initialize folders for each pathway
with open(tsv_paths, 'r', encoding='utf8') as data:
    data = csv.reader(data, delimiter='\t')
    for row in data:
        # skip first row
        if count > 0:
            name = row[0] + ' - ' + row[2]
            
            # setup field directory if requested
            field = ""
            if separate:
                field = '/Field ' + row[1]
                dir_paths_field = dir_game + field + paths
                
                if not os.path.exists(dir_game + field):
                    os.mkdir(dir_game + field)
            
            # initialize containing directory
            if not os.path.exists(dir_paths_field):
                os.mkdir(dir_paths_field)
            
            # setup pathway directory
            if not os.path.exists(dir_paths_field + '/' + name):
                os.mkdir(dir_paths_field + '/' + name)
            
            # gitkeep
            outfile = dir_paths_field + '/' + name + '/.gitkeep'
            print(outfile)
            if not os.path.exists(outfile):
                with open(outfile, 'w') as fp:
                    pass
            
        count += 1