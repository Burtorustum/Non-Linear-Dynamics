#!/bin/bash
echo ''
echo 'Generating up to date html file. Will remove old file if it exists.'
echo ''
rm ../MandelbrotSet/MandelbrotSet.html
jupyter nbconvert --to html ../MandelbrotSet/MandelbrotSet.ipynb
echo ''
echo 'Conversion complete!'
exit
