def user_input(prompt):
    """
    Get input from the user.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        str: The user's input.
    """
    userInput = input(prompt)
    return userInput


def process_user_input(user_input):
    """
    Process the user's input.

    Args:
        user_input (str): The user's input.
    """
    if len(user_input) > 10:
        print("User input is too long.")
    else:
        print("User input is processed successfully.")


if __name__ == "__main__":
    user_input = user_input("Enter your input: ")
    process_user_input(user_input)
