#!/usr/bin/env python

## work sample - Truss  (Jan 2020 - e.andrews)

import os, sys, datetime, csv

class Normal:

	def normalize_csv(self, input_csv_data):
		sys.stdout.reconfigure(encoding='utf-8', errors="replace")   # setup stdout for UTF8 with appropriate replacement character
		cvswrite=csv.writer(sys.stdout, delimiter=",", quotechar='"')  #setup necessary quotes for addresses

		rownumber=0
		dh=['','','','','','','','']  # a list to hold our modified data
		for row in input_csv_data:
			try:
				if rownumber==0:  # These are just the headers - return them as is
					cvswrite.writerow([row[0], row[1], row[2],row[3], row[4], row[5],row[6], row[7]])
				else: 
					dh[0]=self.convert_timestamp(row[0]) # Timestamp
					dh[1]=row[1] # Address column: UTF8 replacement should have already been handed by Python when the file was opened
					dh[2]=row[2].rjust(5,'0') # zip code: ensure it's 5 characters
					dh[3]=row[3].upper() # full name: convert to upper case
					dh[4]=self.extract_seconds(row[4])
					dh[5]=self.extract_seconds(row[5])
					dh[6]=dh[4]+dh[5]  # TotalDuration: sum of Foo and Bar
					dh[7]=row[7]  # Notes column: UTF8 replacement should have already been handed by Python when the file was opened
					cvswrite.writerow([dh[0], dh[1], dh[2],dh[3], dh[4], dh[5], dh[6], dh[7]])  # dump the row to stdout
				rownumber=rownumber+1
			except:
				print ("*WARNING*: Something is wrong with this row (dropping) : " +", ".join(row), file=sys.stderr)  # couldn't process the row, show stderr message

	def extract_seconds(self, input_str):
		h, m ,s = input_str[0:input_str.rindex(".")].split(':')  # hour, minute, second
		f=input_str[input_str.rindex(".")+1:len(input_str)]  # microsecond
		self.totalSeconds = datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s), microseconds=int(f)).total_seconds()
		return self.totalSeconds

	def convert_timestamp(self, input_str):
		#The time is in pacific, so we are going to try to just read it in with an EST offset of -5000
		dd=datetime.datetime.strptime(input_str+" -0500", "%m/%d/%y %I:%M:%S %p %z")  # We are just going to read the time in as EST immediately
		estTimeDelta = datetime.timedelta(hours=3)  # compensate for the 3 hour difference between EST and PST
		estTZObject  = datetime.timezone(estTimeDelta, name="EST")
		dd=dd+estTimeDelta
		return dd.isoformat()


if __name__ == '__main__':
	nc=Normal()
	csvreader=None
	if os.isatty(0):
		if len(sys.argv) < 2:  # we're in a terminal window and no file name was provided, assume a stdin pipe or manual data feed
			sys.stdin.reconfigure(encoding='utf-8', errors="replace") # Python will take care of all necessary replacement characters
			#print ("In a terminal, using stdin")
			csvreader = csv.reader(sys.stdin.readlines(), delimiter=",")
			nc.normalize_csv(csvreader)
		else:  # in a terminal but a file was provided
			filename=sys.argv[1]
			#print ("In a terminal with input file provided")
			with open(filename, encoding="utf8", errors="replace") as csvfile:   # Python will take care of all necessary replacement characters
				csvreader = csv.reader(csvfile, delimiter=",")
				nc.normalize_csv(csvreader)
	else:  # it appears this program is not being run from a terminal : this happens if we use linux 'cat' instead of a pipe
		if len(sys.argv) > 1: 
			filename=sys.argv[1]
			#print ("No terminal, but input file available")
			with open(filename, encoding="utf8" , errors="replace") as csvfile: # Python will take care of all necessary replacement characters
				csvreader = csv.reader(csvfile, delimiter=",")
				nc.normalize_csv(csvreader)
		else : 
			#print ("No Terminal, but stdin available")
			sys.stdin.reconfigure(encoding='utf-8', errors="replace")  # Python will take care of all necessary replacement characters
			csvreader = csv.reader(sys.stdin.readlines(), delimiter=",")
			nc.normalize_csv(csvreader)
	if csvreader==None:
		print ("\nERROR: No input file or stdin data provided. Please provide the input file as a command-line argument. \nExamples:\npython Normal.py sample.csv\npython Normal.py /home/myDir/Downloads/sample.csv\n")



	

	

