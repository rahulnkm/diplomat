import os
import pathlib

from dotenv import load_dotenv
import openai

from . import snapshot_service

load_dotenv(pathlib.Path(__file__).parents[3].joinpath(".env"))

openai.api_key = os.getenv("OPENAI_API_KEY")


def create_chat_completion_from_proposal(proposal):
    dao = snapshot_service.query_snapshot_space(proposal.get("space").get("id"))

    personal_statement = None
    dao_statement = (
        f"The point of the organization is {dao.get('spaces')[0].get('about')}"
        if dao.get("spaces")[0].get("about")
        else ""
    )
    proposal_statement = f"{proposal.get('title')}\n\n{proposal.get('body')}"

    messages = [
        {
            "role": "system",
            "content": (
                "Personal statement: <Name> is <Three sentences about their"
                " interests, values, and identity> \n\nYou are their personal"
                " representative. You are tasked with passing bills that are"
                f" aligned with their interests.\n\n{dao_statement}\n\nThere is"
                f" a proposal:\n{proposal_statement}\n\n"
            ),
        },
        {
            "role": "user",
            "content": (
                "Respond True if you would pass the law, False if you would"
                " reject the law and Not enough info if there is not enough"
                " info. Include your reasoning. Ask questions if there is not"
                " enough info to clarify a Yes/No answer."
            ),
        },
    ]

    return messages, openai.ChatCompletion.create(
        model=os.getenv("OPENAI_MODEL"), messages=messages
    )
