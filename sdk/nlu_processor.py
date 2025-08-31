#
# Author: Rohtash Lakra
#
import spacy


class NLUProcessor:
    """
    Handles Natural Language Understanding: intent recognition and entity extraction.
    """

    def __init__(self):
        # Load a small English model for basic NLP tasks
        # You might need to download it: python -m spacy download en_core_web_sm
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading spaCy model 'en_core_web_sm'...")
            spacy.cli.download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")

        # Define simple keyword-based intents and entities for demonstration
        self.intents = {
            "set_temperature": ["set temperature", "change temp", "adjust climate"],
            "find_location": ["find nearest", "where is the closest", "navigate to"],
            "check_status": ["check", "what is the status of", "is my"],
            "explain_feature": ["what is", "how does", "explain"],
            "open_app": ["open", "launch", "start"],
            "call_contact": ["call", "dial"],
            "general_query": ["tell me about", "what can you do"]
        }
        self.entities = {
            "temperature": ["degrees", "celsius", "fahrenheit", "temp"],
            "location_type": ["gas station", "restaurant", "charging station", "parking"],
            "car_part": ["tire pressure", "fuel level", "oil life", "engine"],
            "app_name": ["spotify", "apple music", "navigation", "radio"],
            "contact_name": ["home", "work"]  # Placeholder for contact names
        }

    def process_text(self, text):
        """
        Processes user text to identify intent and extract entities.
        A more advanced NLU would use machine learning models.
        """
        doc = self.nlp(text.lower())
        intent = "unknown"
        entities = {}

        # Simple keyword-based intent matching
        for key, phrases in self.intents.items():
            if any(phrase in text.lower() for phrase in phrases):
                intent = key
                break

        # Simple keyword-based entity extraction
        for ent_type, keywords in self.entities.items():
            for keyword in keywords:
                if keyword in text.lower():
                    # For demonstration, just store the keyword
                    entities[ent_type] = keyword
                    # A real system would extract the actual value (e.g., "22" for temperature)
                    if ent_type == "temperature":
                        import re
                        match = re.search(r'(\d+)\s*(degrees|c|f)?', text.lower())
                        if match:
                            entities[ent_type] = match.group(1) + (match.group(2) if match.group(2) else '')
                    break  # Assuming one entity of this type for simplicity

        return {"intent": intent, "entities": entities}
