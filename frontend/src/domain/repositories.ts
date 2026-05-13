import { User, Post } from './entities'

export interface UserRepository {
  getAll(): Promise<User[]>
  getById(id: number): Promise<User | null>
  getPostsByUserId(userId: number): Promise<Post[]>
}

export interface PostRepository {
  getAll(): Promise<Post[]>
  getById(id: number): Promise<Post | null>
  getByUserId(userId: number): Promise<Post[]>
}