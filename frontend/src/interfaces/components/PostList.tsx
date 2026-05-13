import { useState, useEffect } from 'react'
import type { Post } from '../../domain/entities'
import { PostUseCases } from '../../application/use-cases'
import { HttpPostRepository } from '../../infrastructure/http-repositories'

export function PostList() {
  const [posts, setPosts] = useState<Post[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const loadPosts = async () => {
      const repo = new HttpPostRepository()
      const useCase = new PostUseCases(repo)
      const data = await useCase.getAllPosts()
      setPosts(data)
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