from langflow.load import run_flow_from_json

TWEAKS = {
  "TextInput-WKjLi": {
    "input_value": "question"
  },
  "Prompt-IRPSh": {},
  "OpenAIModel-t2Fl7": {},
  "ConditionalRouter-YFTSx": {},
  "ToolCallingAgent-a4ApN": {},
  "CalculatorTool-M6ar5": {},
  "OpenAIModel-MVb9I": {},
  "TextOutput-4GiFV": {},
  "Prompt-1caeU": {},
  "TextInput-0RtcB": {
    "input_value": "profile"
  },
  "AstraDB-Lvl0l": {},
  "AstraVectorize-iMbzU": {},
  "ParseData-MnAAg": {},
  "Prompt-X6uIM": {},
  "OpenAIModel-leFdd": {},
  "TextOutput-nb95v": {}
}

result = run_flow_from_json(flow="AskAI.json",
                            input_value="message",
                            fallback_to_env_vars=False, # False by default
                            tweaks=TWEAKS)