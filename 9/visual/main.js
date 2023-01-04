const createButton = document.querySelector(".create-bridge");
const container = document.querySelector(".container");
const bridgeLength = document.querySelector(".length");

function createBrige() {
    for (let i = 0; i < 21; i++){
        const contDiv = document.createElement('div');
        contDiv.classList.add("contStyling");
        
        for (let j = 0; j < bridgeLength.value; j++){
            const blockDiv = document.createElement('div');
            blockDiv.classList.add("blockStyling");
            contDiv.appendChild(blockDiv);
        }
        container.appendChild(contDiv);
    }
}

createButton.addEventListener("click", (e) => {
    e.preventDefault();
    createBrige();
})