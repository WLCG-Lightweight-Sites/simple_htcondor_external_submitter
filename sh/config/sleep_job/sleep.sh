#!/bin/bash
# file name: sleep.sh

TIMETOWAIT="6"
echo "sleeping for $TIMETOWAIT seconds"
echo $(ls /cvmfs/alice.cern.ch)
echo $(hostname -f )
/bin/sleep $TIMETOWAIT