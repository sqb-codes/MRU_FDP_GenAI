from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import SequentialChain
from secret_key import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = OpenAI()
def gen_data(exercise_type, component):


    prompt_template_name = PromptTemplate(
        input_variables = ["exercise_type", "component"],
        template = "I have to start {exercise_type} and suggest {component}"
    )

    component_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="exercise")

    prompt_template_items = PromptTemplate(
        input_variables=["exercise"],
        template = "Suggest some exercises for {exercise}"
    )

    gym_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="exercise_items")

    chain = SequentialChain(
        chains=[component_chain, gym_items_chain],
        input_variables=["exercise_type", "component"],
        output_variables=["exercise", "exercise_items"]
    )
    response = chain({"exercise_type":exercise_type, "component" : component})
    return response

