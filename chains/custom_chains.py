from langchain.prompts import PromptTemplate
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import LLMChain
import os
from output_parsers import summary_parser, ice_breaker_parser, topics_of_interest_parser




def get_summary_chain() -> LLMChain:
    
    llm=AzureChatOpenAI(
            api_version= os.environ.get("api_version"),
            azure_deployment= os.environ.get("azure_deployment"),
            temperature=0,
            azure_endpoint= os.environ.get("azure_endpoint"),
            api_key= os.environ.get("AZURE_OPENAI_API_KEY") 
        )

    summary_template = """
         given the information about a person from linkedin {information} I want you to create:
         1. a short summary
         2. two interesting facts about them
         \n{format_instructions}
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)


def get_interests_chain() -> LLMChain:
    
    llm=AzureChatOpenAI(
            api_version= os.environ.get("api_version"),
            azure_deployment= os.environ.get("azure_deployment"),
            temperature=0,
            azure_endpoint= os.environ.get("azure_endpoint"),
            api_key= os.environ.get("AZURE_OPENAI_API_KEY") 
        )
    interesting_facts_template = """
         given the information about a person from linkedin {information} I want you to create:
         3 topics that might interest them
        \n{format_instructions}
     """

    interesting_facts_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=interesting_facts_template,
        partial_variables={
            "format_instructions": topics_of_interest_parser.get_format_instructions()
        },
    )

    return LLMChain(llm=llm, prompt=interesting_facts_prompt_template)


def get_ice_breaker_chain() -> LLMChain:
    
    llm_creative=AzureChatOpenAI(
            api_version= os.environ.get("api_version"),
            azure_deployment= os.environ.get("azure_deployment"),
            temperature=0,
            azure_endpoint= os.environ.get("azure_endpoint"),
            api_key= os.environ.get("AZURE_OPENAI_API_KEY") 
        )
    ice_breaker_template = """
         given the information about a person from linkedin {information} I want you to create:
         2 creative Ice breakers with them that are derived from their activity on Linkedin preferably on
        \n{format_instructions}
     """

    ice_breaker_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=ice_breaker_template,
        partial_variables={
            "format_instructions": ice_breaker_parser.get_format_instructions()
        },
    )

    return LLMChain(llm=llm_creative, prompt=ice_breaker_prompt_template)
