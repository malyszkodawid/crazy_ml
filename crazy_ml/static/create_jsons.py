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
	tags = ['on_campus', 'free', 'talk', 'food', 'ecs'],
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
	tags = ['city_center', 'dance', 'alcohol'],
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
	tags = ['city_center', 'societies', 'alohol'],
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
	tags = ['on_campus', 'alcohol', 'dance', 'free', 'dance','susu'],
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

# create_event(
# 	id = ,
# 	title = '',
# 	description = "",
# 	category = [],
# 	tags = [],
# 	start_date = '17-02-2018 09:00',
# 	end_date = '17-02-2018 10:00',
# 	place = '',
# 	organisers = [''],
# 	web_link = '',
# 	tickets_link = ''
# 	)

# create_event(
# 	id = ,
# 	title = '',
# 	description = "",
# 	category = [],
# 	tags = [],
# 	start_date = '17-02-2018 09:00',
# 	end_date = '17-02-2018 10:00',
# 	place = '',
# 	organisers = [''],
# 	web_link = '',
# 	tickets_link = ''
# 	)

# create_event(
# 	id = ,
# 	title = '',
# 	description = "",
# 	category = [],
# 	tags = [],
# 	start_date = '17-02-2018 09:00',
# 	end_date = '17-02-2018 10:00',
# 	place = '',
# 	organisers = [''],
# 	web_link = '',
# 	tickets_link = ''
# 	)

# create_event(
# 	id = ,
# 	title = '',
# 	description = "",
# 	category = [],
# 	tags = [],
# 	start_date = '17-02-2018 09:00',
# 	end_date = '17-02-2018 10:00',
# 	place = '',
# 	organisers = [''],
# 	web_link = '',
# 	tickets_link = ''
# 	)


