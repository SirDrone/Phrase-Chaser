#!/usr/bin/env python3

import os
import re
import pandas as pd

from sanitization_pack.functions import *


#########################################################################################################
#					   Helper Function Section					#
#########################################################################################################


def options_are_valid(options):
	if type(options) != list:
		raise TypeError("Object supplied to options must be a list")
	elif len(options) != 9:
		raise IndexError("List supplied to options must contain 9 booleans")
	elif any(type(x) != bool for x in options):
		raise TypeError("All items supplied in the options list must be True/False")
	elif True not in options:
		raise ValueError("Why would you even want to run this?" \
		"There's nothing you set to sanitize..")
	else:
		return True


def get_list_of_csv_files():
	local_files = os.listdir()
	list_of_supposed_csvs = []
	for local_file in os.listdir():
		if ".csv" in local_file:
			if "sanitized" not in local_file:
				if not local_file.startswith("."):
					list_of_supposed_csvs.append(local_file)

	if len(list_of_supposed_csvs) == 0:
		raise FileNotFoundError("Local CSV file not found.  Exiting..")

	return list_of_supposed_csvs


#A helper method used to both determine the existence of start (or end) columns,
#and return them if they exist
def time_column_exists(columns, end=False):
	stamp_tags = ["DATE", "DAY", "STAMP", "TIME"]
	end_date_tags = ["CLOSING", "END", "ENDING", "FINISH", "FINISHING"]
	start_date_tags = ["BEGINNING", "FIRST", "INITIAL", "START"]
	
	for column in columns:
		if any(tag in column.upper() for tag in stamp_tags):
			if end:
				if any(tag in column.upper() for tag in end_date_tags):
					return column
			else:
				if any(tag in column.upper() for tag in start_date_tags):
					return column

	return False


#A helper method that, provided start and end date columns have already been tracked,
#creates sanitized versions of these items in tandem, so that start < end
def create_start_and_end_date_columns(df, start_column, end_column):
	size = len(df.values)
	start_column_index = list(df.columns).index(start_column)
	end_column_index = list(df.columns).index(end_column)
	row_index = 0
	while row_index < size:
		start_date = create_stamp()
		end_date = create_end_date(start_date)
		df.iloc[row_index, start_column_index] = start_date
		df.iloc[row_index, end_column_index] = end_date		
		row_index += 1


#The final helper method that ensures we only have unique IDs.
#Let it be said this is merely a guarantee, as we have over
#285 decillion possible IDs
def create_unique_ids(df):
	size = len(df.values)
	if size > 285794257465697108736779475033784320:
		raise IndexError("I don't even know how you have a dataframe big enough" \
		"to break 285 decillion rows but somehow you did it.  Gratz.\n" \
		"Cannot sanitize IDs..")

	unique_ids = []
	row_index = 0

	while row_index < size:
		current_id = create_id()
		while current_id in unique_ids:
			current_id = create_id()
		unique_ids.append(current_id)
		row_index += 1

	return unique_ids
	

#########################################################################################################
#					    Main Detector Code						#
#########################################################################################################


#This function automatically picks up any CSVs it sees,
#and then attempts to decipher how best to assign dummy values
#for the respective columns to the sanitized version
def auto_create_sanitized_CSVs(options):
	if options_are_valid(options):
		sanitize_phone_numbers = options[0]
		sanitize_ids = options[1]
		sanitize_dates = options[2]
		sanitize_emails = options[3]
		sanitize_ips = options[4]
		sanitize_booleans = options[5]
		sanitize_addresses = options[6]
		sanitize_names = options[7]
		sanitize_numbers = options[8]

	csv_files = get_list_of_csv_files()
	for csv_file in csv_files:
		try:
			df = pd.read_csv(csv_file)
			column_list = df.columns
			df[column_list[0]].values[0]
		except:
			raise TypeError("{} is not a valid CSV".format(csv_file))

		start_column = time_column_exists(column_list)
		end_column = time_column_exists(column_list, end=True)

		unique_tags = ["ID", "UNIQUE", "SSN", "NO.", "MAC"]
		stamp_tags = ["DATE", "TIME", "STAMP", "DAY"]
		ip_tags = [" IP", "IP "]
		boolean_tags = [" HAS", "HAS ", "IS ", " IS"]
		last_name_tags = ["SUR", "L"]
		ambiguous_address_tags = ["SENDER", "RECIPIENT", "ADDRESS"]

		#If we find a predetermined tag in our column, and if the sanitization option
		#is set, we'll apply one of our sanitzation pack's appropriate functions in 
		#creating our sanitized CSV.
		for column in column_list:
			if "PHONE" in column.upper():
				if sanitize_phone_numbers:
					#Lambdas are useful for the apply call, as an argument would
					#have been passed to our functions otherwise, which is a no-go.
					df[column] = df[column].apply(lambda x: create_phone_number())

			elif any(tag in column.upper() for tag in unique_tags):
				if sanitize_ids:
					df[column] = create_unique_ids(df)

			elif any(tag in column.upper() for tag in stamp_tags):
				if sanitize_dates:
					if start_column and end_column:
						if column == start_column:
							create_start_and_end_date_columns( \
							df, start_column, end_column)
						elif column == end_column:
							#Either we've already applied the correlated stamps,
							#or can wait until we hit the designated start_column
							continue	
						else:
							#We just have a normal date column
							df[column] = df[column].apply( \
							lambda x: create_stamp())
					else:
						#Likewise here, the date column is normal, and there's no
						#start or end dates
						df[column] = df[column].apply(lambda x: create_stamp())

			elif "EMAIL" in column.upper():
				if sanitize_emails:
					df[column] = df[column].apply(lambda x: create_email_address())

			elif (any(tag in column.upper() for tag in ip_tags) or column.upper()=="IP"):
				if sanitize_ips:
					df[column] = df[column].apply(lambda x: create_ip())

			elif any(tag in column.upper() for tag in boolean_tags):
				if sanitize_booleans:
					df[column] = df[column].apply(lambda x: create_boolean())

			elif any(tag in column.upper() for tag in ambiguous_address_tags):
				first_value = df[column].values[0]
				ip_matches = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", \
				first_value) #Finds items like 192.168.14.12
				if ((len(ip_matches) > 0) and (sanitize_ips)): #if ip
					df[column] = df[column].apply(lambda x: create_ip())
				elif (("@" in first_value) and (sanitize_emails)): #if email
					df[column] = df[column].apply(lambda x: create_email_address())
				elif sanitize_addresses: #otherwise assume is postal address; MAC is ID
					df[column] = df[column].apply(lambda x: create_address())

			elif "NAME" in column.upper():
				if sanitize_names:
					if (("FULL" in column.upper()) or (column.upper() == "NAME")):
						df[column] = df[column].apply(lambda x: create_name())
					elif "F" in column.upper(): #FNAME or FIRST NAME
						df[column] = df[column].apply(lambda x: create_first_name())
					elif any(tag in column.upper() for tag in last_name_tags):
						df[column] = df[column].apply(lambda x: create_last_name())

			else:
				try:
					#This next test will see if we have numbers for our column.
					#I'd use type(), but these values could be any of the numpy classes.
					#This is simpler.
					int(df[column].values[0])
					max_value = int(max(df[column].values))
					if sanitize_numbers:
						df[column] = df[column].apply(lambda x: create_number())

				except ValueError:
					first_value = str(df[column].values[0]).upper()
					if ((first_value == "") or (first_value == "NAN") or \
					(first_value == " ")):
						df[column] = df[column].apply(lambda x: "")

					#Other than this, I'd wager the column doesn't need sanitizing :P

		df.to_csv("sanitized_{}.csv".format(csv_file[:-4]), index=False)
