import mysql.connector

def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="$@fiya17",
        database="placement_db"
    )

def save_prediction(
    age,
    gender,
    cgpa,
    branch,
    prediction,
    probability
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO student_predictions
    (
        age,
        gender,
        cgpa,
        branch,
        prediction,
        probability
    )
    VALUES
    (%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            age,
            gender,
            cgpa,
            branch,
            prediction,
            probability
        )
    )

    conn.commit()

    cursor.close()

    conn.close()