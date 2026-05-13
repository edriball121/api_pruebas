import { User, Post } from '../entities'
import { UserRepository, PostRepository } from '../repositories'

export class UserUseCases {
  constructor(private userRepository: UserRepository) {}

  async getAllUsers(): Promise<User[]> {
    return this.userRepository.getAll()
  }

  async getUserById(id: number): Promise<User | null> {
    return this.userRepository.getById(id)
  }

  async getUserPosts(userId: number): Promise<Post[]> {
    return this.userRepository.getPostsByUserId(userId)
  }
}

export class PostUseCases {
  constructor(private postRepository: PostRepository) {}

  async getAllPosts(): Promise<Post[]> {
    return this.postRepository.getAll()
  }

  async getPostById(id: number): Promise<Post | null> {
    return this.postRepository.getById(id)
  }

  async getPostsByUserId(userId: number): Promise<Post[]> {
    return this.postRepository.getByUserId(userId)
  }
}