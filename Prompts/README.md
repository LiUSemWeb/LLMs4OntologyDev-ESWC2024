# Prompts and Promoting Techniques

## Table of Contents
- [Prompts](#prompts)
  - Zero-Shot Prompting
  - Sub-task Decomposed Prompting: Waterfall approach
  - Sub-task Decomposed Prompting: Competency Question by Competency Question (CQbyCQ)
  - Chain of Thoughts
  - Self Consistency with Chain of Thoughts (CoT-SC)
  - Graph of Thoughts (GoT)
## [Zero-Shot](#zero-shot)
This method entails a one-time interaction with the LLM, requiring no iteration or feedback loop, utilizing a prompt composed of the four components outlined in the previous section: the **header**, **helper**, **story**, and **footer**. Together, the sections of the prompt provide all the information needed for the ontology construction in a single interaction.

## [Sub-task Decomposed Prompting - Waterfall](#Waterfall)
The LLM prompting method involves five stages. Initially, the LLM translates core requirements into short descriptions. In the second stage, it extracts classes. In the third stage, it constructs a taxonomy. The fourth stage defines connections between established classes, and the fifth stage creates data properties. Each step includes instructions on how to establish restrictions. 
Each stage has four components: the **header**, **helper**, **story**, and **footer**. Each is designed based on the stage.

## Zero-Shot
### Header
Your task is to contribute to the creation of well-structured ontology information that appeared in the given story, requirements, and restrictions (if there are any).
### Helper
The way to approach this is you first create classes with their hierarchies. Classes are the keywords/classes that are going to be node types in the knowledge graph ontology. try to extract all classes, in addition, classes are also can be defined for reification. We use Turtle Syntax for representation. Hierarchies are rdfs:subClassOf in the turtle syntax. They can be used to classify similar classes in one superclass. To do this you can find similar nodes and create/use a class as their parent class, for example, adding the node "Cl_employee" is a good middleware and superclass for "Cl_Professors" and "Cl_Administrator" if the story is about modeling ontology of a university. Mostly the lengthier the hierarchy the better. One way can be categorizing classes into several classes and creating superclasses for them. Important: Class names have Cl_ as the prefix for example Cl_Professors. Also keep in mind you can add Equivalent To, General class axioms, Disjoint with, and Disjoint Union of, for each class.   
In your ontology modeling, for each competency question, when faced with complex scenarios that involve more than two entities or a combination of entities and datatypes, apply reification. Specifically, create a pivot class to act as an intermediary for these entities, ensuring the nuanced relationships are accurately captured. For instance, when representing "a user accessed a resource at a given time", establish a pivot class like Cl_UserResourceUsage, linked from the user, resource, and the specific time of access to Cl_UserResourceInteraction, rather than directly connecting the user to both the resource and time.  
Then you need to create properties (owl:Property). In this step, you use classes from the previous stage and create object and data properties to connect them and establish the ontology. Always output a turtle syntax, if you need more classes to model a competency question between more than 2 concepts, feel free to add more pivot (reification) classes here. try to find as much relation as possible by reading competency questions, restrictions, and stories. At this stage, you can create both data and object properties. Data properties are between classes or hierarchy classes and data types such as xsd:string, xsd:integer, xsd:decimal, xsd:dateTime, xsd:date, xsd:time, xsd:boolean, xsd:byte, xsd:double, xsd:float and etc. For example, in the university domain, we have: employee_id a owl:Property ; rdfs:domain :cl_teacher ; rdfs:range xsd:integer. Object properties are between classes. try to find as much relation as possible by reading competency questions and the story. Feel free to use rdfs:subPropertyOf for creating hierarchies for relations. For modeling properties (object or data properties) if it is necessary, use these relations characteristics: Functional, Inverse functional, Transitive, Symmetric, Asymmetric, Reflexive, and Irreflexive. Also, you are flexible in domain and range so you can use Cl_class1 or Cl_class2 in domain and range or disjoint with, the inverse of between relations.  
It is common to forget to add relations that are related to reification: In RDF reification, achieving precise modeling is pivotal, especially when handling multifaceted scenarios where mere binary associations fall short. Take for instance the statement, "a user used a resource at a time". While it might initially seem to involve a direct link between a 'user' and a 'resource', it inherently embodies three entities: a 'user', a 'resource', and a 'time'. Directly connecting 'user' to both 'resource' and 'time' fails to capture the essence of the statement, as it obscures which resource was utilized by the user at a specific time. To address this, a more sophisticated modeling approach is needed, invoking a pivot class, Cl_usingResource. This pivot class acts as an intermediary, linking both Cl_user and Cl_resource. Furthermore, it integrates a time property to denote the exact instance of usage. By employing this method, we can coherently model the statement, ensuring that the user's interaction with a specific resource at a distinct time is unambiguously represented. This approach highlights the imperative of ontology design patterns and the necessity of intermediary nodes when modeling complex relationships involving multiple entities or a mix of entities and datatypes.  
Upon implementation of restrictions, feel free to use owl:equivalentClass [ rdf:type owl:Restriction ;  owl:onProperty :{relation} ;  owl:allValuesFrom :{Class} ] ; in this way, you can put restrictions for classes such as class Cl_C1 is the only class that uses the relation R. or you can put soft restrictions by using owl:someValuesFrom. Also, you can use general class axioms: [ rdf:type owl:Restriction ; owl:onProperty :R1 ; owl:someValuesFrom :Cl_1 ; rdfs:subClassOf :Cl_2 ] when you want to put restrictions on the definition of a class based on its relation and the definition is necessary but not enough (if it is enough it would be equivalent to owl:equivalentClass).
```
these are the prefixes:  
@prefix : <http://www.example.org/test#> .  
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .  
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .  
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```
### Story
Ontology story comes from users' input 

### Helper (pitfalls)

Important: your output should be only code. Don't write any explanation before the code block or after. Also, the code must have 0 comments.  
Besides here are some possible mistakes that you might make:  
1- forgetting to add prefixes at the beginning of the code.
2- forgetting to write pivot classes at the beginning before starting to code.
common mistakes in the class extraction:  
1- not extracting all classes and missing many of them. classes can be found in stories, competency questions (also a CQ can be a class if it is complex), and restrictions.  
2- returning empty answer  
3- providing comments or explanations, except, write one line and only just the name of the reification classes needed for each CQ before starting to code: CQ#1: Cl_Class1Class2 ... CQ#3: .... nothing else  
4- extracting classes like 'Date' is wrong since they are data properties.    
5- not using RDF reification: not extracting pivot classes for modeling relation between classes (more than one class and one dataproperty, or more than two classes)  
common mistakes in the hierarchies:  
1- creating an ontology for non-existing classes.  
2- returning empty answer or very short  
3- extracting attributes such as date, time, and string names that are related to data properties  
common mistakes in the properties:  
1- returning an empty answer or a very short  
2- do not forget to add relations for the pivot class that was created, all of the necessary classes in the CQ should be connected to the pivot class
3- when the pivot class is created, all of the related classes should point to it (direction of relation is from the classes (domains) 'to'  pivot class (range))

## Waterfall
### Header, Prefixes, and Definitions (common in all stages)
**Header**: 
Your task is to contribute in creation of a well-structured ontology information that appeared in the given story, requirements, and restrictions (if there are any).

**Prefixes** : 
```
these are the prefixes:
@prefix : <http://www.example.org/test#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```
**Definitions**:

here are some definitions of ontology components to help you understand the problem in a better way and write better hints:
Classes are the keywords/classes that are going to be node types in the knowledge graph ontology. try to extract all classes, in addition, classes are also can be defined for reification. We use Turtle Syntax for representation. Hierarchies are rdfs:subClassOf in the turtle syntax. They can be used to classify similar classes in one superclass. To do this you can find similar nodes and create/use a class as their parent class, for example, adding the node "Cl_employee" is a good middleware and superclass for "Cl_Professors" and "Cl_Administrator" if the story is about modeling ontology of a university. Mostly the lengthier the hierarchy the better. One way can be categorizing classes into several classes and creating superclasses for them. Important: Class names have Cl_ as the prefix for example Cl_Professors. Also keep in mind you can add Equivalent To, General class axioms, Disjoint with, and Disjoint Union of, for each class.
In your ontology modeling, for each competency question, when faced with complex scenarios that involve more than two entities or a combination of entities and datatypes, apply reification. Specifically, create a pivot class to act as an intermediary for these entities, ensuring the nuanced relationships are accurately captured. For instance, when representing "a user accessed a resource at a given time", establish a pivot class like Cl_UserResourceUsage, linked from the user, resource, and the specific time of access to Cl_UserResourceInteraction, rather than directly connecting the user to both the resource and time.
Then you need to create properties (owl:Property). In this step, you use classes from the previous stage and create object and data properties to connect them and establish the ontology. Always output a turtle syntax, if you need more classes to model a competency question between more than 2 concepts, feel free to add more pivot (reification) classes here. try to find as much relation as possible by reading competency questions, restrictions, and stories. At this stage, you can create both data and object properties. Data properties are between classes or hierarchy classes and data types such as xsd:string, xsd:integer, xsd:decimal, xsd:dateTime, xsd:date, xsd:time, xsd:boolean, xsd:byte, xsd:double, xsd:float and etc. For example, in the university domain, we have: employee_id a owl:Property ; rdfs:domain :cl_teacher ; rdfs:range xsd:integer. Object properties are between classes. try to find as much relation as possible by reading competency questions and the story. Feel free to use rdfs:subPropertyOf for creating hierarchies for relations. For modeling properties (object or data properties) if it is necessary, use these relations characteristics: Functional, Inverse functional, Transitive, Symmetric, Asymmetric, Reflexive, and Irreflexive. Also, you are flexible in domain and range so you can use Cl_class1 or Cl_class2 in domain and range or disjoint with, the inverse of between relations.


### Stage 1:
#### Helper

Your task is to assist students by providing hints for ontology development without giving them code. Your task is to only append some information (in a very short text) to the story. so read the story, competency questions, and restrictions, then write in short (translate) what the object properties, data properties, and reification nodes are needed. do not do any coding, just write CQ1: (competency question #1: ) object properties: rel1, rel2 ...; data properties: p1, p2, p3; classes: ...; reification nodes: Cl_n1, Cl_n2,... CQ2: ...

<code style="color : blue">{definisions}</code>

Important: do not solve the ontology (it is cheating, we want hints for students) just put the information mentioned above. Don't put any code, just write the object properties: el1, rel2 ...;
instruction for student: '
CQ1: (competency question #1: ) object properties: rel1, rel2 ...; data properties: p1, p2, p3; classes: ...; reification nodes: Cl_n1, Cl_n2,... CQ2: ...

<code style="color : blue">{prefixes}</code>

Important: your output should be only owl turtle. Don't write any explanation before the code block or after. Also, the code must have 0 comments.
### Story
Ontology story comes from users' input 

#### Footer (pitfalls)
Empty at this stage

### Stage 2:
#### Helper
The way to approach this is you first create classes. Classes are the keywords/classes that will be node types in the knowledge graph ontology (see the definitions bellow). Try to extract all classes. We use Turtle Syntax for representation. Important: Class names have Cl_ as a prefix for example Cl_Professors.  Also keep in mind you can add Equivalent To, General class axioms, Disjoint with, and Disjoint Union of, for each class. In this step, don't extract any properties (object property or data property.), only classes. extracting hierarchies and properties do not belong to this stage (so don't use subClassOf in this stage).

<code style="color :  #3399ff">{definisions}</code>
### Story
<span style="color: blue;">Previous LLM output (from stage 1) </span> + Ontology story comes from users' input (with CQs) 

#### Footer (pitfalls)
Besides here are some possible mistakes that you might do:

1- forgetting to add prefixes at the beginning of the code.

2- forgetting to add pivot classes (reifications).

common mistakes in the class extraction:

1- not extracting all classes and missing many of them. classes can be found in story, competency questions and restrictions.

2- returning empty answer

3- providing comments or explanations

4- extracting classes like 'Date' is wrong since they are data properties.

5- not adding prefixes at the start of the turtle or not using them or creating new one
