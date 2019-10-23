#!/bin/bash

echo "----------------------------------"
echo "Initializing HTCondor SCHEDD"
echo "----------------------------------"
cp $SIMPLE_CONFIG_DIR/config/50_PC.conf $HTCONDOR_CONFIG_DIR/config.d/50PC.conf


echo "----------------------------------"
echo "Starting daemons"
echo "----------------------------------"
echo "Starting HTCondor"
systemctl start condor
echo "Starting crond"
systemctl start crond

echo "Initialization Complete!"