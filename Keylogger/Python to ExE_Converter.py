
from distutils.core import setup 
import py2exe, sys, os, shutil 

sys.argv.append('py2exe')

py_script = raw_input(" >>> Enter Script Name: ")
py_icon = raw_input(" >>> Enter Script icon: ")

py2exe_options = {"packages": "encodings", 'bundle_files': 1} 
setup(options = {"py2exe" : py2exe_options},
		console = [{"script": py_script+".py",
					"uac_info": "requireAdministrator", 
					"icon_resources": [(1, py_icon+".ico")]}],
					zipfile = None,
					data_files=[(".",[py_icon+".ico"])],
					compressed=True)
shutil.rmtree('build')
shutil.move("dist\\"+py_script+".exe",py_script+".exe")
shutil.rmtree('dist')

