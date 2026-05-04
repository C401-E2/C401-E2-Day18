# Individual Reflection - Lab 18

**Tên:** Tiến  
**Module phụ trách:** M1

## 1. Đóng góp kỹ thuật

- Module đã implement: M1 - Advanced Chunking
- Các hàm/class chính đã viết: `chunk_basic`, `chunk_semantic`, `chunk_hierarchical`, `chunk_structure_aware`, `compare_strategies`
- Số tests pass: 8/8

## 2. Kiến thức học được

- Khái niệm mới nhất: chunking theo cấu trúc và theo ngữ nghĩa
- Điều bất ngờ nhất: hierarchical chunking phải giữ liên kết parent-child rõ ràng
- Kết nối với bài giảng: document preprocessing cho RAG

## 3. Khó khăn & Cách giải quyết

- Khó khăn lớn nhất: xử lý text đa dạng, có markdown, paragraph, và trường hợp PDF
- Cách giải quyết: viết fallback đơn giản nhưng đúng output contract của test
- Thời gian debug: vài giờ

## 4. Nếu làm lại

- Sẽ thêm sentence splitter tốt hơn
- Muốn benchmark chunk quality trên corpus lớn hơn

## 5. Tự đánh giá

| Tiêu chí | Tự chấm (1-5) |
|----------|---------------|
| Hiểu bài giảng | 4 |
| Code quality | 4 |
| Teamwork | 4 |
| Problem solving | 4 |
