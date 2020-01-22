# 12/21/2018	OTHER	INTERAC e-Transfer From: ARTHUR 	Transferred	2500
# 12/21/2018	OTHER	Referral Bonus	Transferred	50
from datetime import datetime
from zer0.data import Zer0Data


class TangerineAdapter(object):

    def __init__(self):
        self.date_idx = 0
        self.description_idx = 2
        self.memo_idx = 3
        self.inflow_outflow_idx = 4


    def to_date(self, dt):
        datetime_object = datetime.strptime(dt, '%m/%d/%Y')
        return datetime_object

    def strip_description(self, data):
        return data.replace("Interac - Purchase -", "")\
            .replace("INTERAC e-Transfer To:", "") \
            .replace("INTERAC e-Transfer From:", "") \
            .strip()

    def strip_memo(self, data):
        return data.replace("From ", "")\
            .strip()



    def to_zer0(self, row):
        output = Zer0Data()
        output.Date = self.to_date(row[self.date_idx])

        if row[self.memo_idx]:
            output.Payee = self.strip_memo(row[self.memo_idx])
        else:
            output.Payee = self.strip_description(row[self.description_idx])
        if row[self.inflow_outflow_idx].startswith("-"):
            output.Outflow = row[self.inflow_outflow_idx].replace("-", "")
        else:
            output.Inflow = row[self.inflow_outflow_idx]
        return output

