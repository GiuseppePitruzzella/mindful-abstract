document.addEventListener('DOMContentLoaded', function() {
    const abstractForm = document.getElementById('abstractForm');

    abstractForm.addEventListener('submit', function(event) {
        event.preventDefault();
        setAPI();
    });

    function setAPI() {
        const inputField = document.getElementById('inputField');
        const inputData = inputField.value;

        fetch('/setAPI', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ input_data: inputData })
        })
        .then(response => response.text())
        .then(data => { 
            document.open(); 
            document.write(data); 
            document.close();
        })
        .catch(error => console.error('[ERROR] Request Error :', error));
    }
});
