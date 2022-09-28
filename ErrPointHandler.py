import pandas
import sys
from collections import Counter
import json 

filename = "CORE_IP.xlsx"

hop = ['HOP1','HOP2','HOP3','HOP4','HOP5','HOP6','HOP7','HOP8','HOP9']

# 고장 Point를 다루는 클래스
class ErrPointHandler():    
    def __init__(self):
        self.df=''
        self.err_sd = []
        self.df = pandas.read_excel(filename, sheet_name=None)
        self.sheet = list(self.df.keys())
        self.sd_list = []
        self.sd_merge = {'source':{},'destination':{}}
        self.res = []
        self.res_string = ''
        self.err_list = []
        
    # 엑셀 전체 sheet 목록 출력 기능
    def print_sheets(self):
        sys.stdout.write("\n* Sheet 목록 : ")
        for i in self.sheet : 
            sys.stdout.write('['+i+']')
    
    
    # 연동 에러 쉬트와 IP Route 쉬트 표준화 필요  ex) SPGW#155 -> NSA_SPGW 
    # 에러 구간 입력 기능
    def put_err_route(self,value):
        self.err_list = []
        for i in value :
            self.err_list.append(i.replace('<-> ',' '))
        self.err_list = list(set(self.err_list))
        print(self.err_list)
        
    # 에러 구간 프린트 기능
    def print_err_route(self):
        sys.stdout.write("\n에러 구간 확인 : \n" )
        tmp = []
        for i in self.err_list :
            j = i.split()
            tmp.append(j)
            print(j[0] + " -> " + j[1])
        self.err_list = tmp
    
    
    # sheet의 컬럼명 프린트 기능
    def print_columns(self,sheet) :
        sys.stdout.write("\n* 현재 Sheet 컬럼명 : / ")
        for i in sheet : 
            sys.stdout.write(i + ' / ')
    
    # 에러 s/d 과 기존의 IP 구간을 mapping하여
    # 에러 s/d 사이의 route를 mapping하는 기능
    def err_ip_mapping(self,ip_route) : 
        self.ip_err = []
        for i in self.err_list :
            condition = (ip_route.source == i[0]) & (ip_route.destination  == i[1])
            self.ip_err.append(ip_route[condition])
        
    # 에러 s/d기반으로 추출된 route에 해당하는 장비를 Count 순으로 나열 : 에러 Point 추출
    def cal_point(self) :
        self.res = []
        for i in self.ip_err : 
            for j in hop :
                for k in i[j].values:
                    self.res.append(k)
    
        self.res = dict(sorted(dict(Counter(self.res)).items(),key= lambda x: -x[1]))
        if '-' in self.res :
            del self.res['-']
        self.res_json = json.dumps(self.res)
        
        # for key,value in self.res.items() : 
        #     print(key,value)
        
    def save_cal_point(self) :
        self.res_dict = {"name" : self.res.keys(),"err_cnt" : self.res.values()}        
        self.res_df = pandas.DataFrame(self.res_dict)
        sys.stdout.write("* 장비별 에러 발생 횟수 *\n")
        print(self.res_df)
        self.res_df.to_csv("result/result.csv")
        
    def generate_sd_list(self,ip_route) : 
        self.sd_list = ip_route[['source','destination']]
        for idx,row in self.sd_list.iterrows() :
            self.sd_merge['source'][row['source']]=idx
            self.sd_merge['destination'][row['destination']]=idx

        self.source_json = json.dumps(self.sd_merge['source'])
        self.destination_json = json.dumps(self.sd_merge['destination'])
        
    def save_sd_list(self) :
        self.sd_list.to_json("result/result.json",orient='columns')
    
    def merge_sd(self,ip_route) :
        self.sd_merge = ip_route['source'] + "⇔" + ip_route['destination']
        self.sd_merge = set(self.sd_merge)
        self.sd_merge = list(self.sd_merge)
        
if __name__=="__main__" : 
    
    e = ErrPointHandler()
    e.print_sheets()
    ip_route = e.df[e.sheet[0]] 
    e.generate_sd_list(ip_route)
    # e.merge_sd(ip_route)
    # e.save_sd_list()
    # e.print_columns(ip_route)
    
    # sys.stdout.write('\n\n')
    # e.put_err_route()
    # e.print_err_route()
    # e.err_ip_mapping(ip_route)
    
    # sys.stdout.write('\n')
    # e.cal_point()
    # e.save_cal_point()