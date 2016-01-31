from __future__ import print_function
import numpy as np

np.random.seed(1337)  # for reproducibility

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.embeddings import Embedding
from keras.layers.convolutional import Convolution1D, MaxPooling1D
from keras.layers.recurrent import LSTM, GRU
from keras.models import Graph
from recurrent import Bidirectional
######################### settings ###########################

max_features = 200  # vocabulary size
embedding_dims = 128  # dimension of word embedding
maxlen = 140  # max length of a sentence


##############################################################


def cnn(W):
    nb_filter = 250
    filter_length = 3
    hidden_dims = 250

    model = Sequential()

    # we start off with an efficient embedding layer which maps
    # our vocab indices into embedding_dims dimensions
    model.add(Embedding(W.shape[0], W.shape[1], input_length=maxlen, weights=None))
    model.add(Dropout(0.25))

    # we add a Convolution1D, which will learn nb_filter
    # word group filters of size filter_length:
    model.add(Convolution1D(nb_filter=nb_filter,
                            filter_length=filter_length,
                            border_mode='valid',
                            activation='relu',
                            subsample_length=1))
    # we use standard max pooling (halving the output of the previous layer):
    model.add(MaxPooling1D(pool_length=2))

    # We flatten the output of the conv layer,
    # so that we can add a vanilla dense layer:
    model.add(Flatten())

    # We add a vanilla hidden layer:
    model.add(Dense(hidden_dims))
    model.add(Dropout(0.25))
    model.add(Activation('relu'))

    # We project onto a single unit output layer, and squash it with a sigmoid:
    model.add(Dense(1))
    model.add(Activation('linear'))

    return model


def lstm(W):
    model = Sequential()
    model.add(Embedding(W.shape[0], W.shape[1], input_length=maxlen))
    model.add(LSTM(128))  # try using a GRU instead, for fun
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    return model


def gru(W):
    model = Sequential()
    model.add(Embedding(W.shape[0], W.shape[1], input_length=maxlen))
    model.add(GRU(128))  # GRU
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    return model


def bidirectional_lstm():
    model = Graph()
    model.add_input(name='input', input_shape=(maxlen,), dtype=int)
    model.add_node(Embedding(max_features, 128, input_length=maxlen),
                   name='embedding', input='input')
    model.add_node(LSTM(64), name='forward', input='embedding')
    model.add_node(LSTM(64, go_backwards=True), name='backward', input='embedding')
    model.add_node(Dropout(0.5), name='dropout', inputs=['forward', 'backward'])
    model.add_node(Dense(1, activation='sigmoid'), name='sigmoid', input='dropout')
    model.add_output(name='output', input='sigmoid')

    return model


def cnn_lstm(W):
    nb_filter = 64
    filter_length = 3
    pool_length = 2
    lstm_output_size = 70

    model = Sequential()
    model.add(Embedding(W.shape[0], W.shape[1], input_length=maxlen))
    model.add(Dropout(0.25))
    model.add(Convolution1D(nb_filter=nb_filter,
                            filter_length=filter_length,
                            border_mode='valid',
                            activation='relu',
                            subsample_length=1))
    model.add(MaxPooling1D(pool_length=pool_length))
    model.add(LSTM(lstm_output_size))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    return model


def cnn_gru(W):
    nb_filter = 64
    filter_length = 3
    pool_length = 2
    lstm_output_size = 70

    model = Sequential()
    model.add(Embedding(W.shape[0], W.shape[1], input_length=maxlen))
    model.add(Dropout(0.25))
    model.add(Convolution1D(nb_filter=nb_filter,
                            filter_length=filter_length,
                            border_mode='valid',
                            activation='relu',
                            subsample_length=1))
    model.add(MaxPooling1D(pool_length=pool_length))
    model.add(GRU(lstm_output_size))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    return model


def b_rnn(W):
    lstm = LSTM(output_dim=70)
    gru = GRU(output_dim=70)
    brnn = Bidirectional(forward=lstm, backward=gru)

    nb_filter = 64
    filter_length = 3
    pool_length = 2
    lstm_output_size = 70

    model = Sequential()
    model.add(Embedding(W.shape[0], W.shape[1], input_length=maxlen))
    model.add(Dropout(0.25))
    model.add(Convolution1D(nb_filter=nb_filter,
                            filter_length=filter_length,
                            border_mode='valid',
                            activation='relu',
                            subsample_length=1))
    model.add(MaxPooling1D(pool_length=pool_length))
    model.add(brnn)
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    return model

if __name__ == "__main__":
    pass
