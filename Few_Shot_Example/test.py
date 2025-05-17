from utils import DataLoader
from llmChainBuild import FewShotChainBuilder
from runner import Runner
import pandas as pd


# examples and system prompt
examples = [
    {"question": "خدای جنگ کیست؟", "answer": "آرس"},
    {"question": "آتنا معمولاً چه چیزهایی دارد؟", "answer": "سپر و شمشیر"},
]
system_msg = "به کمک داده‌های زیر پاسخ بده: {knowledge}. پاسخ فقط در ۵ کلمه باشد."

# load data
knowledge = DataLoader("gods.json").load()
questions = DataLoader("questions.csv").load()

# build chain
builder = FewShotChainBuilder(
    examples=examples,
    system_instruction=system_msg,
    cohere_api_key= "qVxwbuC88DwFaI3ljCqhvGbQgFtSL6vdNcn1055H",
    model_name = "command-a-03-2025",
    temperature=0.2
)
chain = builder.build_chain()

# run with data and export csv answers
runner = Runner(chain = chain, knowledge_data= knowledge, questions_df = pd.DataFrame(questions.iloc[:5, 0]))
runner.run_questions_csv()
runner.save_to_csv("final_answers.csv")