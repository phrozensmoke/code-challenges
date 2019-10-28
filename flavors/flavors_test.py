import unittest, sys
from flavors import FlavorRanking
 
class FlavorRankingTest(unittest.TestCase):
 
	def setUp(self):
		self.input_file=sys.argv[1]
		self.expected_out=sys.argv[2]

	def runTest(self):
		fr=FlavorRanking()
		exout=open(self.expected_out,"r")
		exoutlines=exout.read()
		self.ex_lines=exoutlines.split("\n") 
		exout.close()
		self.in_rankings=fr.rank_flavors(self.input_file)
		self.numbered_lines=fr.get_numbered_lines()
		self.sorted_scores=fr.get_sorted_scores()

		# These tests are to try to pin-point the reason for the failure: First check for simple stuff like incorrect spacing, punctuation, new-lines, etc
		self.assertEqual( self.in_rankings.count("\n"), exoutlines.count("\n"))
		self.assertEqual( self.in_rankings.count("."), exoutlines.count("."))
		self.assertEqual( self.in_rankings.count(" "), exoutlines.count(" "))
		self.assertEqual( self.in_rankings.count("pt"), exoutlines.count("pt"))
		self.assertEqual( self.in_rankings.count("pts"), exoutlines.count("pts"))

		# check the data - the line numbering, order of the flavors, and point scores from the expected input 
		# against what we produced from the input and make sure everything is in correct order, we numbered lines correctly, and the scores are correct
		lineNums=[]
		flavors=[]
		scores=[]
		
		for ii in self.ex_lines:
			if ii.find(".")== -1: continue 
			if ii.find(",")== -1: continue 
			if ii.find(" pt")== -1: continue 
			lineN=ii[:ii.index(".")]
			lineNums.append(lineN)
			fl=ii[ii.index(".")+1:ii.index(",")].strip()
			flavors.append(fl)
			sc=ii[ii.index(",")+1:ii.index(" pt")].strip()
			scores.append(int(sc)) 

		self.assertEqual(self.numbered_lines, lineNums)
		self.assertEqual(list(self.sorted_scores.keys()), flavors)
		self.assertEqual(list(self.sorted_scores.values()), scores)

		# This is a very simple pass/fail test to verify that whatever we produce from the 'input' exactly matches the expected output
		# If titles, rankings, spacing, or new-lines don't match, the whole test will fail
		self.assertEqual( self.in_rankings, exoutlines)

  
if __name__ == '__main__':
		# The unit test is designed to be used with any input file and expected output file, not necessarily the exact version supplied to me for the code test
		if len(sys.argv) < 3:
			print ("\nERROR: No input or 'expected output' file provided. Please provide the input file AND 'expected output' file as a command-line argument. \nExample:\npython flavors_test.py sample-input.txt expected_output.txt\npython flavors_test.py /home/phrozen/Downloads/phrozensmoke-master/sample-input.txt /home/phrozen/Downloads/phrozensmoke-master/expected-output.txt\n")
			sys.exit(0)
		unittest.TextTestRunner().run(FlavorRankingTest())
