"""
Program to get a page title from a user and search it on wikipedia.
"""

import wikipedia

page_title = input("Page title: ")

while page_title != "":
    try:
        page = wikipedia.page(page_title, auto_suggest=False)
        print(page.title)
        print(page.url)
        print(page.summary)
        print()
    except wikipedia.DisambiguationError:
        print(f"Disambiguation error: {page_title} may refer to multiple pages:")

    except wikipedia.PageError:
        print(f"{page_title} does not exist.")

    page_title = input("Page title: ")

print('Thank you')

