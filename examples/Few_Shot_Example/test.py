from llm import DataLoader
from llm import FewShotChainBuilder
from llm import FewShotRunner
import pandas as pd
import api
import prompt


# examples and system prompt
examples = prompt.examples
system_message = prompt.system_message

# load data
knowledge = DataLoader("data/gods.json").load()
questions = DataLoader("data/questions.csv").load()

# build chain
builder = FewShotChainBuilder(
    examples=examples,
    system_instruction=system_message,
    cohere_api_key= api.COHERE_API_KEY,
    model_name = "command-a-03-2025",
    temperature=0.2
)
chain = builder.build_chain()

# run with data and export csv answers
runner = FewShotRunner(chain = chain, knowledge_data= knowledge, questions_df = pd.DataFrame(questions.iloc[:5, 0]))
runner.run_questions_csv()
runner.save_to_csv("data/final_answers.csv")