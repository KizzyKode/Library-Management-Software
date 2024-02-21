# Library Management System

This is a Django-based Library Management System that allows administrators to manage books, registered users, and issued books. It also provides a user interface for registered users to view their issued books and update their profiles.

## Instructions for Running the Project

1. Ensure that you have Django installed. If not, you can install it using the following command:

   ```bash
   pip install django
   ```

2. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

3. Navigate to the project directory:

   ```bash
   cd your-repository
   ```

4. Run the migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for administrative access:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your web browser and go to [http://127.0.0.1:8000/admin_login/](http://127.0.0.1:8000/admin_login/) to log in as an admin using the superuser credentials you created.

## Project Dependencies

- Django
- Python 3

## Important Points

- **Mobile Data**: Ensure that your mobile data is turned on to enable smooth UI functionalities.

- **Admin Login**:
  - To log in as an admin, either create a superuser using the command mentioned above or use the pre-created admin details:
    - Username: kizzy
    - Password: 123456

- **User Login**:
  - To log in as a registered user, either create a registered account or use the pre-created user details:
    - Username: kizito2
    - Password: 12345

## Project Structure

- The project includes functionality for adding books, viewing books, managing registered users, issuing books, viewing issued books, and user-specific features like viewing issued books and updating profiles.

- The `library` app contains the models, views, forms, and templates for the Library Management System.

## URLs

- Admin login: [http://127.0.0.1:8000/admin_login/](http://127.0.0.1:8000/admin_login/)
- Registered User login: [http://127.0.0.1:8000/registereduser_login/](http://127.0.0.1:8000/registereduser_login/)



