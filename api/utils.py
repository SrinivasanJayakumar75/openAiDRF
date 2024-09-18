import openai
from django.conf import settings

openai.api_key = settings.APIKEY

def send_code_to_api(code):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "context": "You are an experienced developer."},
            {"role": "user", "context": f"tell me what language is that code written?{code}"},
        ],)

        return  res["choices"][0]["messages"]["context"]
    except openai.error.APIError as e:
        raise ValueError(f"OpenAI API returned an API Error: {e}")