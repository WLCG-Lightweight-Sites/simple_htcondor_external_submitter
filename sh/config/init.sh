#!/bin/bash

echo "----------------------------------"
echo "Initializing HTCondor SCHEDD"
echo "----------------------------------"
cp $SIMPLE_CONFIG_DIR/config/50PC.conf $HTCONDOR_CONFIG_DIR/config.d/50PC.conf


echo "----------------------------------"
echo "Starting daemons"
echo "----------------------------------"
echo "Starting HTCondor"
systemctl start condor
echo "Starting crond"
systemctl start crond
echo "Starting fetch-crl-cron"
systemctl start fetch-crl-cron

echo "----------------------------------"
echo "Creating sleep job for condor_user"
echo "----------------------------------"
cp -r $SIMPLE_CONFIG_DIR/config/sleep_job /home/condor_user/sleep_job
chown -R condor_user /home/condor_user/sleep_job
mkdir /home/condor_user/.globus
cp -r $SIMPLE_CONFIG_DIR/config/user* /home/condor_user/.globus
chown -R condor_user /home/condor_user/.globus

echo "Initialization Complete!"