"""Run this file, when prompted for a file, input the entire pathway, including the C:\..."""
"""file_import will import your log file and sort it
mismatch_lists will find the unmatched process reports"""

from file_import import file_import
from mismatched_lists import mismatch_lists

send_list, recv_list = file_import()
mismatch_lists(send_list,recv_list)
