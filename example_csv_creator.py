#!/usr/bin/env python3

import pandas as pd
from random import choice

from sanitization_pack.functions import *


def create_example_email_csv(number_of_rows=72):
	if type(number_of_rows) != int:
		raise TypeError("number_of_rows must be an int")
	elif number_of_rows < 1:
		raise ValueError("number_of_rows cannot be less than one")

	column_names = ["Message ID", "Start date", "End date", "Sender", "Message size", \
	"Subject", "Direction", "Attachments", "Recipient address", \
	"Event target", "Event date", "Event status", "Sender IP address", \
	"Has encryption"]
	
	message_ids = []
	start_dates = []
	end_dates = []
	senders = []
	message_sizes = []
	subjects = []
	directions = []
	attachments = []
	recepients = []
	event_mediums = []
	event_dates = []
	event_statuses = []
	sender_ips = []
	has_encryption = []

	current_index = 0

	while current_index < number_of_rows:
		message_ids.append(create_id())
		start_date = create_stamp()
		start_dates.append(start_date)
		end_dates.append(create_end_date(start_date))
		senders.append(create_email_address())
		message_sizes.append(create_number())
		subjects.append(create_email_subject())
		directions.append(create_email_direction())
		attachments.append(create_number(0,3))
		recepients.append(create_email_address())
		event_mediums.append("GMAIL_INBOX")
		event_dates.append(start_date)
		event_statuses.append("DELIVERED")
		sender_ips.append("")
		has_encryption.append("Not encrypted")

		current_index += 1

	data_lists = [message_ids, start_dates, end_dates, senders, message_sizes, \
	subjects, directions, attachments, recepients, event_mediums, \
	event_dates, event_statuses, sender_ips, has_encryption]

	pd.DataFrame(data=dict(zip(column_names, data_lists)), columns=column_names). \
	to_csv("email_example.csv", index=False)


def create_example_customer_csv(number_of_rows=72):
	if type(number_of_rows) != int:
		raise TypeError("number_of_rows must be an int")
	elif number_of_rows < 1:
		raise ValueError("number_of_rows cannot be less than one")

	column_names = ["ID", "Name", "Email", "Phone Number", "Address", \
	"Purchase Date", "Product", "Points Earned", "Is Premium Member", \
	"Favorite Color"]
	
	customer_ids = []
	names = []
	emails = []
	phone_numbers = []
	addresses = []
	purchase_dates = []
	products = []
	points_earned = []
	premium_members = []
	favorite_color = []

	current_index = 0

	while current_index < number_of_rows:
		customer_ids.append(create_id())
		first_name = create_first_name()
		names.append(create_name(first_name=first_name))
		emails.append(create_email_address(desired_name=first_name))
		phone_numbers.append(create_phone_number())
		addresses.append(create_address())
		purchase_dates.append(create_stamp())
		products.append(choice(["Car", "TV", "CD", "Computer", "Shirt"]))
		points_earned.append(create_number())
		premium_members.append(create_boolean())
		favorite_color.append("")

		current_index += 1

	data_lists = [customer_ids, names, emails, phone_numbers, addresses, \
	purchase_dates, products, points_earned, premium_members, favorite_color]

	pd.DataFrame(data=dict(zip(column_names, data_lists)), columns=column_names). \
	to_csv("customer_example.csv", index=False)


if __name__ == "__main__":
	create_example_email_csv()
	create_example_customer_csv(133)
