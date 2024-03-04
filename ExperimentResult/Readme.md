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


![](https://github.com/saeedizade/LLMsOntology/blob/main/ExperimentResult/images/all.jpg "Table comparing GPT-4 with different prompting techniques against students' first and last submissions. The figure shows the standard deviation and the average percentage of competency questions modelled by the produced ontology over three runs, with and without considering minor issues.")




