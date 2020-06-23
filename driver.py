#!/usr/bin/env python3

from sanitization_pack.auto_detector import auto_create_sanitized_CSVs


#If there's any sanitization feature you'd like to disable or enable,
#you need only alter True to False, or False to True.
sanitize_phone_numbers = 	True
sanitize_ids = 			True
sanitize_dates = 		False
sanitize_emails = 		True
sanitize_ips = 			True
sanitize_booleans = 		False
sanitize_addresses = 		True
sanitize_names = 		True
sanitize_numbers = 		False


options = [sanitize_phone_numbers, sanitize_ids, sanitize_dates, sanitize_emails, \
sanitize_ips, sanitize_booleans, sanitize_addresses, sanitize_names, sanitize_numbers]

auto_create_sanitized_CSVs(options)
