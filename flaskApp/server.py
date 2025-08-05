import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DB_CONFIG = {
    "host": "aws-0-eu-north-1.pooler.supabase.com",
    "port": "5432",
    "database": "postgres",
    "user": "postgres.wtfcaacrrcjzhhtnphlf",
    "password": "mimi2004."
}

def get_db_connection():
    conn = psycopg2.connect(
        dsn=os.environ.get("postgresql://postgres.wtfcaacrrcjzhhtnphlf:mimi2004.@aws-0-eu-north-1.pooler.supabase.com:5432/postgres"),
        cursor_factory=RealDictCursor
    )
    return conn

@app.route("/api/resultats", methods=["GET"])
def get_resultats():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM resultats;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def root():
    return render_template('root.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/resume2')
def resume2():
    return render_template('resume2.html')

@app.route('/resume3')
def resume3():
    return render_template('resume3.html')

@app.route('/api/annee_sexe_moy')
def get_annee_sexe_moy():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT annee, sexe, AVG(moyenne) AS moy 
            FROM resultats 
            GROUP BY sexe, annee
            ORDER BY annee, sexe;
        """)
        data = cur.fetchall()
        row_headers = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()
        json_annee_sexe_moy = [dict(zip(row_headers, row)) for row in data]
        return jsonify(json_annee_sexe_moy)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/annee_etudient')
def get_annee_etudient():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT annee, COUNT(matricule) AS nombre 
            FROM resultats 
            GROUP BY annee
            ORDER BY annee;
        """)
        data = cur.fetchall()
        row_headers = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()
        json_annee_etudient = [dict(zip(row_headers, row)) for row in data]
        return jsonify(json_annee_etudient)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/annee_spec_etudient3')
def get_annee_spec_etudient3():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT annee, COUNT(matricule) AS nombre 
            FROM resultats 
            WHERE specialite IN ('SPECIALITE_1', 'SPECIALITE_2', 'SPECIALITE_3') 
            GROUP BY specialite, annee
            ORDER BY annee;
        """)
        data = cur.fetchall()
        row_headers = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()
        json_annee_spec_etudient3 = [dict(zip(row_headers, row)) for row in data]
        return jsonify(json_annee_spec_etudient3)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/spec_etudient')
def get_spec_etudient():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT specialite, COUNT(*) AS nombre 
            FROM resultats 
            GROUP BY specialite
            ORDER BY specialite;
        """)
        data = cur.fetchall()
        row_headers = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()
        json_spec_etudient = [dict(zip(row_headers, row)) for row in data]
        return jsonify(json_spec_etudient)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/moy_annee')
def getMoyAnne():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""select annee, avg(moyenne) as avgMoyAnnee from resultats group by annee;""")
    data = cursor.fetchall()
    row_headers = [desc[0] for desc in cursor.description]
    cursor.close()
    json_moy_annee=[]
    for result in data:
        json_moy_annee.append(dict(zip(row_headers, result)))
    return jsonify(json_moy_annee)

@app.route('/api/moy_spec')
def getMoySpec():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""select specialite, avg(moyenne) as avgMoySpec from resultats group by specialite;""")
    data = cursor.fetchall()
    row_headers = [desc[0] for desc in cursor.description]
    cursor.close()
    json_moy_spec=[]
    for result in data:
        json_moy_spec.append(dict(zip(row_headers, result)))
    return jsonify(json_moy_spec)

@app.route('/api/annee_spec_etudient')
def getAnnenSpecEtudient():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""select specialite, annee, count(matricule) as nombre from resultats group by specialite, annee order by annee, specialite;""")
    data = cursor.fetchall()
    row_headers = [desc[0] for desc in cursor.description]
    cursor.close()
    json_annee_spec_etudient=[]
    for result in data:
        json_annee_spec_etudient.append(dict(zip(row_headers, result)))
    return jsonify(json_annee_spec_etudient)

@app.route('/api/annee_sexe_etudient')
def getAnnenSexeEtudient():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""select annee, count(matricule) as nombre from resultats group by sexe, annee;""")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_annee_sexe_etudient=[]
    for result in data:
        json_annee_sexe_etudient.append(dict(zip(row_headers, result)))
    return jsonify(json_annee_sexe_etudient)

@app.route('/api/etudient_Spec_2021')
def getEtudientSpec2021():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""select count(matricule) as nombre from resultats where annee=2021 group by specialite order by specialite;""")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_etudient_Spec_2021=[]
    for result in data:
        json_etudient_Spec_2021.append(dict(zip(row_headers, result)))
    return jsonify(json_etudient_Spec_2021)

@app.route('/api/etudient_admis_Spec_2021')
def getEtudientAdmisSpec2021():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""select specialite, count(matricule) as nombre from resultats where moyenne>=10 and annee=2021 group by specialite order by specialite;""")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_etudient_admis_Spec_2021=[]
    for result in data:
        json_etudient_admis_Spec_2021.append(dict(zip(row_headers, result)))
    return jsonify(json_etudient_admis_Spec_2021)

@app.route('/chercher')
def chercher():
    return render_template('chercher.html')

@app.route('/api/etudients_recherchees', methods=['GET'])
def rechercher():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        nompre = request.args.get('nompre', "").strip()
        sexe = request.args.get('sexe', "none")
        specialite = request.args.get('specialite', "none")
        annee = request.args.get('annee', "none")

        base_query = "SELECT * FROM resultats"
        conditions = []
        parameters = []

        if nompre:
            keywords = nompre.split()
            name_conditions = []
            for word in keywords:
                name_conditions.append("(nom ILIKE %s OR prenom ILIKE %s)")
                parameters.extend([f"%{word}%", f"%{word}%"])
            conditions.append("(" + " OR ".join(name_conditions) + ")")

        if sexe != "none":
            conditions.append("sexe = %s")
            parameters.append(sexe)
        if specialite != "none":
            conditions.append("specialite = %s")
            parameters.append(specialite)
        if annee != "none":
            conditions.append("annee = %s")
            parameters.append(annee)

        if conditions:
            base_query += " WHERE " + " AND ".join(conditions)

        base_query += ";"

        cursor.execute(base_query, tuple(parameters))
        data = cursor.fetchall()
        row_headers = [x[0] for x in cursor.description]
        cursor.close()
        conn.close()

        json_result = [dict(zip(row_headers, row)) for row in data]
        return jsonify(json_result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/details')
def details():
    return render_template('details.html')

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")