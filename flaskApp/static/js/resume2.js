updateCharts();
const myColors = [
  "#c29200",
  "#4a8adf",
  "#ff76b6",
  "#ffe083",
  "#0a52be",
  "#ffc107",
  "#B2A1D8",
  "#F1F1F1",
  "#E3D2B9",
];
function updateCharts() {
  httpRequest1 = new XMLHttpRequest();
  httpRequest1.open("GET", "/api/moy_annee");
  httpRequest1.onreadystatechange = function () {
    if (httpRequest1.readyState === 4 && httpRequest1.status === 200) {
      console.log(httpRequest1.response);
      jsonMoyAnnee = JSON.parse(httpRequest1.response);
      updateCards(jsonMoyAnnee);
    }
  };
  httpRequest1.send();
  //////////////
  httpRequest2 = new XMLHttpRequest();
  httpRequest2.open("GET", "/api/moy_spec");
  httpRequest2.onreadystatechange = function () {
    if (httpRequest2.readyState === 4 && httpRequest2.status === 200) {
      console.log(httpRequest2.response);
      jsonMoySpec = JSON.parse(httpRequest2.response);
      updatePieChart(jsonMoySpec);
    }
  };
  httpRequest2.send();
  //////////////
  httpRequest3 = new XMLHttpRequest();
  httpRequest3.open("GET", "/api/annee_spec_etudient");
  httpRequest3.onreadystatechange = function () {
    if (httpRequest3.readyState === 4 && httpRequest3.status === 200) {
      jsonAnneeSpecEtudient = JSON.parse(httpRequest3.response);
      updateRadarChart(jsonAnneeSpecEtudient);
    }
  };
  httpRequest3.send();
  /////////////////
  httpRequest4 = new XMLHttpRequest();
  httpRequest4.open("GET", "/api/annee_sexe_moy");
  httpRequest4.onreadystatechange = function () {
    if (httpRequest4.readyState === 4 && httpRequest4.status === 200) {
      jsonAnneeSexeMoy = JSON.parse(httpRequest4.response);
      updateMixedChart(jsonAnneeSexeMoy);
    }
  };
  httpRequest4.send();
}
function updateCards(jsonMoyAnnee) {
  existingCards = document.getElementsByClassName("dataCards");
  if (existingCards.length) {
    for (let j = existingCards.length - 1; j >= 0; j--) {
      existingCards[j].remove();
    }
  }
  cardsArea = document
    .getElementById("cards-area")
    .getElementsByClassName("card-body")[0];
  myLabels = jsonMoyAnnee.map(function (e) {
    return e.annee;
  });
  myData = jsonMoyAnnee.map(function (e) {
    return e.avgmoyannee.toFixed(2);
  });
  for (let i = 0; i < myLabels.length; i++) {
    card = document.createElement("div");
    card.setAttribute("class", "dataCards");
    card.innerHTML = "<strong>En " + myLabels[i] + "</strong><br>" + myData[i];
    cardsArea.append(card);
  }
}
function updatePieChart(jsonSpecEtudient2021) {
  myLabels = jsonSpecEtudient2021.map(function (e) {
    return e.specialite;
  });
  myData = jsonSpecEtudient2021.map(function (e) {
    return e.avgmoyspec;
  });
  new Chart(document.getElementById("pie-chart"), {
    type: "pie",
    data: {
      labels: myLabels,
      datasets: [
        {
          label: "etudients",
          backgroundColor: [
            "#ffe083",
            "#4a8adf",
            "#ff76b6",
            "#0a52be",
            "#ffc107",
            "#ffb3d6",
            "#B2A1D8",
            "#F1F1F1",
            "#E3D2B9",
            "#c29200",
          ],
          data: myData,
        },
      ],
    },
    options: {
      title: { display: false },
    },
  });
}
function updateRadarChart(jsonAnneeSpecEtudient) {
  const myLabels = [...new Set(jsonAnneeSpecEtudient.map((e) => e.specialite))];
  const myGraphes = [...new Set(jsonAnneeSpecEtudient.map((e) => e.annee))];
  const chunkSize = myLabels.length;
  const chunks = [];
  for (let i = 0; i < jsonAnneeSpecEtudient.length; i += chunkSize) {
    chunks.push(
      jsonAnneeSpecEtudient.slice(i, i + chunkSize).map((e) => e.nombre)
    );
  }
  let myDatasets = [];
  for (let i = 0; i < myGraphes.length; i++) {
    let myDataset = {
      label: myGraphes[i],
      fill: true,
      backgroundColor: myColors[i] + "40",
      borderColor: myColors[i],
      pointBackgroundColor: myColors[i],
      data: chunks[i],
    };
    myDatasets.push(myDataset);
  }
  new Chart(document.getElementById("radar-chart"), {
    type: "radar",
    data: {
      labels: myLabels,
      datasets: myDatasets,
    },
    options: {
      title: { display: false },
    },
  });
}
function updateMixedChart(jsonAnneeSexeMoy) {
  const myLabels = [...new Set(jsonAnneeSexeMoy.map((e) => e.annee))];
  const halfLength = Math.ceil(jsonAnneeSexeMoy.length / 2);
  const myDataF = jsonAnneeSexeMoy.slice(0, halfLength).map((e) => e.moy);
  const myDataM = jsonAnneeSexeMoy.slice(halfLength).map((e) => e.moy);
  new Chart(document.getElementById("mixed-chart"), {
    type: "bar",
    data: {
      labels: myLabels,
      datasets: [
        {
          label: "Hommes",
          type: "line",
          borderColor: "#0d6efd",
          data: myDataM,
          fill: false,
        },
        {
          label: "Femmes",
          type: "line",
          borderColor: "#ff76b6",
          data: myDataF,
          fill: false,
        },
        {
          label: "Hommes",
          type: "bar",
          backgroundColor: "#4a8adf",
          data: myDataM,
        },
        {
          label: "femmes",
          type: "bar",
          backgroundColor: "#ffb3d6",
          data: myDataF,
        },
      ],
    },
    options: {
      title: { display: false },
      legend: { display: false },
    },
  });
}
