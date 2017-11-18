var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
			type: 'line',
			data: {
				datasets: [{
					label: "Dataset 1",
					fill: false,
					data: [{
						x: new Date(0),
						y: 5
					}, {
						x: new Date(2),
						y: 6
					}, {
						x: new Date(4),
						y: 7
					}, {
						x: new Date(5),
						y: 8
					}]
				}]
			},
			options: {
				responsive: true,
				title:{
					display:true,
					text:"Time Data"
				},
				scales: {
					xAxes: [{
						type: "time",
						display: true,
					}],
					yAxes: [{
						display: true,
					}]
				}
			}
});
