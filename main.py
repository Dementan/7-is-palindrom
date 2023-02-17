# is a word or phrase a palindrom?

text = input("Enter the word or phrase you want to check: ")
print(text)
text_glued = text.replace(" ", "")  # if it is a phrase and it contains spaces - they need to be removed
print(text_glued)
text_glued_vice_versa = text_glued[::-1]  #flip using indexes
print(text_glued_vice_versa)
if text_glued == text_glued_vice_versa:
        print("it is a palindrom")
else:
        print("it is not a palindrom")