#!/bin/bash

# Check the Network Connection Information
# Test Ver : RHEL 7.1
# 2022-10-23 yuns@sktelecom.com

# source /home/cnems/.bash_profile

# sysList='MME_01 MME_02 MME_06 MME_10'
# logDir='/home/cnems/SSNOC'

# To Do ( 150 -> 60 Network )
# tgtServer='*.*.*.*'
# clearTime='0300'
# currentTime=$(date +"%H%M")

#function chkFile {
#        if [ -e "$1" ] && [ -s "$1" ] ; then echo "T" ; else echo "F" ; fi
#}

#for sysName in $sysList
#do

#done

awk '/172\./' input1_1.log > tmp1.log
awk '/10\./' input1_2.log >> tmp1.log
awk '$3 ~ /172\./{ print $3 } ' tmp1.log > res_net1.log
awk '$2 ~ /172\./{ print $2 } ' tmp1.log >> res_net1.log
awk '$3 ~ /10\./{ print $3 } ' tmp1.log >> res_net1.log
awk '$2 ~ /10\./{ print $2 } ' tmp1.log >> res_net1.log

