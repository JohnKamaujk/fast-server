# 🚀 fast-server

A lightweight FastAPI-based REST API server powered by PostgreSQL and containerized using Docker Compose 🐳.

## 📦 Tech Stack

- ⚡ **FastAPI** – High-performance Python web framework
- 🐘 **PostgreSQL** – Powerful open-source relational database
- 🐳 **Docker & Docker Compose** – Containerization and service orchestration
- 🧪 **SQLAlchemy** – ORM for database interaction
- 🔐 **python-dotenv** – Manage environment variables securely

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the project

```bash
git clone https://github.com/yourusername/fast-server.git
cd fast-server
```

### 2️⃣ Add your environment variables

Create a .env file inside the app/ directory:

```bash
DATABASE_URL=postgresql://john:kamau123@db:5432/fastapidb
```
📁 This will be used by SQLAlchemy to connect to the PostgreSQL container.

### 3️⃣ Run using Docker Compose

``` bash
docker compose up --build
```