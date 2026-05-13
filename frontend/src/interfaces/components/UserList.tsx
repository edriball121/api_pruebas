import { useState, useEffect } from 'react'
import type { User } from '../../domain/entities'
import { UserUseCases } from '../../application/use-cases'
import { HttpUserRepository } from '../../infrastructure/http-repositories'

export function UserList() {
  const [users, setUsers] = useState<User[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const loadUsers = async () => {
      const repo = new HttpUserRepository()
      const useCase = new UserUseCases(repo)
      const data = await useCase.getAllUsers()
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