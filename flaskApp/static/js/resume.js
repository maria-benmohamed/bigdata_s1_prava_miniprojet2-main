updateCharts();
function updateCharts() {
  httpRequest1 = new XMLHttpRequest();
  httpRequest1.open("GET", "/api/annee_etudient");
  httpRequest1.onreadystatechange = function () {
    if (httpRequest1.readyState === 4 && httpRequest1.status === 200) {
      jsonAnneeEtudient = JSON.parse(httpRequest1.response);
      updateBarChart(jsonAnneeEtudient);
    }
  };
  httpRequest1.send();
  ///////////
  httpRequest2 = new XMLHttpRequest();
  httpRequest2.open("GET", "/api/annee_sexe_etudient");
  httpRequest2.onreadystatechange = function () {
    if (httpRequest2.readyState === 4 && httpRequest2.status === 200) {
      jsonAnneeSexeEtudient = JSON.parse(httpRequest2.response);
      updateGroupedBarsChart(jsonAnneeSexeEtudient);
    }
  };
  httpRequest2.send();
  ///////////
  httpRequest3 = new XMLHttpRequest();
  httpRequest3.open("GET", "/api/annee_spec_etudient3");
  httpRequest3.onreadystatechange = function () {
    if (httpRequest3.readyState === 4 && httpRequest3.status === 200) {
      jsonAnneeSpecEtudient3 = JSON.parse(httpRequest3.response);
      updateLineChart(jsonAnneeSpecEtudient3);
    }
  };
  httpRequest3.send();
  ///////////
  httpRequest4 = new XMLHttpRequest();
  httpRequest4.open("GET", "/api/spec_etudient");
  httpRequest4.onreadystatechange = function () {
    if (httpRequest4.readyState === 4 && httpRequest4.status === 200) {
      jsonSpecEtudient = JSON.parse(httpRequest4.response);
      updatePieChart(jsonSpecEtudient);
    }
  };
  httpRequest4.send();
}
function updateBarChart(jsonAnneeEtudient) {
  myLabels = jsonAnneeEtudient.map(function (e) {
    return e.annee;
  });
  myData = jsonAnneeEtudient.map(function (e) {
    return e.nombre;
  });
  new Chart(document.getElementById("bar-chart"), {
    type: "bar",
    data: {
      labels: myLabels,
      datasets: [
        {
          label: "etudients",
          backgroundColor: [
            "#ffb3d6",
            "#4a8adf",
            "#ffe083",
            "#ffb3d6",
            "#4a8adf",
            "#ffe083",
            "#ffb3d6",
            "#4a8adf",
            "#ffe083",
          ],
          data: myData,
        },
      ],
    },
    options: {
      legend: { display: false },
      title: { display: false },
    },
  });
}
function updatePieChart(jsonSpecEtudient) {
  myLabels = jsonSpecEtudient.map(function (e) {
    return e.specialite;
  });
  myData = jsonSpecEtudient.map(function (e) {
    return e.nombre;
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
function updateLineChart(jsonAnneeSpecEtudient3) {
  const myLabels = [...new Set(jsonAnneeSpecEtudient3.map((e) => e.annee))];
  const chunkSize = myLabels.length;
  const chunks = [];
  for (let i = 0; i < jsonAnneeSpecEtudient3.length; i += chunkSize) {
    chunks.push(
      jsonAnneeSpecEtudient3.slice(i, i + chunkSize).map((e) => e.nombre)
    );
  }
  const myDataS1 = chunks[0] || [];
  const myDataS2 = chunks[1] || [];
  const myDataS3 = chunks[2] || [];
  new Chart(document.getElementById("line-chart"), {
    type: "line",
    data: {
      labels: myLabels,
      datasets: [
        {
          data: myDataS1,
          label: "SPECIALITE_1",
          borderColor: "#4a8adf",
          fill: false,
        },
        {
          data: myDataS2,
          label: "SPECIALITE_2",
          borderColor: "#ffc107",
          fill: false,
        },
        {
          data: myDataS3,
          label: "SPECIALITE_3",
          borderColor: "#ffb3d6",
          fill: false,
        },
      ],
    },
    options: {
      title: { display: false },
    },
  });
}
function updateGroupedBarsChart(jsonAnneeSexeEtudient) {
  const myLabels = [...new Set(jsonAnneeSexeEtudient.map((e) => e.annee))];
  const halfLength = Math.ceil(jsonAnneeSexeEtudient.length / 2);
  const myDataF = jsonAnneeSexeEtudient
    .slice(0, halfLength)
    .map((e) => e.nombre);
  const myDataM = jsonAnneeSexeEtudient.slice(halfLength).map((e) => e.nombre);
  new Chart(document.getElementById("bar-chart-grouped"), {
    type: "bar",
    data: {
      labels: myLabels,
      datasets: [
        {
          label: "Hommes",
          backgroundColor: "#4a8adf",
          data: myDataM,
        },
        {
          label: "Femmes",
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
