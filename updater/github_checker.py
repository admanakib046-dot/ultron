import requests


class GithubChecker:

    BASE = "https://raw.githubusercontent.com/admanakib046-dot/ultron/main"

    def check(self):

        try:

            version_url = self.BASE + "/version.json"
            modules_url = self.BASE + "/modules.json"
            changelog_url = self.BASE + "/CHANGELOG.md"

            version_response = requests.get(version_url, timeout=10)
            modules_response = requests.get(modules_url, timeout=10)
            changelog_response = requests.get(changelog_url, timeout=10)

            print("Version URL:", version_url)
            print(version_response.status_code)
            print(version_response.text)

            print("Modules URL:", modules_url)
            print(modules_response.status_code)
            print(modules_response.text)

            version = version_response.json()
            modules = modules_response.json()
            changelog = changelog_response.text

            return {
                "version": version,
                "modules": modules,
                "notes": changelog
            }
        except Exception:
         import traceback
        traceback.print_exc()
        return None