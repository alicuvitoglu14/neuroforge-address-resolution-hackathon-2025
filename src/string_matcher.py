from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from address_normalizer import normalize_address

def compute_similarity(addr1, addr2):
    """
    İki adres metni arasında TF-IDF + cosine similarity skorunu hesaplar.
    
    Args:
        addr1 (str): 1. adres metni
        addr2 (str): 2. adres metni
        
    Returns:
        float: [0.0 - 1.0] arası benzerlik skoru (1.0 = tamamen aynı)
    """
    # Adresleri normalize et
    norm1 = normalize_address(addr1)
    norm2 = normalize_address(addr2)

    # TF-IDF vektörleştirici
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([norm1, norm2])

    # Cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return similarity[0][0]

# Örnek test
if __name__ == "__main__":
    a1 = "Atatürk Mah. Gül Sok. No: 12/A"
    a2 = "Ataturk Mahallesi Gul Sk No 12A"
    
    score = compute_similarity(a1, a2)
    print(f"Benzerlik Skoru: {score:.4f}")

