import './GameOver.css';

const GameOver = ({score, retry}) => {
  return (
    <div>
        <h1>Fim do Jogo!</h1>
        <h2>A sua pontuação foi: <span>{score}</span></h2>
        <button onClick={retry}>RESETAR JOGO</button>
    </div>
  )
}

export default GameOver