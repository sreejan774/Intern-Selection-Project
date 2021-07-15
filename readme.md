# Intern Selection Task

### Running Project Locally 
First clone the repository to your local
```bash
git clone https://github.com/sreejan774/Intern-Selection-Project.git
```
Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```
Finally, run the development server:

```bash
python manage.py runserver
```
The project will be available at **127.0.0.1:8000**.
