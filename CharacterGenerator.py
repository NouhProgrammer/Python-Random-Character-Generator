class Generator:
    def generate(self, nr_chars, nr_numbers, nr_symbols):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        
        list_char = [random.choice(letters)]
        while len(list_char) < (nr_chars-nr_numbers-nr_symbols):
          list_char.append(random.choice(letters))
        while len(list_char) < (nr_chars-nr_numbers):
          list_char.append(random.choice(numbers))
        while len(list_char) < (nr_chars):
          list_char.append(random.choice(symbols))

        random.shuffle(list_char)
        character = ''.join(list_char)
        return character
