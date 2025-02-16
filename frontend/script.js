
async function getGames() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/games');
        const gamesList = document.getElementById('games-list');
        if (gamesList) {
            gamesList.innerHTML = ''; 
            response.data.games.forEach(game => {
                gamesList.innerHTML += `
                    <div class="game-card" data-game-id="${game.id}">
                        <h3>${game.name}</h3>
                        <p>Creator: ${game.creator}</p>
                        <p>Year: ${game.year_published}</p>
                        <p>Genre: ${game.genre}</p>
                        ${game.picture_url ? `<img src="${game.picture_url}" alt="${game.name}" class="game-image">` : ''}
                        <button class="remove-btn" onclick="del_game(${game.id})">Remove Game</button>
                        <button onclick="editGame(${game.id})">Edit Game</button>
                    </div>
                `;
            });
        }
    } catch (error) {
        console.error('Error fetching games:', error);
        alert('Failed to load games');
    }
}

function addGame(event) {
    event.preventDefault();
    const gameData = {
        name: document.getElementById("game-name").value,
        creator: document.getElementById("game-creator").value,
        year_published: document.getElementById("game-year-published").value,
        genre: document.getElementById("game-genre").value,
        picture_url: document.getElementById("game-picture-url").value || "https://via.placeholder.com/150"
    };
    axios.post("http://127.0.0.1:5000/games", gameData)
        .then(response => {
            alert(response.data.message);
            getGames(); 
        })
        .catch(error => {
            console.error("Error adding game:", error);
            alert("Failed to add game.");
        });
}

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    try {
        const response = await axios.post('http://127.0.0.1:5000/login', { name: username, password: password }, {
            headers: { "Content-Type": "application/json" }
        });
        localStorage.setItem('isloggedIn', 'true');
        alert(response.data.message);
        document.getElementById("auth-section").style.display = "none";
        document.getElementById("main-section").classList.remove('hidden');
        getGames(); 
    } catch (error) {
        console.error('User does not exist or login failed:', error);
        alert('Failed to login');
    }
}

async function logout() {
    try {
        await axios.post("http://127.0.0.1:5000/logout");
    } catch (error) {
        console.error("Logout failed:", error);
    }
    localStorage.removeItem("isloggedIn");
    document.getElementById("main-section").classList.add("hidden");
    document.getElementById("auth-section").classList.remove("hidden");
    alert("Logged out successfully!");
}

function del_game(gameId) {
    axios.delete(`http://127.0.0.1:5000/games/${gameId}`)
        .then(response => {
            console.log('Game deleted:', response.data);
            getGames(); 
        })
        .catch(error => {
            console.error('Error deleting game:', error);
        });
}

async function editGame(gameId) {
    console.log("Game id =", gameId);
    try {
        const response = await axios.get(`http://127.0.0.1:5000/games/${gameId}`);

        const game = response.data;
        document.getElementById('edit-game-id').value = game.id;
        document.getElementById('edit-game-name').value = game.name;
        document.getElementById('edit-game-creator').value = game.creator;
        document.getElementById('edit-game-year').value = game.year_published;
        document.getElementById('edit-game-genre').value = game.genre;
        document.getElementById('edit-game-picture').value = game.picture_url;
        document.getElementById('edit-game-form').style.display = 'block';
    } catch (error) {
        console.error('Error fetching game details:', error);
        alert('Failed to fetch game details');
    }
}


async function submitEditForm(event) {
    event.preventDefault();
    const gameId = document.getElementById('edit-game-id').value;
    const updatedGame = {
        name: document.getElementById('edit-game-name').value,
        creator: document.getElementById('edit-game-creator').value,
        year_published: document.getElementById('edit-game-year').value,
        genre: document.getElementById('edit-game-genre').value,
        picture_url: document.getElementById('edit-game-picture').value,
    };
    try {
        const response = await axios.put(`http://127.0.0.1:5000/games/${gameId}`, updatedGame);
        alert(response.data.message);
        document.getElementById('edit-game-form').style.display = 'none';
        getGames(); 
    } catch (error) {
        console.error('Error updating game:', error);
        alert('Failed to update game');
    }
}



function addCustomer(event) {
    event.preventDefault();
    const customerData = {
        name: document.getElementById('customer-name').value,
        email: document.getElementById('customer-email').value,
        phone: document.getElementById('customer-phone').value
    };
    axios.post('http://127.0.0.1:5000/customers', customerData)
        .then(response => {
            alert(response.data.message);
        })
        .catch(error => {
            console.error('Error adding customer:', error);
            alert('Failed to add customer.');
        });
}

const addCustomerForm = document.getElementById('add-customer-form');
if (addCustomerForm) {
    addCustomerForm.addEventListener('submit', addCustomer);
}


document.addEventListener('DOMContentLoaded', function() {
    // Check if the user is already logged in
    if (localStorage.getItem('isloggedIn') === 'true') {
        // Hide the authentication section and show the main section
        document.getElementById("auth-section").style.display = "none";
        document.getElementById("main-section").classList.remove('hidden');
        getGames();
    } else {
        // Optionally, ensure the correct sections are visible/invisible
        document.getElementById("auth-section").style.display = "block";
        document.getElementById("main-section").classList.add('hidden');
    }
});

