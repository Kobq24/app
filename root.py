from flask import Flask,render_template,send_file,send_from_directory,url_for,redirect
from flask_bootstrap import Bootstrap
import os
from datetime import datetime
import pytz
import imarikuro
import kijima
import ukusima
import ooe
import kosiki
from utils import my_url_for

#dt_now = str(datetime.now(pytz.timezone("Asia/Tokyo")).strftime('%Y_%m_%d-%H%M'))

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
bootstrap = Bootstrap(app)
app.jinja_env.globals[url_for] = my_url_for

@app.route('/')
def hello():
    return render_template('layout.html',title='風向風速予報')

@app.route('/scraping1')
def get1():
    # ↓　実行したいファイルの関数
    imarikuro.scraping()
    return render_template('output1.html',method=['GET'])

@app.route('/download1')
def Download_File1():
    #last_modified=None
    #last_modified=dt_now
    dt_now1 = str(datetime.now(pytz.timezone("Asia/Tokyo")).strftime('%Y_%m_%d-%H%M'))
    PATH='./output/風向風速予報_伊万里市_'+dt_now1+'.xlsx'
    return send_file(PATH,as_attachment=True)#,last_modified=last_modified)

@app.route('/scraping2')
def get2():
    # ↓　実行したいファイルの関数
    kijima.scraping()
    return render_template('output2.html',method=['GET'])

@app.route('/download2')
def Download_File2():
    dt_now2 = str(datetime.now(pytz.timezone("Asia/Tokyo")).strftime('%Y_%m_%d-%H%M'))
    PATH='./output/風向風速予報_五島市_'+dt_now2+'.xlsx'
    return send_file(PATH,as_attachment=True)

@app.route('/scraping3')
def get3():
    # ↓　実行したいファイルの関数
    ukusima.scraping()
    return render_template('output3.html',method=['GET'])

@app.route('/download3')
def Download_File3():
    dt_now3 = str(datetime.now(pytz.timezone("Asia/Tokyo")).strftime('%Y_%m_%d-%H%M'))
    PATH='./output/風向風速予報_佐世保市_'+dt_now3+'.xlsx'
    return send_file(PATH,as_attachment=True)

@app.route('/scraping4')
def get4():
    # ↓　実行したいファイルの関数
    ooe.scraping()
    return render_template('output4.html',method=['GET'])

@app.route('/download4')
def Download_File4():
    dt_now4 = str(datetime.now(pytz.timezone("Asia/Tokyo")).strftime('%Y_%m_%d-%H%M'))
    PATH='./output/風向風速予報_天草市_'+dt_now4+'.xlsx'
    return send_file(PATH,as_attachment=True)

@app.route('/scraping5')
def get5():
    # ↓　実行したいファイルの関数
    kosiki.scraping()
    return render_template('output5.html',method=['GET'])

@app.route('/download5')
def Download_File5():
    dt_now5 = str(datetime.now(pytz.timezone("Asia/Tokyo")).strftime('%Y_%m_%d-%H%M'))
    PATH='./output/風向風速予報_甑町_'+dt_now5+'.xlsx'
    return send_file(PATH,as_attachment=True)

@app.route('/redirect')
def redirect_func():
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run(debug=True)