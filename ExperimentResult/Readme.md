# Table of Contents

1. [Experimental Results](#introduction)
2. [Initial Experiment](#Initial)
3. [Main Experiment](#Main)
## 1- introduction
For our experiments, we assess the quality of the LLM output through the methods described in the method section. Additionally, we compare these results against the same assessment made of the ontologies produced by students, also described above, to use these as a baseline. 
## 2- Initial Experiment
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

According to the results we got from this table, we decided to proceed the rest of the experiment with GPT-3.5 and GPT-4. The reason is no other model could produce a code that could model the stories.
 
## 3- Main Experiment
