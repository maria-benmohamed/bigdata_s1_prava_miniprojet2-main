updateCharts();
function updateCharts() {
  httpRequest1 = new XMLHttpRequest();
  httpRequest1.open("GET", "/api/etudient_Spec_2021");
  httpRequest1.onreadystatechange = function () {
    if (httpRequest1.readyState === 4 && httpRequest1.status === 200) {
      jsonEtudientSpec2021 = JSON.parse(httpRequest1.response);
      httpRequest2 = new XMLHttpRequest();
      httpRequest2.open("GET", "/api/etudient_admis_Spec_2021");
      httpRequest2.onreadystatechange = function () {
        if (httpRequest2.readyState === 4 && httpRequest2.status === 200) {
          jsonEtudientAdmisSpec2021 = JSON.parse(httpRequest2.response);
          updateBarChart(jsonEtudientAdmisSpec2021, jsonEtudientSpec2021);
        }
      };
      httpRequest2.send();
    }
  };
  httpRequest1.send();
  /////////////////////////////
}
function updateBarChart(jsonEtudientAdmisSpec2021, jsonEtudientSpec2021) {
  myLabels = jsonEtudientAdmisSpec2021.map(function (e) {
    return e.specialite;
  });
  myData1 = jsonEtudientSpec2021.map(function (e) {
    return e.nombre;
  });
  myData2 = jsonEtudientAdmisSpec2021.map(function (e) {
    return e.nombre;
  });
  new Chart(document.getElementById("bar-chart-grouped"), {
    type: "bar",
    data: {
      labels: myLabels,
      datasets: [
        {
          label: "nombre des etudients",
          backgroundColor: "#4a8adf",
          data: myData1,
        },
        {
          label: "nombre des etudients admis",
          backgroundColor: "#80e66c",
          data: myData2,
        },
      ],
    },
    options: {
      title: { display: false },
      legend: { display: false },
    },
  });
}
