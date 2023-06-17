# question 1 to check if it has 7

def has_seven(k):
    if k <= 0:
        return False
    
    elif k % 10 == 7:
        return True
    
    else:
        return has_seven(k//10)

def main():
    print(has_seven(7))

if __name__ == "__main__":
    main()
