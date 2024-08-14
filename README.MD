Supplementary materials for the paper:
## Navigating Ontology Development with Large Language Models @ ESWC2024 [See the PDF](https://2024.eswc-conferences.org/wp-content/uploads/2024/04/146640137.pdf)
The <b>video presentation</b> of the work is available [here](https://videolectures.net/eswc2024_saeedizade_ontology_development/), [powerpoint file](./ESWC.pdf]

This repository contains documentation and implementations related to the paper "Navigating Ontology Development with Large Language Models." The paper explores various [prompting techniques](Prompts) and [models](LLM_Models) for ontology development, focusing on creating a tool that helps ontologists by providing modelling suggestions.

We compared students' submissions of the ontology stories with LLMs to have a comparison baseline [click here to see the results](ExperimentResult/Readme.md). There were 10 groups of students (~2 students per group) and three submissions per story to pass the task (stories were in a master course). LLMs outputs for each prompting technique are stored in "LLM_OWL_outputs" folder.
## Contents
### Prompts
  - [Zero-Shot Prompting](Prompts/Zeroshot.md)
  - [Sub-task Decomposed Prompting: Waterfall approach](Prompts/waterfall.md)
  - [Sub-task Decomposed Prompting: Competency Question by Competency Question (CQbyCQ)](Prompts/CQbyCQ.md)
  - [Chain of Thoughts](Prompts/CoT.md)
  - [Self Consistency with Chain of Thoughts (CoT-SC)](Prompts/CoTSC.md)
  - [Graph of Thoughts (GoT)](Prompts/GoT.md)<hr>
### [Models](Models/README.md#large-language-models)
Here is the list of models used in the experiments. [Click here to see more details](LLM_Models/README.md#large-language-models)

  - Open-Source Models
    - Lama-7B
    - Lama-13B
    - Llama2-70B
    - Alpaca
    - Falcon-7B-Instruct
    - WizardLM 
    - Alpaca-LoRA
  - Close-Source Models
    - Bard
    - GPT3-5
    - GPT-4 <hr>
### [Results]()
  #### Initial Experiment 
  - [Initial Experiment: First Phase - Simple binary criteria to exclude models](ExperimentResult/Readme.md)
  - [Initial Experiment: Second Phase - Excluding more models and Prompting techniques](ExperimentResult/Readme.md)
  #### Main Experiment
  - [GPT-4 VS Student in groups](ExperimentResult/Readme.md)
  - [GPT-4 VS Students in groups: Ignoring minor errors](ExperimentResult/Readme.md) <hr>

### [Stories](Stories/README.MD#here-are-ontology-stories-in-the-experiments)
Here are the list of stories that used in the experiments. [Click here to see stories and their CQs](Stories/README.MD#here-are-ontology-stories-in-the-experiments)
#### Short Narratives (Initial Experiment)
  - Short Story 1: Vegetarians 
  - Short Story 2: Lena
  - Short Story 3: Big Festival 
#### Ontology Narratives (Main experiment)
  - Story 1: Theatre Festival
  - Story 2: Music Production 
  - Story 3: Hospital Story

### Students submissions
We included the results of students' course submissions in the story section. However, due to university regulations, the OWL files of the students' submissions will not be available.
But more information about stats and their performance [ can be found here](Stories/README.MD#students-submission-stats) 
