#!/bin/bash

if [ $# -eq 0 ]; then
    cd build
    pyinstaller -F -w "../src/main.py"
    cd ..
elif [ "$1" = "clean" ]; then
    rm -rf build
else
    echo "Invalid argument. Usage: ./build.sh [clean]"
fi
