# Thai Site
Dự án Thai Site là một ứng dụng web được xây dựng bằng framework Django (Python). Trang web cung cấp các tính năng cơ bản như quản lý khóa học, trang giới thiệu, liên hệ, đăng nhập/đăng ký người dùng và tích hợp thông tin thời tiết.

## 🚀 Các tính năng chính
Quản lý khóa học: Xem danh sách khóa học và chi tiết khóa học.

Xác thực người dùng: Đăng ký và đăng nhập tài khoản.

Thông tin cá nhân: Các trang về giới thiệu (about) và liên hệ (contact).

Tích hợp: Hiển thị thông tin thời tiết (weather).

Quản trị: Sử dụng Django Admin để quản lý nội dung.

## 🛠 Công nghệ sử dụng
Backend: Python, Django

Database: SQLite (mặc định)

Frontend: HTML, CSS, JavaScript

## 📦 Cấu trúc thư mục
``` Plantext
thai_site/
├── homepage/          # Ứng dụng chính của dự án
│   ├── migrations/    # Các tệp migration của database
│   ├── static/        # Tệp tĩnh (CSS, JS, images)
│   ├── templates/     # Các tệp giao diện HTML
│   ├── models.py      # Định nghĩa các model dữ liệu
│   ├── views.py       # Xử lý logic nghiệp vụ
│   ├── urls.py        # Định tuyến URL của ứng dụng
│   └── forms.py       # Xử lý form đăng ký/đăng nhập
├── thai_site/         # Thư mục cấu hình project Django (settings, wsgi, v.v.)
├── manage.py          # Script quản lý Django
├── db.sqlite3         # Database
└── .env               # Tệp cấu hình biến môi trường
```
## ⚙️ Hướng dẫn cài đặt
Clone dự án:

```Bash
git clone <link-repository-cua-ban>
cd thai_site
```

Tạo môi trường ảo (Virtual Environment):
```Bash
python -m venv .env
```

## Kích hoạt môi trường ảo
```Bash
source .env/bin/activate  # Trên Linux/macOS
.env\Scripts\activate     # Trên Windows
```

Cài đặt các gói phụ thuộc:

```Bash
pip install -r requirements.txt
```

Chạy Migration:

```Bash
python manage.py migrate
```

Khởi chạy máy chủ:

```Bash
python manage.py runserver
```
Truy cập vào địa chỉ [http://127.0.0.1:8000](http://127.0.0.1:8000) để xem kết quả.

