import os 
import sys

class ProjectException(Exception):
    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message=ProjectException.get_detailed_error_message(error_meassage=error_message,error_detail=error_detail)
    @staticmethod
    def get_detailed_error_message(error_meassage:Exception,error_detail:sys)->str:
        """
        error_message:Exception object
        error_detail:object of keys module
        """
        
        _,_ ,exec_tb = error_detail.exc_info()

        line_number=exec_tb.tb_frame.f_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename
        error_meassage=f"Error occured in script: [{file_name}] at line_number: [{line_number}] error message: [{error_meassage}]"
        
        return error_meassage
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return ProjectException.__name__.str()
