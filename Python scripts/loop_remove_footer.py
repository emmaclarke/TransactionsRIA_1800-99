import os, sys

	
store_text = ''

def read_file(filename):
	global store_text
	read_file_handle = open(filename, 'r')
	for line in read_file_handle.readlines():
         #added a small change to remove blank lines ('\r\n' means 'end of line')
		 if not (line == '\r\n' or line.startswith('This content downloaded from') or
            line.startswith('All use subject to JSTOR Terms and Conditions')):
			store_text = store_text + line
	read_file_handle.close()
	
def write_file(filename):
	write_file_handle = open(filename, 'w')
	write_file_handle.write(store_text)
	write_file_handle.close()

#if you want to specify a whole directory you need to create a function that reads a directory name and calls read_file for each filename found. See listfiles.py 

read_file('1806 11-30.txt')

write_file('1806 11-30_without.txt')	

