#!/bin/bash
echo 'Generating up to date html file. Will remove old file if it exists.'
echo ''
#rm -rf ../MandelbrotSet/MandelbrotSet.html

jupyter nbconvert --to html ../MandelbrotSet/MandelbrotSet.ipynb
echo ''
echo 'Conversion complete!'
