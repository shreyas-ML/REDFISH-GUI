
from flask import Flask, redirect, url_for, render_template, request
from functools import wraps
import os,string
import subprocess, re
from subprocess import run
import sys


app = Flask(__name__)

@app.route("/index",methods = ['POST', 'GET'])
def home():    
    return render_template("index.html")




@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        #result = request.form

        reqdict = {
        "URI" : request.form['host'],
        "Uname" : request.form['uname'],
        "PW" : request.form['Password'],
        "api" : request.form.get('API')
        }
        apidict = {
        "get_lan_config" : "rf_get_lanconfig.py",
        "list_sensors" : "rf_newsensors_list.py",
        "BMC_info" : "rf_get_bmc_info.py",
        "SEL_Logs" : "rf_logs.py",
        "PSU_FW" : "rf_get_psu_fw_ver.py",
        "Monitor" : "rf_UI_monitor.py",
        "Memory" : "rf_memory.py"
        }
        a = reqdict['api']
        x = apidict[a]
        script = " " 
        data = " TEST "
        if a == "SEL_Logs":
            script = script + x + " -u " + reqdict['Uname'] + " -p " + reqdict['PW'] + " -r " + "https://" + reqdict['URI'] + " --log SEL"
            
        else:
            script = script + x + " -u " + reqdict['Uname'] + " -p " + reqdict['PW'] + " -r " + "https://" + reqdict['URI']
            print(script)

        output = subprocess.check_output(script, shell=True,stderr=subprocess.STDOUT,env=dict(os.environ, COLUMNS='200'))
    
        data = output.decode()
        file = open("output.txt","w")
        file.write(data)
        file.close()

        #lines_list = open('output.txt').read().splitlines()

        return render_template("result.html",data=data)

    return render_template("index.html")






if __name__ == "__main__":
    app.run(debug = True)
