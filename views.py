from app import app
from flask import redirect, abort
from flask import Flask, request,render_template

app = Flask(__name__)


users_name = [
    {
        "id": 1,
        "name": "Igor",
    },
    {
        "id": 2,
        "name": "Igor",
    },
    {
        "id": 3,
        "name": "Julia",
    },
    {
        "id": 4,
        "name": "Igor",
    },
    {
        "id": 5,
        "name": "Igor",
    },
    {
        "id": 6,
        "name": "Igor",
    },
    {
        "id": 7,
        "name": "Igor",
    },
    {
        "id": 8,
        "name": "Igor",
    },
    {
        "id": 9,
        "name": "Igor",
    },
    {
        "id": 10,
        "name": "Igor",
    }
]

books_name = [
    {
        "author": "dfghjkl",
        "title": "Igor",
    },
    {
        "author": "dfghjkl",
        "title": "Igor",
    },
    {
        "author": "dfghjkl",
        "title": "Julia",
    },
    {
        "author": "dfghjkl",
        "title": "Igor",
    },
    {
        "author": "dfghjkl",
        "title": "Igor",
    },
    {
        "author": "dfghjkl",
        "title": "Igor",
    },
    {
        "author": "dfghjkl",
        "title": "Igor",
    },
    {
        "author": "dfghjkl",
        "title": "Igor",
    },
    {
        "author": "dfghjkl",
        "title": "Igor",
    },
    {
        "author": "dfghjkl",
        "title": "Igor",
    }
]


@app.get("/users")
def name_randomizator(name_id=''):
    users_html = ''.join([
        f"<li> {random_name['id']} {random_name['name']} </li>"
        for random_name in users_name
    ])
    response = f'''
    <h1> Random name <h1>
    <ul>
        {users_html}
    </ul>
    '''

    return response, 200


@app.get("/books")
def book_list():
    books_html = ''.join([
        f"<li> {author_name['author']} {title['title']} </li>"
        for author_name in books_name
        for title in books_name
    ])
    response = f'''
    <h1> Books list <h1>
    <ul>
        {books_html}
    </ul>
    '''

    return response, 200


@app.get(f"/users/user_info")
def process_user_info():
    transformed_records = []
    for user in users_name:
        transformed_user = {}
        user_id = user.get("id")
        user_name = user.get("name")
        if user_id is not None and user_id % 2 == 0:
            transformed_user["result"] = f"{user_name}: {user_id}"
        else:
            transformed_user["result"] = "404 Not Found"
        transformed_records.append(transformed_user)
    return transformed_records


transformed_users = process_user_info()
print(transformed_users)


@app.get(f"/books/books_title")
def transform_book_titles():
    transformed_records = []
    for book in books_name:
        transformed_book = {}
        for key, value in book.items():
            if isinstance(value, str):
                transformed_book[key] = value.capitalize()
            elif isinstance(value, dict):
                transformed_book[key] = transform_book_titles(value)
            else:
                transformed_book[key] = value
        transformed_records.append(transformed_book)
    return transformed_records


transformed_books = transform_book_titles()
print(transformed_books)


@app.route('/params', methods=['GET'])
def process_params():
    # Отримати query parameters з URL
    params = request.args

    # Створити HTML таблицю з параметрами
    table_html = '<table>\n'
    table_html += '<tr><th>parameter</th><th>value</th></tr>\n'
    table_html += '<tr><th>name </th><th>Test/th></tr>\n'
    table_html += '<tr><th>age</th><th>1</th></tr>\n'

    for key, value in params.items():
        table_html += f'<tr><td>{key}</td><td>{value}</td></tr>\n'
    table_html += '</table>'

    # Повернути HTML відповідь
    return table_html



# Кастомний обробник помилки 404
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Кастомний обробник помилки 500
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Формування HTML форми для методу GET
        form_html = '''
        <form method="POST" action="/login">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br><br>
            <input type="submit" value="Submit">
        </form>
        '''
        return form_html
    elif request.method == 'POST':
        # Отримання даних з запиту POST
        username = request.form.get('username')
        password = request.form.get('password')

        # Валідація username
        if len(username) < 5:
            abort(400, 'Username should be at least 5 characters long')

        # Валідація password
        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(
                char.isupper() for char in password):
            abort(400,
                  'Password should be at least 8 characters long and contain at least 1 digit and 1 uppercase letter')

        # Якщо валідація успішна, перенаправлення користувача на сторінку /users
        return redirect('/users')
@app.route('/users')
def users():
    return 'Welcome to the users page!'

@app.route('/')
def home():
    html_code = '''
    <h1>Welcome to the Home Page!</h1>
    <ul>
        <li><a href="/login">Login</a></li>
        <li><a href="/users">Users</a></li>
        <li><a href="/books">Books</a></li>
        <li><a href="/params">Params</a></li>
    </ul>
    '''
    return html_code


if __name__ == '__main__':
    app.run()
