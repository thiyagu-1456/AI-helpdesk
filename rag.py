from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load knowledge base
with open("it_troubleshooting.txt", "r", encoding="utf-8") as file:
    text = file.read()


# Split knowledge base into sections
documents = [
    section.strip()
    for section in text.split("\n\n")
    if section.strip()
]


# Create TF-IDF vectors
vectorizer = TfidfVectorizer()
document_vectors = vectorizer.fit_transform(documents)


def search_knowledge_base(query, k=3):
    """
    Search the knowledge base and return the most relevant sections.
    """

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    )[0]

    # Get indexes of most relevant documents
    ranked_indexes = similarities.argsort()[::-1][:k]

    results = []

    for index in ranked_indexes:
        if similarities[index] > 0:
            results.append(documents[index])

    return results


# Test RAG
if __name__ == "__main__":

    query = "My computer is connected to Wi-Fi but websites are not opening"

    results = search_knowledge_base(query)

    print("\nUser Query:")
    print(query)

    print("\nRelevant Knowledge:\n")

    for result in results:
        print(result)
        print("-" * 60)