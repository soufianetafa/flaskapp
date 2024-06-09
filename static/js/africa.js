document.addEventListener('DOMContentLoaded', function() {
    fetch('../data_csv/africa.csv')
        .then(response => response.text())
        .then(data => {
            const tableBody = document.querySelector('#data-table tbody');
            const rows = data.split('\n');
            rows.forEach(row => {
                const values = row.split(',');
                const tr = document.createElement('tr');
                values.forEach(value => {
                    const td = document.createElement('td');
                    td.textContent = value;
                    tr.appendChild(td);
                });
                tableBody.appendChild(tr);
            });
        })
        .catch(error => console.error('Erreur lors du chargement des données:', error));
});
