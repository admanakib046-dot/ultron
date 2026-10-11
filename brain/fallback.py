class FallbackEngine:

    def get_chain(self, scores):

        chain = []

        ordered = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for name, score in ordered:

            if score > 0:
                chain.append(name)

        return chain