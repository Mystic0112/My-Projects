document.addEventListener('DOMContentLoaded', function () {

    // --- LÓGICA DA PÁGINA DE LOGIN ---
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Impede o envio real do formulário
            // Simula um login bem-sucedido e redireciona para o dashboard
            window.location.href = 'dashboard.html';
        });
    }

    // --- GRÁFICOS (usando Chart.js) ---
    // Verifique se os elementos do canvas existem antes de criar os gráficos
    
    // Gráfico de Desempenho Geral (Dashboard)
    const desempenhoGeralChartCtx = document.getElementById('desempenhoGeralChart');
    if (desempenhoGeralChartCtx) {
        new Chart(desempenhoGeralChartCtx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul'],
                datasets: [{
                    label: 'Taxa de Vitória %',
                    data: [55, 58, 62, 60, 65, 68, 72],
                    borderColor: '#5046e5',
                    backgroundColor: 'rgba(80, 70, 229, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: false
                    }
                }
            }
        });
    }

    // Gráfico de KDA (Estatísticas)
    const kdaChartCtx = document.getElementById('kdaChart');
    if (kdaChartCtx) {
        new Chart(kdaChartCtx, {
            type: 'bar',
            data: {
                labels: ['Kills', 'Deaths', 'Assists'],
                datasets: [{
                    label: 'Média por Partida',
                    data: [15, 6, 9],
                    backgroundColor: [
                        'rgba(0, 255, 171, 0.6)', // Cor para Kills
                        'rgba(255, 93, 93, 0.6)',   // Cor para Deaths
                        'rgba(0, 186, 255, 0.6)'    // Cor para Assists
                    ],
                    borderColor: [
                        '#00ffab',
                        '#ff5d5d',
                        '#00baff'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }

    // Gráfico de Mapas (Estatísticas)
    const mapasChartCtx = document.getElementById('mapasChart');
    if (mapasChartCtx) {
        new Chart(mapasChartCtx, {
            type: 'doughnut',
            data: {
                labels: ['Mirage', 'Inferno', 'Dust II', 'Nuke'],
                datasets: [{
                    label: 'Partidas Jogadas',
                    data: [120, 95, 70, 45],
                    backgroundColor: [
                        '#5046e5',
                        '#00baff',
                        '#ffc107',
                        '#fd7e14'
                    ],
                    hoverOffset: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
            }
        });
    }

});

