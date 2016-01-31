import pickle

import numpy as np
from keras.preprocessing import sequence
from keras.callbacks import EarlyStopping

from deep_learning_models import cnn_lstm


# from deep_learning_models import b_rnn

def load_pickle(filename):
    out = pickle.load(open(filename, "rb"))
    return out


maxlen = 32

filename_data, filename_w = './tmp/indexed_data.p', './tmp/Weight.p'
data = load_pickle(filename_data)
W = load_pickle(filename_w)
test = load_pickle('./tmp/test_data.p')

vocabulary_size, dims = W.shape
print("Vocabulary_size, dims = %s, %s." % W.shape)

X_train, X_valid, X_test, Y_train, Y_dev, Y_test = data
print(len(X_train), ' train sequences')
print(len(X_valid), ' valid sequences')
print(len(X_test), ' test sequences')

print("Pad sequences (samples x time)")
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
X_valid = sequence.pad_sequences(X_valid, maxlen=maxlen)
submit_test = sequence.pad_sequences(test[2], maxlen=maxlen)

print('X_train shape:', X_train.shape)
print('X_valid shape:', X_valid.shape)
print('X_test shape:', X_test.shape)

# Convert the sentiment scores from [-2, 2] to [0, 1]
Y_train = (np.array(Y_train) + 2) / 4
Y_dev = (np.array(Y_dev) + 2) / 4
Y_test = (np.array(Y_test) + 2) / 4

batch_size = 8
nb_epoch = 10
model = cnn_lstm(W)

model.compile(loss='rmse', optimizer='adagrad')  # loss function: mse
print("Train...")
early_stopping = EarlyStopping(monitor='val_loss', patience=5)
result = model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch, validation_data=(X_valid, Y_dev),
                   callbacks=[early_stopping])

score = model.evaluate(X_test, Y_test, batch_size=batch_size)
print('Test score:', score)

# experiment evaluated by multiple metrics
predict = model.predict(X_test, batch_size=batch_size).reshape((1, len(X_test)))[0]
print('Y_test: %s' % str(Y_test))
print('Predict value: %s' % str(predict))

submit_predict = model.predict(submit_test, batch_size=batch_size).reshape((1, len(submit_test)))[0]

pickle.dump((test, submit_predict), open("./tmp/submit.p", 'wb'))

print("Saving model and weights...")
json_string = model.to_json()
open('./tmp/keras_model_architecture.json', 'w').write(json_string)
model.save_weights('./tmp/keras_model_weights.h5', overwrite=True)
print("Model saved.")

from metrics import continuous_metrics

continuous_metrics(Y_test, predict, 'prediction result:')

# visualization
from visualize import draw_linear_regression

X = range(50, 100)  # or range(len(y_test))
draw_linear_regression(X, np.array(Y_test)[X], np.array(predict)[X], 'Sentence Number', "Sentiment scores",
                       'Comparison of predicted and true scores')

from visualize import plot_keras, draw_hist

plot_keras(result, x_labels='Epoch', y_labels='MAE Loss')
draw_hist(np.array(Y_test) - np.array(predict), title='Histogram of sentiment scores prediction: ')
