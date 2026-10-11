from internet.internet import Internet
import wikipedia


class Wikipedia(Internet):

    def search(self, query):

        wikipedia.set_lang("en")

        q = query.lower()

        if q.startswith("who is "):
            q = query[7:]

        elif q.startswith("what is "):
            q = query[8:]

        try:
            results = wikipedia.search(q)

            if not results:
                return "No Wikipedia results."

            page = wikipedia.page(results[0],auto_suggest=False)

            return f"""
Title: {page.title}

Summary:
{page.summary}

URL:
{page.url}
"""

        except Exception as e:
            return str(e)