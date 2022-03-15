import csv

def demand():
    filename1 = 'demand.csv'
    # | mtime | A B C D E F G H I J |
    # demand = {}
    demand = []
    with open(filename1, 'r') as f:
        reader = csv.reader(f)
        #print(type(reader))
        for row in reader:
            if reader.line_num == 1:
                client_list = list(row[1:])
                continue
            # demand[row[0]] = row[1:]
            demand.append(list(row[1:]))
        #print(row)
    # print(client_list)
    # print(demand)
    return demand,client_list

def site_bandwidth():
    filename2 = 'site_bandwidth.csv'
    # | site_name | bandwidth |
    site_bandwidth = {}
    with open(filename2, 'r') as f:
        reader = csv.reader(f)
        #print(type(reader))
        for row in reader:
            if reader.line_num == 1:
                continue
            site_bandwidth[row[0]] = row[1:]
        #print(row)
    site_list = list(site_bandwidth.keys())
    # print(site_bandwidth)
    # print(site_list)
    return site_bandwidth, site_list

def qos():
    filename3 = 'qos.csv'
    # | site_name | A B C D E F G H I J |
    qos_origin = []
    with open(filename3, 'r') as f:
        reader = csv.reader(f)
        # print(type(reader))
        for row in reader:
            if reader.line_num == 1:
                continue
            # qos_origin[row[0]] = row[1:]
            qos_origin.append(list(row[1:]))
        # print(row)
    # print(qos_origin)
    # transpose
    qos = []
    for i in range(len(qos_origin[0])):
        new_row = []
        for row in qos_origin:
            new_row.append(row[i])
        qos.append(new_row)
    return qos