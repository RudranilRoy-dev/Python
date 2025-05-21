let userScore = 0;
let computerScore = 0;

function playGame(userChoice) {
    const computerChoice = Math.floor(Math.random() * 3) + 1;

    const choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    };

    const resultElement = document.getElementById('result');
    const scoreElement = document.getElementById('score');
    
    // Display the choices
    resultElement.innerHTML = `<strong>Your Choice:</strong> ${choices[userChoice]}<br><strong>Computer's Choice:</strong> ${choices[computerChoice]}`;

    // Determine the result of the game
    if (userChoice === computerChoice) {
        resultElement.innerHTML += "<br>It's a draw!";
    } else {
        if (
            (userChoice === 1 && computerChoice === 3) || // Rock beats Scissors
            (userChoice === 2 && computerChoice === 1) || // Paper beats Rock
            (userChoice === 3 && computerChoice === 2)    // Scissors beats Paper
        ) {
            userScore++;
            resultElement.innerHTML += "<br>You win!";
        } else {
            computerScore++;
            resultElement.innerHTML += "<br>Computer wins!";
        }
    }

    // Update the score
    scoreElement.innerHTML = `<strong>Score:</strong> You: ${userScore} - Computer: ${computerScore}`;
}

function exitGame() {
    window.close();  // Try closing the window (this may not work in all browsers)
}
