// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Pendientes", "En Proceso", "Bloqueadas", "Liberadas", "Rechazadas"],
    datasets: [{
      data: [12, 15, 11, 8, 2],
      backgroundColor: ['#FD7E14', '#6F42C1', '#FFC107', '#198754', '#DC3545'],
    }],
  },
});
