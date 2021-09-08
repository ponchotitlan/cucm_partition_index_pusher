# -*- coding: utf-8 -*-
__author__ = "Alfonso Sandoval"
__version__ = "1.0.1"
__maintainer__ = "Alfonso Sandoval"
__status__ = "Production"

"""UCM Partition Insertion -> CUCMOperator Class

Holder class for the different AXL operations for updating the desired CSS
"""
from CUCMConnectorAXL import *

class CUCMOperator:
    def __init__(self,CUCM_IP,AXL_Username,AXL_Password,debug = False):
        AXL_HANDLER = CUCMConnectorAXL.connector(CUCM_IP,AXL_Username,AXL_Password,debug=debug)
        self._AXL_OPERATOR = AXL_HANDLER[0]

    """
        Retrieves the current Route Partitions within a Calling Search Space

        Args:
            CSS_NAME -> string: Name of the desired CSS
        
        Raises:
            Exception

        Returns:
            Dict with the partitions within the specified CSS
            False, if Exception is raised
    """
    def get_css_partitions(self,CSS_NAME):
        pt_dic_filtered = {}
        try:            
            response = self._AXL_OPERATOR.getCss(
                    name = CSS_NAME
                ) 
            for record in response['return']['css']['members']['member']:
                pt_dic_filtered[record['routePartitionName']['_value_1']] = record['index']
        except Exception as ex:
            print(f'🔥🔥🔥 ERROR: {str(ex)}')
            pt_dic_filtered = False
        finally:
            return pt_dic_filtered

    """
        Updates all the Route Partitions of a Calling Search Space

        Args:
            CSS_NAME -> string: Name of the desired CSS
            PT_LIST -> Dict: Dictionary with the partitions to be updated
        
        Raises:
            Exception

        Returns:
            True, if operation is completed successfully
            False, if Exception is raised
    """
    def update_css_partitions(self,CSS_NAME,PT_LIST):
        result = True
        try:
            self._AXL_OPERATOR.updateCss(
                    name = CSS_NAME,
                    members = {"member" : PT_LIST}
                )  
        except Exception as ex:
           print(f'🔥🔥🔥 ERROR: {str(ex)}')
           result = False
        finally: 
            return result