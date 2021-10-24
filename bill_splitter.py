from abc import ABC, abstractmethod
from datetime import datetime
from functools import reduce

import pandas as pd


class BillSplit:
    def __init__(self):
        self.bills = []
        self.people = []

    def add_bill(self, bill):
        self.bills.append(bill)

    def add_person(self, person):
        self.people.append(person)

    def combine_bills(self):
        bills_df = reduce(
            lambda left, right:
            pd.merge(left, right, on='date', how='outer'),
            [bill.create_row() for bill in self.bills]
        )
        bills_df['total_daily_bills'] = bills_df.sum(axis=1)
        return bills_df

    def combine_people(self):
        people_df = reduce(
            lambda left, right:
            pd.merge(left, right, on='date', how='outer'),
            [person.create_row() for person in self.people]
        )
        people_df['n_people'] = people_df.count(axis=1)
        return people_df

    def split_bill(self):
        merged_df = pd.merge(self.combine_bills(), self.combine_people(), on='date', how='left')
        for person in self.people:
            person_only_df = merged_df[~merged_df[person.name].isna()]
            print(f"{person.name} split: {(person_only_df['total_daily_bills'] / person_only_df['n_people']).sum()}")

    @property
    def total(self):
        return sum(bill.amount for bill in bs.bills)


class Bill:
    def __init__(self, name: str, amount: float, date_start: str, date_end: str):
        self.name = name
        self.amount = amount
        self.date_start = date_start
        self.date_end = date_end

    def create_row(self):
        start = datetime.strptime(self.date_start, "%m/%d/%Y")
        end = datetime.strptime(self.date_end, "%m/%d/%Y")
        n_days = (end - start).days + 1
        daily_amount = self.amount / n_days
        time_series = pd.date_range(start=start, end=end)
        bill_df = pd.DataFrame(time_series, columns=['date'])
        bill_df[f"{self.name}_daily_amount"] = daily_amount
        bill_df.set_index('date', inplace=True)
        return bill_df


class Person:
    def __init__(self, name: str, date_move_in: str = None, date_move_out: str = None):
        self.name = name
        self.date_move_in = date_move_in
        self.date_move_out = date_move_out

    def create_row(self):
        if self.date_move_in:
            start = datetime.strptime(self.date_move_in, "%m/%d/%Y")
        else:
            start = datetime.strptime('9/16/1916', "%m/%d/%Y")

        if self.date_move_out:
            end = datetime.strptime(self.date_move_out, "%m/%d/%Y")
        else:
            end = datetime.strptime('9/16/2069', "%m/%d/%Y")

        time_series = pd.date_range(start=start, end=end)
        person_df = pd.DataFrame(time_series, columns=['date'])
        person_df[self.name] = True
        person_df.set_index('date', inplace=True)
        return person_df


bs = BillSplit()

bs.add_bill(Bill(name='scmu', amount=0.0, date_start='', date_end=''))
bs.add_bill(Bill(name='pge', amount=0.0, date_start='', date_end=''))
bs.add_bill(Bill(name='att', amount=0.0, date_start='', date_end=''))


bs.add_person(Person(name='alli'))
bs.add_person(Person(name='ryan'))
bs.add_person(Person(name='sylv'))
bs.add_person(Person(name='nick', date_move_out='8/21/2021'))
bs.add_person(Person(name='owen', date_move_out='7/31/2021'))
bs.add_person(Person(name='hallie', date_move_in='8/22/2021'))
bs.add_person(Person(name='riv', date_move_in='8/22/2021'))
bs.add_person(Person(name='devin', date_move_out='9/24/2021'))
bs.add_person(Person(name='shroombus', date_move_in='9/24/2021'))
bs.split_bill()
