cqbycq_prompt = '''Your task is to contribute in creation of a well-structured ontology informations that appeared in the given story, requirements, and restrictions (if there are any).
The way you approach this is first you pick this competency question number "{CQ}" and read the given turtle RDF to know what is the current ontology till this stage (it can be empty at the begining). Then you add or change the RDF so it can answer to this competency question. Your output at each stage is an independent turtle, so rewrite/edit the previous RDF and produce the new one. You only need to solve the question number so do not touch the next questions since they belong to the next stages of development. you can read this definisions to understand the concepts:
lasses are the keywords/classes that are going to be node types in the knowledge graph ontology. try to extract all classes, in addition, classes are also can be defined for reification. We use Turtle Syntax for representation. Hierarchies are rdfs:subClassOf in the turtle syntax. They can be used to classify similar classes in one superclass. To do this you can find similar nodes and create/use a class as their parent class, for example, adding the node "Cl_employee" is a good middleware and superclass for "Cl_Professors" and "Cl_Administrator" if the story is about modeling ontology of a university. Mostly the lengthier the hierarchy the better. One way can be categorizing classes into several classes and creating superclasses for them. Important: Class names have Cl_ as the prefix for example Cl_Professors. Also keep in mind you can add Equivalent To, General class axioms, Disjoint with, and Disjoint Union of, for each class.
In your ontology modeling, for each competency question, when faced with complex scenarios that involve more than two entities or a combination of entities and datatypes, apply reification. Specifically, create a pivot class to act as an intermediary for these entities, ensuring the nuanced relationships are accurately captured. For instance, when representing "a user accessed a resource at a given time", establish a pivot class like Cl_UserResourceUsage, linked from the user, resource, and the specific time of access to Cl_UserResourceInteraction, rather than directly connecting the user to both the resource and time.
Then you need to create properties (owl:Property). In this step, you use classes from the previous stage and create object and data properties to connect them and establish the ontology. Always output a turtle syntax, if you need more classes to model a competency question between more than 2 concepts, feel free to add more pivot (reification) classes here. try to find as much relation as possible by reading competency questions, restrictions, and stories. At this stage, you can create both data and object properties. Data properties are between classes or hierarchy classes and data types such as xsd:string, xsd:integer, xsd:decimal, xsd:dateTime, xsd:date, xsd:time, xsd:boolean, xsd:byte, xsd:double, xsd:float and etc. For example, in the university domain, we have: employee_id a owl:Property ; rdfs:domain :cl_teacher ; rdfs:range xsd:integer. Object properties are between classes. try to find as much relation as possible by reading competency questions and the story. Feel free to use rdfs:subPropertyOf for creating hierarchies for relations. For modeling properties (object or data properties) if it is necessary, use these relations characteristics: Functional, Inverse functional, Transitive, Symmetric, Asymmetric, Reflexive, and Irreflexive. Also, you are flexible in domain and range so you can use Cl_class1 or Cl_class2 in domain and range or disjoint with, the inverse of between relations.
It is common to forget to add relations that are related to reification: In RDF reification, achieving precise modeling is pivotal, especially when handling multifaceted scenarios where mere binary associations fall short. Take for instance the statement, "a user used a resource at a time". While it might initially seem to involve a direct link between a 'user' and a 'resource', it inherently embodies three entities: a 'user', a 'resource', and a 'time'. Directly connecting 'user' to both 'resource' and 'time' fails to capture the essence of the statement, as it obscures which resource was utilized by the user at a specific time. To address this, a more sophisticated modeling approach is needed, invoking a pivot class, Cl_usingResource. This pivot class acts as an intermediary, linking both Cl_user and Cl_resource. Furthermore, it integrates a time property to denote the exact instance of usage. By employing this method, we can coherently model the statement, ensuring that the user's interaction with a specific resource at a distinct time is unambiguously represented. This approach highlights the imperative of ontology design patterns and the necessity of intermediary nodes when modeling complex relationships involving multiple entities or a mix of entities and datatypes.
Upon implementation of restrictions, feel free to use owl:equivalentClass [ rdf:type owl:Restriction ;  owl:onProperty :{{relation}} ;  owl:allValuesFrom :{{Class}} ] ; in this way, you can put restrictions for classes such as class Cl_C1 is the only class that uses the relation R. or you can put soft restrictions by using owl:someValuesFrom. Also, you can use general class axioms: [ rdf:type owl:Restriction ; owl:onProperty :R1 ; owl:someValuesFrom :Cl_1 ; rdfs:subClassOf :Cl_2 ] when you want to put restrictions on the definition of a class based on its relation and the definition is necessary but not enough (if it is enough it would be equivalent to owl:equivalentClass).
Do not forget, you output is an independent ontology and is going to replace the previous version. At this promt, only solve the given competency question and dont jumpt to other questions.
these are the prifixes:
@prefix : <http://www.example.org/test#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
Important: before writing the owl code, write this text: is this competency question answarable by the previous version of the RDF (given down) or not? (most likely (~90%) is it not answarable). If no, write a refification class for this question if needed. then solve it. if it was answarable, simply rewrite the given rdf in the output without changing it.
here is one story:
{story}
End of story
here are some possible mistakes that you might make:
1- forgetting to add prefixes at the beginning of the code.
2- forgetting to write pivot classes at the beginning before starting to code.
3- your output must use the previous rdf and concatinate the answer of competency question to it. so your output is create and merge.
4- in your output put all of the previous rdf classes, relations, restrictions and add yours. your output would be passed to the next stage so dont remove previous code (it is going to replace the previous rdf)
5- you usually forget to write the name of the reification (pivot) that you want create at the begining of the output
common mistakes in extracting classes:
1- not extracting all classes and missing many of them. classes can be found in the story, or in the competency question number and restrictions.
2- Returning empty answer
3- Providing comments or explanations
4- Extracint classes like 'Date', and 'integer' are wrong since they are data properties.
5- not using RDF reification: not extracting pivot classes for modeling relation between classes (more than one class and one dataproperty, or more than two classes)
6- extracting individuals in the text as class
7- pivot class is not sublcass of its components.
common mistakes in the hierarchy extraction:
1- creating an ontology for non-existing classes: creating a new leaf and expanding it into the root
2- returning empty answer or very short
3- Providing comments or explanations
4- Extracting attributes such as date, time, and string names that are related to data properties
5- Forget to add "" around the strings in the tuples
Common mistakes in the object_properties:
1- returning new variables with anything except object_properties
2- returning empty answer or very short
3- providing comments or explanations
4- when the pivot class is created, all of the related classes should point to it (direction of relation is from the classes (domains) 'to'  pivot class (range))
Common mistakes in the data_properties:
1- returning new variables with anything except data_properties
2- returning empty answer or very short
3- providing comments or explanations
Here is the last RDF:
{rdf}
'''

