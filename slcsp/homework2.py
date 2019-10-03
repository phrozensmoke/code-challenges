import os, collections
## 'slcsp' homework assignment  (July 2019)
	
def readSLCSP():
	global reportdata

	f=open("slcsp.csv")
	ff=f.read()
	f.close()
	slines=ff.split("\n")
	
	for ii in slines:
		if ii.find(",")== -1:
			continue
		reportdata[ii.split(",")[0]]=ii.split(",")[1]
		
def readPlans():
	global plandata
	global availableStates

	f=open("plans.csv")
	ff=f.read()
	f.close()
	slines=ff.split("\n")
	
	for ii in slines:
		if ii.find(",") == -1:
			continue
		parts=ii.split(",")
		if parts[2] != 'Silver':
			continue
		prate='{:.2f}'.format(float(parts[3]))  # make sure all rates have 2 decimal points
		ratearea=parts[1]+" "+parts[4]		
		if ratearea not in plandata:
			plandata[ratearea]=[prate]
			continue
		plandata[ratearea].append(prate)
	
	# purge rate areas with less than 2 silver plans available and sort the rates in ascending order
	for ii in plandata.keys():
		if len(plandata[ii]) < 2:
			del plandata[ii]
			continue
		plandata[ii].sort() #sort the rates in ascending order
	
def readZips():
	global zipplanarea
	global ambigzips
	
	f=open("zips.csv")
	ff=f.read()
	f.close()
	slines=ff.split("\n")
	
	for ii in slines:
			if ii.find(",") == -1:
				continue
			if ii.find("zipcode") > -1:  # skip first line of file
				continue
			parts=ii.split(",")
			ratearea=parts[1]+" "+parts[4]
			zipc=parts[0]
			if zipc in zipplanarea:
				if zipplanarea[zipc] != ratearea:  # we already have this zip associated with another rate area, so it's ambiguous
					if zipc not in ambigzips:
						ambigzips.append(zipc)
					continue
			zipplanarea[zipc]=ratearea

def updateSLCSP():
	global reportdata
	global zipplanarea
	global ambigzips	
	global plandata
	
	for ii in reportdata.keys():
		if ii in ambigzips:  # This zip code showed up in more than one rate area, so we can't figure out pricing
			continue 
		if ii in zipplanarea:
			rarea=zipplanarea[ii] # find out the rate area for this zip code
			if rarea in plandata: 
				availRates=plandata[rarea]  # We removed any lists shorter than 2 silver rates earlier readPlans and already sorted
				rateForZip=availRates[1]  # grab 2nd lowest rate
				reportdata[ii]=rateForZip

	
def printSLCSP():
	global reportdata
	
	# let's print a csv to stdout
	for ii in reportdata.keys():	
		print(ii+","+reportdata[ii])
	print("\n")   #print the trailing newline character just like the slcsp.csv input file had
	

	
reportdata=collections.OrderedDict()
plandata=collections.OrderedDict()
zipplanarea=collections.OrderedDict()
ambigzips=[]


if __name__ == '__main__':
	readSLCSP()
	readPlans()
	readZips()
	updateSLCSP()
	printSLCSP()

