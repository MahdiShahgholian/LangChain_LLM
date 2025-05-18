from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_cohere import ChatCohere
import pandas as pd

class FewShotChainBuilder:
    def __init__(self, examples: dict, system_instruction: str, cohere_api_key: str, model_name: str, temperature: float):
        self.examples = examples
        self.system_instruction = system_instruction
        self.api_key = cohere_api_key
        self.model_name = model_name
        self.temperature = temperature
        self.chain = None

    def build_chain(self):
        system_message = self.system_instruction

        example_prompt = ChatPromptTemplate.from_messages([
            ("human", "{question}"),
            ("ai", "{answer}")
        ])

        few_shot_prompt = FewShotChatMessagePromptTemplate(
            example_prompt=example_prompt,
            examples=self.examples
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_message),
            few_shot_prompt,
            ("human", "{question}")
        ])

        llm = ChatCohere(
            cohere_api_key= self.api_key,
            model= self.model_name,
            temperature= self.temperature
        )

        self.chain = prompt | llm
        return self.chain
