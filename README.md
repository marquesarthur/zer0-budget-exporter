# zer0-budget-exporter
Exports csv data to zero format


# Setup:


1. Follow the steps described in the pygsheets documentation for [authorization](https://pygsheets.readthedocs.io/en/latest/authorization.html)
    * Use the [Service Account](Service Account) authorization method
    * Make sure to add both the Google Sheets and Drive API when configuring `API & Services`
    
2. Place the Service Account server json under `./config` with the name `service_account_credentials.json`

3. Create a second json under `./config` with the name `spreadsheet.json` 

    ```json
    {
      "spreadsheet-key": "yada yada yada",
      "register-worksheet": "Register"
    }
    ```
   
4. Update the spreadsheet key with your Zer0 key. Instructions available [here](https://support.qooqee.com/hc/en-us/articles/360000471814-How-do-I-find-my-Google-Sheet-Key-)

5. Open `service_account_credentials.json`, go to your Zer0 spreadsheet and share the spreadsheet with the email under the key `client_email`


# Usage

Run the script with python, as in the example:

    `python main.py -f input.csv -c -a "Zer0 account identifier" -b bank_adapter`

where:

* input.csv - is the spreadsheet containing your bank transactions.   
* Zer0 account identifier - is one of your Zer0 accounts. Learn more [here](https://sites.google.com/view/zer0/guide?authuser=0)    
* bank_adapter - is a key indicating how your csv will be parsed. Each bank has one adapter. See more below

There are optional flags for credit card statements (`-c or -ccard`). This is a `true` or `false` flag that adjusts your adapter to parsing csv files from your bank credit card. In the future, I might remove this flag and create adapters specific for credit cards.



# Contributing:

If you want to contribute, make a pull request adding new adapters. 

Adapters are divided by country. At the moment, there are adapters only for `CA`

An adapter should follow the template:

```python
from datetime import datetime
from zer0.data import Zer0Data

class TempalteAdapter(object):

    def __init__(self):
        self.date_idx = 0
        self.description_idx = 1
        self.outflow_idx = 2
        ...

    def to_date(self, dt):
        datetime_object = datetime.strptime(dt, '%Y-%m-%d') # data format used in the bank statement
        return datetime_object

    def to_zer0(self, row):
        output = Zer0Data()
        output.Date = self.to_date(row[self.date_idx])
        output.Payee = row[self.description_idx]
        output.Inflow = row[self.inflow_idx]
        output.Outflow = row[self.outflow_idx]
        return output
```

The fields in this template are the bate minimum needed to import data to Zer0. Feel free to create more refined adapters that fit your needs.

Add your adapter to the list of valid banks on `bank_to_zer0.py`. At the moment, each bank should have a unique name

