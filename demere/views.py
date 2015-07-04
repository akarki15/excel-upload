from flask import render_template, request, url_for, redirect, jsonify, g
from werkzeug import secure_filename
from demere import demere
from forms import upload_excel
from config import DATABASE

import json, sqlite3
import pyexcel as pe
import pyexcel.ext.xls # import it to handle xls file

# Routes stuff        
@demere.route('/' , methods=['GET','POST'])
def upload():     
    print "route"  
    form = upload_excel()       
    if request.method == 'POST':        
        if form.validate() == False:                        
            return render_template('index.html', form=form)
        else:      
            file = request.files[form.file.name]                  
            json_data = read_excel(file)  
            
            return render_template('list.html', form=form, data=json_data)
    elif request.method == 'GET':
        return render_template('index.html', form=form)    

@demere.route('/uploads' , methods=['GET','POST'])
def list_uploads():
    return render_template('list.html')

def read_excel(file):
    """ Takes file and returns json """
    if file: 
        filename = file.filename
        extension = filename.split(".")[1]
        sheet = pe.get_sheet(file_type=extension, file_stream=file.read())
        data  = pe.to_dict(sheet)            
        for key in data:
            print key, data[key]
        return jsonify(data)

# Database stuff

def connect_db():
    return sqlite3.connect(DATABASE)


def init_db():
    """ run initially to setup database """
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@demere.before_request
def before_request():   
    """ Runs before every request """    
    g.db = connect_db()     # Storing the db in our special g object

@demere.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
