#!/bin/bash

# Check the Network Connection Information
# Test Ver : RHEL 7.1
# 2022-10-23 yuns@sktelecom.com

source /home/cnems/.bash_profile

sysList='MME_01 MME_02 MME_06 MME_10'
logDir='/home/cnems/SSNOC'

# To Do ( 150 -> 60 Network )
tgtServer='*.*.*.*'
clearTime='0300'
currentTime=$(date +"%H%M")

function chkFile {
        if [ -e "$1" ] && [ -s "$1" ] ; then echo "T" ; else echo "F" ; fi
}

for sysName in $sysList
do
        :> "${logDir}/${sysName}.net"
        sysType=$(echo "$sysName" | awk -F'_' '{print "Legacy_"$1}')

        (/usr/bin/timeout --foreground 5 cmd "$sysName" RTRV-NE-STS;) |\

        awk -v d="$(date +'%Y-%m-%d %H:%M:%S')" -v s="$sysName" '$0~/^   LE|^                1 /{

                if(NF==4){

                        bd=$1;print d,s"_"$1,s"_"$1,"'$sysType'","CPU"$2,$3,"85"

                        }

                else{

                        print d,s"_"bd,s"_"bd,"'$sysType'","CPU"$1,$2,"85"

                }

        }' > "${logDir}/${sysName}.cur"

        if [ "$(chkFile "${logDir}/${sysName}.cur")" == "F" ]

        then

                echo "$(date +'%Y-%m-%d %H:%M:%S') [ERROR] file not exist - ${logDir}/${sysName}.cur" >> "$errLog"

                continue

        fi

        cat < "${logDir}/${sysName}.cur" > /dev/udp/"$tgtServer"

        sleep 1

done

 

if [ "$clearTime" == "$currentTime" ] && [ -e "$errLog" ]

then

        :> "$errLog"

fi
