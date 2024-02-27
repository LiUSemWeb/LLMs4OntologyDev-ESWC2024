# Here are ontology stories in the experiments
In our experiment, we have two sets of experiments, the Initial experiment and the Main experiment. 
### Goals in short narratives
 - Vegetarians: the individual rabbit must be classified as a non-vegetarian (Error Provocation)
 - Lena: the individual Lena must be classified as a Car (Error Provocation)
 - Big Festival: The existence of a class "Big festival" or a way to extract a big festival (according to definitions) is examined (Inference Verification)
### Goals in ontology stories (the main experiment)
The goal is simple, we want an ontology that can answer/model all CQs. Answering/modeling a CQ is done when a SPARQL query can be written to extract the answer to the CQ.
Competency questions in all of these three stories (for the main experiment) are similar. As described in the paper, we have four types of CQs: 
- 1- Simple data property: to model this CQ, we need a data property and sometimes a class
- 2- Simple object property: to model this CQ, we need an object property between two classes, sometimes one or two classes must be created.
- 3- Reification: Complex scenario, a reification class (or relation class) which is a node type must be added and all properties must be added to the reification class.
- 4- Restrictions: establishing subClassOf or any other axioms that restrict relations between classes.

The stories are as follows:

## Short Narratives (Initial Experiment)
### Story 1: Vegetarians
This story discusses two primary food categories: vegetarian foods and meat. Vegetarian animals exclusively eat vegetables, while non-vegetarian animals can consume vegetables or meat without restrictions on their diets. In the context of animals, rabbits are given as an example of vegetarian eaters. The relation "eats" describes the relationship between animals and the types of food they consume.
here are the competency questions:
```
[ '1- There are two types of food: vegetarian foods and non-vegetarian foods.',
  '2- vegetarian animals do not eat meat but only vegetables.',
  '3- Non-vegetarian animals eat vegetables or meat without any restrictions.',
  '4- Rabbits eat only vegetarian foods.',
  '5- Relation eats is a relation between animals and foods.',
  '6- create an individual rabbit R1 that eats individual meat m1']
```
### Story 2: Lena
This narrative outlines a unique world that models relationships between gender, preferences, and objects, allowing for insights and deductions based on the set ontology.
here are the competency questions:
```
['1- Women are defined as persons that are also female (hint: you can use a class intersection)',
'2- A person cannot be both a man and a woman (hint: disjointness)',
'3- Persons are either men or women (hint: you can use a class union)',
'4- Liking something is a relation applicable to persons (hint: use a domain restriction)',
'5- A car is a kind of vehicle (hint: subclass relation)',
'6- Ferrari and Alfa Romeo are Italian cars (hint: in this case we will model car brands as instances of cars, we do not care about individual physical cars)',
'7- All women like some car (hint: others may also like cars, so use a subclass restriction rather than an equivalent class)',
'8- Women like only Italian cars. Men like at least one car.',
'9- Clara is a woman, so is Samantha. Clara\'s full name is Clara Smith (hint: use either rdfs:label or create a datatype property)',
'10- Clara is 30 years old. Samantha and Clara are different individuals',
'11- Sam is the same person as Samantha',
'12- To adore is a special case of liking, where the thing being liked is always a car',
'13- To be adored by is the inverse of adoring',
'14- To have a part is a transitive relation. Cars have some wheels as parts',
'15- Add an instance of a woman named Lena, add a man named Thomas, then add the fact that Thomas adores Lena. Run a reasoner over the ontology. What is concluded about Lena?',]
```
### Story 3: Big Festival
In this ontology modeling, we are trying to model a theatre festival ontology. A theatre festival is a curated event or series of events that showcase a variety of theatrical performances, often held over a specific period of time in a particular location. These festivals bring together multiple theatre productions, ranging from plays and musicals to experimental and avant-garde performances. Each festival has several plays in it.
here are the competency questions:
```
['When and where does a festival happen?',
 'What is the duration of a festival?',
 'A large festival is defined as a festival with more than three plays in it.']
```
<hr>

## Ontology Narratives (Main Experiment)
### Story 1: Theatre Festival
####Theatre productions
During each year a number of theatre festivals are held in cities around Italy. In January 2007 a festival called “Roma Loves Shakespeare” took place in Rome. Two different productions of “The Merchant of Venice” participated, one from a theatre in Pisa and the other from a theatre institute in Venice, featuring an ensemble of university art students. Other plays were Othello and a Midsummer Night’s Dream.
The Grand Theatre in Rome offers two theatre shows each evening during September and October 2009. The play set up in this period is the "Merchant of Venice",given through an ensemble of well-known Italian actors. The Merchant of Venice was written during 1596 to 1598 by William Shakespeare, and it has 5 distinct acts. The premier of this production at The Grand Theatre was on September 7. Il Gazzettino gave the setup of the play 5 stars in a recent review.
Fabio Bianchi is an Italian actor employed at the theatre since May 2004, he is a part of the ensemble setting up the Merchant of Venice and he plays the Duke of Venice but also a servant in one of the scenes. During the second and third week of September the role of Shylock is played by Arnold Schwarzenegger as a special guest actor.
here are the competency questions:
```
['1- When did a certain theatre festival take place?',
'2- Where did a certain festival take place?',
'3- What plays could be seen during a certain theatre festival?',
'4- In what city is a certain theatre located?',
'5- In what country is a certain city located?',
'6- What play is the basis of this production?',
'7- Who are the members of a certain ensemble at a certain point in time? ',
'8- What plays did a certain author write?',
'9- During what time period was a certain play written?',
'10- How many acts does a particular play contain?',
'11- When was the premier of a certain production?',
'12- What is the “star rating” given by a certain newspaper for a certain production?',
'13- At what time did a certain actor start working for a specific theatre?',
'14- What roles does a certain person have within a certain production at a certain point in time?  ',
'15- A production has exactly one premier.',]
```
### Story 2: Music Production
Music production
The current configuration of the “Red Hot Chili Peppers” are: Anthony Kiedis (vocals), Flea (bass, trumpet, keyboards, and vocals), John Frusciante (guitar), and Chad Smith (drums).  The line-up has changed a few times during they years, Frusciante replaced Hillel Slovak in 1988, and when Jack Irons left the band he was briefly replaced by D.H. Peligo until the band found Chad Smith. In addition to playing guitars for Red hot Chili Peppers Frusciante also contributed to the band “The Mars Volta” as a vocalist for some time.
From September 2004, the Red Hot Chili Peppers started recording the album “Stadium Arcadium”. The album contains 28 tracks and was released on May 5 2006. It includes a track of the song “Hump de Bump”, which was composed in January 26, 2004.
The critic Crian Hiatt defined the album as "the most ambitious work in his twenty-three-year career". On August 11 (2006) the band gave a live performance in Portland, Oregon (US), featuring songs from Stadium Arcadium.
here are the competency questions:
```
['1- What instruments does a certain person play?',
'2- What are the members of a certain band at a certain point in time?',
'3- What role does a certain person have in a certain band at a certain point in time?',
'4- During what time period was a certain album recorded?',
'5- How many tracks does a particular album contain?',
'6- When was a certain album released?',
'7- What song is a specific track a recording of?',
'8- When was a certain song composed?',
'9- What does a certain critic say about a certain record?',
'10- When did a certain performance take place?',
'11- What songs were played in a certain performance?',
'12- Where did a certain performance take place?',
'13- In what region is a certain city located?',
'14- In what country is a certain region located?',
'15- A record always contains at least one track.',]
```
### Story 2: Hospital Story
Hospital setting
Pasquale Di Gennaro first studied to become a nursing assistant, but after working some years he decided to continue studying to become a certified nurse. He took his degree in May 2001. On September 21 (2001) he was employed at Ospedale Riunito delle Tre Valli in the city of Nocera Inferiore (IT). In the hospital there are different unions organising the staff. Pasquale Di Gennaro has been the union representative for male nurses at Ospedale Riunito delle Tre Valli from 2002. Senior doctors regularly evaluate all employees working with patient care, and these written statements are stored for future reference.
To constantly update their knowledge both nurses and doctors read research articles that can be found in article collections at the hospital library. Article collections are usually available both as books and electronically on CDs. In 2008 an article collection entitled “Nurse practices in cancer patient care – longitudinal studies at Italian hospitals” was published as a book. The book contains an article by Pasquale Di Gennaro, entitled “A 5 year-program for improving cancer care – experiences and future directions”. In total the book version of this collection has 346 pages. For discussing new articles Italian hospitals regularly hold seminars where a number of articles are presented. In December 2008 such a seminar was held in Nocera Inferiore at Ospedale Riunito delle Tre Valli.
here are the competency questions:
```
['1- What medical degrees does a certain person have?',
'2- During what time period did a certain person study for a specific degree?',
'3- When was a certain person first employed at a certain hospital?',
'4- In what city is a certain hospital located?',
'5- In what country is a certain city located?',
'6- Who are the members of a certain union at a certain point in time?',
'7- What role does a certain person have within a certain union group at a certain point in time?',
'8- What is the evaluation statement given by a certain doctor for a certain employee?',
'9- What articles is a specific book or CD composed of?',
'10- How many pages does a particular book contain?',
'11- When was a certain book or CD published?',
'12- When did a certain seminar take place?',
'13- What articles were presented in a certain seminar?',
'14- Where did a certain seminar take place?',
'15- At least one article is always presented at each seminar.',]
```