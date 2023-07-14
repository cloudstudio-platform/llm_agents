import openai
import os

from pydantic import BaseModel
from typing import List


class ChatLLM(BaseModel):
    model: str = 'gpt-3.5-turbo'
    temperature: float = 0.0
    openai.api_key = os.environ["OPENAI_API_KEY"]  # Credentials setup
    openai.api_base = 'https://service-4y8atuq4-1259057771.sg.apigw.tencentcs.com/v1'

    def generate(self, prompt: str, stop: List[str] = None):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            stop=stop
        )
        return response.choices[0].message.content

if __name__ == '__main__':
    llm = ChatLLM()
    result = llm.generate(prompt='Who is the president of the USA?')
    print(result)
