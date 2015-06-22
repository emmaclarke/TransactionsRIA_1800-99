import os, sys

import enchant
from nltk.tokenize import sent_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer
import re
from pprint import pprint

def open_directory(dirname):
    if os.path.isdir(dirname):
            files = os.listdir(dirname)
            for source_file in files:
                open_file(os.path.join(dirname,source_file))
    else:
        print 'not a directory or file not found'

def open_file(filename):
    with open(filename, 'rb') as source:
       print '\n--\nreading: %s' % filename
       source_text = source.read()

# each of these is a separate cleaning stage, comment them out to remove them
#      source_text = remove_entities(source_text)
#      source_text = rule_replacement(source_text)
       source_text = check_spelling(source_text)
       
       with open('_cleaned.'.join(filename.split('.',1)), 'w') as target:
           print 'writing: %s' % '_cleaned.'.join(filename.split('.',1))
           target.write(source_text)

def rule_replacement(text):
   #load the rules
    print 'rule replacement'
    rules = None
    with open('rules/rules.txt', 'rb') as ruletxt:
        rules = dict([line.rstrip().split(' ') for line in ruletxt])

    for word in rules.keys():
       text = text.replace(word, rules[word])
    return text

def remove_entities(text):
   print 'entity removal'
   text = text.replace(r'&quot;',' ')
   text = text.replace(r'&apos;',' ')
#   text = re.sub(r'\r\n', ' ', text)
   return text

def check_spelling(text):
    print 'spell checking'
    pwl_name = 'Underwood_words.txt'
    dictionary = enchant.DictWithPWL('en_GB',os.path.join('wordlists',pwl_name))

    sentences = sent_tokenize(text)
    words_sentences = [TreebankWordTokenizer().tokenize(s) for s in sentences]
    words = set([item for sublist in words_sentences for item in sublist])
    #remove digits
    nondigits = re.compile(r'\D+')
    words = filter(nondigits.search, words)
    #gather the unknowns
    unknown = [w for w in words if not dictionary.check(w.lower())]
    #put them in a dictionary
    replacements = dict(zip(unknown, map(dictionary.suggest, unknown)))
			#print 'replacements for this file:'
			#pprint(replacements) 
    #do the replacement 
    for uk_word in replacements.keys():
                #if there is a replacement
        if replacements[uk_word]:
#			print 'replacing %s with %s' % uk_word, replacements[uk_word][0].lower()
                text = text.replace(uk_word, replacements[uk_word][0].lower()) 
    return text

def main(argv):
    try:
        dirname = argv[0]
        open_directory(dirname)  
    except Exception as e:
       print '\n---\n Error: exception %s \n---\n' % e
       print 'This script will clean the data from DIRNAME, filename_clean, make sure that it doesn\'t delete something already there!'

if __name__ == '__main__':
    #strip the first argument
	if len(sys.argv)  == 2:
		main(sys.argv[1:])
	else:
		print 'you need to specify the directory (replace DIRNAME with the name): \n python cleaner.py DIRNAME'

