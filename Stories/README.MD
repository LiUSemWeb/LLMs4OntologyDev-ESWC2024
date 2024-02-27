# Here are ontology stories in the experiments
In our experiment, we have two sets of experiments, the Initial experiment and the Main experiment. 
### Goals in short narratives
 - Vegetarians: the individual rabbit must be classified as a non-vegetarian (Error Provocation)
 - Lena: the individual Lena must be classified as a Car (Error Provocation)
 - Big Festival: The existence of a class "Big festival" or a way to extract a big festival (according to definitions) is examined (Inference Verification)

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
'1- Women are defined as persons that are also female (hint: you can use a class intersection)',
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
'15- Add an instance of a woman named Lena, add a man named Thomas, then add the fact that Thomas adores Lena. Run a reasoner over the ontology. What is concluded about Lena?',
```
    





