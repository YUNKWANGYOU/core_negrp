#!/bin/bash

chkNet.sh
chkTracer.sh

sysList='MME_01 MME_02 MME_06 MME_10'
logDir='/home/cnems/SSNOC'
errLog="$logDir/errLog.log"
tgtServer='60.11.64.13/10003'
clearTime='0300'
currentTime=$(date +"%H%M")

function chkFile {
        if [ -e "$1" ] && [ -s "$1" ] ; then echo "T" ; else echo "F" ; fi
};

cnt=0

for sysName in $sysList
do
        while read line
        do
                if [ "${cnt}" == 0 ]
                then
                        cmd "$sysName" TEST-TRC-ROUTE:DIP="$line"; > res_main_${sysName}.log
                        (( cnt = "${cnt}" + 1 ))

                else
			cmd "$sysName" TEST-TRC-ROUTE:DIP="$line"; >> res_main_${sysName}.log

		fi

        done < res_net_${sysName}.log
done


