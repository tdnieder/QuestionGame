# -*- coding: utf-8 -*-
import csv


# ------------------------------------------------
# Creates a list of arrays. Each array contains one line/row of the csv file.
# returns list object
# ------------------------------------------------
def csv_read(file_path):
    with open(file_path, newline='', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        line = []
        for row in reader:
            line.append(row)
        return line
