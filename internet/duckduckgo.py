from internet.internet import Internet
from ddgs import DDGS


class DuckDuckGo(Internet):

    def search(self, query):
    
        try:
            with DDGS() as ddgs:
                results = ddgs.text(query, max_results=5)

                answer = ""

                for r in results:
                    answer += f"{r['title']}\n"
                    answer += f"{r['body']}\n"
                    answer += f"{r['href']}\n\n"

                if answer == "":
                    return "No results."

                return answer

        except Exception as e:
            return str(e)