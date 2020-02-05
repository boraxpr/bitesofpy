#!/usr/bin/env bash
FILE1=$1
unzip ${FILE1}".zip" -d ${FILE1}
rm ${FILE1}".zip"