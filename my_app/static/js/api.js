function getCat() {
    fetch("https://api.thecatapi.com/v1/images/search?api_key=a7ed07bb-660b-4184-8084-4163dfd5bc14")
    .then(res => res.json())
    .then(res=> {
        const div = document.getElementById("cat-div");
        div.innerHTML = '';
        const cat = new Image();
        cat.src = res[0].url;
        div.appendChild(cat);
    });
}

window.onload = function() { 
    const catButton = document.getElementById("cat-button");
    catButton.onclick = getCat;
}