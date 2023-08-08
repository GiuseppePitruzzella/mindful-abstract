document.addEventListener('DOMContentLoaded', function() {
    // const API = document.getElementById('abstractForm');

    // abstractForm.addEventListener('submit', function(event) {
    //     event.preventDefault();
    //     postAPI();
    // });

    // function postAPI() {
    //     const inputField = document.getElementById('inputField');
    //     const inputData = inputField.value;

    //     fetch('/getAbstract', {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/x-www-form-urlencoded'
    //         },
    //         body: 'input_data=' + inputData
    //     })
    //     .then(response => response.text())
    //     .then(data => document.getElementById('mainContainer').innerHTML = data)
    //     .catch(error => console.error('[ERROR] Request Error :', error));
    // }

    const abstractForm = document.getElementById('abstractForm');

    abstractForm.addEventListener('submit', function(event) {
        event.preventDefault();
        getAbstract();
    });

    function getAbstract() {
        const inputField = document.getElementById('inputField');
        const inputData = inputField.value;

        fetch('/getAbstract', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'input_data=' + inputData
        })
        .then(response => response.text())
        .then(data => { 
            document.open(); 
            document.write(data); 
            document.close()

            // parsedHTML = new DOMParser().parseFromString(document.getElementById("sum_value").innerHTML, "text/html")
            console.log(document.getElementById("sum_value").getAttribute("data-data"))
        })
        .catch(error => console.error('[ERROR] Request Error :', error));
    }
});
