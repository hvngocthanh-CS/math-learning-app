# F01 - Authentication & Authorization

**Phase**: 1 (Uu tien cao nhat)
**Screen**: S-00 Login / Register

## Mo ta
App co giao dien bang English
He thong dang ky, dang nhap va phan quyen nguoi dung.

## Chuc nang chi tiet

### Dang ky
- Input: Email/SDT, Mat khau
- Chon role khi dang ky: Hoc sinh / Phu huynh / Giao vien
- Chi Teacher duoc tao tai khoan cho Student & Parent. Khi dang ky thi sẽ cho chon role và luu role. Khi user dang nhap thi sẽ biet là role nào mà vao cho dung feature của role do
- Xac thuc email/SDT

### Dang nhap
- Dang nhap bang Email/SDT + Mat khau
- Ghi nho dang nhap (Remember me)
- Quen mat khau

### Phan quyen (3 roles)
- **Student**: Truy cap bai hoc, quiz, game, leaderboard, shop
- **Parent**: Xem tien do hoc tap cua con, bao cao
- **Teacher/Admin**: Quan ly noi dung, user, CMS

## Man hinh lien quan
- S-00: Login / Register

## Navigation
- Sau dang nhap -> redirect theo role:
  - Student -> S-01 (Student Dashboard)
  - Parent -> S-09 (Parent Dashboard)
  - Admin -> S-11 (CMS)
