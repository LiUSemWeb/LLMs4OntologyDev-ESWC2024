class Datasets:
  def __init__(self):
    ###################################################
    ###########       Theatre Fest          ###########
    ###################################################    
    self.story_theatre = '''Theatre productions
During each year a number of theatre festivals are held in cities around Italy. In January 2007 a festival called “Roma Loves Shakespeare” took place in Rome. Two different productions of “The Merchant of Venice” participated, one from a theatre in Pisa and the other from a theatre institute in Venice, featuring an ensemble of university art students. Other plays were Othello and a Midsummer Night’s Dream.
The Grand Theatre in Rome offers two theatre shows each evening during September and October 2009. The play set up in this period is the "Merchant of Venice",given through an ensemble of well-known Italian actors. The Merchant of Venice was written during 1596 to 1598 by William Shakespeare, and it has 5 distinct acts. The premier of this production at The Grand Theatre was on September 7. Il Gazzettino gave the setup of the play 5 stars in a recent review.
Fabio Bianchi is an Italian actor employed at the theatre since May 2004, he is a part of the ensemble setting up the Merchant of Venice and he plays the Duke of Venice but also a servant in one of the scenes. During the second and third week of September the role of Shylock is played by Arnold Schwarzenegger as a special guest actor.
'''
    self.story_theatre_cqs = [
      'When did a certain theatre festival take place?',
      'Where did a certain festival take place?',
      'What plays could be seen during a certain theatre festival?',
      'In what city is a certain theatre located?',
      'In what country is a certain city located?',
      'What play is the basis of this production?',
      'Who are the members of a certain ensemble at a certain point in time? ',
      'What plays did a certain author write?',
      'During what time period was a certain play written?',
      'How many acts does a particular play contain?',
      'When was the premier of a certain production?',
      'What is the “star rating” given by a certain newspaper for a certain production?',
      'At what time did a certain actor start working for a specific theatre?',
      'What roles does a certain person have within a certain production at a certain point in time?  ',
      'A production has exactly one premier.',
    ]
    ###################################################
    ###########       Music produc          ###########
    ################################################### 

    self.story_music = '''Music production
The current configuration of the “Red Hot Chili Peppers” are: Anthony Kiedis (vocals), Flea (bass, trumpet, keyboards, and vocals), John Frusciante (guitar), and Chad Smith (drums).  The line-up has changed a few times during they years, Frusciante replaced Hillel Slovak in 1988, and when Jack Irons left the band he was briefly replaced by D.H. Peligo until the band found Chad Smith. In addition to playing guitars for Red hot Chili Peppers Frusciante also contributed to the band “The Mars Volta” as a vocalist for some time.
From September 2004, the Red Hot Chili Peppers started recording the album “Stadium Arcadium”. The album contains 28 tracks and was released on May 5 2006. It includes a track of the song “Hump de Bump”, which was composed in January 26, 2004.
The critic Crian Hiatt defined the album as "the most ambitious work in his twenty-three-year career". On August 11 (2006) the band gave a live performance in Portland, Oregon (US), featuring songs from Stadium Arcadium.
'''
    self.story_music_cqs = [
      'What instruments does a certain person play?',
      'What are the members of a certain band at a certain point in time?',
      'What role does a certain person have in a certain band at a certain point in time?',
      'During what time period was a certain album recorded?',
      'How many tracks does a particular album contain?',
      'When was a certain album released?',
      'What song is a specific track a recording of?',
      'When was a certain song composed?',
      'What does a certain critic say about a certain record?',
      'When did a certain performance take place?',
      'What songs were played in a certain performance?',
      'Where did a certain performance take place?',
      'In what region is a certain city located?',
      'In what country is a certain region located?',
      'A record always contains at least one track.',
    ]
    ###################################################
    ###########       Hospital              ###########
    ################################################### 
    self.story_hospital ='''Hospital setting
Pasquale Di Gennaro first studied to become a nursing assistant, but after working some years he decided to continue studying to become a certified nurse. He took his degree in May 2001. On September 21 (2001) he was employed at Ospedale Riunito delle Tre Valli in the city of Nocera Inferiore (IT). In the hospital there are different unions organising the staff. Pasquale Di Gennaro has been the union representative for male nurses at Ospedale Riunito delle Tre Valli from 2002. Senior doctors regularly evaluate all employees working with patient care, and these written statements are stored for future reference.
To constantly update their knowledge both nurses and doctors read research articles that can be found in article collections at the hospital library. Article collections are usually available both as books and electronically on CDs. In 2008 an article collection entitled “Nurse practices in cancer patient care – longitudinal studies at Italian hospitals” was published as a book. The book contains an article by Pasquale Di Gennaro, entitled “A 5 year-program for improving cancer care – experiences and future directions”. In total the book version of this collection has 346 pages. For discussing new articles Italian hospitals regularly hold seminars where a number of articles are presented. In December 2008 such a seminar was held in Nocera Inferiore at Ospedale Riunito delle Tre Valli.'''
    self.story_hospital_cqs = [
      'What medical degrees does a certain person have?',
      'During what time period did a certain person study for a specific degree?',
      'When was a certain person first employed at a certain hospital?',
      'In what city is a certain hospital located?',
      'In what country is a certain city located?',
      'Who are the members of a certain union at a certain point in time?',
      'What role does a certain person have within a certain union group at a certain point in time?',
      'What is the evaluation statement given by a certain doctor for a certain employee?',
      'What articles is a specific book or CD composed of?',
      'How many pages does a particular book contain?',
      'When was a certain book or CD published?',
      'When did a certain seminar take place?',
      'What articles were presented in a certain seminar?',
      'Where did a certain seminar take place?',
      'At least one article is always presented at each seminar.',
    ]
    ###################################################
    ###########    Intel Bathroom part1     ###########
    ################################################### 
    self.story_intelbath='''Inteligence bathroom
I am alone in the bathroom. I am standing facing the mirror with the electric toothbrush in my hand, hence, the system recognizes that I am brushing my teeth.
I was brushing my teeth in the bathroom on Thursday morning. Morning is between 6 and 10am according to the current user.
I am living in Berlin and I like to get the local weather displayed in the morning as soon as I am brushing my teeth.
There are many different weather services available online, I prefer www.yr.no. My preferred configuration of the service is the weather service for Berlin with the current 3-day prognosis.
When I am standing in front of the mirror brushing my teeth the weather is displayed as graphics on the mirror, but when I walk around the bathroom it is read out through the loudspeakers.
I like going to the movies when it is raining, and I especially like to see action movies.
Today my calendar contains a meeting at noon, but then I have the afternoon and evening off.
Based on the fact that I have the evening off, that it is going to rain, and that I like to go to the movies on my free-time, the system finds a film that I could see tonight.
There is a sneak preview of an action film called “X-men” today at 8pm at CinemaOne.
The system asks me if I want to order tickets to a proposed event if there are tickets available. I am presented with a set of ticket options, and get to select the time of the show, the seat I want at the movie theatre. Finally, I pay by credit card.'''
    self.story_intelbath_cqs = [
      'Who is where in this indoor location?',
      'What sensor data is known about this user’s context?',
      'What is the user doing now?',
      'What did the user do previously?',
      'At what time and day of the week did a certain event occur?',
      'What “abstract time” (e.g. “morning”) is it now according to this particular user?',
      'Where does this user live/where does the system run?',
      'What is the system action preferred by this user in this particular context?',
      'What is the weather service providing this personalized weather information?',
      'What are the attributes of this weather service?',
      'What attribute values for the weather service are to be used in order to derive the personalized weather information for this user?',
      'What devices are available in this indoor location?',
      'What functionalities does this device provide?',
      'Using what device and what functionality of that device should this content be displayed?',
      'How should this content be presented, given the user\'s context?',
      'What are the preferred movie categories of the current user?',
      'What does this user prefer to do in a certain situation?',
      'What bookings does the user’s calendar contain during a certain time period?',
      'What are the free time periods in the user’s calendar today?',
      'What events of a specific event category, e.g. movies, are available during a certain time period?',
      'What is the most suitable event to propose to the user for a certain time period, based on the weather, the calendar and the user’s preferences?',
      'What is the start and end time of this event?',
      'What are the attributes of this event category (e.g. a movie has a genre and a set of actors)?',
      'What are the attribute values for this event?',
      'What are the options available for this event category/specific event (i.e. what can be customized by the user, e.g. seat selection and time of show for a movie)?',
      'What is the default value of this option for this user in this context?',
      'What are my booking details?',
    ]
    ###################################################
    ###########         Toy Stories         ###########
    ################################################### 
    self.toystory1 = '''This story discusses two primary food categories: vegetarian foods and meat. Vegetarian animals exclusively eat vegetables, while non-vegetarian animals can consume vegetables or meat without restrictions on their diets. In the context of animals, rabbits are given as an example of vegetarian eaters. The relation "eats" describes the relationship between animals and the types of food they consume.    '''
    self.toystory1_cqs = [
        'There are two types of food: vegeterian foods and non-vegeratian foods.',
        'vegetarian animals do not eat meat but only vegetables.',
        'non-vegetarian animals eat vegetables or meat without any restrictions.',
        'Rabbits eat only vegeterian foods.',
        'Relation eats is a relation between animals and foods.',
        'create an individual rabit R1 that eats individual meat m1',
    ]
    self.toystory2 = '''This narrative outlines a unique world that models relationships between gender, preferences, and objects, allowing for insights and deductions based on the set ontology.    '''

    self.toystory2_cqs = [
      'Women are defined as persons that are also female (hint: you can use a class intersection)',
      'A person cannot be both a man and a woman (hint: disjointness)',
      'Persons are either men or women (hint: you can use a class union)',
      'Liking something is a relation applicable to persons (hint: use a domain restriction)',
      'A car is a kind of vehicle (hint: subclass relation)',
      'Ferrari and Alfa Romeo are Italian cars (hint: in this case we will model car brands as instances of cars, we do not care about individual physical cars)',
      'All women like some car (hint: others may also like cars, so use a subclass restriction rather than an equivalent class)',
      'Women like only Italian cars. Men like at least one car.',
      'Clara is a woman, so is Samantha. Clara\'s full name is Clara Smith (hint: use either rdfs:label or create a datatype property)',
      'Clara is 30 years old. Samantha and Clara are different individuals',
      'Sam is the same person as Samantha',
      'To adore is a special case of liking, where the thing being liked is always a car',
      'To be adored by is the inverse of adoring',
      'To have a part is a transitive relation. Cars have some wheels as parts',
      'Add an instance of woman named Lena, add a man named Thomas, then add the fact that Thomas adores Lena. Run a reasoner over the ontology. What is concluded about Lena?',
    ]

    self.toystory3 = '''In this ontology modeling, we are trying to model a theatre festival ontology. A theatre festival is a curated event or series of events that showcase a variety of theatrical performances, often held over a specific period of time in a particular location. These festivals bring together multiple theatre productions, ranging from plays and musicals to experimental and avant-garde performances. Each festival has several plays in it.'''
    self.toystory3_cqs = [
      'When and where does a festival happen?',
      'What is the duration of a festival?',
      'A large festival is defined as a festival with more than three plays in it.'
    ]