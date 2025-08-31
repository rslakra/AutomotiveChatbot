#
# Author: Rohtash Lakra
#
def get_tinker_description():
    """Returns a description of what 'tinkering' generally means."""
    return (
        "Tinkering generally refers to the act of experimenting, playing around "
        "with, or making small adjustments to something in an effort to "
        "improve it, understand how it works, or simply for fun. "
        "It often involves a hands-on approach and a willingness to try "
        "different things without a rigid plan."
    )


def chatbot():
    """A simple chatbot that describes tinkering."""
    print("Hello! I'm a simple chatbot.")
    while True:
        user_input = input("What would you like to know? (Type 'tinker' or 'quit'): ").lower()

        if user_input == "tinker":
            print(get_tinker_description())
        elif user_input == "quit":
            print("Goodbye!")
            break
        else:
            print("I'm sorry, I can only describe 'tinker' at the moment. Please try again.")


if __name__ == "__main__":
    chatbot()
