import csv

class FileSchemaMismatchError(Exception):

    def __init__(self, expected,received):
        self.expected=expected
        self.received=received

        message=(
            f"Schema Mismatch! \n"
            f"Expected Columns : {expected} \n"
            f"Received Columns : {received} \n"
        )

        super.__init__(message)

def validate_schema(received_cols,expected_cols):
    if set(received_cols)!=set(expected_cols):
        raise FileSchemaMismatchError(expected_cols,received_cols)
    return True

def process_files(file_path,expected_cols):
    with open(file_path,"r") as f:
        reader=csv.DictReader(f)
        received_cols = reader.fieldnames


        # Validate schema
        validate_schema(received_cols, expected_cols)

        print("Schema is valid! Processing file...")
        for row in reader:
            print(row)  # dummy processing


if __name__=="__main__":
    expected_schema=['STORE_ID','STORE_LOCATION','PRODUCT_CATEGORY','PRODUCT_ID','MRP','CP','DISCOUNT','SP','Date']
    file_path=r'C:\Users\anoop\OneDrive\Documents\raw_store_transactions.csv'

    try:
        process_files(file_path,expected_schema)
    except FileSchemaMismatchError as e:
        print("Custom exception caught")
        print(e)
    except Exception as e:
        print("Other Error:", e)
    
    finally:
        print("Reached end of code")




