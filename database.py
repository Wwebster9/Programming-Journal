# imports
import sqlite3

# make connection to sqlite database
connection = sqlite3.connect('data.db')

# this is optional, but by using this line of code we can access the
# information returned by the SELECT statement using the 'date' and 'content'
# strings. without this line, we would need to use indexing instead.
connection.row_factory = sqlite3.Row


def create_table():
    """Creates a new table, if that table is not already created"""
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )


def add_entry(entry_content, entry_date):
    """
    Updates table by adding in the entry content and date
    :param entry_content: user entered content
    :param entry_date: user entered date
    :return: None
    """
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date)
        )


def get_entries():
    """
    Grabs all entries from the table
    :return: cursor pointing to the first row of the table
    """
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor
