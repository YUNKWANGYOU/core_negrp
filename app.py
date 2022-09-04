from flask import Flask, render_template
from NetworkGraphHandler import NetworkGraphHandler
import plotly.figure_factory as ff 
import plotly
import json
import numpy as np
import pandas as pd
import ErrPointHandler
import DBHandler
import sys


app = Flask(__name__) 

@app.route("/")
def index():
    negrp = generate_graph() 
    return render_template("index.html",plot=negrp)

def generate_graph():
    negrp = NetworkGraphHandler()
    negrp.generate_edges()
    negrp.trace_edges()
    negrp.generate_nodes()
    negrp.trace_nodes()
    negrp.make_connection()
    negrp.make_figure()
    
    graphJSON = json.dumps(negrp.fig,cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__=="__main__" :
    e = ErrPointHandler.ErrPointHandler()
    e.print_sheets()
    ip_route = e.df[e.sheet[3]]
    e.print_columns(ip_route)
    
    sys.stdout.write('\n\n')
    e.put_err_route()
    e.print_err_route()
    e.err_ip_mapping(ip_route)
    
    sys.stdout.write('\n')
    e.cal_point()
    e.save_cal_point()
    
    # app.run(debug=True)