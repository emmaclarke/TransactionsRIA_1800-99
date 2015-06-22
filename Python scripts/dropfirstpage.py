from PyPDF2 import PdfFileWriter, PdfFileReader

filename = '30078743'                                              
output_file = PdfFileWriter()                                  #thing that makes a PDF (variable name)
input_handle = open(filename+'.pdf', 'rb')                     #open file name
input_file = PdfFileReader(input_handle)                       #create a reader from that file

num_pages = input_file.getNumPages()                           #get the number of pages in the pdf

print "document has %s pages \n" % num_pages                   #document has 'this many pages'

#add all pages but the first one
for i in xrange(1, num_pages):                                 #for this number of pages, from 1 instead of 0 (JSTOR page is zero)the first page
    output_file.addPage(input_file.getPage(i))                  
    print 'added page %s \n' % i

output_stream = file(filename+'-stripped.pdf','wb')            #output file,
output_file.write(output_stream)

output_stream.close()
input_handle.close()


