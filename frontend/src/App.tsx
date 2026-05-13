import { UserList } from './interfaces/components/UserList'
import { PostList } from './interfaces/components/PostList'
import { Dashboard } from './interfaces/components/Dashboard'

function App() {
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>App Clean Architecture</h1>
      <Dashboard />
      <hr style={{ margin: '30px 0' }} />
      <div style={{ display: 'flex', gap: '40px' }}>
        <div style={{ flex: 1 }}>
          <UserList />
        </div>
        <div style={{ flex: 1 }}>
          <PostList />
        </div>
      </div>
    </div>
  )
}

export default App