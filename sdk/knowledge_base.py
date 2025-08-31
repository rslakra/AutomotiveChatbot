#
# Author: Rohtash Lakra
#

class KnowledgeBase:
    """
    Manages automobile-specific information.
    """

    def __init__(self):
        self.data = {
            "tire pressure": "Your tire pressure is currently 32 PSI in all tires. Recommended is 35 PSI.",
            "fuel level": "Your fuel tank is 75% full, which is approximately 300 miles of range.",
            "oil life": "Your oil life is at 60%. You should consider an oil change in about 3,000 miles.",
            "engine light": "The engine light typically indicates an issue with the engine or emissions system. Please consult your owner's manual or visit a service center.",
            "adaptive cruise control": "Adaptive Cruise Control (ACC) automatically adjusts your vehicle's speed to maintain a safe distance from the vehicle ahead.",
            "blind spot monitoring": "Blind Spot Monitoring (BSM) uses sensors to detect vehicles in your blind spots and alerts you with visual or audible warnings."
        }

    def get_info(self, topic):
        """Retrieves information from the knowledge base."""
        return self.data.get(topic.lower(), "I don't have specific information on that topic at the moment.")
