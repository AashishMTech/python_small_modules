
#I've tried the above version for writing and reading and it didn't work in Python 3.3 due to "bytes" error. However, after some trial and error I could get the following to work. Maybe it also helps others:

import csv
import gzip
import json
import io


with gzip.open("test.csv.gz", "w", compresslevel=9) as file:
    with open("test.json", "r+") as json_file:
        json_list= json.load(json_file)
        writer = csv.writer(io.TextIOWrapper(file, newline="", write_through=True))
        writer.writerow(json_list[0].keys())
        for json in json_list:
            writer.writerow(json.values())
    
print("done")
    

    