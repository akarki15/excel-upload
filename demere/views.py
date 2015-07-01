from flask import render_template, request, url_for
from demere import demere
from forms import upload_excel
import json 
import pyexcel as pe
import pyexcel.ext.xls # import it to handle xls file

@demere.route('/' , methods=['GET','POST'])
def upload():	
	form = upload_excel()	
	
	if request.method == 'POST':		
		if form.validate() == False:			
			return render_template('index.html', form=form)
		else:						
			return redirect(url_for('list_excel'))
	elif request.method == 'GET':
		return render_template('index.html', form=form)


@demere.route('/list')
def list_excel():
    # return render_template('list.html')
    return read_excel('sample.xlsx')


def read_excel(filename):
	list  = pe.get_array(file_name= filename)
	json_string = json.dumps(list)
	return json_string
