# 🍲 FastText Word Embeddings for Indian Recipes

A Natural Language Processing (NLP) project that demonstrates how **FastText** can generate meaningful word embeddings for Indian food names by training a custom **Skip-gram** model on an Indian Recipes dataset. The project compares the performance of the **pre-trained English FastText model** with a **custom-trained FastText model** for domain-specific vocabulary.

---

# 📌 Project Overview

FastText is a word embedding technique developed by Facebook AI Research (FAIR). Unlike traditional embedding models such as **Word2Vec** and **GloVe**, FastText represents words using **character-level n-grams**, allowing it to understand rare, unseen, and morphologically similar words.

In this project:

- The pre-trained English FastText model (`cc.en.300.bin`) is first used to perform word similarity and analogy tasks.
- It performs well for general English words like **King** and **Good**.
- However, it struggles to understand Indian food names such as **Halwa**, **Chutney**, and **Dosa**.
- To solve this problem, a custom FastText **Skip-gram** model is trained using an Indian Recipes dataset.
- The project automatically preprocesses the dataset, generates the training corpus, trains the model, and compares the results with the English model.

---

# 🚀 Features

- Download and load the pre-trained English FastText model.
- Perform word similarity searches.
- Perform word analogy operations.
- Compare general English vocabulary with Indian food vocabulary.
- Automatically locate the dataset using Python's `os` module.
- Clean and preprocess recipe instructions.
- Automatically generate the training corpus (`food_receipes.txt`).
- Train a custom FastText Skip-gram model.
- Generate domain-specific word embeddings.
- Compare the nearest neighbors produced by both models.

---

# 📂 Dataset

This project uses the **Cleaned Indian Recipes Dataset**.

Download the dataset from Kaggle:

**https://www.kaggle.com/datasets/sooryaprakash12/cleaned-indian-recipes-dataset**

After downloading:

1. Rename the dataset (if necessary) as:

```
Cleaned_Indian_Food_Dataset.csv
```

2. Place it inside the project folder.

The project will automatically generate:

```
food_receipes.txt
```

which is used for training the custom FastText model.

---

# ⚙️ Installation

## VS Code

Install FastText using:

```bash
pip install fasttext-wheel
```

---

## Jupyter Notebook

Install FastText using:

```bash
pip install -q fasttext
```

---

## Install Remaining Libraries

```bash
pip install pandas
```

---

# 📚 Libraries Used

- FastText
- FastText Utility
- Pandas
- Regular Expressions (`re`)
- OS

---

# 🛠 Technologies Used

- Python
- FastText
- Natural Language Processing (NLP)
- Word Embeddings
- Skip-gram
- Text Preprocessing

---

# 📖 Project Workflow

## Step 1 – Download the English FastText Model

The project downloads the pre-trained English FastText model (`cc.en.300.bin`) if it is not already available.

---

## Step 2 – Load the Pre-trained Model

The English FastText model is loaded and its embedding dimension is displayed.

---

## Step 3 – Word Similarity

The model is tested using common English words such as:

- King
- Good

to demonstrate semantic similarity.

---

## Step 4 – Word Analogy

The project performs analogy operations such as:

```
Berlin : Germany :: ? : India
```

using FastText's built-in analogy function.

---

## Step 5 – Test Indian Food Vocabulary

The English model is queried using:

- Halwa

The returned nearest neighbors are not very meaningful because the model has limited knowledge of Indian cuisine.

---

## Step 6 – Load the Dataset

The dataset is automatically loaded from the project directory using Python's `os.path` module.

This makes the project portable across different systems without changing file paths.

---

## Step 7 – Text Preprocessing

The recipe instructions are cleaned before training.

The preprocessing includes:

- Converting text to lowercase
- Removing punctuation
- Removing numbers
- Removing newline characters
- Removing extra spaces

---

## Step 8 – Generate the Training Corpus

The cleaned recipe instructions are automatically saved into:

```
food_receipes.txt
```

This file is used as the training corpus for FastText.

---

## Step 9 – Train a Custom FastText Model

A custom **Skip-gram FastText model** is trained using:

- 300-dimensional word embeddings
- Learning rate = 0.05
- Epoch = 1
- 4 CPU threads

---

## Step 10 – Generate Word Embeddings

The trained model is tested using Indian dishes such as:

- Halwa
- Chutney
- Dosa

The custom model generates much more meaningful nearest-neighbor vectors compared to the English model.

---

# 📊 Results

## Pre-trained English FastText Model

✅ Excellent for general English vocabulary.

✅ Good analogy performance.

❌ Limited understanding of Indian food names.

❌ Poor semantic similarity for domain-specific vocabulary.

---

## Custom-Trained FastText Model

✅ Learns Indian culinary vocabulary.

✅ Produces meaningful nearest-neighbor vectors.

✅ Better semantic understanding of Indian dishes.

✅ Suitable for domain-specific Natural Language Processing tasks.

---

# 🚀 Why FastText over Word2Vec and GloVe?

FastText represents each word as a collection of **character-level n-grams** instead of treating each word as a single token.

This enables FastText to understand subword information, making it much more robust for specialized datasets.

| Feature | Word2Vec | GloVe | FastText |
|---------|----------|--------|-----------|
| Word Embeddings | ✅ | ✅ | ✅ |
| Character-level n-grams | ❌ | ❌ | ✅ |
| Handles Out-of-Vocabulary (OOV) Words | ❌ | ❌ | ✅ |
| Rare Word Support | ❌ | Limited | ✅ |
| Handles Misspelled Words | ❌ | ❌ | ✅ |
| Captures Morphological Information | ❌ | ❌ | ✅ |
| Skip-gram Support | ✅ | ❌ | ✅ |
| CBOW Support | ✅ | ❌ | ✅ |
| Domain-Specific Learning | Moderate | Moderate | Excellent |

---

# ✅ Advantages of FastText

- Uses character-level n-grams.
- Generates embeddings for unseen words.
- Handles Out-of-Vocabulary (OOV) words.
- Performs well on rare words.
- Understands prefixes and suffixes.
- Handles spelling variations.
- Produces richer semantic representations.
- Excellent for domain-specific datasets.
- Supports both Skip-gram and CBOW architectures.

---

# 📁 Project Structure

```
FastText-Indian-Recipes-NLP/
│
├── FastText_Indian_Recipes.py
├── Cleaned_Indian_Food_Dataset.csv
├── food_receipes.txt        # Automatically generated
├── README.md
└── cc.en.300.bin            # Downloaded automatically
```

---

# ▶️ How to Run the Project

### Step 1

Clone the repository.

### Step 2

Install the required libraries.

### Step 3

Download the dataset from Kaggle.

### Step 4

Place the file:

```
Cleaned_Indian_Food_Dataset.csv
```

inside the project folder.

### Step 5

Run the project:

```bash
python FastText_Indian_Recipes.py
```

---

# 💻 Expected Output

The program will:

- Download the English FastText model (if not already available).
- Load the Indian Recipes dataset.
- Preprocess the recipe instructions.
- Generate the training corpus (`food_receipes.txt`).
- Train a custom FastText Skip-gram model.
- Display nearest neighbors for:
  - King
  - Good
  - Halwa (English model)
  - Halwa (Custom model)
  - Chutney
  - Dosa
- Compare the performance of the pre-trained and custom-trained models.

---

# 🎯 Learning Outcomes

Through this project, I learned:

- FastText fundamentals
- Word embeddings
- Skip-gram architecture
- Word similarity
- Word analogies
- Character-level n-grams
- Text preprocessing
- Domain-specific Natural Language Processing
- Training custom word embedding models
- Semantic similarity in NLP

---

# 📌 Conclusion

The pre-trained English FastText model performs well for general English vocabulary but has limited knowledge of Indian cuisine.

By training a custom FastText model on an Indian Recipes dataset, the model learns meaningful semantic relationships between Indian food names and produces significantly better word embeddings for domain-specific vocabulary.

This project demonstrates the importance of **domain-specific training data** and highlights why FastText is a powerful choice for specialized Natural Language Processing applications.

---

# 👨‍💻 Author

**Snehal Vhasure**

Full Stack Developer | AI & Machine Learning Enthusiast | Master's Aspirant in Information Technology
