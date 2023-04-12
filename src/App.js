import logo from './logo.svg';
import './App.css';
import { useEffect} from 'react'
import { embedDashboard } from "@superset-ui/embedded-sdk";


function App() {

  const guestTokenFromBackend = async () => {
    const url = "https://dev-idsp.wadhwaniai.org/api/dashboard?dashboard_type=1";
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoibXNjYW4wMSIsInVzZXJfc3RhdGUiOiIiLCJleHAiOjE2ODEyODExODh9.wyt_BmQqnad_UFV8Wy3qaU9_EbI7SElRxwd9qiye6vQ',
      }
    })
    
    const res = await response.json();
    return res.data.token;
  }

  useEffect(() => {


    const embed = async () => {
      await embedDashboard({
        // id: "14216a07-b423-48d5-8e24-320ac35f95de", // given by the Superset embedding UI
        id: "14216a07-b423-48d5-8e24-320ac35f95de",
        supersetDomain: "http://43.205.125.156:8088",
        mountPoint: document.getElementById("dashboard"), // html element in which iframe render
        fetchGuestToken: () => guestTokenFromBackend(),
        dashboardUiConfig: {
          hideTitle: true,
          hideChartControls: true,
          hideTab: true,
        },
      })
    }
    if (document.getElementById("dashboard")) {
      embed()
    }

  }, [])

  return (
    <div className="App" style={{width: '100%', height: '100%'}}>
      {/* <h1>How to Embed Superset Dashboard into React</h1> */}
      <div id="dashboard" style={{width: '100%', height: '100%'}}>
        <h1>Home</h1>
      </div>
    </div>
  )
}

export default App
