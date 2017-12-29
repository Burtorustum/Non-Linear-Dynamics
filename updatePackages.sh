#!/bin/bash
echo 'Updating packages for NonLinear_Dynamics in Python3...'
echo ''
pip3 install pip-upgrader --upgrade
pip3 install pip --upgrade
pip3 install graphics.py --upgrade
pip3 install sympy --upgrade
pip3 install numpy --upgrade
pip3 install scipy --upgrade
pip3 install matplotlib --upgrade
echo ''
python3 --version
pip3 --version
echo ''
echo 'All done.'
