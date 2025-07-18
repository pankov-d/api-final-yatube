<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">API-FINAL-YATUBE</h1></p>
<p align="center">
	<em>Empowering APIs with seamless data interactions</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/pankov-d/api-final-yatube?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/pankov-d/api-final-yatube?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/pankov-d/api-final-yatube?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/pankov-d/api-final-yatube?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

<details><summary>Table of Contents</summary>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

</details>
<hr>

##  Overview

api-final-yatube is a robust open-source project solving seamless authentication and content management for the Yatube API. Key features include structured data representation, secure user authentication, and customizable admin interfaces. Ideal for developers seeking efficient post rendering, user interaction handling, and simplified content management within Django projects.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes **Django** framework for backend development</li><li>Follows **RESTful** design principles for API endpoints</li><li>Uses **Django REST framework** for building robust APIs</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Adheres to **PEP 8** coding style guidelines</li><li>Includes **unit tests** for critical components</li><li>Utilizes **flake8** for code linting</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive **API documentation** in **Postman collection**</li><li>Includes **inline comments** for clarity in codebase</li><li>Provides **README** with setup instructions</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates **Djoser** for user authentication</li><li>Utilizes **Simple JWT** for token-based authentication</li><li>Includes **Redoc** for rendering API documentation</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Organized into **apps** for posts, comments, and groups</li><li>Utilizes **viewsets and serializers** for data manipulation</li><li>Follows **Django app structure** for scalability</li></ul> |
| 🧪 | **Testing**       | <ul><li>Employs **pytest** for testing framework</li><li>Includes **unit tests** for models, views, and serializers</li><li>Ensures **test coverage** for critical functionalities</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes **database queries** for efficient data retrieval</li><li>Utilizes **caching mechanisms** for improved response times</li><li>Follows **best practices** for handling media files</li></ul> |
| 🛡️ | **Security**      | <ul><li>Implements **JWT tokens** for secure authentication</li><li>Enforces **custom permissions** for data access control</li><li>Follows **OWASP** security guidelines</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Manages dependencies using **pip** and **requirements.txt**</li><li>Includes essential packages like **Django**, **djangorestframework**, and **Simple JWT**</li><li>Ensures compatibility and stability across the codebase</li></ul> |

---

##  Project Structure

```sh
└── api-final-yatube/
    ├── README.md
    ├── postman_collection
    │   ├── API_for_yatube.postman_collection.json
    │   ├── README.md
    │   └── set_up_data.sh
    ├── pytest.ini
    ├── requirements.txt
    ├── setup.cfg
    ├── tests
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── fixtures
    │   │   ├── __init__.py
    │   │   ├── fixture_data.py
    │   │   └── fixture_user.py
    │   ├── test_comment.py
    │   ├── test_follow.py
    │   ├── test_group.py
    │   ├── test_jwt.py
    │   └── test_post.py
    └── yatube_api
        ├── api
        │   ├── __init__.py
        │   ├── apps.py
        │   ├── permissions.py
        │   ├── serializers.py
        │   ├── templates
        │   │   └── redoc.html
        │   ├── urls.py
        │   └── views.py
        ├── manage.py
        ├── posts
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── constants.py
        │   ├── migrations
        │   │   ├── 0001_initial.py
        │   │   ├── 0002_alter_comment_id_alter_post_id.py
        │   │   ├── 0003_group.py
        │   │   ├── 0004_alter_comment_options_alter_post_options.py
        │   │   └── __init__.py
        │   ├── models.py
        │   ├── tests.py
        │   └── views.py
        ├── static
        │   └── redoc.yaml
        └── yatube_api
            ├── __init__.py
            ├── asgi.py
            ├── settings.py
            ├── urls.py
            └── wsgi.py
```


###  Project Index
<details open>
	<summary><b><code>API-FINAL-YATUBE/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/pytest.ini'>pytest.ini</a></b></td>
				<td>- Configures test settings and paths for the pytest framework in the yatube_api project<br>- Sets up the Python path, Django settings module, and test file patterns to run tests with specific options and verbosity levels.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>Manage project dependencies using the provided requirements.txt file, ensuring compatibility and stability across the codebase architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- postman_collection Submodule -->
		<summary><b>postman_collection</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/postman_collection/set_up_data.sh'>set_up_data.sh</a></b></td>
				<td>Initialize and set up data for the Yatube API project by executing necessary commands to migrate, flush, and create default users and groups.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/postman_collection/API_for_yatube.postman_collection.json'>API_for_yatube.postman_collection.json</a></b></td>
				<td>- The provided code file "API_for_yatube.postman_collection.json" contains a Postman collection named "API_for_yatube" that includes tests for authentication scenarios<br>- This collection is crucial for ensuring the proper functioning of the authentication mechanisms within the yatube project<br>- It verifies the response structure and status codes to guarantee seamless authentication processes for regular users.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- yatube_api Submodule -->
		<summary><b>yatube_api</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/manage.py'>manage.py</a></b></td>
				<td>Manages Django administrative tasks by setting the project's settings module and executing command-line operations.</td>
			</tr>
			</table>
			<details>
				<summary><b>posts</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/posts/tests.py'>tests.py</a></b></td>
						<td>Tests the functionality of post-related features in the Yatube API to ensure proper behavior and performance within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/posts/views.py'>views.py</a></b></td>
						<td>Improve post rendering in the Yatube API by leveraging Django's render function.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/posts/apps.py'>apps.py</a></b></td>
						<td>Manages configuration for the posts app within the Django project.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/posts/constants.py'>constants.py</a></b></td>
						<td>Define maximum title length for posts in the Yatube API project.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/posts/admin.py'>admin.py</a></b></td>
						<td>- Registers Post, Group, and Comment models with Django admin to manage posts, groups, and comments<br>- Customizes PostAdmin to display key fields and enable filtering and search<br>- Improves admin interface usability for content management tasks in the Django project.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/posts/models.py'>models.py</a></b></td>
						<td>- Defines models for groups, posts, and comments with specific fields and relationships<br>- Ensures data integrity and consistency by organizing and storing user-generated content<br>- Enhances the project's functionality by providing structured data representation for user interactions within the platform.</td>
					</tr>
					</table>
					<details>
						<summary><b>migrations</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/posts/migrations/0001_initial.py'>0001_initial.py</a></b></td>
								<td>- Defines initial database migrations for creating Post and Comment models with their respective fields and relationships<br>- Sets up the necessary structure for handling user posts and comments, including text, dates, images, and author associations<br>- This file establishes the foundation for storing and managing user-generated content within the project's database.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/posts/migrations/0003_group.py'>0003_group.py</a></b></td>
								<td>- Creates a Django migration for adding a 'Group' model to the 'posts' app, including fields for title, slug, and description<br>- This migration sets up the necessary database schema changes to support the new model within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/posts/migrations/0002_alter_comment_id_alter_post_id.py'>0002_alter_comment_id_alter_post_id.py</a></b></td>
								<td>- Refactored migration file to update primary key fields for 'Comment' and 'Post' models in the Django project, ensuring compatibility with Django 5.1.1<br>- This migration alters the data schema to utilize BigAutoField for primary keys, enhancing scalability and performance of the application.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/posts/migrations/0004_alter_comment_options_alter_post_options.py'>0004_alter_comment_options_alter_post_options.py</a></b></td>
								<td>- Enhances model options for posts and comments in the Django migrations file, improving the clarity and readability of the project's content<br>- This alteration ensures that the terms used for posts and comments are more descriptive and user-friendly within the application.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>yatube_api</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/yatube_api/settings.py'>settings.py</a></b></td>
						<td>- Configures Django settings for the Yatube API project, including database setup, authentication classes, and template directories<br>- Defines middleware, authentication, and password validation settings<br>- Utilizes REST framework for pagination and JWT authentication<br>- Implements Simple JWT for token lifespan and authorization header types.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/yatube_api/urls.py'>urls.py</a></b></td>
						<td>- Defines URL patterns for the project, including admin and API routes<br>- Renders API documentation using Redoc<br>- Organizes navigation and routing for the Django application.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/yatube_api/asgi.py'>asgi.py</a></b></td>
						<td>Expose the ASGI callable as 'application' to facilitate deployment in the yatube_api project, following Django conventions.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/yatube_api/wsgi.py'>wsgi.py</a></b></td>
						<td>- Expose the WSGI callable for the yatube_api project, utilizing Django's get_wsgi_application function<br>- Set the DJANGO_SETTINGS_MODULE environment variable to 'yatube_api.settings' for deployment<br>- The wsgi.py file plays a crucial role in configuring the WSGI for the project.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>api</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/api/views.py'>views.py</a></b></td>
						<td>- Defines viewsets for Posts, Comments, and Groups with permissions to manage and retrieve data<br>- Utilizes serializers and permissions to interact with the database<br>- Facilitates creating, retrieving, updating, and deleting operations on Post and Comment objects<br>- Implements authorization logic to ensure only owners or admins can modify data.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/api/apps.py'>apps.py</a></b></td>
						<td>Defines the configuration for the API app within the Django project.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/api/urls.py'>urls.py</a></b></td>
						<td>- Expose REST API endpoints for posts, groups, comments, user authentication, and JWT tokens<br>- Utilizes Django and Django Rest Framework for routing and viewsets<br>- Integrates Djoser for user authentication<br>- The file plays a crucial role in defining the URL patterns for versioned API endpoints within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/api/serializers.py'>serializers.py</a></b></td>
						<td>- Serializers in 'serializers.py' define the structure for data representation in API responses<br>- 'PostSerializer' handles post data, 'GroupSerializer' manages group information, and 'CommentSerializer' structures comment details<br>- These serializers play a crucial role in formatting and presenting data from the database in a readable format for API endpoints.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/api/permissions.py'>permissions.py</a></b></td>
						<td>- Defines custom permissions for user ownership and admin access control in the Django REST framework, allowing safe methods for authors and admins while restricting other users<br>- The code enhances security by ensuring only authorized users can modify specific resources within the API.</td>
					</tr>
					</table>
					<details>
						<summary><b>templates</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/pankov-d/api-final-yatube/blob/master/yatube_api/api/templates/redoc.html'>redoc.html</a></b></td>
								<td>- Generates an HTML file for ReDoc documentation with adaptive design and no impact on outer page styles<br>- Displays API documentation from a specified URL using Redoc.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with api-final-yatube, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install api-final-yatube using one of the following methods:

**Build from source:**

1. Clone the api-final-yatube repository:
```sh
❯ git clone https://github.com/pankov-d/api-final-yatube
```

2. Navigate to the project directory:
```sh
❯ cd api-final-yatube
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run api-final-yatube using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/pankov-d/api-final-yatube/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/pankov-d/api-final-yatube/issues)**: Submit bugs found or log feature requests for the `api-final-yatube` project.
- **💡 [Submit Pull Requests](https://github.com/pankov-d/api-final-yatube/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/pankov-d/api-final-yatube
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/pankov-d/api-final-yatube/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=pankov-d/api-final-yatube">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
