// const textToAnimate = `                           
//     <h3 class="font-['DT_Getai_Grotesk_Display'] text-xl">Riepilogo</h3>
//     <p>Alberto Fontana, conosciuto come Naska, è diventato pilota automobilistico nonostante le difficoltà economiche. Ha trovato una soluzione creativa per avvicinarsi al suo sogno, iniziando a giocare a videogiochi di corse automobilistiche.</p><br>
//     <h3 class="font-['DT_Getai_Grotesk_Display'] text-xl">Highlights</h3>
//     <p>
//         🏎️ Alberto Fontana aveva il sogno di diventare pilota automobilistico, ma mancavano i soldi necessari per iniziare.<br>
//         🎮 Ha iniziato a giocare a videogiochi di corse automobilistiche per avvicinarsi al suo sogno.<br>
//         🎭 Ha seguito un corso di teatro e iniziato a creare contenuti video su YouTube, ottenendo una grande visibilità.<br>
//         👀 Ha imparato l'importanza di guardarsi da fuori per capire come gli altri lo vedevano e migliorare se stesso.<br>
//     </p>`;

function animateTextChunkByChunk(textToAnimate) {
    const chunkContainer = document.querySelector('.chunkAnimate');
    const chunks = textToAnimate.split(' ');

    let animatedText = '';
    let delay = 100; // Chunk-by-chunk animation speed

    chunks.forEach((chunk, index) => {
        setTimeout(() => {
            animatedText += chunk + ' ';
            chunkContainer.innerHTML = animatedText;
        }, index * delay);
    });
}

async function getAbstract() {
    const link = document.getElementById('link').value;
    console.log("[INFO] Link : " + link);
    fetch('/getAbstract', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            data: link
        })
    })
    .then(response => {
        if (response.ok) {
            console.log(response)
        } else throw new Error('Errore nella chiamata al server');
    })
}
