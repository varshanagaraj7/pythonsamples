class stringreverser:
    def reversemethod(self,sentence):
        words=sentence.split()
        words=words[::-1]
        return''.join(words)
reverser=stringreverser()
s=input("enter the string:")
result=reverser.reversemethod(s)
print(result)
