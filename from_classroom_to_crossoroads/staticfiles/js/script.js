document.addEventListener('DOMContentLoaded', function () {

    try {
        // Parse the data and verify if it is correctly defined.
        console.log("Dropout Risk Data:", dropoutRiskData);
        console.log("Monthly Dropout Data:", monthlyDropoutData);
        console.log("Dropout Reasons Data:", dropoutReasonsData);
        console.log("Gender Risk Data:", genderRiskData);
        console.log("Support Needs Data:", supportNeedsData);

        // Proceed with creating charts if data is valid.
        if (dropoutRiskData) {
            createDropoutRiskChart();
        }
        if (monthlyDropoutData) {
            createMonthlyDropoutChart();
        }
        if (dropoutReasonsData) {
            createDropoutReasonsChart();
        }
        if (genderRiskData) {
            createGenderRiskChart();
        }
        if (supportNeedsData) {
            createSupportNeedsChart();
        }
    } catch (error) {
        console.error("Error parsing JSON data:", error);
    }
    // Dropout Risk Levels - Bar Chart
    const dropoutRiskCtx = document.getElementById('dropoutRiskChart');
    if (dropoutRiskCtx) {
        new Chart(dropoutRiskCtx.getContext('2d'), {
            type: 'bar',
            data: {
                labels: Object.keys(dropoutRiskData),
                datasets: [{
                    label: 'Dropout Risk Levels',
                    data: Object.values(dropoutRiskData),
                    backgroundColor: ['#28a745', '#ffc107', '#dc3545'],
                    borderColor: ['#218838', '#e0a800', '#c82333'],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Monthly Dropout Cases - Line Chart
    const monthlyDropoutCtx = document.getElementById('monthlyDropoutChart');
    if (monthlyDropoutCtx) {
        new Chart(monthlyDropoutCtx.getContext('2d'), {
            type: 'line',
            data: {
                labels: Object.keys(monthlyDropoutData),
                datasets: [{
                    label: 'Monthly Dropout Cases',
                    data: Object.values(monthlyDropoutData),
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Dropout Reasons - Pie Chart
    const dropoutReasonsCtx = document.getElementById('dropoutReasonsChart');
    if (dropoutReasonsCtx) {
        new Chart(dropoutReasonsCtx.getContext('2d'), {
            type: 'pie',
            data: {
                labels: Object.keys(dropoutReasonsData),
                datasets: [{
                    label: 'Dropout Reasons',
                    data: Object.values(dropoutReasonsData),
                    backgroundColor: ['#ff6384', '#36a2eb', '#ffcd56', '#4bc0c0', '#9966ff'],
                    borderColor: ['#fff', '#fff', '#fff', '#fff', '#fff'],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true
            }
        });
    }

    // Gender-Based Dropout Risk - Doughnut Chart
    const genderRiskCtx = document.getElementById('genderRiskChart');
    if (genderRiskCtx) {
        new Chart(genderRiskCtx.getContext('2d'), {
            type: 'doughnut',
            data: {
                labels: Object.keys(genderRiskData),
                datasets: [{
                    label: 'Gender-Based Dropout Risk',
                    data: Object.values(genderRiskData),
                    backgroundColor: ['#36a2eb', '#ff6384'],
                    borderColor: ['#fff', '#fff'],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true
            }
        });
    }

    // Support Needs - Radar Chart
    const supportNeedsCtx = document.getElementById('supportNeedsChart');
    if (supportNeedsCtx) {
        new Chart(supportNeedsCtx.getContext('2d'), {
            type: 'radar',
            data: {
                labels: Object.keys(supportNeedsData),
                datasets: [{
                    label: 'Support Needs',
                    data: Object.values(supportNeedsData),
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                scales: {
                    r: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
});
