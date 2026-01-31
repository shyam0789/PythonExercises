
def square_of_odd():
    num = 10
    print(__name__)
    if __name__ == "__main__":
        for i in range(1,num+1):
            if i%2 == 0:
                continue
            else:
                print(i*i)


square_of_odd()