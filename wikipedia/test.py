import os
import openai
import pandas as pd
import matplotlib.pyplot as plt

openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.FineTune.retrieve(id="ft-B9gjRDIsPaJS00Yd63a2eaPl"))

test = pd.read_json('categories_prepared_valid.jsonl', lines=True)
print(test.head(1))


results = pd.read_csv('result.csv')

print(results[results['classification/accuracy'].notnull()].tail(1))
results[results['classification/accuracy'].notnull()
        ]['classification/accuracy'].plot()

plt.show()

ft_model = 'ada:ft-personal-2023-10-12-19-40-01'

sample_software_text = """The Process of creating software has been difficult because our team has been struggling, the tools that we have been using to build this product has become deprecated and we the person in charge has been fired"""
res = openai.Completion.create(model=ft_model, prompt=sample_software_text +
                               '\n\n###\n\n', max_tokens=2, temperature=0, logprobs=2)

print(res['choices'][0]['text'])

sample_network_text = """The http protocol that was used to connect the business organisation hasn't met the needs becasue it wasn't version http 2.0 """
res = openai.Completion.create(model=ft_model, prompt=sample_network_text +
                               '\n\n###\n\n', max_tokens=2, temperature=0, logprobs=2)


print(res['choices'][0]['text'])
