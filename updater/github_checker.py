import requests


class GithubChecker:

    URL = "https://api.github.com/repos/YOUR_USERNAME/Ultron/releases/latest"

    def check(self):

        try:

            r = requests.get(self.URL, timeout=10)

            if r.status_code != 200:
                return None

            data = r.json()

            return {

                "version": data["tag_name"],
                "name": data["name"],
                "notes": data["body"]

            }

        except Exception:

            return None