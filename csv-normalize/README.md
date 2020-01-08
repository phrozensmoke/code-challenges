# WORK SAMPLE - TRUSS, CSV normalization task
erica andrews - 01.07.2020

Language: Python

Recommended Operating System: Ubuntu or another LINUX flavor (Not tested on Mac or Windows)

REQUIRED Python version: Python 3.7 or above (Tested on Python 3.7.3  on  Tumbleweed-SuSE LINUX  )

	You can verify your version of Python by running 'python --version' in a command-line or terminal. 
	
	No special libraries are required. Only built-in Python libraries are utilized.

	The solution uses features that may not be available in Python 2.x versions.  
	This solution was not tested with Python versions earlier than 3.7.


## RUNNING THE SOLUTION:

1. Place both the Normal.py and sample-with-broken-utf8.csv files in the same directory

2. Open a terminal window

3. Change your current working directory to the directory in step (1) where you placed the 2 files

4. Ensure that the Python script has correct execution permissions using the following command in Linux:
	chmod 755 Normal.py

5. Running the script:
	You can run the script by providing data through stdin (via a pipe or 'cat') or by providing a file name parameter.

	COMMAND LINE EXAMPLES: 

		./Normal.py < sample-with-broken-utf8.csv > output.csv

		cat sample-with-broken-utf8.csv | ./Normal.py > output.csv

		./Normal.py  sample-with-broken-utf8.csv > output.csv


		python ./Normal.py < sample-with-broken-utf8.csv > output.csv

		cat sample-with-broken-utf8.csv | python ./Normal.py > output.csv

		python ./Normal.py  sample-with-broken-utf8.csv > output.csv

