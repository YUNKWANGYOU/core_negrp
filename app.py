# ------------------------- *
# Code By Yuns              |
# SK Telecom Core Operator  |
# Date : 2022 09            |
# ------------------------- *

from glob import glob
from flask import Flask, render_template, jsonify
from flask import request
import plotly.figure_factory as ff 
import plotly
import json
import numpy as np
import pandas as pd
import sys
import os

from NetworkGraphHandler import NetworkGraphHandler
import ErrPointHandler
import DBHandler


app = Flask(__name__) 
e = ErrPointHandler.ErrPointHandler()
ip_route = e.df[e.sheet[0]] 
sellist = []
result = []

#----- App. Route -----#
@app.route("/index")
def index():
    negrp = generate_graph() 
    return render_template("index.html",plot=negrp)

@app.route("/updatelist",methods=['get','post'])
def get_sellist():
    global sellist
    updatelist = sellist
    return json.dumps(updatelist)

@app.route("/test",methods=['get','post'])
def coreip_api():
    global sellist
    set_errpoint()
    return render_template('test.html',source=e.source_json,destination=e.destination_json,result=e.res)

@app.route("/test/data",methods=['get','post'])
def post2():
    global sellist
    if request.method == 'POST':
        cal_errpoint(sellist)
        sellist = []
    return render_template('post.html')

@app.route("/test/add",methods=['get','post'])
def post3():
    global sellist
    if request.method == 'POST':
        tmp = request.get_json(silent=True)
        sellist.append(tmp[0])
        print("가져온 목록 아래 첨부")
        print(sellist)
    return render_template('test.html')

@app.route("/test/delete",methods=['get','post'])
def post4():
    global sellist
    if request.method == 'POST':
        tmp = request.get_json(silent=True)
        print(tmp)
        for i in tmp :
            if i in sellist :
                sellist.pop(sellist.index(i))
        
        # print(sellist)
    return render_template('post.html')

#----- Function -----#
def generate_graph():
    negrp = NetworkGraphHandler()
    negrp.generate_edges()
    negrp.trace_edges()
    negrp.generate_nodes()
    negrp.trace_nodes()
    negrp.make_connection()
    negrp.make_figure()
    
    graphJSON = json.dumps(negrp. fig,cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def set_errpoint():
    e.print_sheets()
    e.generate_sd_list(ip_route)
    # e.merge_sd(ip_route)
    # e.save_sd_list()

def cal_errpoint(value):
    e.print_columns(ip_route)
    sys.stdout.write('\n\n')
    e.put_err_route(value)
    e.print_err_route()
    e.err_ip_mapping(ip_route)
    sys.stdout.write('\n')
    e.cal_point()
    e.save_cal_point()

if __name__=="__main__" :
    print("* --------------------------- *")
    print("| SK Telecom Core Operator    |")
    print("| Code By : Yuns              |")
    print("| Data : 2022.09              |")
    print("|                             |")
    print("|       'Hello, I'm Yuns'     |")
    print("|                             |")
    print("* --------------------------- *")
    app.run(debug=True,port=5000)
