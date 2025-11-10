# Django Polls Application

A Django web application for creating and managing polls

## What You Need First

Before you can run this project, you'll need a couple of things installed on your computer:

**Python 3.13 or higher**
- This is the programming language Django uses. To check if you have it, open your terminal and type:
  ```bash
  python3 --version
  ```
- If you don't have it or have an older version, you'll need to install it first.

**uv**
- This is a tool that helps install Python packages (like Django) really fast. It's way better or rather easier than using pip to install all the requirements.
- Here's how to install it:

  **If you're on Mac and have Homebrew:**
  ```bash
  brew install uv
  ```
  
  **Or you can use pip (works everywhere):**
  ```bash
  pip install uv
  ```

## Getting Started

### Step 1: Get the Code

First, you need to download this project from GitHub.

1. Go to the repository page: https://github.com/doreenr/django-polls
2. Click the green "Code" button near the top right
3. Copy the HTTPS URL (it should look like `https://github.com/doreenr/django-polls.git`)
4. Open your terminal and navigate to the folder where you want to place the project:
   ```bash
   cd /path/to/your/projects/folder
   ```
   (Replace `/path/to/your/projects/folder` with wherever you want to keep your projects, like `~/Projects` or `~/Documents/code`)
5. Run the clone command:
   ```bash
   git clone https://github.com/doreenr/django-polls.git
   ```
6. Navigate into the project folder:
   ```bash
   cd django-polls
   ```

### Step 2: Install Everything

This is the magic command that sets everything up:
```bash
uv sync
```

**What does this do?** It basically sets up everything you need. It creates a virtual environment (think of it as a separate space for this project), installs Python if you don't have the right version, and downloads Django and all the other stuff the project needs. It's like a one-click setup button!

### Step 3: Activate the Virtual Environment

After `uv sync` finishes, you need to "activate" the virtual environment. This tells your computer to use the Python and packages from this project.

**On Mac/Linux:**
```bash
source .venv/bin/activate
```

**On Windows:**
```bash
.venv\Scripts\activate
```

You'll know it worked when you see `(.venv)` or the '(project-name)' at the start of your terminal prompt.


### Step 4: Set Up the Database

Django needs a database to store information. Run this command to create it:
```bash
python manage.py migrate
```

**What's happening here?** Django is creating a database file (it's called `db.sqlite3`) and setting up all the tables it needs. 

### Step 5: Create an Admin Account (Optional but Recommended)

If you want to use Django's admin page (which is super helpful for managing polls), create an admin account:
```bash
python manage.py createsuperuser
```

It will ask you for a username, email, and password. Just follow the prompts!

Here access the admin page at `http://127.0.0.1:8000/admin/` where you can manage polls through a web interface instead of typing commands.

### Step 6: Start the Server

Start the Django development server:

```bash
python manage.py runserver
```

You should see something like "Starting development server at http://127.0.0.1:8000/". That means it's working!

**What's this doing?** It's starting a web server on your computer. The server automatically reloads when you change code, which is super convenient. When you want to stop it, just press `Ctrl+C`.

### Step 7: Open It in Your Browser

Once the server is running, open your web browser and go to:
- **Main page:** `http://127.0.0.1:8000/`
- **Admin page:** `http://127.0.0.1:8000/admin/` (if you created a superuser)
- **Polls page:** `http://127.0.0.1:8000/polls/`


#
```


**Adding new packages:**
If you want to add a new Python package:
1. Open `pyproject.toml` and add it to the dependencies list
2. Run `uv sync` to install it
3. That's it! uv handles the rest


- **Python 3.13+** - The programming language
- **Django 5.2.8** - The web framework (makes building web apps way easier)
- **uv** - The package manager (super fast!)
- **SQLite** - The database (comes built-in, perfect for learning)

## Links
- [Django Documentation](https://docs.djangoproject.com/) - The official docs 
- [uv Documentation](https://github.com/astral-sh/uv) - Learn more about uv
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) - The official Django tutorial
