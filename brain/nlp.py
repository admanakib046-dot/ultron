from brain.intent import intent


class NLP:

    def understand(self, text):

        text = text.strip()
        lower = text.lower()

        # =========================
        # MEMORY
        # =========================

        if lower.startswith("remember "):

            body = text[9:]

            if "=" in body:
                key, value = body.split("=", 1)

                return intent(
                    action="remember",
                    data={
                        "key": key.strip(),
                        "value": value.strip()
                    }
                )

        elif lower.startswith("recall "):

            return intent(
                action="recall",
                data={
                    "key": text[7:].strip()
                }
            )

        # =========================
        # CALCULATOR
        # =========================

        elif lower.startswith("calculate "):

            return intent(
                action="calculate",
                data={
                    "expression": text[10:].strip()
                }
            )

        # =========================
        # KNOWLEDGE
        # =========================

        elif lower.startswith("learn "):

            return intent(
                action="learn",
                data={
                    "file": text[6:].strip()
                }
            )

        elif lower.startswith("search document "):

            return intent(
                action="knowledge_search",
                data={
                    "query": text[16:].strip()
                }
            )

        # =========================
        # INTERNET
        # =========================

        search_prefixes = [

            "search",
            "who",
            "what",
            "where",
            "when",
            "why",
            "how",
            "latest",
            "news",
            "today",
            "weather",
            "price",
            "wiki",
            "wikipedia"

        ]

        if any(lower.startswith(word) for word in search_prefixes):

            return intent(
                action="search",
                data={
                    "query": text
                }
            )

        # Questions ending with '?'
        if text.endswith("?"):

            return intent(
                action="search",
                data={
                    "query": text
                }
            )

        # Common search keywords anywhere
        internet_keywords = [

            "retired",
            "release",
            "released",
            "launch",
            "launched",
            "president",
            "population",
            "capital",
            "history",
            "meaning",
            "definition",
            "news"

        ]

        if any(word in lower for word in internet_keywords):

            return intent(
                action="search",
                data={
                    "query": text
                }
            )

        # =========================
        # AI
        # =========================

        return intent(
            action="ai",
            data={
                "prompt": text
            }
        )
     

