from flask.ext.wtf import Form
from wtforms.fields import TextField, SubmitField,PasswordField
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import Required

class upload_excel(Form):
	
	file = FileField('Excel File', validators = [FileAllowed(['xls', 'xlsx'], 'File format not supported!'), Required("Upload some file!")])		
	submit = SubmitField("Upload! ")	

	# Constructor calls the Form's default constructor
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
	
	