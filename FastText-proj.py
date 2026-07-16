import fasttext as ft
import fasttext.util as ft_util
import pandas as pd
import re
import os

ft_util.download_model('en', if_exists= 'ignore')

model_en = ft.load_model('cc.en.300.bin')
print(model_en.get_dimension())

print("Nearest neighbors of 'king':", model_en.get_nearest_neighbors("king"))
print("Nearest neighbors of 'good':", model_en.get_nearest_neighbors("good"))

print("Analogies:", model_en.get_analogies("berlin", "germany", "india"))
print("Nearest neighbors of 'halwa' (k=3):", model_en.get_nearest_neighbors("halwa", k=3))

# project to train model so that it can understand the Indian recepies better than the English model

# print(os.getcwd())
# df = pd.read_csv("Cleaned_Indian_Food_Dataset.csv")

script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct full CSV path
csv_path = os.path.join(
    script_dir, 
    "Cleaned_Indian_Food_Dataset.csv"
    )
df = pd.read_csv(csv_path)
print(df.head(5))

print(  "Training Labels Shape :", df.shape)
print( df.TranslatedInstructions[0] )

# 1. Text Cleansing
text = df.TranslatedInstructions[0]
print(text)

def preprocess(text):
    text = re.sub(r'[^\w\s]', ' ', text)  # Remove punctuation and extra spaces
    text = re.sub(r'\d+', ' ', text)  # Remove numbers
    text = re.sub(r'[\n]+', ' ', text)  # Remove newlines

    return text.strip().lower() # strip will remove leading and trailing spaces and lower will convert the text to lower case

print("Preprocessed Text :", preprocess(text))

df.TranslatedInstructions = df.TranslatedInstructions.map(preprocess)
print(df.TranslatedInstructions[0])

food_recepies = "food_receipes.txt"
df.to_csv(
    food_recepies, 
    columns = ["TranslatedInstructions"], 
    header = None, 
    index = False
    )
model = ft.train_unsupervised(
    food_recepies, 
    model='skipgram', 
    dim=300, 
    epoch=1, 
    lr=0.05, 
    thread=4
    )

print("Nearest neighbors of 'chutney':", model.get_nearest_neighbors("chutney"))
print("Nearest neighbors of 'halwa':", model.get_nearest_neighbors("halwa"))
print("Nearest neighbors of 'dosa':", model.get_nearest_neighbors("dosa"))



