import re
def opening(t):
    with open(t,encoding="UTF-8") as f:
        r = f.readlines()
    return r

def count(text):
    i=0
    for line in text:
        i
        i+=1
    f1 = open("text_1.txt", "w", encoding="UTF-8")
    f2 = f1.write(str(i))
    f1.close()
    return f2
    

def main():
    count(opening("C://Users//student//Desktop//text.xml"))


if __name__ == "__main__":
    main()
