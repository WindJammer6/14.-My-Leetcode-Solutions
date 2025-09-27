class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        if strs == [""]:
            return ""

        plain_text = ""
        
        for str in strs:
            for char in str:
                ascii_value = ord(char)
                plain_text += f"{ascii_value}"
                plain_text += " "
            plain_text += "|"

        print(plain_text)

        return plain_text 

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        if s == "":
            return [""]

        list = []
        words = s.split("|")
        print(words)
        
        for i in range(len(words) - 1):
            word = words[i].split(" ")
            list.append("placeholder")

        for i in range(len(words) - 1):
            string = ""
            word = words[i].split(" ")

            for j in range(len(word) - 1):
                print(word[j])
                print(chr(int(word[j])))
                string += chr(int(word[j]))
            
            list[i] = string
            string = ""

        return list



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

codec = Codec()
print(codec.decode(codec.encode(["Hello", "World"])))       # ["Hello", "World"]   
print(codec.decode(codec.encode([""])))                     # [""]   