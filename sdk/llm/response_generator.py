#
# Author: Rohtash Lakra
#
import json

import requests


class LLMResponseGenerator:
    """
    Generates natural language responses using the Gemini API.
    """

    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url

    async def generate_response(self, prompt, structured_output_schema=None):
        """
        Generates a response using the Gemini API.
        Optionally, requests a structured JSON output from the LLM.
        """
        chat_history = []
        chat_history.append({"role": "user", "parts": [{"text": prompt}]})

        payload = {"contents": chat_history}
        if structured_output_schema:
            payload["generationConfig"] = {
                "responseMimeType": "application/json",
                "responseSchema": structured_output_schema
            }

        headers = {'Content-Type': 'application/json'}

        try:
            # Using a synchronous request for simplicity in this example.
            # In a real async app, use an aiohttp or httpx.
            response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            result = response.json()

            if result.get("candidates") and result["candidates"][0].get("content") and \
                    result["candidates"][0]["content"].get("parts") and \
                    result["candidates"][0]["content"]["parts"][0].get("text"):
                if structured_output_schema:
                    try:
                        return json.loads(result["candidates"][0]["content"]["parts"][0]["text"])
                    except json.JSONDecodeError:
                        print("Warning: LLM did not return valid JSON for structured output.")
                        return {"error": "Invalid JSON response from LLM"}
                else:
                    return result["candidates"][0]["content"]["parts"][0]["text"]
            else:
                print(f"LLM response structure unexpected: {result}")
                return "I'm sorry, I couldn't generate a response at this time."
        except requests.exceptions.RequestException as e:
            print(f"Error calling Gemini API: {e}")
            return "I'm experiencing technical difficulties. Please try again later."
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "An unexpected error occurred."
