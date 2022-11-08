#!/bin/bash

<<<<<<< HEAD
=======
# Check the Network Access Fail Information
# Test Ver : RHEL 7.1
# 2022-10-23 yuns@sktelecom.com
>>>>>>> 1ae3540b2d276d689f0abaf6831cb7905ee9b79f

sysList='MME_01 MME_02 MME_06 MME_10'
logDir='/home/cnems/SSNOC'
errLog="$logDir/errLog.log"
tgtServer=''
clearTime='0300'
currentTime=$(date +"%H%M")

<<<<<<< HEAD
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
=======
declare -a priList_1
declare -a priList_2
declare -a secList_1
declare -a secList_2
cnt=0

for sysName in $sysList
do
        priList_1[$cnt]=$(awk '$3 ~ /172\./{ print $3 } ' input1_${sysName}.log)
        priList_2[$cnt]=$(awk '$3 ~ /10\./{ print $3 } ' input1_${sysName}.log)
        secList_1[$cnt]=$(awk '$2 ~ /172\./{ print $2 } ' input1_${sysName}.log)
        secList_2[$cnt]=$(awk '$2 ~ /10\./{ print $2 } ' input1_${sysName}.log)

        netList="$priList_1\n$priList_2\n$secList_1\n$secList_2"
        
        (( cnt = "${cnt}" + 1 ))
done

echo -e "$netList"

# chkTracer.sh

# cnt=0

# for sysName in $sysList
# do
#         while read line
#         do
#                 if [ "${cnt}" == 0 ]
#                 then
#                         cmd "$sysName" TEST-TRC-ROUTE:DIP="$line"; > res_main_${sysName}.log
#                         (( cnt = "${cnt}" + 1 ))

#                 else
# 			cmd "$sysName" TEST-TRC-ROUTE:DIP="$line"; >> res_main_${sysName}.log

# 		fi

#         done < res_net_${sysName}.log
# done
>>>>>>> 1ae3540b2d276d689f0abaf6831cb7905ee9b79f


