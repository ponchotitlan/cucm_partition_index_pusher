# -*- coding: utf-8 -*-
__author__ = "Alfonso Sandoval"
__copyright__ = "HCA Healthcare, 2021"
__version__ = "1.0.1"
__maintainer__ = "Alfonso Sandoval"
__email__ = "alfsando@cisco.com"
__status__ = "Production"

"""UCM Partition Insertion -> Execution script

This script inserts a Route partition in the desired position in a specified Calling Search Space.
If the index provided is greater than the amount of partitions present, the partition is appended to the end of the list.
"""

from CUCMOperator import *
import argparse

def GetArgs():
   """
   Supports the command-line arguments listed below.
   """
   parser = argparse.ArgumentParser(description= 'UCM Route Partition adding script')
   parser.add_argument('-ip', '--ip', required=True, help='CUCM IP address')
   parser.add_argument('-user', '--username', required=True, help='CUCM AXL-enabled username')
   parser.add_argument('-pwd', '--password', required=True, help='CUCM AXL-enabled password')
   parser.add_argument('-css', '--css', required=True, help='Calling Search Space name')
   parser.add_argument('-part', '--partition', required=True, help='Route Partition to insert')
   parser.add_argument('-i', '--index', required=True, type=int, help='Route Partition desired index. This value must be greater than 0 (the first position is 1)')
   args = parser.parse_args()
   return args

def main():
    ARGS = GetArgs()
    #Create CUCM Connection instance
    TARGET_CUCM = CUCMOperator(
        ARGS.ip,
        ARGS.username,
        ARGS.password
    )
    #Get dictionary with current partitions of the desired CSS
    pt_current_list = TARGET_CUCM.get_css_partitions(ARGS.css)
    if pt_current_list:
        #Sort the dictionary by index
        pt_sorted = list(sorted( pt_current_list.items(), key = lambda x:x[1] ))
        #If the desired position is bigger than the current amount of partitions, push to the end
        if ARGS.index >= len(pt_sorted):
            pt_sorted.append((ARGS.partition, len(pt_sorted)+1))
        else:
            #If not, insert the new PT in the desired position
            pt_sorted.insert(ARGS.index - 1,(ARGS.partition , ARGS.index))
            #Update the rest of the positions
            for i in range(ARGS.index,len(pt_sorted)):
                updated_tuple = (pt_sorted[i][0] , pt_sorted[i][1] + 1)
                pt_sorted[i] = updated_tuple
        #Issue the AXL instruction to insert all partitions at once
        axl_pt_list = []
        for record in pt_sorted:
            axl_pt_list.append({
                    "routePartitionName" : record[0],
                    "index" : record[1]
                })    
        update_result = TARGET_CUCM.update_css_partitions(ARGS.css,axl_pt_list)
        if update_result:
            pt_new_list = TARGET_CUCM.get_css_partitions(ARGS.css)
            print(f'\n⏳ Former partitions of {ARGS.css}: \n {pt_current_list}')
            print(f'\n✅ Current partitions of {ARGS.css}: \n {pt_new_list}')

if __name__ == "__main__":
    main()