#!/usr/bin/env bash

##This script is run after TestSuiteRunner. It removes the old lcov files and recreates the lcov files
cd /home/satabdi/mozilla-central/
find . -name jchuff.gcda -delete
lcov -c -d . -o coverage.info
genhtml -o coverage coverage.info
echo "Resetting to Directory"
cd /home/satabdi/Dropbox/MasterThesis/Dev\ Code/DevCode/Application_FireFox