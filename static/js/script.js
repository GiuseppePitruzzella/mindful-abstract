function printAbstract()

function getAbstract() {
    const link = document.getElementById('link').value;
    console.log(link)
    fetch('/getAbstract', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            data: link
        })
    })
    .then(response => {console.log(response)})
}