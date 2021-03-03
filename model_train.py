import tensorflow as tf
from tensorflow import keras
from util import predict
import keras_preprocessing
# from keras_proprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image_dataset_from_directory


def get_data():
    train_data = image_dataset_from_directory('data',image_size=(32,32),seed=123,subset="training",validation_split=0.3)
    test_data = image_dataset_from_directory('data',image_size=(32,32),seed=123,subset="validation",validation_split=0.3)
    return train_data , test_data
def main(no_of_label):
    train_data , test_data = get_data()
    model = keras.Sequential([
        keras.layers.Conv2D(32,3,activation="relu"),
        keras.layers.MaxPool2D(),
        keras.layers.Conv2D(32,3,activation="relu"),
        keras.layers.MaxPool2D(),
        keras.layers.Conv2D(32,3,activation="relu"),
        keras.layers.MaxPool2D(),
        keras.layers.Flatten(),
        keras.layers.Dense(200,activation="relu"),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(128,activation="relu"),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(no_of_label,activation="sigmoid")
        ])
    model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=['accuracy'])
    model.fit(train_data,validation_data = test_data,epochs=20)
    predict(model)

