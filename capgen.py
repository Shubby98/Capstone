import numpy as np
import pickle
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.applications.resnet50 import ResNet50
from keras.models import Model
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input

dpath = "../"
max_len = 32

def load_mymodel():
    model = load_model(dpath + 'Capstone/model/model_10.h5')
    return model

def load_vocab():
    f = open(dpath + "Capstone/saved/idx_to_word.pkl", "rb")
    idx_to_word = pickle.load(f)
    f.close()

    f = open(dpath + "Capstone/saved/word_to_idx.pkl", "rb")
    word_to_idx = pickle.load(f)
    f.close()

    vocab_size = len(word_to_idx) + 1

    return idx_to_word , word_to_idx , vocab_size

def preprocess_img(img):
    img = image.load_img( img , target_size=(224 , 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img , axis = 0)
    #Normalisation
    img = preprocess_input(img)
    return img

def load_resnet():
    model = ResNet50(weights="imagenet", input_shape=(224, 224, 3))
    resnet = Model(model.input, model.layers[-2].output)
    return resnet

def encode_image(img , model):
    img = preprocess_img(img)
    feature_vector = model.predict(img)
    feature_vector = feature_vector.reshape((-1,))
    return feature_vector

def predict_caption(photo , word_to_idx , idx_to_word , model , resnet):
    img_vec = encode_image(photo , resnet)
    photo = img_vec.reshape((1, 2048))
    in_text = "startseq"
    for i in range(max_len):
        sequence = [word_to_idx[w] for w in in_text.split() if w in word_to_idx]
        sequence = pad_sequences([sequence], maxlen=max_len, padding='post')

        ypred = model.predict([photo, sequence])
        ypred = ypred.argmax()
        word = idx_to_word[ypred]
        in_text += (' ' + word)

        if word == "endseq":
            break

    final_caption = in_text.split()[1:-1]
    final_caption = ' '.join(final_caption)
    return final_caption


model = load_mymodel()
idx_to_word , word_to_idx , vocab_size = load_vocab()
resnet = load_resnet()
caption = predict_caption("test7.jpg", word_to_idx , idx_to_word , model , resnet)
print(caption)