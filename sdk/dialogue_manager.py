#
# Author: Rohtash Lakra
#

class DialogueManager:
    """
    Manages the conversation flow and determines actions based on NLU output.
    """

    def __init__(self, knowledge_base, llm_generator):
        self.knowledge_base = knowledge_base
        self.llm_generator = llm_generator
        self.context = {}  # Stores conversation context

    async def handle_query(self, nlu_output):
        """
        Processes NLU output and generates a response or action.
        """
        intent = nlu_output["intent"]
        entities = nlu_output["entities"]
        response_text = "I'm not sure how to respond to that."
        action = None  # Structured action for the integrating app

        if intent == "set_temperature":
            temp = entities.get("temperature")
            if temp:
                response_text = f"Setting temperature to {temp}."
                action = {"type": "set_climate", "value": temp}
            else:
                response_text = "What temperature would you like to set it to?"
        elif intent == "find_location":
            location_type = entities.get("location_type")
            if location_type:
                # In a real app, this would query a map service
                response_text = f"Searching for the nearest {location_type}."
                action = {"type": "find_poi", "poi_type": location_type}
            else:
                response_text = "What kind of location are you looking for?"
        elif intent == "check_status":
            car_part = entities.get("car_part")
            if car_part:
                response_text = self.knowledge_base.get_info(car_part)
                action = {"type": "display_info", "info_type": car_part}
            else:
                response_text = "Which car status would you like to check?"
        elif intent == "explain_feature":
            feature = entities.get("car_part")  # Reusing car_part for features
            if feature:
                response_text = self.knowledge_base.get_info(feature)
                action = {"type": "display_info", "info_type": feature}
            else:
                response_text = "Which feature would you like me to explain?"
        elif intent == "open_app":
            app_name = entities.get("app_name")
            if app_name:
                response_text = f"Opening {app_name}."
                action = {"type": "launch_app", "app_name": app_name}
            else:
                response_text = "Which app would you like to open?"
        elif intent == "call_contact":
            contact_name = entities.get("contact_name")
            if contact_name:
                response_text = f"Calling {contact_name}."
                action = {"type": "make_call", "contact": contact_name}
            else:
                response_text = "Who would you like to call?"
        elif intent == "general_query":
            # Use LLM for more general or complex queries not covered by explicit intents
            prompt = f"The user asked: '{nlu_output['original_text']}'. Respond as a helpful car assistant."
            response_text = await self.llm_generator.generate_response(prompt)
            action = {"type": "informational_response"}
        else:
            # Fallback to LLM for unknown intents
            prompt = f"I didn't understand '{nlu_output['original_text']}'. Can you rephrase or ask about something else? Respond as a helpful car assistant."
            response_text = await self.llm_generator.generate_response(prompt)
            action = {"type": "informational_response", "fallback": True}

        return {"response": response_text, "action": action}
