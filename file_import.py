import pandas as pd
import re


def file_import():
    """This file takes in raw MPE logs and searches them for send a receive reports. It will then organize them into a DataFrame table
    and sorts them numerically.
    
    This file assumes that your MPE send and receive reports have the form
    [0] Starting MPI_Isend with count = x, dest = y, tag = z
    [4] Starting MPI_Irecv with count = x, dest = y, tag = z
    
    It will return sorted DataFrame tables to be passed to mismatch_lists"""
    
    
    print "Ok, I will import and sort your MPE send and receive logs"
    file = raw_input("Please input the path to your file destination")
    f = open(file,'r')

    #create empty lists to fill with MPE_Isend and MPI_Irecv strings
    list_send = []
    list_recv = []
    print "Searching the file for what I want"
    #search for MPI_Isend and MPI_Irecv and sort them into the corresponding list
    for line in f:
        if "Starting MPI_Isend" in line:
            list_send.append(line)
        if "Starting MPI_Irecv" in line:
            list_recv.append(line)

    print "Now I'll organize the logs into DataFrames"

    #Create empty DataFrame to store MPI_Isend information
    #column names are what we are searching for. We want to find
    #the sending process, the destination, the count (length) and finally the tag
    df_send = pd.DataFrame([],columns=["Sender","Length","Destination","Tag"])
    for i in range(0,len(list_send)):
        #extract the numbers from MPI_Isend string, and return them as integers
        num = map(int, re.findall("\d+",list_send[i]))
        #create a DataFrame to be appending to the master list, df_send
        #make sure it has the same column names
        df_app = pd.DataFrame([num],columns = ["Sender","Length","Destination","Tag"])
        #append the new MPI_Isend process, making sure it is indexed correctly
        df_send = df_send.append(df_app,ignore_index=True)

    #same as above only for MPI_Irecv
    df_recv = pd.DataFrame([],columns=["Destination","Length","Sender","Tag"])
    for i in range(0,len(list_recv)):
        num = map(int, re.findall("\d+",list_recv[i]))
        df_app = pd.DataFrame([num],columns = ["Destination","Length","Sender","Tag"])
        df_recv = df_recv.append(df_app,ignore_index=True)

    print "I've got them all in tables, just have to sort them"

    #Sort numerically, starting with 0. This should group our processes by sender
    #We first want it to sort by sender, then by destination, and then finally by the tag
    #this will make comparisons much easier
    df_send_sorted = df_send.sort_values(["Sender", "Destination","Tag"],ascending=[True,True,True])
    df_recv_sorted = df_recv.sort_values(["Sender","Destination","Tag"],ascending=[True,True,True])
    #re-order columns so that each table has the same information in the same place
    df_send_sorted = df_send_sorted[["Sender","Destination","Tag","Length"]]
    df_recv_sorted = df_recv_sorted[["Sender","Destination","Tag","Length"]]

    print "Done sorting!"
    #return sorted tables for comparisons
    return df_send_sorted, df_recv_sorted
