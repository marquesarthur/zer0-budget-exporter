# 2020-01-02	Internet Banking INTERNET TRANSFER 000000268734	2106.49
# 2019-12-31	Branch Transaction SERVICE CHARGE DISCOUNT		3.9
from datetime import datetime
from zer0.data import Zer0Data


class CibcAdapter(object):

    def __init__(self):
        self.date_idx = 0
        self.description_idx = 1
        self.outflow_idx = 2
        self.inflow_idx = 3

    def to_date(self, dt):
        datetime_object = datetime.strptime(dt, '%Y-%m-%d')
        return datetime_object

    def to_zer0(self, row):
        output = Zer0Data()
        output.Date = self.to_date(row[self.date_idx])
        output.Payee = row[self.description_idx]
        output.Inflow = row[self.inflow_idx]
        output.Outflow = row[self.outflow_idx]
        return output
