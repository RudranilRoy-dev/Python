let number;
let attempts = 0;
let highscore = 0;  // Initialize high score to 0
let gameEnded = false;

function startGame() {
    number = Math.floor(Math.random() * 10001);  // Generate random number between 0 and 10000
    attempts = 0;
    gameEnded = false;
    document.getElementById("feedback").innerText = "";
    document.getElementById("attempts-info").innerText = `Attempts: ${attempts}`;
    document.getElementById("highscore-info").innerText = `High Score: ${highscore}`;
    document.getElementById("play-again").style.display = "none";  // Hide Play Again button initially
    document.getElementById("user-guess").value = "";  // Reset input field
}

function makeGuess() {
    if (gameEnded) return;

    const userGuess = parseInt(document.getElementById("user-guess").value);

    if (isNaN(userGuess) || userGuess < 0 || userGuess > 10000) {
        alert("Please enter a valid number between 0 and 10000!");
        return;
    }

    attempts++;

    if (userGuess === number) {
        document.getElementById("feedback").innerText = `Your guess is correct! 🎉 The number is ${number}. You took ${attempts} attempts.`;

        // Update highscore if this attempt is lower than the current highscore
        if (highscore === 0 || attempts < highscore) {
            highscore = attempts;
        }
        
        document.getElementById("attempts-info").innerText = `Attempts: ${attempts}`;
        document.getElementById("highscore-info").innerText = `High Score: ${highscore}`;
        document.getElementById("play-again").style.display = "inline-block";  // Show Play Again button
        gameEnded = true;  // End the game
    } else if (userGuess > number) {
        document.getElementById("feedback").innerText = "You chose a bigger number.";
    } else {
        document.getElementById("feedback").innerText = "You chose a smaller number.";
    }

    document.getElementById("attempts-info").innerText = `Attempts: ${attempts}`;

    // Reset the guess input after every attempt (whether correct or incorrect)
    document.getElementById("user-guess").value = "";
}

function playAgain() {
    startGame();  // Restart the game
}

function exitGame() {
    window.close(); // This might not work in all browsers. It could be replaced by window.location.href = 'about:blank'; to avoid any errors in browsers that don't allow closing tabs.
}

startGame();  // Initialize the game when the page loads