import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer


def embedding_data():
    """
    This function is responsible for generating sentence embeddings for the cleaned dataset,
    it uses the 'all-MiniLM-L6-v2' model from the SentenceTransformers library,
    then save it as a NumPy array file.
    """

    try:
        df = pd.read_csv("data/cleaned/NTOT2023_cleaned.csv",
                         encoding="ISO-8859-1")

    except Exception as e:
        print(f"Exception: {e}")

    print("\nEmbedding in progress..")

    model = SentenceTransformer('all-MiniLM-L6-v2')
    corpus = df['l_pre_spe'].tolist()

    embeddings = model.encode(corpus)

    np.save("data/embeddings/embeddings.npy", embeddings)
