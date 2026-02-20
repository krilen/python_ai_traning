namn = input("Skriv in ditt namn: ")
lista_av_namnet = list(namn)
langden_på_listan = len(lista_av_namnet)
halva = langden_på_listan//2
print(lista_av_namnet[:halva])
print(lista_av_namnet[0])
print(lista_av_namnet[-1])