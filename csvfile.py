# -*- coding: utf-8 -*-
# !/usr/bin/env python
import csv


def rows_to_csv(filepath, rows, columns=[]):
    """
    Takes list of dictionaries and filepath and outputs a spreadsheet
    Params:
        rows(list):
            A list of dictionaries

        columns(list):
            A list of the key in the rows that you want to export in the csv file
            by default it will display all

    """
    csv_columns = columns

    dict_data = {}
    for i, item in rows:
        dict_data[i] = item

    csv_file = filepath
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                w_data = dict_data[data]
                for col in list(w_data):
                    if col not in csv_columns:
                        del w_data[col]
                writer.writerow(w_data)
    except IOError:
        print("I/O error")


def csv_to_rows(filepath):
    """
    Converts csv file to list of dicts.
    """
    with open(filepath, 'r') as file:
        csv2dict = csv.reader(file)  # 'Artist', 'ID', 'Stock number', 'Title', 'Dimensions'
        next(csv2dict)
        csv2dict = {rows[0]: {
            'Artist': rows[1],
            'ID': rows[2],
            'Stock number': rows[3],
            'Title': rows[4],
            'Dimensions': rows[5]
        } for rows in csv2dict}
    return csv2dict.items()


def get_distinct_artist(rows):
    s = set()
    for i, item in rows:
        for col in list(item):
            if col == 'Artist' and item[col].strip() != "":
                s.add(item[col])

    return s


def get_initials_dic(rows):

    artists = get_distinct_artist(rows)

    init_dict = {}
    for item in artists:
        initial = None
        name_split = item.split()
        name_cnt = len(name_split)
        if name_cnt == 1:
            initial = name_split[0][:2].upper()
        elif name_cnt > 1:
            first = name_split[0][:1]
            last = name_split[-1][:1]
            initial = first + last

        while True:
            if not is_initial_exist(init_dict, initial):
                break
            for c in name_split[0][1:]:
                print('Exist Found {}, Next is {}{}, Dict is {}'
                      .format(initial, name_split[0][:1].upper(), c.upper(), init_dict.items()))
                initial = name_split[0][:1].upper() + c.upper()
                if not is_initial_exist(init_dict, initial):
                    break

        init_dict[item] = initial

    return init_dict


def is_initial_exist(initials_dict, initial):
    for k, v in initials_dict.items():
        if v == initial:
            return True
    return False
