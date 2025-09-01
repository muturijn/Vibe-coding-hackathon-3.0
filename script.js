async function loadData() {
  const res = await fetch("/get_entries");
  const data = await res.json();

  const labels = data.map(e => e.date_created);
  const fever = data.map(e => e.fever);
  const cough = data.map(e => e.cough);
  const headache = data.map(e => e.headache);
  const fatigue = data.map(e => e.fatigue);

  new Chart(document.getElementById("symptomChart"), {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        { label: "Fever", data: fever, borderColor: "red", fill: false },
        { label: "Cough", data: cough, borderColor: "orange", fill: false },
        { label: "Headache", data: headache, borderColor: "blue", fill: false },
        { label: "Fatigue", data: fatigue, borderColor: "green", fill: false }
      ]
    }
  });
}
loadData();
