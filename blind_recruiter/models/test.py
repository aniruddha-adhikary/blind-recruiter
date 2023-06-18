from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain.prompts import ChatPromptTemplate, PromptTemplate, SystemMessagePromptTemplate
from tqdm import tqdm
import logging

resume = dict()
models = (Experiences, EducationHistory, ProfileLinks, Skills)
progress_bar = tqdm(models)

for pydantic_model in progress_bar:
    progress_bar.set_description(
        "Processing {}".format(pydantic_model.__name__)
    )
    
    resume_output_parser = PydanticOutputParser(pydantic_object=pydantic_model)

    prompt = PromptTemplate(
        template="I am providing a JSON Schema followed by a resume in plain text. Format the plain text into the JSON format.\n{format_instructions}\n{resume}\n",
        input_variables=["resume"],
        partial_variables={
            "format_instructions": resume_output_parser.get_format_instructions()},
    )

    chat_prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate(
            prompt=prompt.format_prompt(resume=resume_content))
    ])

    output = chat_llm(chat_prompt.to_string())

    progress_bar.set_description(
        "Fixing Output {}".format(pydantic_model.__name__))
    output_fixing_parser = OutputFixingParser.from_llm(
        parser=resume_output_parser, llm=chat_llm)

    resume.update(output_fixing_parser.parse(output).dict())
