#!/usr/bin/env bash

# move up one directory
# search for other common directories
# copy files into them
PROJ_DIR="./common"

cd ..
commons=$(find . -type d -name "common")
for d in $commons; do
  if [ "$d" != "$PROJ_DIR" ]; then
    cp -vf ${PROJ_DIR}/app/* $d
  fi
done

