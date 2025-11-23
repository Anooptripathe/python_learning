import os
import logging
from custom_exceptions import Filetoosmall

logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def vaildate_file_size(file_path,min_file_size):
    file_size=os.path.getsize(file_path)/(1024*1024)
    logging.info(f"Checking file size:{file_size:.2f}")

    if file_size<min_file_size:
        logging.error(f"File size:{file_size:.2f} is less than required size:{min_file_size:.2f}")
        raise Filetoosmall(file_size,min_file_size)
    logging.info("File size is lesser than limit.")
    return True

def process_file(file_path):
    try:
        logging.info(f"Starting processing of the file:{file_path}")
        vaildate_file_size(file_path=file_path,min_file_size=2)
        logging.info("Processing file... (business logic here)")

    except Filetoosmall as e:
        logging.error(f"Custom exception caught:{e}")
        print(f"Error:{e}")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("Unexpected error occurred:", e)
    
    else:
        logging.info("File processed successfully.")
        print("File processed successfully!")


file_path=r'C:\Users\anoop\OneDrive\Documents\raw_store_transactions.csv'

if __name__=="__main__":
    process_file(file_path=file_path)