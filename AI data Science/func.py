import csv
def read_csv(file_name,header= True):
    data=list(csv.reader(open(file_name,encoding="utf-8")))
    if header== True:
        return data[0],data[1:]
    else:
        return data