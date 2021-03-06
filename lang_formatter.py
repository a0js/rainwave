#!/usr/bin/python

import os
import glob

def format_locales(in_filename, out_filename):
	original_file = open(in_filename, 'r')
	out_file = open(out_filename, 'w')
	for line in original_file:
		if line.find(":") == -1:
			out_file.write("%s\n" % line.strip())
		else:
			s = line.split(":", 1)
			if s[0].find("__comment__") != -1:
				out_file.write("   %-30s: %s\n" % (s[0].strip(), s[1].strip()))
			else:
				out_file.write("   %-50s: %s\n" % (s[0].strip(), s[1].strip()))
	original_file.close()
	out_file.close()

if __name__ == "__main__":
	files = [ os.path.basename(f) for f in glob.glob("./lang/*.json") ]
	for filename in files:
		format_locales("./lang/%s" % filename, "./lang2/%s" % filename)
