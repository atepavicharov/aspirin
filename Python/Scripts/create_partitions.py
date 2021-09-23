from datetime import datetime
import pandas as pd

date_from = datetime.strptime(input("date from (yyyy-mm-dd):"), "%Y-%m-%d")
date_to = datetime.strptime(input("date_to (yyyy-mm-dd):"), "%Y-%m-%d")
term = input("term (month/year):")


def days_between(d1, d2, t):
    if t == "month":
        return (d2.year - d1.year) * 12 + (d2.month - d1.month)
    else:
        return d2.year - d1.year


interval = days_between(date_from, date_to, term)

current_dt = date_from
partition_func = "alter table <table>\npartition by range(to_days(<column>)) ("

for i in range(interval):
    if term == "month":
        next_dt = current_dt + pd.DateOffset(months=1)
        if i == 0:
            partition_func = partition_func + "\npartition p_before_" + current_dt.strftime("%Y_%m") + \
                             " values less than (to_days('" + current_dt.strftime("%Y-%m-%d") + "')),"

            partition_func = partition_func + "\npartition p_" + current_dt.strftime("%Y_%m") + \
                             " values less than (to_days('" + next_dt.strftime("%Y-%m-%d") + "')),"
        else:
            partition_func = partition_func + "\npartition p_" + current_dt.strftime("%Y_%m") + \
                             " values less than (to_days('" + next_dt.strftime("%Y-%m-%d") + "')),"

        current_dt = current_dt + pd.DateOffset(months=1)

    else:
        # year
        next_dt = current_dt + pd.DateOffset(years=1)
        if i == 0:
            partition_func = partition_func + "\npartition p_before_" + current_dt.strftime("%Y") + \
                             " values less than (to_days('" + current_dt.strftime("%Y-01-01") + "')),"
            partition_func = partition_func + "\npartition p_" + current_dt.strftime("%Y") + \
                             " values less than (to_days('" + next_dt.strftime("%Y-01-01") + "')),"
        else:
            partition_func = partition_func + "\npartition p_" + current_dt.strftime("%Y") + \
                             " values less than (to_days('" + next_dt.strftime("%Y-01-01") + "')),"

        current_dt = current_dt + pd.DateOffset(years=1)

partition_func = partition_func + "\nPARTITION p_future VALUES LESS THAN MAXVALUE\n);"

print(partition_func)
