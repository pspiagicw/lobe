import util
import model_train
def main():
    no_of_label = util.main()
    model_train.main(no_of_label)
if __name__ == '__main__':
    main()
