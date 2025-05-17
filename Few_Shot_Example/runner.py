import time
from llmChainBuild import FewShotChainBuilder
import pandas as pd

class Runner:
    def __init__(self, chain: FewShotChainBuilder, knowledge_data, questions_df : pd.DataFrame):
        self.chain = chain
        self.knowledge_data = knowledge_data
        self.questions_df = questions_df
        self.answers = []

    def run_questions_csv(self, batch_size=9, delay_seconds=60):
        self.answers = []
        count = 0

        for idx, row in self.questions_df.iterrows():
            question = row["question"]

            response = self.chain.invoke({
                "question": question,
                "knowledge": self.knowledge_data
            })

            answer = response.content
            self.answers.append(answer)

            print(f"[{idx}] {question} → {answer}")
            count += 1

            if count >= batch_size:
                time.sleep(delay_seconds)
                count = 0

        self.questions_df["answer"] = self.answers

    def save_to_csv(self, output_path="answers.csv"):
        self.questions_df.to_csv(output_path, index=False)
        print(f"Results saved to: {output_path}")