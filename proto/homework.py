import os
import struct
## 'proto' homework assignment for Erica Andrews (July 2019)

	
def readFile():
	global filedata
	
	fdata=open('txnlog.dat','rb')
	filedata=fdata.read()
	fdata.close()
	print('read in file: length is  - ' +str(len(filedata)))

def parseHeader():
	global filedata
	global fheader
	global fbinaryT
	global numRecords
	global numDebit
	global numCredit
	global numStartAutopay
	global numEndAutopay
	
	# print('read in file: length is  - ' +str(filedata))
	fbinaryT=filedata[9:]
	fheader=filedata[:9]
	numRecords=int.from_bytes(fheader[5:],"big")
	print('number of total records is : '+str(numRecords)) 
	

def parseFile():
	global fbinaryT
	global numDebit
	global numCredit
	global numStartAutopay
	global numEndAutopay
	global numRecords
	
	fbinaryTbuffer=fbinaryT
	firstbyte=''
	recorddata=''
	numRecords=-1
	
	userIDbalance=0
	
	totalCredits=0
	totalDebits=0
	
	while len(fbinaryTbuffer) > 0:
		firstbyte=fbinaryTbuffer[0]
		fbinaryTbuffer=fbinaryTbuffer[1:]
		if firstbyte == 0  : #debit
			numRecords=numRecords+1
			numDebit=numDebit+1
			recorddata = fbinaryTbuffer[:20]
			fbinaryTbuffer=fbinaryTbuffer[20:]
			amount=struct.unpack('!d',recorddata[12:20])[0]
			userID=str(int.from_bytes(recorddata[4:12],"big"))
			#print('NUM REC '+str(numRecords)+' Debit: '+str(int.from_bytes(recorddata[0:4],"big")) +' '+userID+' '+str(amount))
			totalDebits=totalDebits-amount
			if userID=='2456938384156277127':
				userIDbalance=userIDbalance-amount; # debit it
			continue
		if firstbyte == 1  : #credit
			numRecords=numRecords+1
			numCredit=numCredit+1
			recorddata = fbinaryTbuffer[:20]
			fbinaryTbuffer=fbinaryTbuffer[20:]		
			amount=struct.unpack('!d',recorddata[12:20])[0]
			userID=str(int.from_bytes(recorddata[4:12],"big"))
			#print(' NUM REC'+str(numRecords)+' credit: '+str(int.from_bytes(recorddata[0:4],"big")) +' '+str(int.from_bytes(recorddata[4:12],"big"))+' '+str(amount))	
			totalCredits=totalCredits+amount
			if userID=='2456938384156277127':
				userIDbalance=userIDbalance+amount; # debit it			
			continue			
		if firstbyte == 2  : #StartAutopay
			numRecords=numRecords+1
			numStartAutopay=numStartAutopay+1
			recorddata = fbinaryTbuffer[:12]
			fbinaryTbuffer=fbinaryTbuffer[12:]			
			#print('NUM REC '+str(numRecords)+' numStartAutopay: '+str(int.from_bytes(recorddata[0:4],"big")) +' '+str(int.from_bytes(recorddata[4:12],"big")))			
			continue			
		if firstbyte == 3  : #EndAutopay
			numRecords=numRecords+1
			numEndAutopay=numEndAutopay+1
			recorddata = fbinaryTbuffer[:12]
			fbinaryTbuffer=fbinaryTbuffer[12:]	
			#print('NUM REC '+str(numRecords)+' numEndAutopay: '+str(int.from_bytes(recorddata[0:4],"big")) +' '+str(int.from_bytes(recorddata[4:12],"big")))		
		#print ('record was : '+str(firstbyte) +''+str(recorddata) )
		
	#print('total record types numRecords: '+str(numRecords)+' numDebit : '+str(numDebit)+'  numCredit: '+str(numCredit)+'  numStartAutopay: '+str(numStartAutopay)+'  numEndAutopay: '+str(numEndAutopay)) 	
	#print ('User ID balance for 2456938384156277127 is $'+str(userIDbalance)); 
	
	print ('\n\n---------ANSWERS TO QUESTIONS [PYTHON VERSION]---------\n\n')
	
	print ('What is the total amount in dollars of debits?   ANSWER: '+str(totalDebits)+'\n')
	print ('What is the total amount in dollars of credits?   ANSWER: '+str(totalCredits)+'\n')
	print ('How many autopays were started?   ANSWER: '+str(numStartAutopay)+'\n')
	print ('How many autopays were ended?   ANSWER: '+str(numEndAutopay)+'\n')
	print ('What is balance of user ID 2456938384156277127?   ANSWER: $'+str(userIDbalance)+'\n')
	
filedata=''
fheader=''
fbinaryT=''
numRecords=0
numDebit=0
numCredit=0
numStartAutopay=0
numEndAutopay=0


if __name__ == '__main__':
	readFile()
	parseHeader()
	parseFile()

