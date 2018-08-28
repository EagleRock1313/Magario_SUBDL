'''
Author:Sandy Lynn Ortiz Stanford University Libraries - Born Digital Forensics Lab
created using python 3.6.4

Purpose: Create a tab-delimited manifest file with SourceID(SID) and Label for files in a series directory. 
Collection File and Naming convention must be in the following form:
File Naming Convention: YY-MON-DD and data type INT-ALPHA-INT
Directory Naming Convention: YY-MON and data type INT-INT

Algorithim:
1)Get a list of filenames in dir to be processed using regular expressions. Exclude python and other files.
2)Parse the file name, excluding file extension
3)Sort,group all files by year, month and day
4)Calculate a date spread value between files for label processing
5)Create a human readable date spread label/title
6)Reformat date spread to integer values YY-MON-DD
7)Get user input for Collection ID(CID) and validate input
8)Create SID: Append CID to Reformat Date spread
9)Get user input: filter list for series end date
10)Output tab delimited manifest file with SourceID(SID) and label/title
11)Output QualityControl(QC) file for auditing of processing
'''
