import csv
import time
import pandas as pd


def unitconverted():
    print('Unit Converter Started...')
    time.sleep(6)

    df = pd.read_csv("CSV/dawrf_star_data.csv")

    mass_value = df['dawf_Star_Mass'].tolist()
    radius_value = df['dawf_Star_Radius'].tolist()

    name = df['dawf_Star_name'].tolist()
    distance = df['dawf_Star_Distance'].tolist()
    mass = []
    radius = []

    for data in mass_value:
        try:
            value = float(data)*0.000954588
            mass.append(value)
        except:
            mass.append('unknown')

    for data in radius_value:
        try:
            value = float(data)*0.102763
            radius.append(value)
        except:
            radius.append('unknown')

    print('Making a Unit Converted csv file... ')
    time.sleep(3)

    rows = pd.DataFrame(list(zip(name, distance, mass, radius)), columns=[
        'dawf_Star_name', 'dawf_Star_Distance', 'Mass', 'Radius'])

    rows.to_csv('CSV/unite_converted.csv')

    print('Unit Converted Successfully.')





def merging():
    print('\n\nData Marging Started...')
    time.sleep(3)

    dataset_1 = []
    dataset_2 = []

    with open('CSV/unite_converted.csv', 'r') as f:
        csv_reader = csv.reader(f)

        for i in csv_reader:
            dataset_1.append(i)

    with open('CSV/star_data.csv', 'r') as f:
        csv_reader = csv.reader(f)

        for i in csv_reader:
            dataset_2.append(i)

    header_1 = dataset_1[0]
    header_2 = dataset_2[0]

    star_data_1 = dataset_1[1:]
    star_data_2 = dataset_2[1:]

    headers = header_1 + header_2

    final_data = []

    for idx, data in enumerate(star_data_2):
        final_data.append(star_data_1[idx] + star_data_2[idx])

    print('Data Merging Completed')
    time.sleep(2)
    
    print('Uploading Data to the final.csv file.... ')
    time.sleep(5)

    with open('final.csv', 'a+') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(final_data)

    print('Data Uploaded Successfully.')
    time.sleep(5)


unitconverted()
merging()
