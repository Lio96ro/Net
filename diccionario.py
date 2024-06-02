meme_dict = {
    "LOL": "Una respuesta a algo gracioso",
    "CRINGE": "Algo raro o embarazoso",
    "ROFL": "Respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado"
}
while True:
    word = input("Escribe una palabra que no entiendas")

    if word in meme_dict.keys():
        print("Es ",meme_dict[word])
    else:
        print("Esa palabra no está en el diccionario")
        
    print("")
