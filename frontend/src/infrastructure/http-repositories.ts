import { User, Post } from '../domain/entities'
import { UserRepository, PostRepository } from '../domain/repositories'

const API_BASE = import.meta.env.VITE_API_URL || 'https://api-pruebas-y9uv.onrender.com'

export class HttpUserRepository implements UserRepository {
  async getAll(): Promise<User[]> {
    const response = await fetch(`${API_BASE}/api/users`)
    return response.json()
  }

  async getById(id: number): Promise<User | null> {
    const response = await fetch(`${API_BASE}/api/users/${id}`)
    if (!response.ok) return null
    return response.json()
  }

  async getPostsByUserId(userId: number): Promise<Post[]> {
    const response = await fetch(`${API_BASE}/api/users/${userId}/posts`)
    return response.json()
  }
}

export class HttpPostRepository implements PostRepository {
  async getAll(): Promise<Post[]> {
    const response = await fetch(`${API_BASE}/api/posts`)
    return response.json()
  }

  async getById(id: number): Promise<Post | null> {
    const response = await fetch(`${API_BASE}/api/posts/${id}`)
    if (!response.ok) return null
    const data = await response.json()
    return {
      id: data.id,
      user_id: data.userId,
      title: data.title,
      body: data.body
    }
  }

  async getByUserId(userId: number): Promise<Post[]> {
    const response = await fetch(`${API_BASE}/api/posts?userId=${userId}`)
    const data = await response.json()
    return data.map((p: any) => ({
      id: p.id,
      user_id: p.userId,
      title: p.title,
      body: p.body
    }))
  }

  async getDashboard(): Promise<any> {
    const response = await fetch(`${API_BASE}/api/dashboard`)
    return response.json()
  }
}