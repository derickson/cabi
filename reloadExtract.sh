#!/bin/sh

#./CapitalbikeshareData/small

# $1 is directory (no final slash)
# $2 is _index
# $3 is _type

echo "about to load: "
find $1 -type f -exec echo {}  \;

echo "loading all your files with curl"

find $1 -type f -exec curl -s -XPUT http://localhost:9200/$2/$3/_bulk --data-binary @{} > /dev/null \;

echo "Done. Done."
