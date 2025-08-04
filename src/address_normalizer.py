import re
import unidecode

# Sık kullanılan bazı kısaltmaların açılımı
ABBREVIATIONS = {
    "mah": "mahalle",
    "cad": "cadde",
    "sok": "sokak",
    "apt": "apartman",
    "no": "numara",
    "blv": "bulvar",
    "sk": "sokak",
    "sb": "sube"
}

def expand_abbreviations(text):
    """
    Bilinen adres kısaltmalarını açar (örnek: 'mah' → 'mahalle')
    """
    words = text.split()
    expanded_words = [ABBREVIATIONS.get(word.lower().rstrip("."), word) for word in words]
    return " ".join(expanded_words)

def normalize_address(text):
    """
    Girdi olarak verilen adres metnini normalize eder:
    - Küçük harfe çevirir
    - Türkçe karakterleri sadeleştirir
    - Noktalama işaretlerini kaldırır
    - Kısaltmaları açar
    """
    # Küçük harf
    text = text.lower()

    # Türkçe karakterleri düzleştir
    text = unidecode.unidecode(text)

    # Noktalama ve özel karakterleri temizle
    text = re.sub(r"[^\w\s]", " ", text)

    # Fazla boşlukları sadeleştir
    text = re.sub(r"\s+", " ", text).strip()

    # Kısaltmaları aç
    text = expand_abbreviations(text)

    return text

# Örnek test
if __name__ == "__main__":
    sample = "Atatürk Mah. Gül Sok. No: 12/A"
    print("Orijinal:", sample)
    print("Normalize:", normalize_address(sample))

