#!/bin/bash
pushd . > /dev/null

. Desktop/NonLinear_Dynamics/Shell/colorization.sh

echo ''
echo "${txtgrn}Ignore any errors produced by this... These are generated by packages not installed by pip3. Updating Python3 Packages...${txtrst}"
echo ''

a=`pip3 freeze | sed s/==// | sed s/[0-9][0-9]*//g | sed s/[.]//g`

for package in $a
do
  pip3 install $package --upgrade
  echo "${txtbld}${txtblu}----------${txtrst}"
done

echo ''
python3 --version
pip3 --version
echo ''
echo "${txtgrn}All done!${txtrst}"
echo ''

popd > /dev/null
exit
