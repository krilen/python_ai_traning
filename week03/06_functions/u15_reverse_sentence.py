sentence = "De flesta väggarna i båda rummen var klädda med bokhyllor och arkivskåp."
sentence_reversed = " ".join(sentence[:-1].split(" ")[::-1]) +"."

print(f"{sentence=}")
print(f"{sentence_reversed=}")