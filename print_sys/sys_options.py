#!/usr/bin/python
# coding: utf-8

import sys,getopt

def usage():
	print '-{} {}'.format('i','inputfile')
	print '-{} {}'.format('o','outputfile')
	print '-{} {}'.format('h','help')
	

def print_sys_options():
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
	for op,value in opts:
		if op == '-i':
			print 'input file :{}'.format(value)
		if op == '-o':
			print 'output file :{}'.format(value)
		if op == '-h':
			usage()
			sys.exit()


if __name__ == '__main__':
	print_sys_options()
