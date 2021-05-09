# import csv
import csv
  
# open input CSV file as source
# open output CSV file as result
with open("copy3.csv", "r") as source:
    reader = csv.reader(source)
      
    with open("copy4.csv", "w") as result:
        writer = csv.writer(result)
        for r in reader:
            
            # Use CSV Index to remove a column from CSV
            #r[3] = r['year']
            writer.writerow(r[0])