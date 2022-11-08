#!/bin/bash

# Check the Network Access Fail Information
# Test Ver : RHEL 7.1
# 2022-10-23 yuns@sktelecom.com

sysList=(MME_01 MME_02 MME_06 MME_10)
logDir='/home/cnems/SSNOC'
errLog="$logDir/errLog.log"
tgtServer=''
clearTime='0300'
currentTime=$(date +"%H%M")

<<<<<<< HEAD
=======
# sysList에 속한 장비들의 RTRV-NE-STS; 수행하여 input1_${sysList[@]}.log로 저장하기
for sysName in "${sysList[@]}"
do
        # 실제 CN_EMS에서는 아래 주석처리 된 두 줄의 커맨드 이용 예정
        echo "cmd ${sysName} RTRV-NE-STS;" 
        # input_tmp=$(cmd ${sysName} RTRV-NE-STS;)
        # echo $input_tmp > input1_${sysName}_bk.log
done

# 변수 선언
>>>>>>> 21d180df3b2d31336465a80835aee113a5d88c64
declare -a priList_1
declare -a priList_2
declare -a secList_1
declare -a secList_2

cnt=0

# RTRV-NE-STS; 결과 중 172. 또는 10.을 포함하는 연동 정보 가져오기
for sysName in "${sysList[@]}"
do
        priList_1[$cnt]=$(awk '$3 ~ /172\./{ print $3 } ' input1_${sysName}.log)
        priList_2[$cnt]=$(awk '$3 ~ /10\./{ print $3 } ' input1_${sysName}.log)
        secList_1[$cnt]=$(awk '$2 ~ /172\./{ print $2 } ' input1_${sysName}.log)
        secList_2[$cnt]=$(awk '$2 ~ /10\./{ print $2 } ' input1_${sysName}.log)

        # 합치기
        netList[$cnt]="$priList_1 $priList_2 $secList_1 $secList_2"

        (( cnt = "${cnt}" + 1 ))
done

# echo ${netList[1]}

# 연동 IP 정보를 이용하여 TEST-TRC-ROUTE를 날리고 해당 결과를 res_$i_$netName.log 에 저장
for i in $(seq $cnt)
do      
        (( i = "${i}" - 1 ))

        echo
        for netName in ${netList[$i]}
        do
                # 실제 CN_EMS에서는 아래 주석처리 된 두 줄의 커맨드 이용 예정
                echo "cmd ${sysList[$i]} TEST-TRC-ROUTE:DIP=$netName;" 
                # res_tmp=$(cmd ${sysList[$i]} TEST-TRC-ROUTE:DIP=$netName;)
                # echo $res_tmp > res_$i_$netName.log
        done
done


