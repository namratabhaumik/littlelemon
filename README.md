## LittleLemon Web Application

### Description

The LittleLemon Web Application is a fully dynamic and scalable web application built using Django as part of the Meta Backend Developer Specialization. The goal of this project was to explore CI/CD using Github Actions. It includes functionalities like product management, inventory tracking and order handling. The project follows modern web development practices and integrates advanced tools for deployment and automation, ensuring a smooth and efficient user experience.

### Features

- **Product Management**: Admin users can add, update, and delete products. Each product includes details like name, price, and description.
- **Inventory Tracking**: Manage inventory levels, monitor stock availability, and track changes in real-time.
- **Menu Display**: The restaurant menu is available for customers to view, showcasing available products and their details.
- **Order Handling**: Admins can process orders, updating inventory levels based on new orders and ensuring stock data is accurate.
- **RESTful API**: Exposed APIs allow for easy integration with external systems and support CRUD operations for menu items and orders.

### Technologies Used

- **Django**: A powerful and efficient web framework for rapid backend development in Python.
- **Python**: The primary programming language for the backend.
- **Django Rest Framework (DRF)**: A toolkit for building RESTful APIs with Django, enabling seamless communication between frontend and backend.
- **MySQL**: A robust relational database for storing application data, including product and inventory details.
- **HTML, CSS**: Used for creating a simple, clean, and user-friendly interface for the web application.
- **GitHub Actions**: A CI/CD tool for automating the build, test, and deployment process. It ensures that code is consistently integrated, tested, and deployed to production without manual intervention.
- **Render**: A platform for deploying the Django application, handling environment variables, and scaling the application as needed.

### CI/CD Pipeline

The LittleLemon project integrates a fully automated **CI/CD pipeline** using **GitHub Actions**. The pipeline follows the **build, test, and deploy** stages:
- **Build**: Installs dependencies, sets up a virtual environment, and ensures that the app runs in the correct environment.
- **Test**: Runs automated tests to ensure functionality works as expected. It also includes integration testing with a live MySQL database by using **ngrok** for tunneling local ports to GitHub Actions.
- **Deploy**: If the tests pass, the app is automatically deployed to **Render**, where the production environment is managed and scaled.

### APIs Created

The application exposes two key RESTful APIs:
- **GET API**: `/restaurant/get_menu` – Fetches the current menu, including all products and their details.
- **POST API**: `/restaurant/modify_menu` – Allows admins to modify the menu, add new products, or update existing ones.

### Deployment and Environment Management

The deployment process is entirely automated using **GitHub Actions**, ensuring that new features and bug fixes are quickly integrated and deployed. The application is hosted on **Render**, a platform that provides seamless integration with GitHub for continuous deployment. To keep sensitive information secure, critical environment variables (like `SECRET_KEY`, `DB_PASSWORD`) are stored in **GitHub Secrets**, ensuring they are kept out of the codebase and properly encrypted.

### Challenges Faced and Solutions

- **MySQL in CI/CD**: GitHub-hosted runners do not have MySQL pre-installed, so it was configured as a service to work with the CI pipeline. A retry mechanism was introduced to ensure the database was ready before running Django migrations.
- **ALLOWED_HOSTS Issue**: During deployment, Render was not picking up the `ALLOWED_HOSTS` setting from the `.env` file, causing a `DisallowedHost` error. The solution was to explicitly define `ALLOWED_HOSTS` in the deployment settings on Render, ensuring consistency across environments.
- **Local Development Constraints**: Initially, GitHub Actions could not access the locally running MySQL instance, so **ngrok** was introduced to tunnel the local database to a public URL. This allowed integration tests to run against a live database, mimicking the production environment more closely.

### Conclusion

The LittleLemon project is an excellent showcase of Django's power and flexibility in handling backend development, while also demonstrating my ability to set up and manage an automated CI/CD pipeline using GitHub Actions. This project has provided hands-on experience in deploying, testing, and managing production-grade applications with robust security and scalability.
