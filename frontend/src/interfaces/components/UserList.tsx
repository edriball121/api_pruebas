import { useState, useEffect } from 'react'
import type { User } from '../../domain/entities'

const API_BASE = import.meta.env.VITE_API_URL || 'https://api-pruebas-y9uv.onrender.com'

export function UserList() {
  const [users, setUsers] = useState<User[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const loadUsers = async () => {
      const response = await fetch(`${API_BASE}/api/users`)
      const data = await response.json()
      setUsers(data)
      setLoading(false)
    }
    loadUsers()
  }, [])

  if (loading) return <div>Cargando usuarios...</div>

  return (
    <div>
      <h1>Usuarios</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            <strong>{user.name}</strong> - {user.email}
          </li>
        ))}
      </ul>
    </div>
  )
}