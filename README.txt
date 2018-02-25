Innovaccer_Analytics_Assignment
Dependencies packages:
	1. Pandas
	2. Numpy
	3. sys 

To run the program
Command:  python dedupe.py <filename>  > <outputfile>
Note: default file name is "Deduplication-Problem-Sample-Dataset.csv"
Output will be  clusters of unique patients


Output Format

###########Females################# 
>>>>>>>> with DOB: <DOB>
Cluster: <Cluster number>
		<index of entry in sample data> <lastName> <DOB> <gn> <lastName>
       .
       .
       <index of entry in sample data> <lastName> <DOB> <gn> <lastName>
       .

--------------------------------------
###########Males#################
>>>>>>>> with DOB: <DOB>
Cluster: <Cluster number>
		<index of entry in sample data> <lastName> <DOB> <gn> <lastName>
       .
       .
Cluster: <Cluster number>
		<index of entry in sample data> <lastName> <DOB> <gn> <lastName>
       .
       .
----------------------------------------
