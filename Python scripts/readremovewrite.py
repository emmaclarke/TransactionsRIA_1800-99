import sys, os

store_text = ''

def read_file(filename):
	global store_text
	read_file_handle = open(filename, 'r')
	for line in read_file_handle.readlines():
		 if not (line.startswith('This content downloaded from') or
            line.startswith('All use subject to JSTOR Terms and Conditions')):
			store_text = store_text + line
	read_file_handle.close()
	
def write_file(filename):
	write_file_handle = open(filename, 'w')
	write_file_handle.write(store_text)
	write_file_handle.close()
	
read_file('FrontMatter.txt')

write_file('FrontMatter_without.txt')	
		
	