import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react';
import {Deploy} from './Component/Deploy/Deploy';
import {Distancetime} from './Component/Deploy/Distancetime';
import TextField from '@material-ui/core/TextField';


function App() {
  const [state, setState] = useState({})
  
  useEffect(() => {
    fetch("/api", {mode: "no-cors"}).then(response => {
      if(response.status == 200){
        return response.json()
      }
    }).then(data => setState(data))
    .then(error => console.log(error))
  }, [])


  return (
    <div className="App">
      <Deploy prop={state}/>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome!
        </p>
        <TextField id="outlined-basic" label="Name" variant="outlined" />
        <TextField id="outlined-basic" label="License Plate Number" variant="outlined" />
        <p>
          Click below for an interactive map of the stops and route.
        </p>
        <Distancetime prop={state}/>
        <a
          className="App-link"
          href="http://127.0.0.1:5000/map"
          target="_blank"
          rel="noopener noreferrer"
        >
          Map of stops
        </a>
      </header>
    </div>
  );
}

export default App;
