document.addEventListener('DOMContentLoaded', function() {
    function animateTextChunkByChunk(textToAnimate) {
        const chunkContainer = document.getElementById('chunkAnimate');
        const chunks = textToAnimate.split(' ');
    
        let currentChunkIndex = 0;
        let animatedText = '';
        let delay = 50; // Chunk-by-chunk animation speed
    
        function animateNextChunk() {
            if (currentChunkIndex < chunks.length) {
                animatedText += chunks[currentChunkIndex] + ' ';
                chunkContainer.innerHTML = animatedText;
                currentChunkIndex++;
    
                setTimeout(animateNextChunk, delay);
            }
        }
    
        animateNextChunk();
    }

    const abstractForm = document.getElementById('abstractForm');

    abstractForm.addEventListener('submit', function(event) {
        event.preventDefault();
        getAbstract();
    });

    function getAbstract() {
        const inputField = document.getElementById('inputField');
        const inputData = inputField.value;

        // const apiField = document.getElementById('apiField');
        // const apiData = apiField.value;

        // console.log(inputData + " " + apiData)

        fetch('/getAbstract', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            // body: JSON.stringify({ input_data: inputData, api_data: apiData })
            body: JSON.stringify({ input_data: inputData })
        })
        .then(response => response.text())
        .then(data => document.getElementById('mainContainer').innerHTML = data)
        .catch(error => console.error('[ERROR] Request Error :', error));
    }
});
