from flask import Flask, render_template, redirect, request

from Dobot import Dobot
from pdf import PDF
import asyncio
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.report import Report
from threading import Thread
import threading
from time import sleep

IP ="10.128.66.31"

PDF_WIDTH = 210
PDF_HEIGHT = 297
process = None

app = Flask(__name__)
header = []
engine = create_engine("sqlite+pysqlite:///reports.db", echo=True)
Session = sessionmaker(bind = engine)
session = Session()

Base.metadata.create_all(engine)

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/report')
def report():
    return render_template('report.html')

def routine():
    arm = Dobot(225, 3, 140, 0)
    arm.moveHome()
    arm.pickToggle()

    # #bandeja 1
    arm.moveArmXY(174, 222, 77, 51)

    arm.moveArmXY(265, 175, -11, 32)
    arm.moveArmXY(64, 169, -11, 67)
    arm.moveArmXY(276, 202, -11, 35)
    arm.moveArmXY(66, 195, -11, 69)
    arm.moveArmXY(268, 241, -11, 41)
    arm.moveArmXY(64, 271, -11, 75)
    arm.moveArmXY(260, 266, -11, 44)

    arm.moveArmXY(174, 222, 77, 51)
    
    # #bandeja 2
    arm.moveHome()
    arm.moveArmXY(325, -36, -8, -7)
    arm.rotateTool(-90)
    arm.moveArmXY(181, -18, -8, -6)
    arm.moveArmXY(313, 52, -8, 8)
    arm.rotateTool(-80)
    arm.moveArmXY(177, 43, -8, 12)
    arm.moveHome()

    # #bandeja 3
    arm.moveArmXY(185, -229, 77, -51)
    arm.moveArmXY(185, -229, -10, -51)
    sleep(2)

@app.route('/on')
async def control_on():
    global process
    try:
        # request.args.get('http://${IP}/on')
        process = Thread(target=routine, args=())
        process.start()
        process.join()
        return redirect('/')
    except Exception as e:
        print("error")
        return e
    
@app.route('/stop')
async def control_stop():
    try:
        # request.args.get('http://${IP}/stop')
        # arm = Dobot(225,3,140,0)
        return redirect('/')
    except  Exception as e:
        print("error")
        return e

@app.route('/off')
async def control_off():
    try:
        #await request.args.get('http://${IP}/off')
        return redirect('/')
    except Exception as e:
        print("error")
        return e


@app.route('/post', methods=["POST"])
async def postForm():
    print(request.form)
    header.clear()
    for i in request.form:
        header.append((i.capitalize(), request.form[i]))

    r1 = Report(project=request.form['projeto'], client=request.form['cliente'], sample=request.form['amostra'], operator=request.form['operador'], cycles=request.form['ciclos'], liquid_initial_mass=request.form['peso solido'], solid_initial_mass=request.form['peso solido'])

    session.add(r1)
    session.commit()
    return render_template('index.html', project=request.form['projeto'], client=request.form['cliente'], sample=request.form['amostra'])

@app.route('/pdf')
async def generatePDF():
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.header()
    a = [10,10]
    side = True
    for i in header:
        pdf.element(i[0] + ': ' + i[1], a, side)
        a[1] += 5 if(not side) else 0
        side = not side 
    pdf.generate(datetime.now().strftime("%d-%m-%Y-%H%M%S"))
    return render_template("index.html")


app.run(host = '0.0.0.0', port=3000, debug=True)