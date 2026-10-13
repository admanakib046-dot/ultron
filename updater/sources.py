import requests


class Sources:

    def find_updates(self):

        return [

            {
                "module": "Memory",
                "version": "2.1",
                "reason": "Better retrieval"
            },

            {
                "module": "Vision",
                "version": "1.4",
                "reason": "OCR support"
            },

            {
                "module": "Planner",
                "version": "3.0",
                "reason": "Faster reasoning"
            }

        ]