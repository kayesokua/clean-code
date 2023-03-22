## Refactoring
Refactoring for code found [here](https://gist.github.com/fatma-meawad/4237b66aa74ceef899802b17a3a553e5/revisions)

### Suggestions:

1. Extracting repeated logic into functions: The original code contains duplicated code for checking if a parameter is a list or not, which has been extracted into a new function named if_file_exists.
2. Using a dictionary to store messages: Instead of using multiple string literals, all the messages used in the code have been stored in a dictionary named MESSAGES.
3. Simplifying the do_command function: The do_command function has been simplified by using a command_map dictionary instead of a series of if-else statements.
4. Separation of concerns: The refactored code separates the different concerns into their respective functions, such as status, commit, log, and diff, making the code more modular and easier to understand.
5. Error handling: The refactored code includes better error handling with the use of specific messages for each error, making it easier to identify the type of error and how to fix it.
