from flask import Flask, render_template
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
ip_route = e.df[e.sheet[3]] # C_TOTAL_IP별 

#----- App. Route -----#
@app.route("/index")
def index():
    negrp = generate_graph() 
    return render_template("index.html",plot=negrp)

@app.route("/errpoint",methods=['get','post'])
def errpoint():
    set_errpoint()
    negrp = generate_graph() 
    e.sd_merge = '//'.join([str(i) for i in list(e.sd_merge)])
    return render_template("errpoint.html",sd_merge=e.sd_merge,plot=negrp,result=e.res)

@app.route('/errpoint/data', methods=['GET','POST'])
def post():
    if request.method == 'POST':
        value = request.get_json(silent=True)
        res = cal_errpoint(value)
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
    e.merge_sd(ip_route)
    e.save_sd_list()

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
    app.run(debug=True,port=5000)
