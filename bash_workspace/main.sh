#!/bin/bash


sysList='MME_01 MME_02 MME_06 MME_10'
logDir='/home/cnems/SSNOC'
errLog="$logDir/errLog.log"
tgtServer='60.11.64.13/10003'
clearTime='0300'
currentTime=$(date +"%H%M")

function chkFile {
        if [ -e "$1" ] && [ -s "$1" ] ; then echo "T" ; else echo "F" ; fi
};

for sysName in $sysList
do
	tmp_${sysName}=`awk '/172\./' input1_${sysName}.log`
	tmp_${sysName}=`awk '/10\./' input1_${sysName}.log`
#	awk '$3 ~ /172\./{ print $3 } ' tmp_${sysName}.log > res_net_${sysName}.log
#	awk '$2 ~ /172\./{ print $2 } ' tmp_${sysName}.log >> res_net_${sysName}.log
#	awk '$3 ~ /10\./{ print $3 } ' tmp_${sysName}.log >> res_net_${sysName}.log
#	awk '$2 ~ /10\./{ print $2 } ' tmp_${sysName}.log >> res_net_${sysName}.log
	echo ${tmp_${sysName}}
done

#cnt=0

#for sysName in $sysList
#do
#	while read line
#	do
#		if [ "${cnt}" == 0 ]
#		then
#			echo 'cmd '${sysName}' TEST-TRC-ROUTE:DIP='$line';' > res_tracert_${sysName}.log
#			(( cnt = "${cnt}" + 1 ))	
#		else
#			echo 'cmd '${sysName}' TEST-TRC-ROUTE:DIP='$line';' >> res_tracert_${sysName}.log
#		fi
#	done < res_net_${sysName}.log
#done

#cnt=0

#for sysName in $sysList
#do
#        while read line
#        do
#                if [ "${cnt}" == 0 ]
#                then
#                        cmd "$sysName" TEST-TRC-ROUTE:DIP="$line"; > res_main_${sysName}.log
#                        (( cnt = "${cnt}" + 1 ))
#                else
#			cmd "$sysName" TEST-TRC-ROUTE:DIP="$line"; >> res_main_${sysName}.log
#		fi
#        done < res_net_${sysName}.log
#done


