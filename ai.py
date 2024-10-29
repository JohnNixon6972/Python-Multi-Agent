from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import requests
from typing import Optional
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "3c8795f4-3632-49b1-b7c0-302e1629c5cf"
APPLICATION_TOKEN = os.getenv("LANGFLOW_TOKEN")



def ask_ai(profile,question):
  TWEAKS = {
    "TextInput-WKjLi": {
      "input_value": question
    },
    "TextInput-0RtcB": {
      "input_value": profile
    },
  }

  result = run_flow_from_json(flow="AskAI.json",
                              input_value="message",
                              fallback_to_env_vars=True,
                              tweaks=TWEAKS)
  return result[0].outputs[0].results["text"].data["text"]




def get_macros(profile,goals):

  TWEAKS = {
    "TextInput-Md4Dc": {
      "input_value": goals
    },
    "TextInput-kbKmV": {
      "input_value": profile
    },
  }

  return run_flow("",tweaks=TWEAKS,application_token=APPLICATION_TOKEN)

def run_flow(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/macros"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)

    return response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]


result = get_macros("name:John Age:24 Weight:75kg, 175cms","muscle gain")
print(result)