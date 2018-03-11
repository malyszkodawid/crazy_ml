import os
import json
from pprint import pprint


data_directory = 'data'


def create_event(id, title, description, category, tags,
 	start_date, end_date, place, organisers, web_link, tickets_link):

	data = {}
	data['id'] = id
	data['title'] = title
	data['description'] = description
	data['category'] = category
	data['tags'] = tags
	data['start_date'] = start_date
	data['end_date'] = end_date
	data['place'] = place
	data['organisers'] = organisers
	data['web_link'] = web_link
	data['tickets_link'] = tickets_link

	json_data = json.dumps(data)

	with open(os.path.join(data_directory,
	 			'event_%.3d.json' % id), 'w') as outfile:
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
	category = ['academic'],
	tags = ['on_campus', 'free', 'talk', 'food'],
	start_date = '08-03-2018 18:00',
	end_date = '08-03-2018 19:00',
	place = '46/2003',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/1587158544654735/',
	tickets_link = ''
	)

create_event(
	id = 1,
	title = 'TPP Code Quiz',
	description = "Wouldn't pub quizzes be amazing if the questions were all coding challenges? Wouldn't it be even better if you were fed and watered for free? We are excited to announce a Code Quiz at Bar 2 of the Student's Union on Wednesday 7th March, in collaboration with TPP! Unlike a typical pub quiz, you'll need to exercise your problem solving skills to tackle the range of challenges set instead of applying your general knowledge. There will be free food and drinks, both soft and alcoholic, available for attendees throughout the whole event. There will also be great prizes on offer for the winning teams (Raspberry Pi computers and a Hotel Chocolat hamper).",
	category = ['academic', 'hobbies', 'contests'],
	tags = ['free', 'food', 'alcohol'],
	start_date = '07-03-2018 17:30',
	end_date = '07-03-2018 22:00',
	place = 'Union Southampton',
	organisers = ['ECSS', 'TPP Careers'],
	web_link = 'https://www.facebook.com/events/1944840719163622/',
	tickets_link = ''
	)

create_event(
	id = 2,
	title = 'ECSS Disney Film Night',
	description = "With deadlines coming up, why not take the evening off to destress with us as we watch a voted for Disney film! Popcorn and drinks will be provided, so come in your comfiest clothes (Pyjamas are encouraged) and kick your feet up and enjoy a wholesome film. Poll is in the discussion below!",
	category = ['hobbies'],
	tags = ['movie', 'on_campus', 'food'],
	start_date = '06-03-2018 19:30',
	end_date = '06-03-2018 23:00',
	place = '53/4025',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/828086887375779/',
	tickets_link = ''
	)

create_event(
	id = 3,
	title = 'Pizza Party with Jump Trading',
	description = "Love algorithms?vKeen on financial tech? Want to eat free, delicious pizza? Founded in 1999, Jump Trading has been at the forefront of electronic trading for 19 years, and now have over 500 employees spread across Chicago, New York, Singapore and London. And they're visiting ECS. Employees from Jump Trading will be in labs with free pizza, and they are looking forward to meeting you! They trade across all major asset classes in dozens of financial exchanges around the world. Their casual atmosphere, culture of continuous learning and innovation, and philosophy of rewarding outstanding performance based on merit rather than tenure or title has attracted some of the most brilliant people from around the trading industry, Silicon Valley tech companies and startups, and top PhD programs and research labs. So turn up, grab some free food, learn a thing or two and maybe land yourself a lucrative job or placement!",
	category = ['academic'],
	tags = ['on_campus', 'free', 'talk', 'food'],
	start_date = '01-03-2018 11:00',
	end_date = '01-03-2018 13:00',
	place = 'Zepler Level 3 Computing Labs',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/784441845094925/',
	tickets_link = 'https://docs.google.com/forms/d/e/1FAIpQLSf0mLgVuC7SxG4yU9fammqJJz2IoFh9r9T4hO-cMqotwU7tmg/viewform'
	)

create_event(
	id = 4,
	title = "Snowflake: Solving Aviation's problems",
	description = "Next up in this semester's series of industry talks, we're visited by ECSS Bronze Sponsor Snowflake Software! Oli Deakin, Snowflake Software's Principal Software Developer, will talk about how Snowflake is using containerised micro-services to solve one of Aviation's most significant problems. Focusing on a recent deployment at the UAE's air traffic control centre, the talk will introduce the problem being solved, and then discuss Snowflake's solution approach and the technologies involved. Over 25% of Snowflake's UK workforce is made up of ECS graduates, and they're always looking for fresh local talent! This is a great opportunity to network with a Southampton based company, don't miss out!",
	category = ['academic'],
	tags = ['on_campus', 'free', 'talk', 'food'],
	start_date = '27-02-2018 18:00',
	end_date = '27-02-2018 19:00',
	place = '53/4025',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/167297240727150/',
	tickets_link = ''
	)

create_event(
	id = 5,
	title = 'Board Games Night!',
	description = "Its that time again folks! Come along and play board games alongside fellow members of ECSS and enjoy the free pizza as you play. Hope to see you there!",
	category = ['hobbies'],
	tags = ['on_campus', 'free', 'food', 'play'],
	start_date = '26-02-2018 19:00',
	end_date = '26-02-2018 23:00',
	place = '54/7033 & 7035',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/212985659252439/',
	tickets_link = ''
	)

create_event(
	id = 6,
	title = 'Playzone Pandemonium Ft. Psychosoc & ECSS',
	description = "Psychosoc and ECSS have come together to create one big epic social! Alcoholic slushies combined with indoor play set and a ball pit, the evening is set to be crazy fun. Playzone is based in Portsmouth so we will be taking two coaches to get there, limited tickets available! Tickets are £20, last year Psychosoc sold out really quick so buy them ASAP to avoid disappointment. The ticket covers the cost for the hire of playzone and a seat on the coach. Please press GOING so we can get an idea of numbers!",
	category = ['party', 'hobbies'],
	tags = ['alcohol', 'food', 'play'],
	start_date = '24-02-2018 20:00',
	end_date = '24-02-2018 21:30',
	place = 'Playzone Portsmouth',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/185798265355257/',
	tickets_link = ''
	)

create_event(
	id = 7,
	title = 'OCEAN WAVES',
	description = "You've been asking for it, here it is. Ladies and gentlemen, boys and girls, pull out your waviest shirts and garms and join us for a retro-themed boogie in the Disco Room until 4 in the morning! Meet us at The Standing Order on High Street (Wetherspoons = cheap drinks!) for 8:00. We'll be leaving for Oceana at about 10:15 to make sure we all get in before 11:00! By doing so, Oceana will sort us out with booths on arrival and free bottles of vodka for every 10 people! (Make sure you bring your student ID card with ECS visible).",
	category = ['party'],
	tags = ['city_centre', 'dance', 'alcohol'],
	start_date = '21-02-2018 20:00',
	end_date = '22-02-2018 04:00',
	place = 'Oceana Southampton',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/435010040265227/',
	tickets_link = ''
	)

create_event(
	id = 8,
	title = 'Factset: The benefits of unit testing',
	description = "ECSS is back with another series of industry talks from our sponsors! This time we'll be visited by FactSet, a leading provider of financial data and analytic applications. During this industry talk, we'll be looking at what unit testing is and why it is important to have this as part of any developer's workflow. Moreover, we'll look into when and how to write unit tests, ranging from small applications to complex ones, and using a variety of programming languages. This is a great chance to meet one of ECSS' Silver sponsors, network, and find out more FactSet, a company listed in Fortune's 100 Best Companies to Work For!",
	category = ['academic'],
	tags = ['on_campus', 'free', 'talk', 'food'],
	start_date = '20-02-2018 18:00',
	end_date = '20-02-2018 19:00',
	place = '53/4025',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/1969679610016734/',
	tickets_link = ''
	)

create_event(
	id = 9,
	title = 'ECSS Parkrun',
	description = "The perfect way to get into running! See you all tomorrow at the start :) Don't forget to join the ECSS Running club on the site too!",
	category = ['sports'],
	tags = ['free'],
	start_date = '17-02-2018 09:00',
	end_date = '17-02-2018 10:00',
	place = 'The Common',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/152012505434449/',
	tickets_link = 'http://www.parkrun.org.uk/register/'
	)

create_event(
	id = 10,
	title = '4YGDP Handin | Free Pizza & Beer',
	description = "Everyone's done with 4YGDP (mostly) so let's crack some beer open and chill out. Join us on the evening of hand-in day for some free food and booze to celebrate turning in a major part of the GDP. Invite all your 4th year friends!",
	category = ['food'],
	tags = ['on_campus', 'free', 'alcohol'],
	start_date = '15-02-2018 18:00',
	end_date = '15-02-2018 20:00',
	place = 'Mountbatten Level 3 Postgraduate Common Room',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/160260404762685/',
	tickets_link = ''
	)

create_event(
	id = 11,
	title = 'ECSS Plays Videogames',
	description = "Come along to our second video games social of the year! With access to consoles as well as the lab computers join fellow members of ECS for a night of fun filled gaming. Free pizza as always! Team Fortress 2 will not work on any of the lab computers, but we will be hosting a server for anyone who wants to bring in their own laptop, no VPN required. Battle.net games are working but you need to change the install directory to the root of the C drive. Fortnite will not work as they use their own launcher which is not currently installed or verified on any of the lab computers. A Minecraft server may also be hosted if there is enough interest on the night.",
	category = ['hobbies'],
	tags = ['on_campus', 'free', 'food', 'play'],
	start_date = '08-02-2018 19:00',
	end_date = '08-02-2018 23:00',
	place = 'Zepler Level 3',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/2227753863966386/',
	tickets_link = ''
	)

create_event(
	id = 12,
	title = 'ECSS White T-Shirt Refreshers Social!',
	description = "Welcome to the ECSS White T-Shirt Social! This is an event we run twice a year and is a great way to meet people. We'll be meeting up in Stag's and then heading down through a number of Portswood's finest establishments throughout the night. The route, though it's subject to change, is Stag's -> Mitre -> Wild Lime -> Gordon Arms/Richmond Inn -> Hobbit -> Jesters/Sobar. If you're not the drinking type, the night usually starts out on the quiet side of things so you're welcome to come along for the start! If you'd like to meet up with us along the way then you're very welcome to, and we'll be posting up our location on this event. Remember to **BRING PENS** so you can draw on people. You can never have enough. You also need student ID to get into Stag's, and legal ID to get into everywhere else! Our white T-shirt social was great fun last semester, so don't miss out!",
	category = ['hobbies', 'party'],
	tags = ['on_campus', 'alcohol'],
	start_date = '30-01-2018 19:00',
	end_date = '31-01-2018 01:00',
	place = "The Stag's",
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/139252063423937/',
	tickets_link = ''
	)

create_event(
	id = 13,
	title = 'Bike Doctor',
	description = "Get your bicycle checked up and fixed at the Bike Doctor!",
	category = ['sports', 'hobbies'],
	tags = ['bike', 'on_campus', 'free', 'susu'],
	start_date = '09-03-2018 at 10:00',
	end_date = '09-03-2018 at 14:00',
	place = 'Red Brick Area',
	organisers = ['SUSU'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 14,
	title = 'Free Fruit Friday (WSA)',
	description = "Grab one of your five a day, courtesy of the WSA Student Committee! This week it's exotic fruit!",
	category = ['food'],
	tags = ['free', 'food', 'on_campus','susu'],
	start_date = '09-03-2018 10:00',
	end_date = '09-03-2018 14:00',
	place = 'WSA Cafe',
	organisers= ['SUSU'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 15,
	title = 'CI Careers Session: What It Takes To Be An Editor',
	description = "Want to know what it takes to be an Editor of a magazine in today's evolving\
    multi-media world? Join us to discover more, with Carl Loben, Editor-in-Chief of DJ Mag.\
    With many years of experience as a music journalist, Carl will discuss how the 'Editor'\
    role has become more of a multi-media job over the last decade. He will discuss choosing\
    quality content that you know will engage with your audience, importance of relationships\
    with other staff members and section editors and how this is relevant to you as students and future careers.",
	category = ['academic'],
	tags = ['on_campus', 'free', 'talk', 'susu'],
	start_date = '09-03-2018 12:00',
	end_date = '09-03-2018 14:00',
	place = 'Meeting Room 2, Building 42, Highfeld campus',
	organisers= ['SUSU', 'SUSU Creative Industries Zone'],
	web_link = '',
	tickets_link = 'https://www.eventbrite.co.uk/e/ci-careers-session-what-it-takes-to-be-an-editor-with-carl-loben-dj-mag-postponed-tickets-43830529293'
	)

create_event(
	id = 16,
	title = 'Beginners Cuban Salsa Lessons',
	description = "Come along to our Beginners Cuban Salsa lessons! No need to bring a partner!!",
	category = ['hobbies'],
	tags = ['on_campus', 'societies', 'dance'],
	start_date = '09-03-2018 19:00',
	end_date = '09-03-2018 20:00',
	place = 'The Cube',
	organisers= ['Salsa Society Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 17,
	title = 'Inter-Society Challenge Semi Final and Final',
	description = "Will the Natural Quiztorians cause an extinction event?\
    Will Counts in Hesters short circuit their rivals? Will Korfball net a\
    big victory? Or will Mini Rich Choral Hop hit all the right notes? Come along\
    and find out this Friday, where one of these four teams will see themselves £500 richer.",
	category = ['hobbies','contests'],
	tags = ['on_campus', 'societies', 'free'],
	start_date = '09-03-2018 19:00',
	end_date = '09-03-2018 21:00',
	place = '32/3077',
	organisers= ['Quiz Society Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 18,
	title = 'Intermediate Cuban Salsa Lessons',
	description = "Come along to our Intermedaite Cuban Salsa lessons! No need to bring a partner!!",
	category = ['hobbies'],
	tags = ['on_campus', 'societies', 'dance'],
	start_date = '09-03-2018 20:00',
	end_date = '09-03-2018 22:00',
	place = 'The Cube',
	organisers= ['Salsa Society Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 19,
	title = 'Independence Party',
	description = "",
	category = ['hobbies', 'party'],
	tags = ['on_campus', 'societies','dance', 'alcohol'],
	start_date = '09-03-2018 20:00',
	end_date = '10-03-2018 00:00',
	place = 'The Cube',
	organisers= ['Ghanaian Society Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 20,
	title = 'Student Groups Committee',
	description = "Student Groups Committee",
	category = ['hobbies'],
	tags = ['on_campus', 'societies','talks', 'free'],
	start_date = '08-03-2018 11:00',
	end_date = '08-03-2018 13:00',
	place = 'Meeting Room 1',
	organisers= ['SUSU'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 21,
	title = 'SHOUT REVIVE',
	description = "JOIN US FOR OUR BI-WEEKLY\
    REVIVE FELLOWSHIP. WHERE WE SPEND TIME WITH GOD AND SPEAK ABOUT WAYS WE CAN SERVE GOD AND SERVE OUR COMMUNITY.",
	category = ['hobbies'],
	tags = ['on_campus', 'societies','talks','religion','free'],
	start_date = '08-03-2018 18:00',
	end_date = '08-03-2018 19:15',
	place = '06/1129 Nuffield Lecture Theatre F',
	organisers= ['SHOUT Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 22,
	title = 'Judo beginners session',
	description = "Everyone welcome all year round - just come in comfy clothes!",
	category = ['hobbies'],
	tags = ['on_campus', 'societies'],
	start_date = '08-03-2018 18:00',
	end_date = '08-03-2018 20:00',
	place = 'Martial Arts Room',
	organisers= ['Judo Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 23,
	title = 'Fast-track your feedback',
	description = "Create positive change at the next Student Forum on 2 May",
	category = ['academic', 'hobbies'],
	tags = ['food', 'on_campus', 'free'],
	start_date = '02-05-2018 at 13:00',
	end_date = '02-05-2018 at 15:00',
	place = 'Garden Court, Highfield',
	organisers = ['University of Southampton - Student Communications'],
	web_link = 'https://www.facebook.com/events/1618632988244372/',
	tickets_link = 'https://www.eventbrite.co.uk/e/create-positive-change-at-the-next-student-forum-on-2-may-tickets-43988136701?aff=efbeventtix'
	)


create_event(
	id = 24,
	title = "Future Worlds Dragons' Den",
	description = "Future Worlds Dragons' Den",
	category = ['sports', 'hobbies'],
	tags = ['business', 'on_campus', 'free'],
	start_date = '12-05-2018 at 13:00',
	end_date = '12-05-2018 at 17:00',
	place = 'Future Words, University of Southampton',
	organisers = ['University of Southampton - Student Communications',
               'Entrepreneurs Club', 'Future Worlds', 'Enactus Southampton', 'University of Southampton',
               'Fish on Toast', 'University of Southampton Alumni'],
	web_link = 'https://www.facebook.com/events/348244035688996/',
	tickets_link = 'https://www.eventbrite.co.uk/e/future-worlds-dragons-den-2018-tickets-43604945566?aff=efbeventtix'
	)

create_event(
	id = 25,
	title = 'Beginners Bachata Salsa Lessons',
	description = "Come along to our Beginners Bachata lessons! No need to bring a partner!!",
	category = ['hobbies'],
	tags = ['on_campus', 'societies', 'dance'],
	start_date = '08-03-2018 19:00',
	end_date = '08-03-2018 20:00',
	place = 'The Cube',
	organisers = ['Salsa Society Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 26,
	title = 'QuizSoc Tramstop Takeover',
	description = "An exciting new opportunity for QuizSoc and all\
    those interested in Pub Quizzes since the Stile closed. What could\
    be a one-off or the first of many so please come along and take part\
    at the Tramstop Pub in Portswood. £1 entry. £50 prize for the winners and\
    other prizes for runners up.",
	category = ['hobbies', 'contests'],
	tags = ['city_centre', 'societies', 'alcohol'],
	start_date = '08-03-2018 19:45',
	end_date = '08-03-2018 21:15',
	place = 'The Tramstop Bar & Kitchen (Portswood Rd, SO17 2NJ)',
	organisers = ['Quiz Society Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 27,
	title = 'Beginners Crossbody Salsa Lessons',
	description = "Come along to our Beginners Crossbody Salsa lessons! No need to bring a partner!!",
	category = ['hobbies'],
	tags = ['on_campus', 'societies', 'dance'],
	start_date = '08-03-2018 20:00',
	end_date = '08-03-2018 21:00',
	place = 'Activities Room',
	organisers = ['Salsa Society Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 28,
	title = 'ECSS at the Inter-Society Challenge!',
	description = "Want to win a quick £200 for you and three mates? Southampton's Quiz Society are running the annual Inter-Society Challenge (ISC), a general knowledge quiz tournament with the chance to win big money for the society you represent! The prize money for the winning team is a sweet £500. If you enter a team representing ECSS (we can enter as many ECSS teams as we like!) and win the ISC, you get to keep £200 of the winnings, with the remaining £300 going into the society budget that allows us to run our events. The Qualifier Round takes place in early February after exams, with an entry fee of £1 per person. After this stage, successful teams are put through to the Knockout Rounds (played on the buzzer) with a £1.50 entry fee per person. ",
	category = ['contests'],
	tags = ['on_campus', 'free', 'play'],
	start_date = '13-12-2017 16:00',
	end_date = '18-12-2017 12:00',
	place = 'Highfield Campus',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/163277347758358/',
	tickets_link = 'https://docs.google.com/forms/d/1sryNHdTH3azSTH1rwa7hm8Iph9qaG82iFSd6cYhTr18/viewform?edit_requested=true'
	)

create_event(
	id = 29,
	title = 'ECS Christmas Party (Free Drink Included!)',
	description = "Join us for our final social of the year: the department christmas party! Our bash this year will be in The Bridge, in the main SUSU building. Entry to the event is free, and the dress code is smart casual and upwards, so dress fancy if you want! Please feel welcome to bring friends, but non-ECS students will not be able to get a drink token. The union bars will be open as usual if you wish to buy more drinks and we'll be heading to Portswood when the night ends to continue the party! We look forward to seeing you there for a night of festivity and celebration to close out 2017 :)",
	category = ['party'],
	tags = ['on_campus', 'free', 'dance', 'alcohol', 'play', 'food'],
	start_date = '07-12-2017 18:00',
	end_date = '07-12-2017 23:00',
	place = 'The Bridge',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/360768204344521/',
	tickets_link = ''
	)

create_event(
	id = 30,
	title = 'TGM + Games Night',
	description = "It's time for our TGM (Termly General Meeting), followed by a games night! At 7pm, we'll be holding our TGM. This is a chance to hear about what the committee have been up to so far this term, gain an insight into the growth of the society and this term's cash flow, as well as details about what is in store for the rest of this academic year. There will also be a Q&A session, where you'll be able to voice your suggestions about how the society, and our events, are ran. From 8pm, we'll be transitioning to our usual games night in rooms 1065 and 1025 (in the same building), so pop along, play some games and eat some pizza! Whilst the two events are back-to-back, they are unrelated. You can attend either one, or both!",
	category = ['academic', 'hobbies'],
	tags = ['on_campus', 'free', 'talk', 'food', 'play'],
	start_date = '05-12-2017 19:00',
	end_date = '05-12-2017 22:30',
	place = '58/1065',
	organisers = ['ECSS'],
	web_link = 'https://www.facebook.com/events/811248419079654/',
	tickets_link = ''
	)

create_event(
	id = 31,
	title = 'Intermediate Crossbody Salsa Lessons',
	description = "Come along to our Intermediate Crossbody Salsa lessons! No need to bring a partner!!",
	category = ['hobbies'],
	tags = ['on_campus', 'societies', 'dance'],
	start_date = '08-03-2018 21:00',
	end_date = '08-03-2018 22:00',
	place = 'Activities Room',
	organisers = ['Salsa Society Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 32,
	title = 'Karaoke',
	description = "",
	category = ['party'],
	tags = ['on_campus', 'alcohol', 'dance', 'free','susu'],
	start_date = '08-03-2018 20:00',
	end_date = '09-03-2018 01:00',
	place = 'The Stags',
	organisers = ['SUSU'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 33,
	title = 'CI Careers Session: Media and Advertising Workshop',
	description = "Curious about the media and advertising industry?\
    Come along to this workshop with Richard Willis, founder of Talent Works\
    to find out how to get in to the industry, who you should be networking with,\
    which roles to aim for and more. It doesn't stop there, Final Year students can\
    also book a one-to-one with Richard throughout the whole day! You can do this here:\
    https://www.talent-works.net/book (select Southampton option). Talent Works aim to\
    advance young talent in media, so this is the perfect opportunity to discuss your desired\
    career path, consider your options and gain some help and guidance from Richard. \
    This is a FREE event but spaces are limited. Secure your place here: http://bit.ly/2FfyVqg",
	category = ['academic'],
	tags = ['on_campus', 'talk', 'susu'],
	start_date = '07-03-2018 14:30',
	end_date = '07-03-2018 15:30',
	place = 'Building 58, Room 1041 Murray Building',
	organisers = ['SUSU', 'SUSU Creative Industries Zone'],
	web_link = '',
	tickets_link = 'http://bit.ly/2FfyVqg'
	)

create_event(
	id = 34,
	title = 'Learn the Lindy Hop',
	description = "Come and learn a fun and stylish partner dance! \
    4pm-5pm: Free Practice Session\
    5pm-6pm: Beginners' Lindy Hop Lesson\
    Like our page to keep up to date!",
	category = ['hobbies'],
	tags = ['on_campus', 'societies', 'dance'],
	start_date = '07-03-2018 16:00',
	end_date = '07-03-2018 18:00',
	place = 'Union Cafe',
	organisers = ['Southampton Swing Dancers Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 35,
	title = 'Karate-do Shotokai',
	description = "Come along to our informal practice sessions to learn self defence and keep fit!",
	category = ['hobbies', 'sports'],
	tags = ['on_campus', 'societies'],
	start_date = '06-03-2018 17:00',
	end_date = '06-03-2018 19:00',
	place = 'Activities Room, Union Building (42)',
	organisers = ['Karate-Do Shotokai Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 36 ,
	title = 'Karaoke',
	description = "Tuesday Karaoke Night. Sad that you missed out\
    last week because of the Beast from the East? We're hosting a special Karaoke TONIGHT.",
	category = ['party'],
	tags = ['on_campus', 'alcohol', 'dance', 'free', 'susu'],
	start_date = '06-03-2018 20:00',
	end_date = '07-03-2018 01:00',
	place = 'The Stags',
	organisers = ['SUSU'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 37 ,
	title = 'Farmers Market',
	description = "Stock up on delicious fruit and vegetables at our weekly Farmers Market on the Redbrick.",
	category = ['food'],
	tags = ['on_campus', 'susu', 'food'],
	start_date = '05-03-2018 09:00',
	end_date = '05-03-2018 16:00',
	place = 'Red Brick Area',
	organisers = ['SUSU'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 38 ,
	title = 'Skepticism Series: Michael Marshall | Pseudoscience',
	description = "Join us for an evening with Michael Marshall, of the Good\
    Thinking Society, Merseyside Skeptics and more, as he presents a talk titled\
    Lifting The Lid: Ongoing Adventures in Pseudoscience. The talk will begin at 7.30pm.\
    It’s easy to think of pseudoscience existing in a glass case at a museum – something\
    to be examined and critiqued from a safe distance, but not something to touch and to play\
    with. Using examples taken from his own personal experiences in skepticism, Michael Marshall\
    will show what happens when you begin to crack the surface of the pseudosciences that surround\
    us – revealing the surprising, sometimes-shocking and often-comic adventures that lie beneath.\
    Michael Marshall is the Project Director of the Good Thinking Society and the Vice President of\
    the Merseyside Skeptics Society. He regularly speaks with proponents of pseudoscience for the Be\
    Reasonable podcast. His work has seen him organising international homeopathy protests and co-founding\
    the popular QED conference. He has written for the Guardian, The Times and New Statesman.",
	category = ['academic'],
	tags = ['on_campus', 'talk', 'societies', 'free'],
	start_date = '05-03-2018 19:00',
	end_date = '05-03-2018 21:00',
	place = '06.1081 (Nuffield Theatre, Lecture Theatre B)',
	organisers = ['Humanist Students Southampton Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 39 ,
	title = 'SSAGO: Student Scouts And Guides Organisation',
	description = "If you have ever been involved in either Scouts or Guides,\
    or just like spending time outdoors and want to try something different,\
    then SSAGO is the place for you! Join us for a drink every Monday in the Crown\
    and see what we get up to during the year. We would love to meet you! If the idea\
    of exciting themed camps, fire, fun activities, and a great set of socials appeals\
    to you then come along and meet lovely (and maybe slightly crazy) people at Southampton\
    SSAGO! Get involved in activities like archery, climbing and zorbing, trips around the UK,\
    as well as camps and socials with other SSAGO members all over the country... and that's just the start!",
	category = ['hobbies'],
	tags = ['on_campus', 'alcohol', 'societies'],
	start_date = '05-03-2018 20:00',
	end_date = '05-03-2018 23:00',
	place = 'The Crown Inn, Highfield',
	organisers = ['Student Scout And Guide Organisation Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 40 ,
	title = 'Sunday Hop',
	description = "Sunday Hop is a weekly social for the Southampton Swing Dancers.\
    This is a great place for social dancing, having a drink, and meeting new people.\
    There’s no formal class, but we’re happy to show you some basic steps if you’re new\
    to lindy hop. Bring your friends – there is nothing better than moving to swing music on a Sunday.",
	category = ['hobbies'],
	tags = ['city_center', 'alcohol', 'societies',  'dance'],
	start_date = '04-03-2018 18:30',
	end_date = '04-03-2018 20:00',
	place = 'The Shooting Star, 40-42 Bevois Valley Road, SO14',
	organisers = ['Southampton Swing Dancers Group'],
	web_link = 'https://www.facebook.com/SouthamptonSwingDancers/',
	tickets_link = ''
	)


create_event(
	id = 41 ,
	title = 'SUSingers Rehearsals',
	description = "Join us for the Southampton University Singers' for\
    our weekly rehearsal! We are a friendly non-auditioned choir with the\
    university's most varied choir repertoire - from traditional to modern\
    - and we welcome anyone who loves singing, regardless of previous experience.\
    We rehearse every Sunday 6:45-9 pm in 02/1083!",
	category = ['hobbies'],
	tags = ['on_campus',  'societies',  'sing'],
	start_date = '04-03-2018 18:45',
	end_date = '04-03-2018 21:00',
	place = '02/1083',
	organisers = ['SUSingers Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 42 ,
	title = 'Karate-do Shotokai',
	description = "Come along to our informal practice sessions to learn self defence and keep fit!",
	category = ['hobbies', 'sports'],
	tags = ['on_campus', 'societies'],
	start_date = '03-03-2018 09:00',
	end_date = '03-03-2018 11:00',
	place = 'Activities Room, Union Building (42)',
	organisers = ['Karate-Do Shotokai Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 43 ,
	title = 'Live Music Society Weekly Jam session',
	description = "Join us for our free weekly jam sessions! It's an\
    open jam, so feel free to turn up, and play, sing, or simply watch.\
    We provide a relaxed and engaging environment for musicians of any genre\
    and ability to enjoy playing music. Songs, solos, or improvised jams! Stags afterwards...",
	category = ['hobbies'],
	tags = ['on_campus', 'societies', 'free', 'alcohol'],
	start_date = '03-03-2018 15:00',
	end_date = '03-03-2018 18:00',
	place = 'Clubs & Socs Room',
	organisers = ['Live Music Society Group'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 44 ,
	title = 'Girls Night In: Part 2',
	description = "A cozy ladies' night in with special guest Pearl Kasi!\
    The topic for the night is self love and focuses on learning how to deal\
    with the past and letting go of pain. Join us for a snug night in and a chance\
    to mingle, confront our demons and conquer our issues",
	category = ['hobbies'],
	tags = ['city_center', 'societies', 'talk'],
	start_date = '02-03-2018 19:00',
	end_date = '02-03-2018 21:00',
	place = 'Hampton Square',
	organisers = ['Women of Colour Society Group'],
	web_link = 'https://www.wocsoc.co.uk/',
	tickets_link = ''
	)

create_event(
	id = 45 ,
	title = 'University Mental Health Day Chill Out Space',
	description = "Take some time for yourself this University Mental Health Day!\
    We will have mindful colouring, friendship bracelet making, bubbles, drinks and snacks in Meeting Room 5.",
	category = ['hobbies'],
	tags = ['on_campus', 'societies', 'free', 'food', 'alcohol', 'susu'],
	start_date = '01-03-2018 10:00',
	end_date = '01-03-2018 17:00',
	place = 'Meeting Room 5',
	organisers = ['SUSU'],
	web_link = '',
	tickets_link = ''
	)

create_event(
	id = 46 ,
	title = 'Mentor Masterclass Jan Ward',
	description = "‘How to start an international business from your bedroom.’\
    Join Future Worlds’ Mentor Jan Ward, CBE, for March’s Masterclass talk.\
    Jan has been celebrated as a female entrepreneur throughout her career,\
    she was named the ‘UK’s most inspirational female entrepreneur‘ and won the\
    coveted NatWest Everywoman Award. Jan’s business career had a humble start,\
    having left school at 15 with no qualifications, however her passion for engineering\
    started when she undertook a trainee role at a local metal supply and distribution company.\
    After working her way up and developing strong international connections in markets such as\
    the Middle East, she decided to start an engineering company herself, from her front room.\
    22 years later her company, Corrotherm International, has a great international reputation\
    with offices currently in 8 countries around the world.\
    In this talk Jan will share stories from her fascinating career and offer advice for anyone hoping\
    to do the same.\
    The Future Worlds Mentor Masterclass series allows students and staff at the University of Southampton\
    exclusive access to learn from entrepreneurs and industry experts as well as an exclusive opportunity\
    to see pitches and product demos from startups and spinouts in the Future Worlds network.",
	category = ['academic'],
	tags = ['on_campus', 'free', 'food', 'talk'],
	start_date = '07-03-2018 12:30',
	end_date = '07-03-2018 14:00',
	place = 'Foyer, Turner Sims',
	organisers = ['Future Worlds'],
	web_link = 'https://www.facebook.com/events/216398882243721/',
	tickets_link = ''
	)

create_event(
	id = 47 ,
	title = 'Christmas Lights 2017',
	description = "Join the University and the Students' Union as we switch on our\
    Christmas Lights on Tuesday 21 November 2017. Come together with your friends and\
    the University community as we enjoy a Christmas market, carols and a glass of mulled\
    wine, mulled cider or a festive soft drink! Register now to receive a complimentary drink. Timings:\
    From 16:00 - Visit the Christmas market around the crescent area for gifts and festive\
    foods| 16:30 - Enjoy Christmas carols performed by our brass band | 18:00 - Christmas Lights\
    Switch On from the balcony of B40 | 18:10 - Live music until late in The Stag's & The Bridge | Further\
    Info: This event is for staff and students of the University of Southampton only. Due to expected\
    large numbers we cannot allow children to attend this event and you will be turned away on arrival.\
    Our Family Christmas event will take place on the afternoon of Monday 11 December, and is specifically\
    for children, further details will soon be on SUSSED. If you have pre-registered for a complimentary\
    drink please have your QR code available (either printed or on your to view on your phone) to exchange\
    for a drinks token. This can be done on the day from 16:00, at one of the drinks outlets (The Bridge,\
    The Stag's or one of the outside bars). There will a selection of both alcoholic and non-alcoholic drinks\
    available. Please note that the complimentary drink is limited to one per person (either mulled wine, mulled\
    cider or a soft drink). Tickets will be scanned in exchange for each drink. You may be asked to show your\
    University ID so please ensure you have this to hand. This event is outside so please wear appropriate\
    footwear and warm clothing.",
	category = ['party', 'hobbies'],
	tags = ['on_campus', 'alcohol', 'sing', 'dance', 'free'],
	start_date = '21-11-2017 16:00',
	end_date = '22-11-2017 01:00',
	place = 'University of Southampton, Highfield Campus',
	organisers = ['University of Southampton - Student Communications'],
	web_link = 'https://www.facebook.com/events/280374559138828/',
	tickets_link = ''
	)

create_event(
	id = 48 ,
	title = 'Full Band Open Mic/Jam',
	description = "As part of this years Culture Festival, we're running a jam style\
    open mic in the Bridge. Slots are 15 minutes and will be available first come first\
    serve on the night. A full backline of drums, guitar/bass amps, keyboards and mics\
    are provided, but feel free to bring your own instruments! All instruments are welcome.\
    The house band will be the fantastic LiveSoc committee who will try to cater to any songs\
    or jam ideas.",
	category = ['party', 'hobbies'],
	tags = ['on_campus', 'alcohol', 'sing', 'dance', 'free','susu'],
	start_date = '09-03-2017 19:00',
	end_date = '09-03-2017 23:00',
	place = 'The Bridge',
	organisers = ['SUSU','University of Southampton Live Music Society - Livesoc'],
	web_link = 'https://www.facebook.com/events/581116465557572/',
	tickets_link = ''
	)

create_event(
	id = 49 ,
	title = 'Movie: Black Panther',
	description = "T'Challa, the new ruler of the advanced kingdom of Wakanda,\
    must defend his land from being torn apart by enemies from outside and inside the country.",
	category = ['hobbies'],
	tags = ['on_campus', 'movie','susu'],
	start_date = '11-03-2017 14:30',
	end_date = '',
	place = 'Union Films',
	organisers = ['SUSU'],
	web_link = 'https://www.unionfilms.org/films/reviews/black-panther.html',
	tickets_link = 'http://boxoffice.susu.org/view/26/union-films'
	)

create_event(
	id = 50 ,
	title = 'Movie: Paddington 2',
	description = "Paddington, now happily settled with the Brown family and a popular member of the\
    local community, picks up a series of odd jobs to buy the perfect present for his Aunt Lucy's\
    100th birthday, only for the gift to be stolen.",
	category = ['hobbies'],
	tags = ['on_campus', 'movie','susu'],
	start_date = '13-03-2017 19:30',
	end_date = '',
	place = 'Union Films',
	organisers = ['SUSU'],
	web_link = 'https://www.unionfilms.org/films/reviews/paddington-2.html',
	tickets_link = 'http://boxoffice.susu.org/view/26/union-films'
	)