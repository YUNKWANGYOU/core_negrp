#!/bin/bash

sysList='MME_01 MME_02 MME_06 MME_10'
logDir='/home/cnems/SSNOC'
errLog="$logDir/errLog.log"
tgtServer='60.11.64.13/10003'
clearTime='0300'
currentTime=$(date +"%H%M")

function chkFile {
        if [ -e "$1" ] && [ -s "$1" ] ; then echo "T" ; else echo "F" ; fi
}

for sysName in $sysList
do




#while read line
#do echo $line
	
#done <	res_net1.log

