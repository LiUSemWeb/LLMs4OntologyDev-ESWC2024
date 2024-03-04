# Table of Contents

1. [Experimental Results](#introduction)
2. [Initial Experiment](#Initial)
3. [Main Experiment](#Main)
## 1- introduction
For our experiments, we assess the quality of the LLM output through the methods described in the method section. Additionally, we compare these results against the same assessment made of the ontologies produced by students, also described above, to use these as a baseline. 
## 2- Initial Experiment
### Phase One
The initial phase of an experiment was conducted to evaluate the performance of various Language Learning Models (LLMs) when paired with different prompting techniques. The results indicate that the smaller models (< 20B parameters) such as **LlaMA7B, LlaMA13B, WizardLM, Falcon7B, Alpaca-LoRA, and CodeLlama-13b** lack the ability to provide accurate suggestions. These models consistently failed to produce relevant output for the small tasks in this phase. Larger models such as **LlaMA2-70B and Bard** also exhibited an **inability to generate outputs in the Turtle syntax**.

On the other hand, GPT-3.5 and GPT-4 emerged as the only models capable of successfully completing the tasks and generating outputs that aligned with the expected prompt. An analysis of the prompting techniques revealed that the Sub-task Decomposed Prompting approach, specifically the waterfall method, failed to produce satisfactory results with GPT-3.5 and GPT-4. The CQbyCQ technique was too complex for GPT-3.5, leading to failures across all short stories.

In summary, the results from phase one of the preliminary experiment underscore the significant variation in performance across different LLMs and prompting techniques. Only GPT-3.5 and GPT-4 provided sufficiently high-quality results to proceed to the next phase. The findings also emphasize the need for careful consideration and refinement of prompting techniques to ensure compatibility and effectiveness with the chosen LLMs.

This table shows information about LLMs' performance on small stories. Models are combined with prompting techniques and tested to see can they pass or fail on the stories.

| Model  | Prompting Techniques              | Vegetarian story | Lena story | Large Festival |
|-------|-----------------|:-----------------:|:------------:|:--------------:|
| GPT4   | Zero-Shot           | :x: | :heavy_check_mark: | :heavy_check_mark: |
| GPT4   | Waterfall           | :x: | :x: | :heavy_check_mark: |
| GPT4   | CQ by CQ            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| GPT4   | Chain of thoughts   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| GPT4   | Tree of thoughts    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| GPT4   | Graph of thoughts   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| GPT3.5 | Zero-Shot           | :x: | :heavy_check_mark: | :heavy_check_mark: |
| GPT3.5 | Waterfall           | :x: | :x: | :heavy_check_mark: |
| GPT3.5 | CQ by CQ            | :x: | :x: | :x: |
| GPT3.5 | Chain of thoughts   | :x: | :heavy_check_mark: | :heavy_check_mark: |
| GPT3.5 | Tree of thoughts    | :x: | :heavy_check_mark: | :heavy_check_mark: |
| GPT3.5 | Graph of thoughts   | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Bard   |  all prompts        | :x: | :x: | :x: |  
| Llama-70B | all prompts      | :x: | :x: | :x: |  

According to the results from this table, we decided to proceed with the rest of the experiment with GPT-3.5 and GPT-4. The reason is no other model could produce a code that could model the stories.
 
 ### Phase Two
The retained models' outputs were then evaluated based on the established binary criteria. In aspects such as the implementation of **'owl:EquivalentClass'**, **restrictions**, the **presence of reification classes**, and the **correctness of the Turtle syntax**, GPT-3.5 exhibited considerable shortcomings in comparison to GPT-4. For example, across all prompting techniques, GPT-3.5 missed almost half of the** necessary reifications** while GPT-4 caught and correctly modeled 95% of them. It should be noted that during this phase, GPT-4 outperformed GPT-3.5 by approximately 15% on average for all criteria and prompting techniques. The only comparable performance between GPT-3.5 and GPT-4 was on CoT and Waterfall approaches, with almost the same performance. %These elements are crucial for creating ontologies that accurately reflect the complexities of the given requirements and adhere to ontology modeling best practices.
Conversely, in criteria involving the expression of domain and range for properties, the creation of hierarchical structures using 'rdfs:subClassOf', semantic coherence in class hierarchies, definition of data properties, and the provision of instances, GPT-4 and GPT-3.5 showed similar levels of competence. This suggests that while **GPT-3.5** is capable in certain aspects of ontology modeling, **it falls short in more complex** and nuanced tasks.

Considering the overall performance in phase two, **it was decided to proceed exclusively with GPT-4 in the subsequent phases of our research**. Again, it is worth noting that the purpose of the study is to explore the feasibility of LLMs to assist in OWL modeling, not to compare and quantify the capabilities of different models. %This decision was informed by the comparative analysis, which clearly indicated GPT-4’s superior capability in handling the complexities of ontology generation. The advanced performance of GPT-4 in meeting the set criteria reinforces its suitability for more sophisticated applications in ontology engineering and related fields.


![image](https://github.com/saeedizade/LLMsOntology/blob/main/ExperimentResult/images/excel%2C%20phase2.jpg)

This table shows binary criteria (pass or fail) on some tasks (columns) for each pair of LLMs and Prompting Techniques). We took an average of each row and presented them as a final score. At the end, we proceed the experiment with GPT-4 and only removed the Waterfall and Tree.

## 3- Main Experiment
Our experiment aimed to evaluate GPT-4's performance with various prompting techniques. We ran the model three times for each technique, and each one of the three stories, to obtain an average output, ensuring that our results were consistent and not influenced by random variations. Then, we compared these averaged outputs from our framework against the average of students' submissions. Also, each LLM-prompting technique was run three times to reduce the randomness of LLMs.

This comparison is detailed in Figure \ref{fig:image1}, where each row represents a different ontology story. The figure is split into two sections: on the left, we compare the direct performance of students' submissions with our framework's outputs. This comparison focuses on addressing the competency questions. The right-hand side of first figure provides a modified view, ignoring minor errors (as defined previously). This approach allows us to evaluate how overlooking minor mistakes, which may be easy for even a novice ontology engineer to spot and fix, influences the overall effectiveness of the LLMs.

Through this dual analysis, we offer a comprehensive view of the capabilities of LLMs in ontology modeling, comparing them with human-generated models both in direct performance and under a more lenient evaluation of minor issues.


![](https://github.com/saeedizade/LLMsOntology/blob/main/ExperimentResult/images/all.jpg )
Table comparing GPT-4 with different prompting techniques against students' first and last submissions. The figure shows the standard deviation and the average percentage of competency questions modelled by the produced ontology over three runs, with and without considering minor issues.


A notable observation from Figure 1 is that the CoT and CoT-SC methodologies generally underperformed compared to other models and the manual baseline. This trend was consistent across almost all scenarios. It suggests that while these methods have potential, there are more effective methods of prompting for ontology development.

An interesting finding is that the students' last submissions typically yielded the best output. This outcome indicates that students improve significantly after multiple resubmissions and feedback. However, it is noteworthy that the GoT and CQbyCQ prompting techniques were closer in performance to the students' last submissions than their first submissions. This implies that these techniques are particularly effective, aligning closely with the refined understanding students develop over time.

When examining the right-hand side of Figure 1 which disregards minor issues, there is a significant increase in the quality of the LLM-generated OWL files. This improvement suggests that many errors in the LLM's outputs are minor. The fact that overlooking these minor issues leads to a substantial boost in performance highlights the potential of LLMs in ontology generation. It underscores that with minimal human intervention for error correction, regarding minor issues in the suggested model, LLMs can be highly effective for assisting the modelling process.


To gain a deeper understanding of the types of questions that posed challenges for both GPT-4 and students in their modeling efforts, we categorized the CQs into four distinct types:

* Simple Datatype Property: This category includes questions that can be addressed by adding one or more datatype properties. For example, questions related to the date of an event fall under this category.
* Simple Object Property: These questions involve establishing a connection between two classes by creating an object property. An example would be determining the author of a book.
* Reification: This category is reserved for questions that require the creation of an abstract class to connect other classes, often in complex situations. For instance, identifying the role of a person in an event at a specific time is a question of reifying the 'role-playing situation'.
* Restrictions: Questions in this category involve imposing restrictions on classes or properties. An example of such a question would be: At least one article is always presented at each seminar.

![](https://github.com/saeedizade/LLMsOntology/blob/main/ExperimentResult/images/F3.png)
![](https://github.com/saeedizade/LLMsOntology/blob/main/ExperimentResult/images/M3.png)
![](https://github.com/saeedizade/LLMsOntology/blob/main/ExperimentResult/images/H3.png)
 
In Figure 2-4 of this section, we delve into the performance of GPT-4 using various prompting techniques, as well as student submissions, categorized by the four types of CQs presented above. In these bar charts, where minor issues are again disregarded, each row corresponds to a different story. %The key findings from this analysis are as follows:
Analysis of student submissions and GPT-4 outputs over the range of prompting techniques across the three stories over four different categories of CQs. The vertical axis represents the percentage of CQs successfully modelled when ignoring minor issues, showcasing the effectiveness of each approach in answering the posed questions.


The performance of the CQbyCQ technique stands out in its ability to model simple object properties, datatype properties, and apply reification. It consistently performs at a level that is either better or comparable to other techniques. However, its effectiveness in creating restrictions is less reliable, indicating an area of concern.
In the tasks of creating reification classes, and establishing restrictions, both CoT and CoT-SC displayed the least stability. Their performance varied significantly across the three stories, indicating poor robustness. On the other hand, the GoT technique excelled in creating restrictions. This indicates its strong capability to capture and address the nuanced requirements present in ontology stories, making it a more reliable choice for dealing with complex modelling scenarios.
When comparing the first and last submissions of students across different categories, in part two of the experiment, there was an average improvement of approximately 20\%. This improvement showcases the learning and adaptation process students undergo, enhancing their ability to address competency questions.


