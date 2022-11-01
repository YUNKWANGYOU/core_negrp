Gmail	유윤광 <1996yyk@gmail.com>
(제목 없음)
유윤광님(Yuns) <yuns@sk.com>	2022년 10월 23일 오전 3:23
받는사람: "1996yyk@gmail.com" <1996yyk@gmail.com>
#!/bin/bash

 

# Legacy EPC temperature query

# Test Ver : RHEL 7.1

# 2019-09-05 jungki.kim@sk.com

 

source /home/cnems/.bash_profile

sysList='MME_01 MME_02 MME_06 MME_10'

#sysList='MME_01'

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

        :> "${logDir}/${sysName}.cur"

        sysType=$(echo "$sysName" | awk -F'_' '{print "Legacy_"$1}')

        (/usr/bin/timeout --foreground 5 cmd "$sysName" RTRV-TEMP-STS;) |\

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
