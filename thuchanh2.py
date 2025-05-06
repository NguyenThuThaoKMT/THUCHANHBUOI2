import requests

# Thông tin cần thiết
access_token = 'EAAas79OGVL8BO7s9ZC7qSjhzgjuBhgkpwd8EOwBJusKxXW04unMJtQlcF1M4qSECjwAX9gIrkL7ihd2kHl8iHwYZCS90ZBlTygqSZA7ZCqLmZCSLnF0ap6fmHjO29S9iOgXaUP8yWYBrI9qRPyrZB33hWpxiT4rv03IhBn3ioZAr1dbbjg08M1BH0UsGxiYwZAtSp3HZCzr3SeFfW41Y5xXPEF7IwG'  # Thay bằng access token của bạn
page_id = '566715649869474'            # Thay bằng ID của trang bạn quản lý
message = 'Nguyễn Thu Thảo Thực Hành BUổi 2'  # Nội dung bài đăng

# URL API của Facebook để đăng bài
url = f'https://graph.facebook.com/{page_id}/feed'

# Dữ liệu gửi đi
payload = {
    'message': message,
    'access_token': access_token
}

# Gửi yêu cầu POST đến Facebook Graph API
response = requests.post(url, data=payload)

# Xử lý kết quả
if response.status_code == 200:
    print("✅ Đăng bài thành công!")
    print("ID bài viết:", response.json().get('id'))
else:
    print("❌ Lỗi khi đăng bài:")
    print(response.status_code)
    print(response.text)