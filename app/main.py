#
# Author: Rohtash Lakra
#
import os

import asyncio

from sdk.main_sdk import AutomobileChatbotSDK

# --- Configuration ---
# Replace with your actual Gemini API Key.
# In a real application, this should be loaded securely (e.g., from environment variables).
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)  # Your Gemini API Key here
GEMINI_API_BASE_URL = os.getenv("GEMINI_API_BASE_URL",
                                "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash")  # Gemini API Base URL here
GEMINI_API_URL = f"{GEMINI_API_BASE_URL}:generateContent?key={GEMINI_API_KEY}"


async def main():
    # initialize the chatbot
    chatbot_sdk = AutomobileChatbotSDK(gemini_api_key=GEMINI_API_KEY, gemini_api_url=GEMINI_API_URL)
    print("Automobile Chatbot SDK Demo. Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break

        response_data = await chatbot_sdk.process_user_input(user_input)
        print(f"Bot: {response_data['response']}")
        if response_data['action']:
            print(f"Action to perform (for integrating app): {response_data['action']}")

    # Example of getting structured data from LLM (e.g., for complex queries)
    print("\n--- Structured LLM Query Example ---")
    structured_prompt = "From the following text, extract the car's make, model, and year: 'I have a 2023 Honda Civic, it's a great car.'"
    car_info_schema = {
        "type": "OBJECT",
        "properties": {
            "make": {"type": "STRING"},
            "model": {"type": "STRING"},
            "year": {"type": "NUMBER"}
        },
        "required": ["make", "model", "year"]
    }
    structured_result = await chatbot_sdk.get_structured_llm_response(structured_prompt, car_info_schema)
    print(f"Structured LLM Result: {structured_result}")


if __name__ == "__main__":
    # Run the asynchronous main function
    asyncio.run(main())
