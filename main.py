import argparse
import csv

from zer0.adapter.bank_to_zer0 import BankCsvReader


parser = argparse.ArgumentParser()


parser.add_argument("-b", "--bank", help="Bank so the proper bank adapter is loaded", choices=['cibc', 'tangerine'])
parser.add_argument("-c", "--account", help="Bank account")
parser.add_argument("-f", "--file", help="Input file")


args = parser.parse_args()



b2_zer0 = BankCsvReader.get_reader(args.bank)
zer0 = []

with open(args.file) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        zer0.append(b2_zer0.to_zer0(row))




output_file = "{}_{}_zer0.csv".format(args.file.replace(".csv", ""), args.account)

with open(output_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    for d in zer0:
        d.Account = args.account
        writer.writerow(d.to_zer0())




