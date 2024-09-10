#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from gensim.similarities import MatrixSimilarity
from gensim import similarities
import tkinter as tk
from tkinter import ttk
import random

# Sample book data
books_data = {
    'Title': ['Pride and Prejudice', 'To Kill a Mockingbird', '1984', 'The Great Gatsby', 'Moby-Dick', 'Harry Potter and the Sorcerer\'s Stone', 'The Catcher in the Rye', 'The Hobbit', 'The Lord of the Rings', 'The Da Vinci Code'],
    'Genre': ['Romantic', 'Drama', 'Dystopian', 'Drama', 'Adventure', 'Fantasy', 'Fiction', 'Fantasy', 'Fantasy', 'Mystery'],
    'Author': ['Jane Austen', 'Harper Lee', 'George Orwell', 'F. Scott Fitzgerald', 'Herman Melville', 'J.K. Rowling', 'J.D. Salinger', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'Dan Brown'],
    'Description': [
        'A romantic novel that charts the emotional development of the protagonist Elizabeth Bennet.',
        'The novel is renowned for its warmth and humor, despite dealing with serious issues of rape and racial inequality.',
        'A dystopian social science fiction novel and cautionary tale about the dangers of totalitarianism.',
        'A story about the young and mysterious millionaire Jay Gatsby and his quixotic passion for the beautiful Daisy Buchanan.',
        'The narrative is sailor Ishmael\'s account of the obsessive quest of Ahab for revenge on Moby Dick, the white whale.',
        'The story follows a young boy who discovers that he is a wizard and is invited to attend a magical school.',
        'A story about a teenager named Holden Caulfield and his experiences in New York City after being expelled from prep school.',
        'The hobbit Bilbo Baggins and his adventures with thirteen dwarves and the wizard Gandalf as they quest to reclaim the Lonely Mountain and its treasure from the dragon Smaug.',
        'An epic high fantasy novel that follows the quest of a group of characters to destroy the Dark Lord Sauron.',
        'A mystery thriller novel that follows symbologist Robert Langdon and cryptologist Sophie Neveu as they investigate a murder in the Louvre Museum.'
    ]
}

# Convert data to DataFrame
books_df = pd.DataFrame(books_data)

# Preprocess data
books_df['Title'] = books_df['Title'].str.lower()
books_df['Genre'] = books_df['Genre'].str.lower()
books_df['Author'] = books_df['Author'].str.lower()
books_df['Description'] = books_df['Description'].str.lower()

# Create a dictionary and TF-IDF model
documents = [text.split() for text in books_df['Description']]
dictionary = Dictionary(documents)
corpus = [dictionary.doc2bow(doc) for doc in documents]
tfidf = TfidfModel(corpus)

# Compute document similarity
index = similarities.MatrixSimilarity(tfidf[corpus])

# Function to recommend books based on user preferences
import random

def recommend_books_by_genre(genre):
    genre = genre.lower()
    idx = books_df[books_df['Genre'] == genre].index
    if not idx.empty:
        sims = [index[tfidf[corpus[i]]] for i in idx]
        sims = [item for sublist in sims for item in sublist]  # Flatten the list of similarities
        if sims:
            sims = sorted(enumerate(sims), key=lambda item: -item[1])
            book_indices = [i[0] for i in sims]
            # Randomly select one book from the top 5 similar books
            random_book_index = random.choice(book_indices[:5])
            return books_df.iloc[random_book_index]
    return "No books found for the selected genre."

# Create Tkinter GUI
def recommend_books():
    selected_genre = genre_combobox.get()
    book_details = recommend_books_by_genre(selected_genre)
    if isinstance(book_details, pd.Series):
        title = "Title: " + book_details['Title']
        author = "Author: " + book_details['Author']
        description = "Description:\n" + book_details['Description']
        book_details_str = "\n".join([title, author, description])
        result_label.config(text=book_details_str)
    else:
        result_label.config(text=book_details)

root = tk.Tk()
root.title("Book Recommendation System")

# Label
label_genre = tk.Label(root, text="Select a genre:")
label_genre.pack(pady=5)

# Combobox for genre selection
genres = books_df['Genre'].unique().tolist()
genre_combobox = ttk.Combobox(root, values=genres, state="readonly")
genre_combobox.pack(pady=5)
genre_combobox.set(genres[0])  # Default selection

# Recommend button
recommend_button = tk.Button(root, text="Recommend Book", command=recommend_books)
recommend_button.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()


# In[ ]:




