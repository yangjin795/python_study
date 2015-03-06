import optparse

parser = optparse.OptionParser()
parser.add_option('-v','--verbose',dest='verbose',help='verbose logging', action='store_true')
parser.add_option('-f','--filename',dest='filename',help='filename name')


(options,args)=parser.parse_args()
print options
print args

########## runing result
"""
$ python optparse_test.py -h
Usage: optparse_test.py [options]

Options:
  -h, --help            show this help message and exit
  -v, --verbose         verbose logging
  -f FILENAME, --filename=FILENAME
                        filename name
"""
####################
"""
$ python optparse_test.py -v -f filename1 argsssss
{'verbose': True, 'filename': 'filename1'}
['argsssss']

"""
