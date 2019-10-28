import collections, sys

class FlavorRanking:

	def rank_flavors(self, input_file_name):
		#	5 points should be given to an attendee's favorite flavor, 3 points to their second favorite, 
		#	2 points to their third favorite, 1 point to their fourth favorite and 0 points to their fifth favorite.
		score_translation={1:5,2:3,3:2,4:1,5:0}

		ifile=open(input_file_name,"r")   # such as 'sample-input.txt'
		# 	assuming normally formatted file as the instructions said and using 'readlines' for ease
		flist=ifile.readlines()
		# 	fall-back plan: We could also read the whole text in and manually split the lines if we 
		#	needed to accomodate for some strange new-line characters or other separators
		#		itext=ifile.read()
		#		flist=itext.split("\n") # parse indivdual lines
		#	or if we don't know the line separator for this particular OS:
		#		import os
		#		flist=itext.split(os.linesep)
		ifile.close()
		flavor_scores={}

		for ii in flist:
			if ii.find(" ") == -1:  #ignore empty line (at end of file)
				continue

			flavor=ii[:ii.rindex(" ")]
			flavorrank=int(ii[ii.rindex(" "):].strip())

			if flavor not in flavor_scores:
				flavor_scores[flavor]=score_translation[flavorrank]
			else: 
				current_score=flavor_scores[flavor]
				flavor_scores[flavor]=score_translation[flavorrank]+current_score

		# 	sort first by the score value, then by the length of the flavor name
		sorted_x = sorted(flavor_scores.items(), key=lambda kv: (kv[1],-len(kv[0]) ))  
		# 	re-sort from highest score to lowest
		sorted_x.reverse()  
		sorted_dict = collections.OrderedDict(sorted_x)
		#	used for the unit tests
		self.sorted_scores=sorted_dict 
		#	print sorted_dict
		return self.format_output(sorted_dict )


	# 	used for the unit tests
	def get_sorted_scores(self):  
		return self.sorted_scores


	# 	used for the unit tests
	def get_numbered_lines(self):  
		return self.numbered_lines


	def format_output(self,sorted_dict_in):
		flav_out=""
		frank=0
		last_score=0
		line_number=0
		self.numbered_lines=[]
		# 	make necessary grammar adjustments
		psuffix = lambda x : "pts" if (x > 1) else "pt" 
		for ii in sorted_dict_in.keys():
			frank=frank+1
			if sorted_dict_in[ii] != last_score:			
				line_number=frank
				last_score=sorted_dict_in[ii]		

			flav_out=flav_out+str(line_number)+". "+ii+", "+str(sorted_dict_in[ii])+" "+(psuffix(sorted_dict_in[ii]) )+"\n"
			# 	used for the unit tests
			self.numbered_lines.append(str(line_number))  
		return flav_out
	


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print ("\nERROR: No input file provided. Please provide the input file as a command-line argument. \nExamples:\npython flavors.py sample-input.txt\npython flavors.py /home/phrozen/Downloads/sample-input.txt\n")
		sys.exit(0)
	fr=FlavorRanking()
	print (fr.rank_flavors(sys.argv[1]))
