const todoInput = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');

let todos = [];

addBtn.addEventListener('click', function() {
  const todoText = todoInput.value.trim();
  if (todoText !== '') {
    const todo = {
      id: Date.now(),
      text: todoText,
      completed: false
    };
    todos.push(todo);
    renderTodos();
    todoInput.value = '';
  }
});

function renderTodos() {
  todoList.innerHTML = '';
  todos.forEach(todo => {
    const li = document.createElement('li');
    li.textContent = todo.text;
    li.style.textDecoration = todo.completed ? 'line-through' : 'none';
    li.addEventListener('dblclick', () => toggleComplete(todo.id));
    todoList.appendChild(li);
  });
}

function deleteTodo(id) {
  todos = todos.filter(todo => todo.id !== id);
  renderTodos();
}

function toggleComplete(id) {
  todos = todos.map(todo => {
    if (todo.id === id) {
      return {...todo, completed: !todo.completed};
    }
    return todo;
  });
  renderTodos();
}

