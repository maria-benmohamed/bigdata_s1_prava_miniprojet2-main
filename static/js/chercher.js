function rechercher() {
  nompre = document.querySelector('input[name="nompre"]').value;
  sexe = document.querySelector('select[name="sexe"]').value;
  const specialite = document.querySelector('select[name="specialite"]').value;
  const annee = document.querySelector('select[name="annee"]').value;
  const queryString = `nompre=${encodeURIComponent(
    nompre
  )}&sexe=${encodeURIComponent(sexe)}&specialite=${encodeURIComponent(
    specialite
  )}&annee=${encodeURIComponent(annee)}`;
  httpRequest1 = new XMLHttpRequest();
  httpRequest1.open("GET", `/api/etudients_recherchees?${queryString}`);
  httpRequest1.onreadystatechange = function () {
    if (httpRequest1.readyState === 4 && httpRequest1.status === 200) {
      jsonEtudientsRechercher = JSON.parse(httpRequest1.response);
      makeResutatsTable(jsonEtudientsRechercher);
    }
  };
  httpRequest1.send();
}
function makeResutatsTable(jsonEtudientsRechercher) {
  existingTable = document.getElementsByTagName("table")[0];
  if (existingTable) {
    existingTable.remove();
  }
  existingText = document.getElementsByTagName("p")[0];
  if (existingText) {
    existingText.remove();
  }
  main = document.getElementsByTagName("main")[0];
  console.log(jsonEtudientsRechercher.length);
  if (jsonEtudientsRechercher.length == 0) {
    let text = document.createElement("p");
    text.innerHTML = "<strong>aucun résultat n'a été trouvé</strong>";
    main.append(text);
  } else {
    table = document.createElement("table");
    table.setAttribute("border", 1);
    table.setAttribute("id", "result-table");
    let headRow = document.createElement("tr");
    headRow.setAttribute("id", "result-table-header");
    let matriculeH = document.createElement("th");
    matriculeH.innerText = "Matricule";
    let nomH = document.createElement("th");
    nomH.innerText = "Nom";
    let prenomH = document.createElement("th");
    prenomH.innerText = "Prenom";
    let sexeH = document.createElement("th");
    sexeH.innerText = "Sexe";
    let specialiteH = document.createElement("th");
    specialiteH.innerText = "Spécialité";
    let anneeH = document.createElement("th");
    anneeH.innerText = "Anneé";
    let moyenneH = document.createElement("th");
    moyenneH.innerText = "Moyenne";
    headRow.append(matriculeH);
    headRow.append(nomH);
    headRow.append(prenomH);
    headRow.append(sexeH);
    headRow.append(specialiteH);
    headRow.append(anneeH);
    headRow.append(moyenneH);
    table.append(headRow);
    for (let i = 0; i < jsonEtudientsRechercher.length; i++) {
      let row = document.createElement("tr");
      let matricule = document.createElement("td");
      matricule.innerText = jsonEtudientsRechercher[i].matricule;
      let nom = document.createElement("td");
      nom.innerText = jsonEtudientsRechercher[i].nom;
      let prenom = document.createElement("td");
      prenom.innerText = jsonEtudientsRechercher[i].prenom;
      let sexe = document.createElement("td");
      sexe.innerText = jsonEtudientsRechercher[i].sexe;
      let specialite = document.createElement("td");
      specialite.innerText = jsonEtudientsRechercher[i].specialite;
      let annee = document.createElement("td");
      annee.innerText = jsonEtudientsRechercher[i].annee;
      let moyenne = document.createElement("td");
      moyenne.innerText = jsonEtudientsRechercher[i].moyenne;
      row.append(matricule);
      row.append(nom);
      row.append(prenom);
      row.append(sexe);
      row.append(specialite);
      row.append(annee);
      row.append(moyenne);
      table.append(row);
    }
    main.append(table);
  }
}
