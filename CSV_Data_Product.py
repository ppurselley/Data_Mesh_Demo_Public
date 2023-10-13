import pandas as pd
import csv
import random
from pathlib import Path
import fire 


######################## second attempt

# CSV Writer Function
def write_csv_header(header, folder, file_name):
    with open(file_name,'wt') as csvFile:
        writer = csv.DictWriter(csvFile,fieldnames=header,lineterminator='\n')
        writer.writeheader()
        for i in range(records):
            writer.writerow({
                "schema" : "Core Operations",
                "file_version" : random.choice(['v_1']),
                "location_csv" : random.choice(['data_folder']),
                "data_owner" : random.choice(['Carol','Bianca','Cindy']),
                "data_domain" : "Core Operations"
            })
        print(f'Hello from the register data prduct function')

# Data Product Registration Function
def register_csv_port(name):
    header_list = []
    folder = "data_folder/"
    file_name = f'{name}.csv'
    write_csv_header(header,folder,file_name)

# register the data product
def register_data_product(name="default_name"):
    
    print(f'Registering {name} CSV port...')
    register_csv_port(name)


if __name__ == "__main__":
    records = 10
    header = ["schema","file_version","location_csv","data_owner","data_domain"]
    fire.Fire(register_data_product)

#########################
######################### first attempt
'''
# 
fpath = Path('Data_Mesh/data_folder')
fpath.mkdir(parents=True,exist_ok=True)

def register_data_product (records, headers, name):
    with fpath.open(name,'wt') as csvFile:
        writer = csv.DictWriter(csvFile,fieldnames=headers,lineterminator='\n')
        writer.writeheader()
        for i in range(records):
            writer.writerow({
                "schema" : "Core Operations",
                "file_version" : random.choice(['v_1']),
                "location_csv" : random.choice(['data_folder']),
                "data_owner" : random.choice(['Carol','Bianca','Cindy']),
                "data_domain" : "Core Operations"
            })
        print(f'Hello from the register data prduct function')

if __name__ == '__main__':
    records = 10
    headers = ["schema","file_version","location_csv","data_owner","data_domain"]
    name = 'file_name'
    register_data_product(records, headers, name)
    print(f'CSV generation complete!')
'''