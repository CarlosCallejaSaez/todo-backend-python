# FastAPI Todo Backend

This is a project of a To Do application developed with FastAPI and MongoDB.




## API Endpoints

| Method | Endpoint              | Description                  |
|--------|-----------------------|------------------------------|
| GET    | `/`                   | Author Message               |
| GET    | `/api/todo`           | Get all todos                |
| GET    | `/api/todo/{title}`   | Get a todo by title          |
| POST   | `/api/todo`           | Create a new todo            |
| PUT    | `/api/todo/{title}`   | Update a todo by title       |
| DELETE | `/api/todo/{title}`   | Delete a todo by title       |
| ANY    | `/{path:path}`        | Custom 404 Handling          |


