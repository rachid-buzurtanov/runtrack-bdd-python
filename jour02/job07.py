import mysql.connector

def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="140470Bu!",
        database="lethalcompany"
    )

def employeriche(conn):
    query = "SELECT * FROM employe WHERE salaire > %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (3000,))
        for employe in cursor.fetchall():
            print(employe)

def employeservice(conn):
    query = """
    SELECT e.nom, e.prenom, s.nom AS service_name
    FROM employe e
    INNER JOIN service s ON e.id_service = s.id
    """
    with conn.cursor() as cursor:
        cursor.execute(query)
        for employe in cursor.fetchall():
            print(employe)

# Connexion à la base de données
with connection() as conn:
    # Exécution des opérations
    print("Employé avec un salaire plus de 3000:")
    employeriche(conn)

    print("\nEmployés et leur service:")
    employeservice(conn)
