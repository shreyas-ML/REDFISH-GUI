import cssutils
from flask import Flask, redirect, url_for, render_template, request
from functools import wraps
import os,string
import subprocess, re
from subprocess import run


app = Flask(__name__)

@app.route("/index",methods = ['POST', 'GET'])
def home():    
    if request.method == 'POST':
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
        "Monitor" : "rf_monitor.py"
        }
        a = reqdict['api']
        x = apidict[a]
        script = " " 
        if a == "SEL_Logs":
            script = script + x + " -u " + reqdict['Uname'] + " -p " + reqdict['PW'] + " -r " + "https://" + reqdict['URI'] + " --log SEL"
        else:
            script = script + x + " -u " + reqdict['Uname'] + " -p " + reqdict['PW'] + " -r " + "https://" + reqdict['URI']
        print(script)

        output = subprocess.check_output(script, shell=True,stderr=subprocess.STDOUT, env=dict(os.environ, COLUMNS='100'))
    
        data = output.decode()
        file = open("output.txt","w")
        file.write(data)
        file.close()

        
        #return f"<div style=\"width:1200px;overflow:auto\" font-size:150px><pre>{data}</pre></div>"  
        #return f"<div class=\"output\"><pre>{data}</pre></div>"
        return redirect(url_for('result',data=data)) 
        

       


    return render_template("index.html")


@app.route('/result')
def result():
    data = request.form.get('data',None)
    print(data)
    return render_template("result.html",data=data)
  


if __name__ == "__main__":
    app.run(debug = True)
