#!/usr/bin/env python

#Imports
from flask import Flask, render_template, request, redirect
import os
import subprocess

#Globals
app = Flask(__name__);
fileName = None
#Used to hold imagePath data

@app.route('/')
def main():
    return render_template("index.html", output="Nothing currently")

@app.route('/success', methods = ['POST'])
def success():
    global fileName
    if request.method == 'POST':    
        f = request.files['image']
        fileName = f.filename
        f.save(fileName)
        return render_template("runstego.html", filename=fileName);
    
@app.route('/runstego', methods = ['POST'])
def runstego():
    global fileName
    with open("stdout.txt","wb") as out, open("stderr.txt","wb") as err:
        command = os.popen('bash /opt/scripts/check_jpg.sh /opt/webstego/{0} | tee /data/testing.output'.format(fileName))
        out = command.read().split('\n')
        return render_template("runstego.html", filename=fileName, output=out)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')