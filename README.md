# EAI-kelompok-1

🛍️ JWT Marketplace API

API Marketplace berbasis **JWT (JSON Web Token)** yang dibangun menggunakan Python, dirancang untuk mengelola autentikasi pengguna, transaksi, serta operasi data dasar dalam sistem marketplace.  
Proyek ini memanfaatkan struktur modular dengan konfigurasi berbasis environment (`.env`) untuk keamanan dan fleksibilitas.

🚀 Fitur
- 🔑 **Autentikasi JWT** – Login dan verifikasi token untuk menjaga keamanan akses API.
- 👥 **Manajemen Pengguna** – Registrasi, login, dan update data pengguna.
- 💾 **Pengelolaan Data** – Operasi CRUD terhadap data marketplace (produk, transaksi, dll).
- ⚙️ **Konfigurasi .env** – Pengaturan rahasia seperti JWT secret key dan database.
- 📦 **Struktur Modular** – Mudah dikembangkan dan dimaintain.


🧰 Teknologi yang Digunakan
- **Python 3.8+**
- **Flask** *(sesuaikan jika pakai FastAPI)*
- **PyJWT** – Untuk manajemen token JWT.
- **python-dotenv** – Untuk membaca konfigurasi `.env`.
- **Requests / JSON** – Untuk komunikasi data antar endpoint.
