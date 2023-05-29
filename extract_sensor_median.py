import csv
import glob
import os
import numpy
import sys

def median(list_temp):
    return numpy.median(numpy.array(list_temp))

def main(args):
        
    path = args[0]
    data = []
    data.append(['csv', 'Red Clear Median', 'Blue Clear Median','Temperature', 'Battery'])


    for i,filename in enumerate(glob.glob(os.path.join(path, '*.csv'))):
        print (filename, i)
        csv_name = filename.split('/')[-1]
        if 'output' in filename:
            continue

        with open(filename,'rU') as f:
            reader = csv.reader(f)

            blue_clear = [] #Blue LED, Clear Channel
            blue_seq = [] #Blue LED, Sequence number
            red_clear = [] #Red LED, Clear Channel
            red_seq = [] #Red LED, Sequence number
            temperature = [] #Temperature recorded
            battery = [] #battery voltage
            sensor_data_start = False

        
            for i, row in enumerate(reader):
                if "Timestamp" in row[0]:
                    sensor_data_start = True
                
                elif sensor_data_start and "BLUE" in row[6]:
                    blue_clear.append(int(row[4]))
                    blue_seq.append(int(row[5]))
                    temperature.append(float(row[7]))
                    battery.append(float(row[8]))

                elif sensor_data_start and "RED" in row[6]:
                    red_clear.append(int(row[4]))
                    red_seq.append(int(row[5]))
                    temperature.append(float(row[7]))
                    battery.append(float(row[8]))

                #print row

        data.append([csv_name, median(red_clear[0:]), median(blue_clear[0:]), median(temperature[0:]), median(battery[0:])])

        output_file = path +  '/output.csv'


    with open(output_file,'w+') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    
if __name__ == "__main__":
    main(sys.argv[1:])
