import os
import json
from pprint import pprint


data_directory = 'data'


def create_event(ev_id, title, description, category, tags,
 	start_date, end_date, place, organiser, web_link, tickets_link):

	data = {}
	data['id'] = ev_id
	data['title'] = title
	data['description'] = description
	data['category'] = category
	data['tags'] = tags
	data['start_date'] = start_date
	data['end_date'] = end_date
	data['place'] = place
	data['organiser'] = organiser
	data['web_link'] = web_link
	data['tickets_link'] = tickets_link

	json_data = json.dumps(data)

	with open(os.path.join(data_directory,
	 			'event_%.3d.json' % ev_id), 'w') as outfile:
	    json.dump(json_data, outfile, indent=4, separators=(',', ': '),
	    		ensure_ascii=False)

def read_event(ev_id):

	event_path = os.path.join(data_directory, 'event_%.3d.json' % ev_id)
	json_data = json.load(open(event_path))
	data = json.loads(json_data) 
	
	print(data['title'])


# ------------------------------------------ #

create_event(
	id = 0,
	title = 'Research Talk: Prof. Nixon on Biometrics',
	description = "Want to find out what's happening in the exciting world of \
	advanced Biometrics from one of Southampton's best speakers? \
	There'll be snacks! Prof. Mark Nixon is one of the star \
	researchers in the fields of Biometrics and Computer Vision \
	at ECS and President of IEEE Biometrics Council. His talks \
	are always something to behold and he's well known for his \
	great teaching style. In this talk, perfect for MSc, 4th and \
	3rd year students, Prof. Nixon will offer an in-depth look at \
	the cutting-edge Biometrics technology research: A future for \
	biometrics - where will identity science go? It is time to take stock and address what is the future of biometrics. Some biometrics are considered to be a solved problem, whilst some remain in the research phase. Some of the ramifications have yet to be explored further. Drawing on my long experience in biometrics, since 1984 before it was even so named, I shall discuss where biometrics is and where it is going. What indeed is the Future of Biometrics?",
	category = 'academic',
	tags = ['on_campus', 'free', 'talk', 'food', 'ecs'],
	start_date = '08-03-2018 18:00',
	end_date = '08-03-2018 19:00',,
	place = '46/2003',
	organiser = 'ECSS',
	web_link = 'https://www.facebook.com/events/1587158544654735/',
	tickets_link = 'free entry'
	)

create_event(
	id = 1,
	title = '',
	description = "",
	category = '',
	tags = [],
	start_date = '08-03-2018 18:00',
	end_date = '08-03-2018 19:00',
	place = '',
	organiser = '',
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = ,
	title = '',
	description = "",
	category = '',
	tags = [],
	start_date = '08-03-2018 18:00',
	end_date = '08-03-2018 19:00',
	place = '',
	organiser = '',
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = ,
	title = '',
	description = "",
	category = '',
	tags = [],
	start_date = '08-03-2018 18:00',
	end_date = '08-03-2018 19:00',
	place = '',
	organiser = '',
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = ,
	title = '',
	description = "",
	category = '',
	tags = [],
	start_date = '08-03-2018 18:00',
	end_date = '08-03-2018 19:00',
	place = '',
	organiser = '',
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = ,
	title = '',
	description = "",
	category = '',
	tags = [],
	start_date = '08-03-2018 18:00',
	end_date = '08-03-2018 19:00',
	place = '',
	organiser = '',
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = ,
	title = '',
	description = "",
	category = '',
	tags = [],
	start_date = '08-03-2018 18:00',
	end_date = '08-03-2018 19:00',
	place = '',
	organiser = '',
	web_link = '',
	tickets_link = ''
	)