def main():
    with open("input.txt", "r") as f:
        chars = f.readline()
        # Start after 4 characters because this is the earlist a start of message marker can occur
        n = 4
        # iterate through every other letter
        for i in range(0, len(chars)):
            chunk = []
            # each 4 letters gets turned into a list, then a set. If the sets len is 4 then each letter is different
            chunk = "".join([chars[i:i+4]])
            # return the nth character
            if len(set(chunk)) == 4:
                print(n)
                break
            n+=1
        
if __name__ == '__main__':
    main()