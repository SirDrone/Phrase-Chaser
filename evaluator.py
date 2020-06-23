#!/usr/bin/env python3

import pandas as pd
import os

from sanitization_pack.auto_detector import get_list_of_csv_files


csvs = get_list_of_csv_files()

for csv in csvs:
	sanitized_csv = "sanitized_{}".format(csv)
	if not os.path.isfile(sanitized_csv):
		raise FileNotFoundError("Cannot compare column changes.\n"\
		"{} does not exist for {}.  Please run the driver first". \
		format(sanitized_csv, csv))
	else:
		print("Comparing {} and {}:".format(csv, sanitized_csv))
		df1 = pd.read_csv(csv)
		df2 = pd.read_csv(sanitized_csv)

		column_list = df1.columns.values
		differing_columns = []
		for column in column_list:
			if df1[column].all() != df2[column].all():
				differing_columns.append(column)

		print("\tColumns Changed:\n\t{}\n".format(differing_columns))
