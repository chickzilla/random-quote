const API_URL = import.meta.env.VITE_API_URL

export async function login(email: string, password: string) {
    console.log('API_URL', API_URL)
    const res = await fetch(`${API_URL}/auth/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username: email, password: password })
    })
  
    if (!res.ok) {
      const error = await res.json()
      throw new Error(error.error)
    }
  
    return res.json()
  }

export async function register(email: string, password: string) {
    const res = await fetch(`${API_URL}/auth/register/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username: email, password: password })
    })
  
    if (!res.ok) {
      const error = await res.json()
      throw new Error(error.error)
    }
  
    return res.json()
  }