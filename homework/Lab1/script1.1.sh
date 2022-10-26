#!/bin/bash

grep --include=\*.{c,h} -h 'linux' -e "dragons" -r > dragons.txt
