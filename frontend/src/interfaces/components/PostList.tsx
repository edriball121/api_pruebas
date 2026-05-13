import { useState, useEffect } from 'react'
import type { Post } from '../../domain/entities'

const API_BASE = import.meta.env.VITE_API_URL || 'https://api-pruebas-y9uv.onrender.com'

export function PostList() {
  const [posts, setPosts] = useState<Post[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const loadPosts = async () => {
      const response = await fetch(`${API_BASE}/api/posts`)
      const data = await response.json()
      setPosts(data.map((p: any) => ({
        id: p.id,
        user_id: p.userId,
        title: p.title,
        body: p.body
      })))
      setLoading(false)
    }
    loadPosts()
  }, [])

  if (loading) return <div>Cargando posts...</div>

  return (
    <div>
      <h1>Posts</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            <strong>{post.title}</strong>
            <p>{post.body.substring(0, 100)}...</p>
          </li>
        ))}
      </ul>
    </div>
  )
}