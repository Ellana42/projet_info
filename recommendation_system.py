import pandas as pd
#import nltk

data = pd.read_csv('movies_prepared.csv')

def recommend_best():
    return data.sort_values('weighted_rating',
                            ascending=False).head(10)['title']

def genre_proximity(movie1, movie2):
    genres1, genres2 = movie1.genres.iloc[0], movie2.genres
    common_genres = [genre for genre in genres1 if genre in genres2]
    return 2 * len(common_genres)/(len(genres1) + len(genres2))

def recommend_by_genre(movie_name):
    movie = data[data['title'] == movie_name]
    sub_data = data.drop(index=movie.index) 
    sub_data['proximity'] = sub_data.apply(lambda x: genre_proximity(movie, x), axis=1)
    sub_data.sort_values(['proximity', 'weighted_rating'], ascending=False, inplace=True)
    return sub_data.head(5)['title'].to_string(index=False)

# from sklearn.feature_extraction.text import TfidfVectorizer
# 
# indexed_data = pd.read_csv('indexed_data.csv')
# vect = TfidfVectorizer(min_df=1, stop_words='english')
# tfidf = vect.fit_transform(indexed_data.overview)
# pairwise_similarity = tfidf * tfidf.T
# 
# def overview_proximity(movie1, movie2):
    # index1, index2 = movie1.index, movie2.index
    # return pairwise_similarity[index1][index2]
# 
# def overview_recommend(movie_name):
    # vect = TfidfVectorizer(min_df=1, stop_words='english')
    # tfidf = vect.fit_transform(indexed_data.overview)
    # pairwise_similarity = tfidf * tfidf.T
    # movie_index = indexed_data[indexed_data.title == movie_name].index
    # indexed_data['overview_prox'] = pd.DataFrame(pairwise_similarity.toarray()[movie_index].T)
    # return indexed_data.sort_values(by='overview_prox', ascending=False).drop(index=movie_index).head(10).title.to_string(index=False)
# 
# from gensim.models.doc2vec import Doc2Vec, TaggedDocument
# 
# tokenized_overviews = data.overview.apply(nltk.word_tokenize)
# corpus = [TaggedDocument(doc, [i]) for i, doc in tokenized_overviews.iteritems()]
# model2 = Doc2Vec(corpus, vector_size=100, window=5, min_count=3, workers=4, epochs=10)
# 
# def overview_recommend2(movie_name):
    # movie_index = data[data.title == movie_name].index
    # most_similar = model2.docvecs.most_similar(movie_index)
    # recommended = pd.Series([data.loc[movie[0]].title for movie in
                             # most_similar])
    # return recommended.to_string(index=False)
# 
# from scipy import spatial
# 
# def similarity(movie1, movie2):
    # director_sim = spatial.distance.cosine(movie1.director_bin, movie2.director_bin)
    # genre_sim = spatial.distance.cosine(movie1.genres_bin, movie2.genres_bin)
    # keyword_sim = spatial.distance.cosine(movie1.keywords_bin, movie2.keywords_bin)
    # return director_sim + genre_sim + keyword_sim
# 
# def similarity_recommend(movie_name):
    # movie = data[data['title'] == movie_name]
    # sub_data = data.drop(index=movie.index) 
    # sub_data['similarity'] = sub_data.apply(lambda x: similarity(movie.iloc[0], x), axis=1)
    # sub_data.sort_values(['similarity', 'weighted_rating'], ascending=[True, False], inplace=True)
    # return sub_data.head(5)['title'].to_string(index=False)
