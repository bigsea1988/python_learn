#!/usr/bin/python
#coding: utf-8
import sys

def print_sys():
	if len(sys.argv) > 2:
		print '{}-{}-{}'.format(sys.argv[0],sys.argv[1],sys.argv[2])

if __name__ == '__main__':
	print_sys()
