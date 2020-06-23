#!/usr/bin/env python3

import string
from random import *
from calendar import monthrange
from datetime import datetime as dt


def create_id():
	#Example: <asGG78hawyHBHJW9249Bie4>
	string_id = "<"
	index = 0
	number_indices = [4, 5, 15, 16, 17, 18, 22, 23]
	while index < 24:
		if index in number_indices:
			character = choice(string.digits)
		else:
			character = choice(string.ascii_letters)
		string_id += character
		index += 1
	string_id += ">"

	return string_id


def create_email_address(desired_name=None, gmail=True):
	if desired_name != None:
		if type(desired_name) != str:
			raise TypeError("If desired_name is set, it must be a string")
		elif len(desired_name) > 15:
			raise ValueError("If desired_name is set, it cannot exceed 15 characters")

	example_names = ["john", "jack", "jeremy", "jane", "june", "julie", "johnathan", \
	"parker", "peterson", "alexander", "alexis", "alexandria", "alexa", "alejandro", \
	"avery", "arnold", "adrian", "andrew", "bob", "baker", "bill", "boris", "barry", \
	"becky", "charles", "chuck", "chester", "carlson", "catrina", "derek", "drew", \
	"elenore", "elaine", "evans", "eric", "fabio", "fernanda", "frederick", "farley", \
	"gabe", "haaa", "ivanna", "irene", "kirk", "lucy", "licey", "mason", "matthew", \
	"merek", "merick", "maddison", "macabee", "nathan", "noob", "oswaldt", "oscar", \
	"rinea", "rogers", "ricardo", "remmy", "steve", "stephanie", "sally", "sully", \
	"silly", "samuel", "terry", "travis", "ulric", "vonnie", "xenomorph", "zachary"]

	if gmail:
		email_site = "gmail.com"
	else:
		email_site = "corp.org"

	if desired_name != None:
		return "{}{}{}@{}".format(desired_name.lower(), choice(string.digits), \
		choice(string.digits), email_site)
	else:
		return "{}{}{}@{}".format(choice(example_names), choice(string.digits), \
		choice(string.digits), email_site)


def create_first_name():
	first_names = ["John", "Jack", "Jeremy", "Jane", "June", "Julie", "Johnathan", \
	"Peter", "Alexander", "Alexis", "Alexandria", "Alexa", "Alejandro", \
	"Avery", "Arnold", "Adrian", "Andrew", "Bob", "Bill", "Boris", "Barry", \
	"Becky", "Charles", "Chuck", "Chester", "Catrina", "Derek", "Drew", \
	"Elenore", "Alaina", "Evan", "Eric", "Fabio", "Fernanda", "Frederick", \
	"Gabe", "Ivanna", "Irene", "Lucy", "Licey", "Mason", "Matthew", \
	"Merek", "Merick", "Nathan", "Noob", "Oswaldt", "Oscar", \
	"Rinea", "Rogers", "Ricardo", "Remmy", "Steve", "Stephanie", "Sally", \
	"Sully", "Samuel", "Terry", "Travis", "Ulric", "Vonnie", "Zachary"]

	return choice(first_names)


def create_last_name():
	last_names = ["Johnson", "Evans", "Peterson", "Jackson", "Nixon", "Smith", \
	"Andrews", "Garcia", "Gonzalez", "Preston", "Liu", "Carlson", "Baker", \
	"Miller", "Fisher", "Hollister", "Jones", "Williams", "Wilson", "Brown", \
	"Doe", "Patel", "Dias", "Perez", "Lopez", "Reyes", "Martinez", "Hernandez", \
	"Chen", "Cheung", "Lee", "Li", "Wang", "Wong", "Lin", "Moore", "Clark", \
	"Adams", "Collins", "Edwards", "Cook", "Ward", "Price", "Hall", "Young", \
	"Kirk", "Robinson", "Wright", "O'Neill", "O'Connor", "McLaughlin", \
	"Hamilton", "Campbell", "MacDonald", "Paterson", "Phillips", "Owen", \
	"Morozov", "Volkov", "Ivanov", "Hansen", "Berg", "Larsen", "Weber"]

	return choice(last_names)


def create_name(first_name=None, last_name=None):
	if first_name != None:
		if type(first_name) != str:
			raise TypeError("If first_name is set, it must be a string")
		elif len(first_name) > 15:
			raise ValueError("If first_name is set, it cannot exceed 15 characters")
		else:
			first_name = first_name
	else:
		first_name = create_first_name()

	if last_name != None:
		if type(last_name) != str:
			raise TypeError("If last_name is set, it must be a string")
		elif len(last_name) > 20:
			raise ValueError("If last_name is set, it cannot exceed 20 characters")
		else:
			last_name = last_name
	else:
		last_name = create_last_name()

	return "{} {}".format(first_name, last_name)


def create_message_size():
	return randrange(3000, 20000)


def create_stamp():
	year = dt.now().strftime("%Y")
	month = dt.now().strftime("%m")
	int_days = list(range(1, monthrange(int(year), int(month))[1] + 1))
	days = [ "0{}".format(x) if x<10 else "{}".format(x) for x in int_days ]
	hours = [ "0{}".format(x) if x<10 else "{}".format(x) for x in range(0, 24) ]
	sixties = [ "0{}".format(x) if x<10 else "{}".format(x) for x in range(0, 60) ]
	stamp = "{}/{}/{} {}:{}:{} UTC".format(year, month, \
	choice(days), choice(hours), choice(sixties), choice(sixties))

	return stamp


def create_end_date(stamp):
	date = stamp.split(' ')[0]
	if (("UTC" not in stamp) or (":" not in stamp) or ("/" not in date)):
		raise TypeError("Stamp invalid.  Needs to be YYYY/MM/DD HH:MM:SS UTC")
	hours = [ "0{}".format(x) if x<10 else "{}".format(x) for x in range(0, 24) ]
	sixties = [ "0{}".format(x) if x<10 else "{}".format(x) for x in range(0, 60) ]
	generate_end_stamp = lambda: "{} {}:{}:{} UTC".format(date, choice(hours), \
	choice(sixties), choice(sixties))

	end_stamp = generate_end_stamp()

	while stamp >= end_stamp:
		end_stamp = generate_end_stamp()

	return end_stamp


def create_phone_number():
	us_area_codes = ["201", "202", "203", "204", "205", "206", "207", "208", \
	"209", "210", "212", "213", "214", "215", "216", "217", "218", "219", \
	"220", "223", "224", "225", "226", "228", "229", "231", "234", "236", \
	"239", "240", "242", "246", "248", "249", "250", "251", "252", "253", \
	"254", "256", "260", "262", "264", "267", "268", "269", "270", "272", \
	"276", "279", "281", "284", "289", "301", "302", "303", "304", "305", \
	"306", "307", "308", "309", "310", "312", "313", "314", "315", "316", \
	"317", "318", "319", "320", "321", "323", "325", "330", "331", "332", \
	"334", "336", "337", "339", "340", "341", "343", "345", "346", "347", \
	"351", "352", "360", "361", "364", "365", "367", "380", "385", "386", \
	"401", "402", "403", "404", "405", "406", "407", "408", "409", "410", \
	"412", "413", "414", "415", "416", "417", "418", "419", "423", "424", \
	"425", "430", "431", "432", "434", "435", "437", "438", "440", "441", \
	"442", "443", "445", "450", "456", "458", "463", "469", "470", "473", \
	"475", "478", "479", "480", "484", "500", "501", "502", "503", "504", \
	"505", "506", "507", "508", "509", "510", "512", "513", "514", "515", \
	"516", "517", "518", "519", "520", "530", "531", "533", "534", "539", \
	"540", "541", "544", "548", "551", "559", "561", "562", "563", "564", \
	"566", "567", "570", "571", "573", "574", "575", "577", "579", "580", \
	"581", "585", "586", "587", "600", "601", "602", "603", "604", "605", \
	"606", "607", "608", "609", "610", "612", "613", "614", "615", "616", \
	"617", "618", "619", "620", "623", "626", "628", "629", "630", "631", \
	"636", "639", "640", "641", "646", "647", "649", "650", "651", "657", \
	"658", "660", "661", "662", "664", "667", "669", "670", "671", "672", \
	"678", "680", "681", "682", "684", "689", "700", "701", "702", "703", \
	"704", "705", "706", "707", "708", "709", "710", "712", "713", "714", \
	"715", "716", "717", "718", "719", "720", "721", "724", "725", "726", \
	"727", "731", "732", "734", "737", "740", "743", "747", "754", "757", \
	"758", "760", "762", "763", "765", "767", "769", "770", "772", "773", \
	"774", "775", "778", "779", "780", "781", "782", "784", "785", "786", \
	"787", "800", "801", "802", "803", "804", "805", "806", "807", "808", \
	"809", "810", "812", "813", "814", "815", "816", "817", "818", "819", \
	"820", "825", "828", "829", "830", "831", "832", "833", "838", "843", \
	"844", "845", "847", "848", "849", "850", "854", "855", "856", "857", \
	"858", "859", "860", "862", "863", "864", "865", "866", "867", "868", \
	"869", "870", "872", "873", "876", "877", "878", "888", "900", "901", \
	"902", "903", "904", "905", "906", "907", "908", "909", "910", "911", \
	"912", "913", "914", "915", "916", "917", "918", "919", "920", "925", \
	"928", "929", "930", "931", "934", "936", "937", "938", "939", "940", \
	"941", "947", "949", "951", "952", "954", "956", "959", "970", "971", \
	"972", "973", "978", "979", "980", "984", "985", "986", "989"]

	last_four_digits = [ "000{}".format(x) if x < 10 else "00{}". \
	format(x) if x < 100 else "0{}".format(x) if x < 1000 else "{}". \
	format(x) for x in range(0,10000) ]
	return "1-{}-000-{}".format(choice(us_area_codes), choice(last_four_digits))
	#I wrote it this way to ensure it is clear these numbers are duds,
	#though made it differential enough to allow for aggregate operations

	
def create_address():
	generic_street_names = ["Broadway", "Main", "Jackson", "Park", \
	"Oak", "Dogwood", "Elm", "Lake", "Maple", "Pine", "Ranch", \
	"First", "Second", "Third", "Fourth", "Fifth", "Sixth", \
	"Seventh", "Eighth"]
	generic_street_names += list(string.ascii_uppercase[:8]) #A-H streets

	street_suffix = ["St.", "Dr.", "Ct." , "Blvd.", "Ln.", \
	"Av.", "Ave", "Rd.", "Street", "Court", "Lane", "Drive", \
	"Road"]
	apartment_suffix = ["Apt. ", "Unit ", "#"]

	street = choice(generic_street_names)
	random_number = randrange(1,21)
	if random_number == 20:
		street += " {}".format(choice(street_suffix))
		street += ", {}{}".format(choice(apartment_suffix), \
		randrange(1,301))
	elif random_number > 8:
		street += " {}".format(choice(street_suffix))
	else:
		street += " St."

	return "{} {}".format(randrange(1, 10000), street)
	

def create_email_subject():
	example_subject = ["Help", "Immediate Attention", "Urgent Request", \
	"Stuck on Task", "Project Completed", "Hiring Process", \
	"New Hire Packet", "Fired", "Meeting Today", \
	"Potential Candidate", "Look at This!", "Wireless Down..", \
	"Payment", "Greetings", "Bad Connection", "If you have spare time..", \
	"What Have You Done Bob", "Dr. Robert's OneDrive", "Lunch Discussion", \
	"Matthew's Expedition", "Results", "What we uncovered today..", "Progress Report"]
	subject = choice(example_subject)

	tags = ["Re:", "Fwd:", "FW:","[EXTERNAL]"]

	random_number = randrange(1,21)
	if random_number > 18:
		subject = "{} {} {}".format(choice(tags), choice(tags), subject)
	elif random_number > 10:
		subject = "{} {}".format(choice(tags), subject)

	return subject 


def create_email_direction():
	random_value = randrange(1,21)
	if random_value < 15:
		direction = "Mixed"
	else:
		direction = "Received"

	return direction


def create_boolean():
	return choice([True, False])


def create_number(minimum=0, maximum=50000):
	if type(minimum) != int:
		raise TypeError("If minimum is set, it must be an int")
	elif type(maximum) != int:
		raise TypeError("If maximum is set, it must be an int")
	elif minimum > maximum:
		raise ValueError("Minimum cannot exceed maximum")
	else:
		return randrange(minimum, maximum + 1)


def create_ip():
	return "192.168.{}.{}".format(randrange(0,256), randrange(0,256))
