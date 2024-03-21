// static/script.js

document.addEventListener('DOMContentLoaded', () => {
    const gameBoard = document.getElementById('game-board');

    // Fetch initial card data from the server
    fetch('/get_cards')
        .then(response => response.json())
        .then(cards => {
            initializeGame(cards);
        });

    let flippedCards = [];
    let matchedPairs = 0;

    function initializeGame(cards) {
        cards.forEach((card, index) => {
            const cardElement = document.createElement('div');
            cardElement.classList.add('card');
            cardElement.dataset.index = index;

            // Create an inner element for the card value
            const cardValue = document.createElement('span');
            cardValue.classList.add('card-value');
            cardValue.textContent = card;

            // Append the card value to the card element
            cardElement.appendChild(cardValue);

            // Add click event listener to the card element
            cardElement.addEventListener('click', () => flipCard(cardElement));

            // Append the card element to the game board
            gameBoard.appendChild(cardElement);
        });
    }

    function flipCard(cardElement) {
        if (!cardElement.classList.contains('flipped') && flippedCards.length < 2) {
            cardElement.classList.add('flipped');
            flippedCards.push(cardElement);

            if (flippedCards.length === 2) {
                setTimeout(checkMatch, 500);
            }
        }
    }

    function checkMatch() {
        const [card1, card2] = flippedCards;

        if (card1.textContent === card2.textContent) {
            card1.removeEventListener('click', () => flipCard(card1));
            card2.removeEventListener('click', () => flipCard(card2));
            matchedPairs++;

            if (matchedPairs === cards.length / 2) {
                alert('Congratulations! You won!');
            }
        } else {
            card1.classList.remove('flipped');
            card2.classList.remove('flipped');
        }

        flippedCards = [];
    }
});
