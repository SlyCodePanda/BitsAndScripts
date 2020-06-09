#!/bin/bash

# UN-FINISHED

# Get all the sub directories that have a 'trunk' dir inside them.
subDirs=$(find . -maxdepth 2 -type d | grep "./*/trunk")
echo $subDirs

# Make sure these directories are working subversion copies.
for dir in subDirs
do
  svn status --depth=empty $dir
done
