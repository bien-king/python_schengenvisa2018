import csv
from pprint import pprint

def read_data():
    data = []

    with open('visa.csv', 'r') as visa_csv:
        spreadsheet = csv.DictReader(visa_csv)
        for row in spreadsheet:
            data.append(row)

    return data


def run():
    data = read_data()

    total_visa_application = []
    for row in data:
        visa_applied = int(row['application'])
        total_visa_application.append(visa_applied)

    total_application = sum(total_visa_application)

    print('Total visa application: {}'.format(total_application))


    total_visa_issued = []
    for row in data:
        visa_issued = int(row['application']) - int(row['not_issued'])
        total_visa_issued.append(visa_issued)

    total_issued = sum(total_visa_issued)
    print('Total visa issued list per country: {}'.format(total_visa_issued))
    print('Total visa issued: {}'.format(total_issued))


    # list of schengen countries and visa issued and % of the total visa issued
    # country_list_percent = []
    # for row in data:
    #     visa_issued_percent = int(row[total_visa_issued]) / int(row[total_issued])
    #     country_list_percent.append(visa_issued_percent)
    # 
    # print(tabulate[country], [visa_issued_percent])



    # average total of the visa application
    average_visa_issued = []
    for row in data:
        ave_issued = (int(row['application']) - int(row['not_issued']))
        average_visa_issued.append(ave_issued)

    total_ave = sum(average_visa_issued) / len(row['application'])
    print('Average visa issued: {}'.format(total_ave))


    # highest and lowest
    max_visa_issued = []
    for row in data:
        max_issued = (int(row['application']) - int(row['not_issued']))
        max_visa_issued.append(max_issued)

    total_max = max(max_visa_issued)
    print('Maximum value visa issued: {}'.format(total_max))

    min_visa_issued = []
    for row in data:
        min_issued = (int(row['application']) - int(row['not_issued']))
        min_visa_issued.append(min_issued)

    total_min = min(min_visa_issued)
    print('Minimum value visa issued: {}'.format(total_min))


run()


