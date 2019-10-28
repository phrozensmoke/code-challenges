# COMMAND LINE IMPLEMENTATION
e.andrews - 09.27.2019

Language: Python

Recommended Python version: Python 3.7 or above (Tested on Python 3.7.3  and Python 2.7.16 / Tumbleweed-SuSE Linux  )

	You can verify your version of Python by running 'python --version' in a command-line or terminal. 
	
	No special libraries are required. Only built-in Python libraries are utilized.


## RUNNING THE SOLUTION:

1. Place both the flavors.py and flavors_test.py files in the same directory

2. Open a terminal or DOS prompt

3. Change the current working directory to the directory where you stored the flavors.py and flavors_test.py files
	Example: cd /home/phrozen/Downloads/

4. Run the solution with the command 'python flavors.py sample-input.txt'
	An input file must be provided as a command line option.  Otherwise, the program will quit with an informational error/warning. 

	If the sample input file is stored in another file name or directory, simply adjust the supplied file input parameter accordingly, providing the full path. 
	
		Example: python flavors.py /home/phrozen/Downloads/sample-input-another-filename.txt

	NOTE: On some Linux distributions, you may need to execute the 'python3' command, instead of 'python' (which might run the old Python version 2); This happened to be the case on my machine
	
		Example: python3 flavors.py /home/phrozen/Downloads/sample-input-another-filename.txt

		The solution should run just fine on Python 2.7 or above, though 3.7 is definitely recommended



## RUNNING THE UNIT TEST:

1. Place both the flavors.py and flavors_test.py files in the same directory  (This should have already been completed before running the solution.)

2. Open a terminal or DOS prompt

3. Change the current working directory to the directory where you stored the flavors.py and flavors_test.py files

	Example: cd /home/phrozen/Downloads/

4. Run the unit tests with the command 'python flavors_test.py sample-input.txt expected_output.txt'

	An input file AND an 'expected output' file must be provided as command line options.  Otherwise, the program will quit with an informational error/warning. 

	If the sample input file and expected output file are stored in another file name or directory, simply adjust the supplied file parameters accordingly, providing the full paths. 
	
		Example: python flavors_test.py /home/phrozen/Downloads/sample-inputABC.txt /home/phrozen/Downloads/expected-outputXYZ.txt

	NOTE: On some Linux distributions, you may need to execute the 'python3' command, instead of 'python' (which might run the old Python version 2); This happened to be the case on my machine
	
		Example: python3 flavors_test.py sample-input.txt expected_output.txt

		The unit tests should run just fine on Python 2.7 or above, though 3.7 is definitely recommended
