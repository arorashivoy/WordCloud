# Word Count NLP Project
# For learning NLP
#
# Tutorial - https://towardsdatascience.com/3-super-simple-projects-to-learn-natural-language-processing-using-python-8ef74c757cd9

import pandas as pd
import regex as re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Creating data frame
df = pd.read_csv('emails.csv')

# Removing spam
print("Spam count:", len(df.loc[df['spam'] == 1]))
print("Not spam count:", len(df.loc[df['spam'] == 0]))

df["spam"] = df["spam"].astype(int)

df = df.drop_duplicates()
df = df.reset_index(inplace=False)[['text', 'spam']]

# Using Regex to clean the data
clean_desc = []
for i in range(len(df["text"])):
    desc = df["text"][i].lower()

    # removing punctuation
    desc = re.sub('[^a-zA-Z]', ' ', desc)

    # removing tags
    desc = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", desc)

    # remove digits and special chars
    desc = re.sub("(\d|\W)+", " ", desc)

    clean_desc.append(desc)

df["text"] = clean_desc

# Removing stop words
stopWords = ['is', 'you', 'your', 'and', 'the', 'to', 'from', 'or', 'I', 'for', 'do', 'get', 'not', 'here', 'in',
             'im', 'have', 'on', 're', 'new', 'subject', "a", "am", "pm", "ect", "kaminski", "of", "will", "be", "it", "all"]

cloud = WordCloud(width=800, height=800, background_color="black", stopwords=stopWords,
                  max_words=1000, min_font_size=20).generate(" ".join(df["text"]))

# plot the wordCloud
fig = plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(cloud)
plt.axis("off")
plt.show()
