class Filetoosmall(Exception):
    def __init__(self,file_size,min_size):
        message=f"file size {file_size}MB iss less tha min size:{min_size}MB"
        super().__init__(message)  # super is a function


