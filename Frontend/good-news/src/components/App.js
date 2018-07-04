import React from 'react';
import ReactDOM from 'react-dom';
import Button from '@material-ui/core/Button';
import Footer from './Footer';

export default class App extends React.Component {
  render() {
    return (
      <Footer></Footer>
    );
  }
}

// import React from 'react';
// import { BrowserRouter as Router } from 'react-router-dom';
// import { Layout } from './Layout';

// export class App extends React.Component {
//   render() {
//     return (
//       <Router>
//         <Layout />
//       </Router>
//     );
//   }
// };

/*
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
*/