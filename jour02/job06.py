import mysql.connector

connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="140470Bu!",
            database="LaPlateforme"
)

curseur = connexion.cursor()
curseur.execute("SELECT SUM(capacite) FROM salle")
resultat = curseur.fetchone()

print(f"La capacité total des salles est de : {resultat[0]}")

