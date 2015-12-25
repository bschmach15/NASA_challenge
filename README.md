# NASA_challenge
My submission for the NASA programming challenge
These programs were written in python 2.7
#Required Packages:
These programs run using the following packages:
* Pandas 0.17.1 [(download)](https://pypi.python.org/pypi/pandas/0.17.1/#downloads)
* re
* os

These are all standard included in the Anaconda distribution

#Instructions
1. Download the .zip file, and extract all files to the destination of your choice
2. Run master_run.py (It should find the necessary files in the same folder it is located it)
3. file_input will ask you where your error report is stored, please feed it the entire path (C:\Users\...)
4. It will then return send_list and recv_list, ready to pass to mismatch_lists
  * send_list is the sorted dataframe containing MPI send reports sorted numerically by sender
  * recv_list is the same, with received reports
5. master_run will then pass the lists to mismatched_lists to be searched for unmatched send and received reports
6. A log file will be outputted detailing where the unmatched reports are. 


#Output
mismatched_lists will output four items:
 1. The number of messages each process is sending
 2. The number of messages each process is expected to send
 3. A table that contains the send processes with no process to receive
 4. A table that contains the receving processes with no process to send to them

You can quickly tell where the unmatched processes are by looking at items 1 and 2. If the numbers do not match, then there is an extra send process or receiving process, whichever number is larger. This is an easy way to check that mismatched_lists found all the unmatched process, since you already know how many to expect. 


