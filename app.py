# imports
from database import create_table, add_entry, get_entries


# menu options
menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

# welcome message
welcome = "\nWelcome to the programming diary!"


def prompt_new_entry():
    """
    prompts the user to enter what they have learned and the date in a second prompt.
    :return: None
    """
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    """
    display all entries currently in the programming log
    :param entries: a cursor passed in
    :return: None
    """
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


# display welcome message and create a table
print(welcome)
create_table()

# keep displaying the menu options until the user enters '3' to exit
while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option, please try again!")
