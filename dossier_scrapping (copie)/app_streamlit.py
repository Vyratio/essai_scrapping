import streamlit as st
from pymongo import MongoClient
import pymongo
# Connect to the MongoDB server

cluster = "mongodb://localhost:27017/"
client = MongoClient(cluster)
db_scrapping = client.Top_250_film.Donnee_film
st.subheader("Bonjour , je suis Omar :wave")
st.title("Voici la réponse à la question n°1: Quelle est le film le plus long ?")
#Question n°1

db_question_1 = db_scrapping
my_collection_reponse_question_1 ={}
for i in db_question_1.find():
    duree_sauvegarde=0 
    duree = i["Duree"].split(",")
#    print(duree)
    if len(duree)== 2:
        if duree[1]=="h":
            duree_sauvegarde=int(duree[0])*60
        if duree[1]=="min":
            duree_sauvegarde=int(duree[0])
    else:
        duree_sauvegarde=int(duree[0])*60+int(duree[3])    

    my_collection_reponse_question_1[i["Nom du film"]] = str(duree_sauvegarde)

db2 = client.test_pymongo_reponse_3.test_film
for i in my_collection_reponse_question_1.items():
    db2.insert_one({i[0] : int(i[1])})
#Je récupère une base de données 
film_le_plus_long = db2.find().sort("Duree",pymongo.DESCENDING).limit(1)

st.write(film_le_plus_long[0])

st.title("Voici la réponse à la question n°2: Quels sont les 5 films les mieux notés ?")
#Question n°2
db_question_2 = db_scrapping
collection_reponse_question_2 = {}
for i in db_question_2.find():
    my_collection_reponse_question_1[i["Nom du film"]] = i["Score"]

db_insert = client.test_pymongo_reponse_3.reponse_2
for i in my_collection_reponse_question_1.items():
    db_insert.insert_one({i[0] : i[1]})
#Je récupère une base de données 

db_insert.find().sort("Score",pymongo.DESCENDING).limit(5)
for i in range(0,5):
    st.write(db_insert.find().sort("Score",pymongo.DESCENDING).limit(5)[i])



st.title("Voici la réponse à la question n°3: Dans combien de films a joué Morgan Freeman ? Tom Cruise ?")
#Question n°3
doc_reponse = client.test_pymongo.test_film

db_question_3 = db_scrapping
compteur_morgan_freeman = 0
compteur_tom_cruise = 0

for i in db_question_3.find():
    liste_acteur=i["Acteur"].split(",")
#    print(liste_acteur)
    for j in liste_acteur:
        if j== "Morgan Freeman":

            compteur_morgan_freeman = compteur_morgan_freeman + 1
        if j== "Tom Cruise":
            compteur_tom_cruise = compteur_tom_cruise +1


st.write(compteur_tom_cruise)
st.write(compteur_morgan_freeman)


st.title("Voici la réponse à la question n°4: Quels sont les 3 meilleurs films d’horreur ? Dramatique ? Comique ?")
#Question n°4
db_question_4 = db_scrapping
db_insert_question_4_comedy = client.test_pymongo_reponse_3.reponse_4_comedy
db_insert_question_4_horror = client.test_pymongo_reponse_3.reponse_4_horror
db_insert_question_4_drama = client.test_pymongo_reponse_3.reponse_4_drama

my_collection_reponse_question_4_horror ={}
my_collection_reponse_question_4_drama ={}
my_collection_reponse_question_4_comedy ={}
for i in db_question_4.find():
    liste_genre=i["Genre"].split(",")
    for j in liste_genre:
        if j == "Horror":
            my_collection_reponse_question_4_horror[i["Nom du film"]] = i["Score"] 
        if j == "Drama":
            my_collection_reponse_question_4_drama[i["Nom du film"]] = i["Score"]  
        if j=="Comedy":
            my_collection_reponse_question_4_comedy[i["Nom du film"]] = i["Score"] 

for i in my_collection_reponse_question_4_comedy.items():
    db_insert_question_4_comedy.insert_one({i[0] : i[1]})

for i in my_collection_reponse_question_4_horror.items():
    db_insert_question_4_horror.insert_one({i[0] : i[1]})

for i in my_collection_reponse_question_4_drama.items():
    db_insert_question_4_drama.insert_one({i[0] : i[1]})

for i in range(0,3):
    st.write(db_insert_question_4_comedy.find().sort("Score",pymongo.DESCENDING).limit(3)[i])

for i in range(0,3):
    st.write(db_insert_question_4_horror.find().sort("Score",pymongo.DESCENDING).limit(3)[i])

for i in range(0,3):
    st.write(db_insert_question_4_drama.find().sort("Score",pymongo.DESCENDING).limit(3)[i])


st.title("Voici la réponse à la question n°5: Parmi les 100 films les mieux notés, quel pourcentage sont américains ? Français ?")
#Question n°5
db_question_5 = db_scrapping

compteur_americain =0
compteur_francais =0
for i in range(0,100):
    if db_question_5.find().sort("Score",pymongo.DESCENDING).limit(100)[i]["Pays"]=="United States":
        compteur_americain =compteur_americain + 1
    if db_question_5.find().sort("Score",pymongo.DESCENDING).limit(100)[i]["Pays"]== "France":
        compteur_francais = compteur_francais + 1

st.write(compteur_americain)
st.write(compteur_francais)


def moyenne(liste): 
  somme = 0
  for i in liste: 
    somme += i 
  return somme / len(liste) 


st.title("Voici la réponse à la question n°6: Quel est la durée moyenne d’un film en fonction du genre ?")
#Question n°6
db_question_6 = db_scrapping
liste_genre_total = []
for i in db_question_6.find():
    for j in i["Genre"].split(","):
        liste_genre_total.append(j)

liste_genre_unique=[]
liste_genre_unique =set(liste_genre_total)
liste_genre_film =[]
my_collection_reponse_question_6 ={}
for i in db_question_6.find():
    duree_sauvegarde=0 
    duree = i["Duree"].split(",")
#    print(duree)
    if len(duree)== 2:
        if duree[1]=="h":
            duree_sauvegarde=int(duree[0])*60
        if duree[1]=="min":
            duree_sauvegarde=int(duree[0])
    else:
        duree_sauvegarde=int(duree[0])*60+int(duree[3])    

    liste_genre_film = i["Genre"].split(",")
    for j in i["Genre"].split(","):
        my_collection_reponse_question_6[j]=int(duree_sauvegarde)

collection_des_moyennes={}
somme_duree =0
nombre_film=0
moyenne = 0
for i in liste_genre_unique:
    for key, value in my_collection_reponse_question_6.items():
        if key==i:
            somme_duree = somme_duree +value
            nombre_film = nombre_film +1
    moyenne=somme_duree/nombre_film
    collection_des_moyennes[i]=moyenne
    somme_duree =0
    nombre_film=0
    moyenne = 0
st.write(collection_des_moyennes)