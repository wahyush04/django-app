# 🖥️ PC Component Backend API (Django + MySQL)

Sebuah backend API sederhana untuk mengelola data komponen PC (CPU, GPU, RAM, dll) menggunakan Django dan database MySQL. Mendukung fitur CRUD tanpa Django Admin Panel.

---

## 🛠️ Setup dan Instalasi

### 1. Clone repository
```bash
git clone https://github.com/wahyush04/django-app.git
cd repo-name
```

### 2. Buat dan aktifkan virtual environment
```bash
python -m venv venv
venv\Scripts\activate           # Windows
# source venv/bin/activate       # Mac/Linux
```

### 3. Install dependencies
```bash
pip install django mysqlclient
```

> Jika gagal install `mysqlclient`, gunakan:
```bash
pip install pymysql
```

Lalu tambahkan ini ke `myproject/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

---

### 4. Setup konfigurasi database

Buka file `myproject/settings.py`, ubah bagian `DATABASES`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nama_database',
        'USER': 'root',
        'PASSWORD': 'password_anda',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 🚀 Menjalankan Proyek

### 1. Jalankan migrasi database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Menjalankan server lokal
```bash
python manage.py runserver
```

Server akan berjalan di `http://127.0.0.1:8000`

---

## 🌱 Menambahkan Data Dummy (Seeder)

### Jalankan seeder manual via shell:
```bash
python manage.py shell
```

Lalu jalankan:
```python
from api.models import Component

Component.objects.bulk_create([
    Component(name="Intel Core i5-12400F", brand="Intel", category="CPU", price=2300000, stock=10),
    Component(name="NVIDIA RTX 4060", brand="NVIDIA", category="GPU", price=5000000, stock=5),
    Component(name="Kingston Fury 16GB DDR4", brand="Kingston", category="RAM", price=800000, stock=20),
])
exit()
```

### Atau gunakan custom command:
```bash
python manage.py seed_components
```

---

## 📡 Endpoint API

Base URL: `http://localhost:8000/api/components/`

| Method | Endpoint               | Keterangan             |
|--------|------------------------|------------------------|
| GET    | `/components/`         | Ambil semua komponen   |
| POST   | `/components/`         | Tambah komponen baru   |
| GET    | `/components/<id>/`    | Ambil detail komponen  |
| PUT    | `/components/<id>/`    | Update komponen        |
| DELETE | `/components/<id>/`    | Hapus komponen         |

---

## 📦 Contoh Body JSON

### POST / PUT
```json
{
  "name": "AMD Ryzen 5 5600",
  "brand": "AMD",
  "category": "CPU",
  "price": 2200000,
  "stock": 15,
  "description": "6-core, 12-thread processor."
}
```

---

## ⚠️ Catatan

- **Admin panel telah dihapus.** Jika ingin menggunakan kembali, aktifkan `django.contrib.admin` di `settings.py`.
- Pastikan MySQL sudah berjalan di komputer kamu dan database sudah dibuat sebelumnya.
- Untuk testing API, bisa gunakan Postman, Insomnia, atau curl.

---

## 🧑‍💻 Author

Wahyu Syarif  
Informatics Engineering @ Universitas Teknologi Bandung  
Mentor Bangkit Academy 2024

---

## 📃 Lisensi

MIT License