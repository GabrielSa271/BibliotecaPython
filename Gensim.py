import gensim
from gensim import corpora

# Cria um conjunto de documentos de exemplo
documents = ["A great day for fishing",
             "I went fishing today",
             "The fishing was good today",
             "We caught many fish"]

# Remove palavras comuns e aplica a tokenização
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]

# Cria um dicionário a partir dos documentos
dictionary = corpora.Dictionary(texts)

# Cria uma representação do corpus em formato Bag-of-Words
corpus = [dictionary.doc2bow(text) for text in texts]

# Cria um modelo de tópicos a partir do corpus
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                            id2word=dictionary,
                                            num_topics=2)

# Exibe os tópicos do modelo
for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))

