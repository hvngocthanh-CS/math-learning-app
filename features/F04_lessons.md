# F04 - Grade Selection & Lesson System

**Phase**: 1 (Uu tien cao nhat)
**Screen**: S-02, S-03, S-04

## Mo ta

He thong chon lop, danh sach bai hoc va noi dung bai hoc theo chuong trinh giao duc tieu hoc.

## Chuc nang chi tiet

### S-02: Chon khoi lop
- Grid hien thi Lop 1 -> Lop 5
- Progress bar theo tung lop (% hoan thanh)
- Click chon lop -> chuyen sang danh sach bai hoc

### S-03: Danh sach bai hoc
- Danh sach chuong (Accordion UI)
- Moi bai co trang thai:
  - **Locked**: Chua mo khoa (icon khoa)
  - **In Progress**: Dang hoc (icon dang lam)
  - **Completed**: Da hoan thanh (icon tick)
- Lock/Unlock logic: Bai sau mo khi hoan thanh >= 80% bai truoc
- Breadcrumb: Grade -> Chapter -> Lesson

### S-04: Noi dung bai hoc
- Video bai giang
- Slide bai giang sinh dong
- Mini interactions (quiz nho giua bai de kiem tra hieu bai)
- CTA: "Lam bai tap" -> chuyen sang S-05 (Quiz)

## Noi dung hoc tap
- Bai hoc toan tu Lop 1 den Lop 5
- Theo chuong trinh giao duc tieu hoc Viet Nam
- Cac dang: So hoc, Hinh hoc, Do luong, Thong ke

## Navigation
- S-02 -> S-03 (Chon lop -> Danh sach bai)
- S-03 -> S-04 (Chon bai -> Noi dung)
- S-04 -> S-05 (Hoan thanh bai -> Lam quiz)
