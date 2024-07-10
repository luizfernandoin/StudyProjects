import styles from './Login.module.css';

import { useAuthentication } from '../../hooks/useAuthentication';
import { useState, useEffect } from 'react';

const Login = () => {
  const [email, setEmail] = useState("");
  const[password, setPassword] = useState("");
  const [error, setError] = useState("");

  const {error:authError, loading, login} = useAuthentication();

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    setError("");

    const user = {
      email,
      password
    }

    const res = await login(user);
  }

  useEffect(() => {
    
    if (authError) {
      setError(authError);
    }

  }, [authError]);

  return (
    <div className={styles.login}>
        <h1>Login</h1>
        <p>Faça login para utilizar o Blog</p>
        <form onSubmit={handleSubmit}>
          <label>
            <span>E-mail: </span>
            <input 
              type="email" 
              name="email" 
              required 
              placeholder='E-mail do Usuário' 
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </label>
          <label>
            <span>Senha: </span>
            <input 
              type="password" 
              name="password" 
              required 
              placeholder='Insira sua Senha'
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </label>
          {!loading && <button className='btn'>Entrar</button>}
          {loading && (<button className='btn' disabled>Aguarde...</button>)}

          {error && <p className='error'>{error}</p>}
        </form>
    </div>
  )
}

export default Login