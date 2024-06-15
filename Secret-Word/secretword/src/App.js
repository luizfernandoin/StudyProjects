// Imagens
// import logo from './logo.svg';

// CSS
import './App.css';

// React
import { useState, useEffect, useCallback } from 'react';

// Data
import wordsList from './data/words';

// Components
import StartScreen from './components/StartScreen';
import Game from './components/Game';
import GameOver from './components/GameOver';

const stages = [
  {id: 1, name: "start"},
  {id: 2, name : "game"},
  {id: 3, name: "end"}
]

const guessesQty = 3;

function App() {
  const [stage, setStage] = useState(stages[0].name);
  const [words] = useState(wordsList);

  const [pickedWord, setPickedWord] = useState("");
  const [pickedCategory, setPickedCategory] = useState("");
  const [letters, setLetters] = useState([]);

  const [guessedLetters, setGuessedLetters] = useState([]);
  const [wrongLetters, setWrongLetters] = useState([]);
  const [guesses, setGuesses] = useState(guessesQty);
  const [score, setScore] = useState(0);

  const pickWordAndCategory = useCallback(() => {
    const categories = Object.keys(words);
    const category = categories[Math.floor(Math.random() * categories.length)]
    const word = words[category][Math.floor(Math.random() * words[category].length)]
    
    return {word, category};
  }, [words]);

  const startGame = useCallback(() => {
    clearLetterStates();
    const {word, category} = pickWordAndCategory();
    
    let wordLetters = word.split("");
    wordLetters = wordLetters.map((letter) => letter.toLowerCase());
    
    setPickedWord(word);
    setPickedCategory(category);
    setLetters(wordLetters);
    setStage(stages[1].name);
  }, [pickWordAndCategory]);

  const verifyLetter = (letter) => {
    const normalizedLetter = letter.toLowerCase();
    if (
      guessedLetters.includes(normalizedLetter) || 
      wrongLetters.includes(normalizedLetter)
    ) return;

    if (letters.includes(normalizedLetter)) {
      setGuessedLetters((actualGuessedLetters) => [
        ...actualGuessedLetters, 
        normalizedLetter
      ])
    } else {
      setWrongLetters((actualWrongLetters) => [
        ...actualWrongLetters, 
        normalizedLetter
      ])

      setGuesses((actualGuesses) => actualGuesses - 1);
    }
  }

  function clearLetterStates() {
    setGuessedLetters([]);
    setWrongLetters([]);
  }

  useEffect(() => {
    if (guesses <= 0) {
      clearLetterStates();
      setStage(stages[2].name);
    }
  }, [guesses]);

  useEffect(() => {
    const uniqueLetters = [...new Set(letters)];
    console.log("Unique letters:", uniqueLetters);
    console.log("Guessed letters length:", guessedLetters.length);
  
    if (uniqueLetters.length === guessedLetters.length) {
      setScore((actualScore) => actualScore + 100);
      startGame();
    }
  }, [guessedLetters, letters, startGame]);
  

  const retry = () => {
    setScore(0);
    setGuesses(guessesQty);

    setStage(stages[0].name)
  }

  function verifyGuesses() {
    setGuesses(guesses - 1);

    if (guesses === 0) {
      setStage(stage[2].name);
    }
  }

  return (
    <div className="App">
      {stage === stages[0].name && <StartScreen startGame={startGame}/>}
      {stage === stages[1].name && 
        <Game
          pickedWord={pickedWord} 
          pickedCategory={pickedCategory} 
          letters={letters}
          guessedLetters={guessedLetters}
          wrongLetters={wrongLetters}
          guesses={guesses}
          score={score}
          verifyLetter={verifyLetter}
          verifyGuesses={verifyGuesses}
        />}
      {stage === stages[2].name && <GameOver retry={retry} score={score}/>}
    </div>
  );
}

export default App;
