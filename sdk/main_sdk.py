#
# Author: Rohtash Lakra
#
from sdk.dialogue_manager import DialogueManager
from sdk.knowledge_base import KnowledgeBase
from sdk.llm.response_generator import LLMResponseGenerator
from sdk.nlu_processor import NLUProcessor


class AutomobileChatbotSDK:
    """
    Main class for the Automobile Chatbot SDK.
    Orchestrates NLU, dialogue management, and response generation.
    """

    def __init__(self, gemini_api_key: str, gemini_api_url: str):
        self.nlu_processor = NLUProcessor()
        self.knowledge_base = KnowledgeBase()
        self.llm_generator = LLMResponseGenerator(api_key=gemini_api_key, api_url=gemini_api_url)
        self.dialogue_manager = DialogueManager(self.knowledge_base, self.llm_generator)

    async def process_user_input(self, user_text):
        """
        Processes a user's text input and returns a chatbot response and potential action.
        """
        print(f"User input: '{user_text}'")
        nlu_output = self.nlu_processor.process_text(user_text)
        nlu_output["original_text"] = user_text  # Store original text for LLM
        print(f"NLU Output: Intent='{nlu_output['intent']}', Entities={nlu_output['entities']}")

        response_data = await self.dialogue_manager.handle_query(nlu_output)
        return response_data

    async def get_structured_llm_response(self, prompt, schema):
        """
        Allows direct structured queries to the LLM for specific data extraction.
        Example: Extracting a list of car features from a user's description.
        """
        return await self.llm_generator.generate_response(prompt, structured_output_schema=schema)
