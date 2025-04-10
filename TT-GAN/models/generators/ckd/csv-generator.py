import sys
import os
import pandas as pd
import pickle

sys.path.append(r"C:\Users\rafae\Sally\TT-GAN")

pkl_path = r"C:\Users\rafae\Sally\TT-GAN\models\generators\ckd\TTGAN-O.pkl"
csv_path = r"C:\Users\rafae\Sally\TT-GAN\models\generators\ckd\TTGAN-O.csv"

# Carrega o objeto
with open(pkl_path, "rb") as f:
    obj = pickle.load(f)

# Gera os dados sintéticos
synthetic_df = obj.sample(1000) 

# Salva em CSV
synthetic_df.to_csv(csv_path, index=False)

print("Arquivo CSV salvo com sucesso!")
