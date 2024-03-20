const moviesList = document.querySelector(".movies-container");
const movieInput = document.getElementById("search-input");

window.onload = function movies() {
    createCards(filmes);
};

const filmes = [{
    "titulo": "Dawn of the Planet of the Apes",
    "lancamento": 2014,
},
{
    "titulo": "District 9",
    "lancamento": 2009,
},
{
    "titulo": "Transformers: Age of Extinction",
    "lancamento": 2014,
},
{
    "titulo": "X-Men: Days of Future Past",
    "lancamento": 2014,
},
{
    "titulo": "The Machinist",
    "lancamento": 2004,
},
{
    "titulo": "The Last Samurai",
    "lancamento": 2003,
},
{
    "titulo": "The Amazing Spider-Man 2",
    "lancamento": 2014,
},
{
    "titulo": "Tangled",
    "lancamento": 2010,
},
{
    "titulo": "Rush",
    "lancamento": 2013,
},
{
    "titulo": "Drag Me to Hell",
    "lancamento": 2009,
},
{
    "titulo": "Despicable Me 2",
    "lancamento": 2013,
},
{
    "titulo": "Kill Bill: Vol. 1",
    "lancamento": 2003,
},
{
    "titulo": "A Bug's Life",
    "lancamento": 1998,
},
{
    "titulo": "Life of Brian",
    "lancamento": 1972,
},
{
    "titulo": "How to Train Your Dragon",
    "lancamento": 2010,
}];

function createCards(movieArray) {
    movieArray.forEach(movie => {
        const card = document.createElement('div');
        card.classList.add('movie-post');
        card.innerHTML = `
            <div class="data-event">
                <h3>${movie.lancamento}</h3>
            </div>
            <div class="main-event">
                <p class="event-meta">
                    ${movie.titulo}
                </p>
            </div>
        `;
        moviesList.appendChild(card);
    });
}

function filterMovies() {
    const filterText = movieInput.value.toLowerCase();
    const filteredMovies = filmes.filter(movie => movie.titulo.toLowerCase().includes(filterText));
    displayMovies(filteredMovies);
}

function displayMovies(movieArray) {
    moviesList.innerHTML = "";
    createCards(movieArray);
}

movieInput.addEventListener("keyup", filterMovies);





