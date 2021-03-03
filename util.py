import numpy as np
import time
import os
import cv2

def capture_device():
    print('Camera going to take input in 5 sec')
    print('Press q to quit')
    time.sleep(5)
    capture = cv2.VideoCapture(0)

    frames = list()
    while True:
        ret , frame = capture.read()
        cv2.imshow('image',frame)
        frames.append(frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()
    return frames
def get_label_frame():
    no_of_labels = int(input('How many labels do you need?'))
    label_frame = list()
    for i in range(no_of_labels):
        label = input('Enter the label {}>'.format(i))
        label_frame.append((label,capture_device()))
    return label_frame
def create_directory_structure(label_frame):
    try:
        if os.path.isdir('data'):
            os.rmdir('data')
        os.mkdir('data')
    except:
        print('There was some error')
    for label , frames in label_frame:
        os.mkdir(os.path.join('data',label))
        write_data(os.path.join('data',label),frames)
def write_data(path,frames):
    for index in range(len(frames)):
        result = cv2.imwrite(str(os.path.join(path,str(index))) + '.png',frames[index])
        if not result:
            print('One image was not sucessfully written')

def preprocess_frame(frame):
    new_frame = cv2.resize(frame,(32,32))
    new_frame.resize((1,32,32,3))
    return new_frame
def predict(model):
    capture = cv2.VideoCapture(0)
    while True:
        ret , frame = capture.read()
        cv2.imshow('image',frame)
        print(model.predict_classes(preprocess_frame(frame)))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def main():
    label_frame = get_label_frame()
    cireate_directory_structure(label_frame)
