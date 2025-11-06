import os
import datetime

def extract_metadata(file_path):
    print("File Metadata:")
    print(f"Name: {os.path.basename(file_path)}")
    file_size = os.path.getsize(file_path)
    print(f"Size: {file_size/1024/1024:.2f} MB ({file_size/1024:.2f} KB)")
    created_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
    modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    accessed_date = datetime.datetime.fromtimestamp(os.path.getatime(file_path))
    print(f"Created: {created_date.strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"Modified: {modified_date.strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"Accessed: {accessed_date.strftime('%d-%m-%Y %H:%M:%S')}")
    print("------------------------")
 
def main():
    directory = '/home/kali/Downloads' 
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        extract_metadata(file_path)

if __name__ == "__main__":
    main()

