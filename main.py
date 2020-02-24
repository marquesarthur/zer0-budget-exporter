import argparse
import csv
import pygsheets
import json
import pandas as pd

from zer0.adapter.bank_to_zer0 import BankCsvReader
from zer0.data import ZER0_COLUMNS
from zer0.gsheet import next_available_row

with open('./config/spreadsheet.json') as f:
    cfg = json.load(f)
    gc = pygsheets.authorize(service_file='./config/service_account_credentials.json')

parser = argparse.ArgumentParser()

parser.add_argument("-b", "--bank", help="Bank so the proper bank adapter is loaded", choices=['cibc', 'tangerine'])
parser.add_argument("-a", "--account", help="Bank account")
parser.add_argument("-f", "--file", help="Input file")
parser.add_argument("-c", "--ccard", help="Whether the input is a credit card", action='store_true')
parser.add_argument("-v", "--verbose", help="If print statements should be part of the program output",
                    action='store_true', default=False)

args = parser.parse_args()

b2_zer0 = BankCsvReader.get_reader(args.bank)
new_rows = []

if args.ccard:
    b2_zer0.reader.cc = args.ccard

with open(args.file) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        data = b2_zer0.to_zer0(row)
        data.Account = args.account

        new_rows.append(data)

sh = gc.open_by_key(cfg["spreadsheet-key"])
wks = sh.worksheet_by_title(cfg["register-worksheet"])

row_idx = next_available_row(wks)

lst = [d.to_zer0() for d in new_rows]

df = pd.DataFrame(lst, columns=ZER0_COLUMNS)

wks.set_dataframe(df, "A{}".format(row_idx), copy_head=False, extend=True)

