#!/usr/bin/env bash

##This script is run after TestSuiteRunner. It removes the old lcov files and recreates the lcov files
cd /home/tasu/Mozilla/mozilla-central/
cd objdir
find . -name jchuff.gcda -delete
lcov -c -d . -o coverage.info
genhtml -o coverage coverage.info
echo "Resetting to Directory"
cd cd /home/tasu/Dropbox/MasterThesis/Dev\ Code/TimeSortcode/