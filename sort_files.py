import os

# Function that extract name from a file of formate ddmmyyy_filename_hhmmss
def extract_name(file_name):
    city_name = file_name[file_name.find("_")+1:]
    city_name = city_name[:city_name.find("_")]
    return city_name
