import json 
import pyexcel as pe
import pyexcel.ext.xls # import it to handle xls file
list  = pe.get_array(file_name="sample.xlsx")
json_string = json.dumps(list)
print json_string
