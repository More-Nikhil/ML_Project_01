import sys
import logging

def error_message_datils(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error Occured in python script name[{0}] line number [{1}] error message [{2}]".format()
    file_name,exc_tb.lineno,str(error)

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_datils(error_message,error_details=error_details)

    def __init__(self):
        return self.error_message

