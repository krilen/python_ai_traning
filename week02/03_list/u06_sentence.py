while True:
    sentence = input("Please write me a correct sentence >> ")
    
    if len(sentence) > 0:
        break

sentence_words = sentence.split(" ")

print(f"The number of words in the sentence was: {len(sentence_words)}.")
print(f"Did the sentence begin with a capital letter? - {"Yes it did" if sentence[0].isupper() else "No it did not"}.")
print(f"Did the sentence end with a dot? - {"Yes it did" if sentence[-1] == "." else "No it did not"}.")