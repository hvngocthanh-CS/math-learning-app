import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import { Toaster } from 'react-hot-toast'
import App from './App.jsx'
import { AuthProvider } from './features/auth'
import './styles/index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <App />
        <Toaster
          position="top-right"
          toastOptions={{
            duration: 3000,
            style: { borderRadius: '12px', fontFamily: 'Nunito, sans-serif', fontWeight: 600 },
            success: { iconTheme: { primary: '#34D399', secondary: '#fff' } },
            error: { iconTheme: { primary: '#FF2D78', secondary: '#fff' } },
          }}
        />
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>,
)
