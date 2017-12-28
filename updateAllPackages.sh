#!/bin/bash
echo 'Updating Packages...'
echo ''
pip freeze | sed s/==// | sed s/[0-9][0-9]*//g | sed s/[.]//g
