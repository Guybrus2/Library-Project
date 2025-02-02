// Function to get all games from the API
async function getGames() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/games');
        const gamesList = document.getElementById('games-list');
        gamesList.innerHTML = ''; // Clear existing list

        response.data.games.forEach(game => {
            gamesList.innerHTML += `
                <div class="game-card">
                    <h3>${game.name}</h3>
                    <p>Creator: ${game.creator}</p>
                    <p>Year: ${game.year_published}</p>
                    <p>Genre: ${game.genre}</p>
                    ${game.picture_url ? `<img src="${game.picture_url}" alt="${game.name}" class="game-image">` : ''}
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching games:', error);
        alert('Failed to load games');
    }
}

// Function to add a new game to the database
async function addGame() {
    const name = document.getElementById('game-name').value;
    const creator = document.getElementById('game-creator').value;
    const year_published = document.getElementById('game-year-published').value;
    const genre = document.getElementById('game-genre').value;
    const picture_url = document.getElementById('game-picture-url').value; // New field for images

    try {
        await axios.post('http://127.0.0.1:5000/games', {
            name: name,
            creator: creator,
            year_published: year_published,
            genre: genre,
            picture_url: picture_url // Include the image URL
        });

        // Clear form fields
        document.getElementById('game-name').value = '';
        document.getElementById('game-creator').value = '';
        document.getElementById('game-year-published').value = '';
        document.getElementById('game-genre').value = '';
        document.getElementById('game-picture-url').value = '';

        // Refresh the games list
        getGames();
        
        alert('Game added successfully!');
    } catch (error) {
        console.error('Error adding game:', error);
        alert('Failed to add game');
    }
}

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await axios.post('http://127.0.0.1:5000/login', {
            name: username,
            password: password
        });


        console.log('Login successful:', response.data);
    } catch (error) {

        console.error('User does not exist or login failed:', error);
        alert('Failed to login');
    }
}


async function logout(){
    pass
}
async function del_game(){
    pass
}
async function add_customer(){
    pass
}

async function edit_customer(){
    pass
}
async function edit_game(){
    pass
}
// Load all games when the page loads
document.addEventListener('DOMContentLoaded', getGames);

