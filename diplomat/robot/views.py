import pathlib
import os

from rest_framework.response import Response
from rest_framework.decorators import api_view
from dotenv import load_dotenv
import openai
from openai import Completion

load_dotenv(pathlib.Path(__file__).parents[2].joinpath('.env'))


@api_view(['GET'])
def prompt(request):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    completion = Completion.create(
        model=os.getenv('OPENAI_MODEL'),
        prompt='Hello',
        temperature=0.05,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return Response(completion)
