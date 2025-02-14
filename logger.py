# Simple Python code that logs messages to a file, similar to Git commit functions.
def log_message(message):
    """Append a message to log.txt with a newline."""
    with open("log.txt", "a") as file:
        file.write(message + "\n")
    print(f'Logged: "{message}"')

# Example usage
log_message("Initialized the project")
log_message("Created a new feature")
log_message("Fixed a bug")
