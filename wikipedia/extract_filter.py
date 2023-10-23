import pandas as pd
import wikipedia
from tokenize import extract_sections


def filter_relevant_titles(titles, context):
    arr = []
    for title in titles:
        context = context.lower()
        page = get_wiki_page(title)
        if page == None:
            continue
        elif context in page.summary.lower():
            arr.append(title)
    return arr


def get_wiki_page(title):
    try:
        return wikipedia.page(title, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError:
        return
    except wikipedia.exceptions.PageError:
        return


def find_related_pages(original_title, limit):
    pages = []

    topic_page = get_wiki_page(original_title)
    pages.append(topic_page)
    related_pages = topic_page.links[:limit]

    related_pages = filter_relevant_titles(
        related_pages, original_title)

    for t in related_pages:
        r_page = get_wiki_page(t)
        pages.append(r_page)

    return pages


def topic_tuple(topics):
    arr = []
    for topic in topics:
        print("Starting topic: \n")
        print(topic)
        pages = find_related_pages(topic, 400)
        for page in pages:
            topic_page = (topic, page)
            arr.append(topic_page)
            print("Finished Topic: \n")
            print(topic)
    return arr


dicts = topic_tuple(["Software Engineering", "Computer Network",
                    "Cryptography", "Programming Languages"])

res = []
for dict_entry in dicts:
    page = dict_entry[1]
    category = dict_entry[0]
    res += extract_sections(page.content, page.title, category)

df = pd.DataFrame(
    res, columns=["title", "heading", "content", "tokens", "category"])
df = df[df.tokens > 40]
df = df.drop_duplicates(['title', 'heading'])
df = df.reset_index().drop('index', axis=1)  # Reset index
print(df.head())
df.to_csv('softwareeng.csv', index=False)
