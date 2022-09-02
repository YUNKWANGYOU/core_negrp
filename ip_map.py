import pandas
import sys
from collections import Counter

filename = "220820_코어_IP_맵.xlsx"
hop = ['one','two','three','four','five',
       'six','seven','eight','nine']

class ErrPointHandler():
    
    def __init__(self):
        self.df=''
        self.err_sd = []
        self.df = pandas.read_excel(filename, sheet_name=None)
        self.sheet = list(self.df.keys())
    
    def print_sheets(self):
        sys.stdout.write("\n* Sheet 목록 : ")
        for i in self.sheet : 
            sys.stdout.write('['+i+']')
    
    
    # 연동 에러 쉬트와 IP Route 쉬트 표준화 필요
    # Ex ) SPGW#155 -> NSA_SPGW 
    def err_route(self):
        self.err_list = []
        
        sys.stdout.write("에러 구간을 입력해 주세요. ( 종료하고 싶으시면 Ctrl + C 를 입력하세요. )\n\n")
        try :
            while 1 : 
                a = input()
                self.err_list.append(a)
                    
        except KeyboardInterrupt :
            print("\n\n에러 구간 입력이 종료되었습니다.")
    
    def print_err_route(self):
        sys.stdout.write("\n에러 구간 확인 : \n" )
        tmp = []
        for i in self.err_list :
            j = i.split()
            tmp.append(j)
            print(j[0] + " -> " + j[1])
        self.err_list = tmp
        
    def print_columns(self,sheet) :
        sys.stdout.write("\n* 현재 Sheet 컬럼명 : / ")
        for i in sheet : 
            sys.stdout.write(i + ' / ')
    
    def err_ip_mapping(self,ip_route) : 
        self.ip_err = []
        for i in self.err_list :
            condition = (ip_route.source == i[0]) & (ip_route.destination == i[1])
            self.ip_err.append(ip_route[condition])
        
    
    def cal_point(self) :
        res = []
        for i in self.ip_err : 
            for j in hop :
                for k in i[j].values:
                    res.append(k)
        res = dict(sorted(dict(Counter(res)).items(),key= lambda x: -x[1]))
        del res['-']
        
        sys.stdout.write("* 장비별 에러 발생 횟수 *\n")
        for key,value in res.items() : 
            print(key,value)
        # for i in hop :
        #     print(self.ip_err[i])
if __name__=="__main__" : 
    
    e = ErrPointHandler()
    e.print_sheets()
    ip_route = e.df[e.sheet[3]]
    e.print_columns(ip_route)
    sys.stdout.write('\n\n')
    
    e.err_route()
    e.print_err_route()
    # print(ip_route.iloc[0])
    # err_route에 해당하는 ip_route mapping 하여 불러오기
    e.err_ip_mapping(ip_route)
    sys.stdout.write('\n')
    e.cal_point()