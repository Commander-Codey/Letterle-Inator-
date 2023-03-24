import threading
import shuffler
import letterle


def run_letterle():
    letterle.play_letterle()

def run_shuffler():
    shuffler.shuffle_enable()

if __name__ == "__main__":
    t1 = threading.Thread(target=run_shuffler)
    t2 = threading.Thread(target=run_letterle)

    t1.start()
    
    t2.start()

    t1.join()
    t2.join()
