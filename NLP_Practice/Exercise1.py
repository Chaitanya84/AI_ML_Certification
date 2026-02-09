import re
from sklearn.feature_extraction.text import TfidfVectorizer
text = [
    "I loved this movie, it was fantastic !",
    "I hated this movie ,this time it was really bad !",
    "This movie was not good, I will not recommend it to anyone !",
    "This movie was not bad, I will recommend it to everyone !",
]

def clean_text(t):
    t= t.lower() # Convert the text to lowercase, this is done so that in next line when we substitute the 
    #non alphabet character then we can easily differentiate between the words and the non alphabet characters
    t = re.sub(r"[^a-z\s]", "", t) # re.sub substitutre all non-alphabetic characters with an empty string
    return t

cleaned_text = [clean_text(t) for t in text]

print("Oringinal text :", text[0])
print("Cleaned Text: ", cleaned_text[0])

vectoriser = TfidfVectorizer(stop_words="english")
X = vectoriser.fit_transform(cleaned_text)

print("Shape: ", X.shape)
print("Feature Names: ", vectoriser.get_feature_names_out())
print("TF-IDF Matrix: ", X.toarray())
