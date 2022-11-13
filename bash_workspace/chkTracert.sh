#!/bin/bash

# Save Trace Route
# Test Ver : RHEL 8.2
# 2022-10-23 yuns@sktelecom.com

# mkdir /home/cnems/tracert

# crontab -e
# 0 3 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31 * /home/cnems/SSNOC/tracert/chkErrpoint.sh

sysList=(MME_01)
logDir='/home/cnems/SSNOC/tracert'
errLog="$logDir/errLog_tracert.log"
targetServer='*.*.*.*/*'

# sysList에 속한 장비들의 RTRV-NE-STS; 수행하여 input1_${sysList[@]}.log로 저장하기
for sysName in "${sysList[@]}"1
do
        # 실제 CN_EMS에서는 아래 주석처리 된 두 줄의 커맨드 이용 예정
        echo "cmd ${sysName} RTRV-NE-STS;" 
        # $(cmd ${sysName} RTRV-NE-STS;) > /home/cnems/tracert/input_${sysName}.log
done

# 변수 선언
declare -a priList
declare -a secList

cnt=0

# RTRV-NE-STS; 결과 중 172. 또는 10.을 포함하는 연동 정보 가져오기
for sysName in "${sysList[@]}"
do
        priList[$cnt]=$(awk '$2 ~ /\./ { print $2 }' input_${sysName}.log)
        secList[$cnt]=$(awk '$3 ~ /\./ { print $3 }' input_${sysName}.log)

        # 합치기
        targetList[$cnt]="$priList $secList"

        (( cnt = "${cnt}" + 1 ))
done

# 연동 IP 정보를 이용하여 TEST-TRC-ROUTE를 날리고 해당 결과를 res_$i_$netName.log 에 저장
for i in $(seq $cnt)
do      
        (( i = "${i}" - 1 ))

        echo
        for targetIP in ${targetList[$i]}
        do
                # 실제 CN_EMS에서는 아래 주석처리 된 두 줄의 커맨드 이용 예정
                echo "cmd ${sysList[$i]} TEST-TRC-ROUTE:DIP=$targetIP;" 
                # $(cmd ${sysList[$i]} TEST-TRC-ROUTE:DIP=$netName;) > res_$i_$netName.log
        done
done


