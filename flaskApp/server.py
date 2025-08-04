from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_PASSWORD'] = 'mimi2004.'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'db_university'

mysql.init_app(app)

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
def getAnnenSexeMoy():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select annee, avg(moyenne) as moy from resultats group by sexe, annee;")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_annee_sexe_moy=[]
    for result in data:
        json_annee_sexe_moy.append(dict(zip(row_headers, result)))
    return jsonify(json_annee_sexe_moy)

@app.route('/api/annee_etudient')
def getAnnenEtudient():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select annee, count(matricule) as nombre from resultats group by annee;")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_annee_etudient=[]
    for result in data:
        json_annee_etudient.append(dict(zip(row_headers, result)))
    return jsonify(json_annee_etudient)

@app.route('/api/annee_spec_etudient3')
def getAnnenSpecEtudient3():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select annee, count(matricule) as nombre from resultats where specialite='SPECIALITE_1' or specialite='SPECIALITE_2' or specialite='SPECIALITE_3' group by specialite, annee;")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_annee_spec_etudient3=[]
    for result in data:
        json_annee_spec_etudient3.append(dict(zip(row_headers, result)))
    return jsonify(json_annee_spec_etudient3)

@app.route('/api/spec_etudient')
def getSpecEtudient2021():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select specialite, count(*) as nombre from resultats group by specialite;")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_spec_etudient=[]
    for result in data:
        json_spec_etudient.append(dict(zip(row_headers, result)))
    return jsonify(json_spec_etudient)

@app.route('/api/moy_annee')
def getMoyAnne():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select annee, avg(moyenne) as avgMoyAnnee from resultats group by annee;")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_moy_annee=[]
    for result in data:
        json_moy_annee.append(dict(zip(row_headers, result)))
    return jsonify(json_moy_annee)

@app.route('/api/moy_spec')
def getMoySpec():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select specialite, avg(moyenne) as avgMoySpec from resultats group by specialite;")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_moy_spec=[]
    for result in data:
        json_moy_spec.append(dict(zip(row_headers, result)))
    return jsonify(json_moy_spec)

@app.route('/api/annee_spec_etudient')
def getAnnenSpecEtudient():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select specialite, annee, count(matricule) as nombre from resultats group by specialite, annee order by annee, specialite;")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_annee_spec_etudient=[]
    for result in data:
        json_annee_spec_etudient.append(dict(zip(row_headers, result)))
    return jsonify(json_annee_spec_etudient)

@app.route('/api/annee_sexe_etudient')
def getAnnenSexeEtudient():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select annee, count(matricule) as nombre from resultats group by sexe, annee;")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_annee_sexe_etudient=[]
    for result in data:
        json_annee_sexe_etudient.append(dict(zip(row_headers, result)))
    return jsonify(json_annee_sexe_etudient)

@app.route('/api/etudient_Spec_2021')
def getEtudientSpec2021():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select count(matricule) as nombre from resultats where annee=2021 group by specialite order by specialite;")
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_etudient_Spec_2021=[]
    for result in data:
        json_etudient_Spec_2021.append(dict(zip(row_headers, result)))
    return jsonify(json_etudient_Spec_2021)

@app.route('/api/etudient_admis_Spec_2021')
def getEtudientAdmisSpec2021():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select specialite, count(matricule) as nombre from resultats where moyenne>=10 and annee=2021 group by specialite order by specialite;")
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
    conn = mysql.connect()
    cursor = conn.cursor()
    nompre = request.args.get('nompre', "").strip()
    sexe = request.args.get('sexe', "none")
    specialite = request.args.get('specialite', "none")
    annee = request.args.get('annee', "none")
    if nompre:
        mySqlQuery = """
            SELECT *, MATCH(nom, prenom) AGAINST (%s IN NATURAL LANGUAGE MODE) AS relevance
            FROM resultats
        """
    else:
        mySqlQuery = "SELECT * FROM resultats"
    conditions = []
    parameters = []
    if nompre:
        conditions.append("MATCH(nom, prenom) AGAINST (%s IN NATURAL LANGUAGE MODE)")
        parameters.append(nompre)
        parameters.append(nompre)
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
        mySqlQuery += " WHERE " + " AND ".join(conditions)
    mySqlQuery += ";"
    cursor.execute(mySqlQuery, tuple(parameters))
    data = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    cursor.close()
    json_etudients_recherchees=[]
    for result in data:
        json_etudients_recherchees.append(dict(zip(row_headers, result)))
    return jsonify(json_etudients_recherchees)

@app.route('/details')
def details():
    return render_template('details.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)