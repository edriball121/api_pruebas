import { useState, useEffect } from 'react'
import type { User, Post } from '../../domain/entities'

interface DashboardData {
  total_users: number
  total_posts: number
  total_comments: number
  users: { id: number; name: string; username: string; email: string; post_count: number }[]
  recent_posts: { id: number; user_id: number; title: string; body: string }[]
  user_distribution: Record<string, number>
}

export function Dashboard() {
  const [data, setData] = useState<DashboardData | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const fetchDashboard = async () => {
    try {
      const response = await fetch('/api/dashboard')
      if (!response.ok) throw new Error('Failed to fetch dashboard data')
      const result = await response.json()
      setData(result)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchDashboard()
    const interval = setInterval(fetchDashboard, 10000)
    return () => clearInterval(interval)
  }, [])

  if (loading) return <div className="loading">Loading dashboard...</div>
  if (error) return <div className="error">Error: {error}</div>
  if (!data) return <div>No data available</div>

  return (
    <div className="dashboard">
      <h1>📊 Dashboard</h1>
      
      <div className="stats-grid">
        <div className="stat-card">
          <h3>👥 Users</h3>
          <p className="stat-number">{data.total_users}</p>
        </div>
        <div className="stat-card">
          <h3>📝 Posts</h3>
          <p className="stat-number">{data.total_posts}</p>
        </div>
        <div className="stat-card">
          <h3>💬 Comments</h3>
          <p className="stat-number">{data.total_comments}</p>
        </div>
      </div>

      <div className="section">
        <h2>📈 Posts por Usuario</h2>
        <div className="chart">
          {Object.entries(data.user_distribution).map(([user, count]) => (
            <div key={user} className="bar">
              <span className="bar-label">{user}</span>
              <div className="bar-container">
                <div className="bar-fill" style={{ width: `${count * 10}%` }}></div>
              </div>
              <span className="bar-value">{count}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="section">
        <h2>🕒 Posts Recientes</h2>
        <ul className="posts-list">
          {data.recent_posts.map(post => (
            <li key={post.id} className="post-item">
              <strong>{post.title}</strong>
              <p>{post.body.substring(0, 100)}...</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}