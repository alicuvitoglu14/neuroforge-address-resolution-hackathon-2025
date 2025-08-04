import pandas as pd
import random

# Adres parçaları
neighborhoods = ["Atatürk", "Yenimahalle", "Çınar", "Gülbahar", "İnönü"]
streets = ["Gül", "Menekşe", "Çam", "Fıstık", "Lale"]
suffixes = ["Mah.", "Mahallesi", "Mah", "mah", "MAH"]
street_suffixes = ["Sok.", "Sk.", "Sokak", "sk", "SOK"]
numbers = ["No: 5", "No 5", "Numara 5", "5 numara", "5"]

def generate_address_pair():
    mahalle = random.choice(neighborhoods)
    mahalle_suffix = random.choice(suffixes)
    sokak = random.choice(streets)
    sokak_suffix = random.choice(street_suffixes)
    numara = random.choice(numbers)

    # Bozuk versiyon
    raw_address = f"{mahalle} {mahalle_suffix} {sokak} {sokak_suffix} {numara}"

    # Normalize hedefi (doğru hali)
    normalized_address = f"{mahalle.lower()} mahallesi {sokak.lower()} sokak numara 5"

    return raw_address, normalized_address

# Listeyi üret
samples = [generate_address_pair() for _ in range(100)]

# DataFrame olarak ayır
df_raw = pd.DataFrame([x[0] for x in samples], columns=["original_address"])
df_norm = pd.DataFrame([x[1] for x in samples], columns=["normalized_address"])

# CSV olarak kaydet
df_raw.to_csv("data/sample_addresses.csv", index=False)
df_norm.to_csv("data/normalized_targets.csv", index=False)

print("Örnek veri dosyaları oluşturuldu: data/sample_addresses.csv, data/normalized_targets.csv")

