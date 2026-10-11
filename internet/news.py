from internet.internet import Internet
from ddgs import DDGS


class News(Internet):

    def search(self, query):

        with DDGS() as ddgs:

            results = ddgs.news(query, max_results=5)

            answer = ""

            for r in results:

                answer += f"{r['title']}\n"

                answer += f"{r['body']}\n\n"

            if answer == "":
                return "No news found."

            return answer