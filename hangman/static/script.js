function createKeyboard() {
    const keyboard = document.getElementById('keyboard');
    keyboard.innerHTML = '';
    for (let i = 65; i <= 90; i++) {
        const btn = document.createElement('button');
        btn.innerText = String.fromCharCode(i);
        btn.onclick = () => guessLetter(btn.innerText.toLowerCase());
        keyboard.appendChild(btn);
    }
}

function startGame() {
    fetch('/start')
        .then(res => res.json())
        .then(data => updateUI(data));
    createKeyboard();
}

function guessLetter(letter) {
    fetch('/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ letter })
    })
        .then(res => res.json())
        .then(data => updateUI(data));
}

function updateUI(data) {
    document.getElementById('word-display').innerText = data.display;
    document.getElementById('tries').innerText = data.tries_left;
    document.getElementById('status').innerText = data.status !== 'playing' ? `Game ${data.status}! ${data.word ? 'Word: ' + data.word : ''}` : '';

    if (data.status !== 'playing') {
        document.getElementById('keyboard').querySelectorAll('button').forEach(btn => btn.disabled = true);
    }
}

window.onload = startGame;
