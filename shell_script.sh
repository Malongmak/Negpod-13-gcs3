#!/bin/bash

if [ -e "$1" ]; then
  if [ -s "$1" ]; then
    echo "0"
  else
    echo "1"
  fi
else
  echo "2"
fi

#to check any file run "bash shell_script [file name]"
