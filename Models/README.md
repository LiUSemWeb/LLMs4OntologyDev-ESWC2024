# Large Language Models
LLMs are sophisticated computational systems in natural language processing. Utilizing deep learning, particularly neural network architectures like transformers, LLMs are trained on extensive text datasets, enabling them to understand, interpret, and generate human-like text. These models are adept at various language tasks such as translation, summarization, and content creation.

In our research methodology, it was crucial to ensure a comprehensive examination of various LLMs to achieve generalizable results and avoid model-specific biases. We, therefore, use a representative selection of models spanning both proprietary and open-source versions. We engaged with the following models: 
- **[GPT-3.5](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)**
- **[GPT-4](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)**
- **[Bard - obsoleted](Bard.google.com)**, replaced by Gemini

And  from the closed-source spectrum. Regarding open-source models, our experiments encompass 
- **[Lama-7B](https://ai.meta.com/llama/)** - [implementation](https://colab.research.google.com/github/camenduru/text-generation-webui-colab/blob/main/llama-2-7b-chat.ipynb)
- **[Lama-13B](https://ai.meta.com/llama/)** - [implementation](https://colab.research.google.com/github/camenduru/text-generation-webui-colab/blob/main/llama-2-13b-chat.ipynb)
- **[Llama2-70B](https://ai.meta.com/llama/)** - [implementation](https://replicate.com/meta/llama-2-70b-chat)
- **[Alpaca](https://huggingface.co/chavinlo/gpt4-x-alpaca)**- [implementation](https://colab.research.google.com/github/camenduru/text-generation-webui-colab/blob/main/gpt4-x-alpaca-13b-native-4bit-128g.ipynb)
- **[Falcon-7B-Instruct](https://falconllm.tii.ae/)** - [implementation](https://colab.research.google.com/github/camenduru/text-generation-webui-colab/blob/main/falcon-7b-instruct-GPTQ-4bit.ipynb)
- **[WizardLM](https://github.com/nlpxucan/WizardLM)** [implementation](https://colab.research.google.com/github/camenduru/text-generation-webui-colab/blob/main/wizard-lm-13b-1.1-GPTQ-4bit-128g.ipynb)
- **[Alpaca-LoRA](https://huggingface.co/chavinlo/gpt4-x-alpaca)** [implementation](https://colab.research.google.com/github/camenduru/text-generation-webui-colab/blob/main/gpt4-x-alpaca-13b-native-4bit-128g.ipynb).

By using this broad selection, we aimed to achieve a holistic understanding and validation of our research objectives. However, it is important to note that the purpose of our study is not to compare the effectiveness of these models but merely to determine if any of them can produce sufficiently high-quality OWL suggestions and study the characteristics of such suggestions. Hence, this is why we first performed initial experiments on a broad range of models but then quickly settled for a smaller set in subsequent experiments.

An important component when using LLMs is the memory. Since an LLM can only handle a certain size of the current context, i.e., what it takes into account when addressing a new prompt, therefore an external memory can be used as a module that stores information, such as previously generated code, plans and provides a history of past communications with an LLM for future prompts if the prompting techniques need them. In our experiments, a memory is used for all prompting methods except zero-shop. 


References:

- [Touvron et al., 2023](#touvron2023llama)
- [Author, Year](#alpaca)
- [Author, Year](#falcon40b)
- [Author, Year](#penedo2023refinedweb)
- [Author, Year](#xu2023wizardlm)


