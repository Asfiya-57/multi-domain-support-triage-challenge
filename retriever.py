from sklearn.feature_extraction.text import TfidfVectorizer

class Retriever:
    def __init__(self):
        self.docs = []
        self.sources = []
        self.vectorizer = TfidfVectorizer()

    def load_docs(self, files):
        for source, file_path in files.items():
            with open(file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        self.docs.append(line)
                        self.sources.append(source)

        self.matrix = self.vectorizer.fit_transform(self.docs)

    def retrieve(self, query):
        query_vec = self.vectorizer.transform([query])
        scores = (self.matrix * query_vec.T).toarray().flatten()

        top_indices = scores.argsort()[-2:][::-1]

        results = []
        for i in top_indices:
            results.append({
                "text": self.docs[i],
                "source": self.sources[i],
                "score": float(scores[i])
            })

        return results