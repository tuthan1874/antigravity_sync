# Phân tích & Cải tiến `generate_mesh_canny.py`

## Kết quả chạy thử trên hero1

Script đã chạy **thành công 100%** - xử lý 52/52 parts, 0 lỗi.

### Thống kê tổng quan

| Metric | Giá trị |
|--------|---------|
| Tổng parts xử lý | 52 |
| Tổng vertices | 1,748 |
| Tổng triangles | 1,761 |
| Trung bình verts/part | 33.6 |
| Trung bình tris/part | 33.9 |
| File size | 9.7KB → 210.4KB (x21.8) |

### Phân bố Internal Points

| Nhóm | Số lượng | Ví dụ |
|-------|----------|-------|
| Nhiều internal points (5+) | 5/52 | `chest` (35), `gun` (15), `chest_front` (10) |
| Ít internal points (1-4) | 22/52 | `arm_l` (4), `hat` (4), `head` (4) |
| Không có internal (0) | **25/52** | `jacket_back`, `palm_l`, `leg_lower_l`... |

> [!WARNING]
> **25/52 parts (48%) không có internal vertex nào.** Canny edge detection không phát hiện được cạnh nội bộ ở gần nửa số parts → mesh sẽ chỉ có hull vertices, biến dạng kém khi animate.

---

## Các vấn đề phát hiện

### 1. 🔴 Internal detection yếu (48% parts = 0 internal)
**Nguyên nhân:** Canny threshold cố định (50-150) không phù hợp cho tất cả loại ảnh. Parts nhỏ (finger, foot) hoặc parts có ít chi tiết (legs, belt) Canny không tìm được edge nào đủ dài.

### 2. 🟡 Hull vertex quá nhiều cho parts nhỏ
`jacket_back` có 54 hull vertices cho ảnh 699x384 nhưng 0 internal. Ngược lại, `finger2_l` chỉ có 13 vertices cho 83x56. Hull spacing cố định 15px không scale theo kích thước part.

### 3. 🟡 Không có fallback khi Canny thất bại
Khi Canny không tìm thấy edge nào, part chỉ có hull vertices mà không có nội bộ → biến dạng không tự nhiên cho parts lớn.

### 4. 🟠 File output tăng x22 kích thước
210KB cho 52 parts là hợp lý cho mesh data, nhưng có thể tối ưu bằng cách giảm decimal precision.

### 5. 🟠 Không có visualization/debug output
Không có cách nào kiểm tra mesh trực quan trước khi import vào Spine.

### 6. 🟡 Không support batch xử lý nhiều hero
Script chỉ xử lý 1 file JSON mỗi lần.

---

## Đề xuất cải tiến

### Improvement 1: Adaptive Internal Point Generation (Ưu tiên cao)
**Vấn đề:** 48% parts không có internal point.
**Giải pháp:** Khi Canny không tìm đủ internal points, fallback sang **grid-based sampling** bên trong hull.

```
Nếu internal_points < min_required:
  → Tạo grid đều bên trong hull (spacing dựa theo kích thước part)
  → Filter chỉ giữ points nằm trong alpha mask
```

#### [MODIFY] [generate_mesh_canny.py](file:///e:/TDC_App/TDGAMES_App/Auto_Mesh_Spine/generate_mesh_canny.py)
- Thêm hàm `generate_grid_fallback()` sau `detect_internal_edges()`
- Gọi fallback trong `process_skeleton()` khi Canny trả về ít điểm

---

### Improvement 2: Adaptive Canny Thresholds (Ưu tiên cao)
**Vấn đề:** Threshold 50-150 cố định.
**Giải pháp:** Tự động tính threshold dựa trên **Otsu's method** hoặc median pixel intensity.

```python
median = np.median(gray[alpha_mask > 0])
canny_low = int(max(0, 0.66 * median))
canny_high = int(min(255, 1.33 * median))
```

#### [MODIFY] [generate_mesh_canny.py](file:///e:/TDC_App/TDGAMES_App/Auto_Mesh_Spine/generate_mesh_canny.py)
- Thêm option `--auto-canny` để tự tính threshold
- Giữ manual threshold làm override

---

### Improvement 3: Adaptive Hull Spacing (Ưu tiên trung bình)
**Vấn đề:** Hull spacing 15px cố định → quá nhiều vertices cho parts lớn, quá ít cho parts nhỏ.
**Giải pháp:** Tính hull spacing dựa theo **perimeter ratio**.

```python
perimeter = contour_perimeter(hull_pts)
adaptive_spacing = max(8, min(30, perimeter / target_hull_vertices))
# target_hull_vertices vd: 20-30 vertices
```

#### [MODIFY] [generate_mesh_canny.py](file:///e:/TDC_App/TDGAMES_App/Auto_Mesh_Spine/generate_mesh_canny.py)
- Thêm option `--target-hull-count` (mặc định 25)
- Tính spacing tự động per-part

---

### Improvement 4: Debug Visualization Output (Ưu tiên trung bình)
**Giải pháp:** Thêm option `--debug` để xuất ảnh PNG cho mỗi part, vẽ:
- Hull contour (xanh)
- Internal points (đỏ)
- Triangles (xám nhạt)
- Canny edges (trắng)

#### [MODIFY] [generate_mesh_canny.py](file:///e:/TDC_App/TDGAMES_App/Auto_Mesh_Spine/generate_mesh_canny.py)
- Thêm hàm `save_debug_image()`
- Thêm `--debug` flag + `--debug-dir` option

---

### Improvement 5: Output Size Optimization (Ưu tiên thấp)
- Giảm UV precision từ 5 decimal → 4
- Giảm vertex precision từ 2 decimal → 1
- Sử dụng `separators=(',', ':')` trong `json.dump` thay vì tab indent

---

### Improvement 6: Batch Processing (Ưu tiên thấp)
**Giải pháp:** Thêm option `--batch` để xử lý tất cả `.json` files trong một thư mục.

```bash
python generate_mesh_canny.py --batch hero_folder/ --images-subdir images
```

---

### Improvement 7: Statistics Summary Report (Ưu tiên thấp)
Thêm bảng tổng kết cuối với:
- Min/Max/Avg vertices per part
- Parts không có internal points
- Cảnh báo parts quá lớn/nhỏ

---

### Improvement 8: Multi-scale Canny (Ưu tiên trung bình)
Chạy Canny ở nhiều scale (blur levels) và merge edges → phát hiện được cả chi tiết lớn lẫn nhỏ.

---

## Open Questions

> [!IMPORTANT]
> 1. **Bạn muốn ưu tiên cải tiến nào trước?** Gợi ý: Improvement 1 (Grid fallback) + 4 (Debug visualization) sẽ cho hiệu quả lớn nhất ngay.
> 2. **Bạn có muốn xem debug visualization** để kiểm tra mesh quality trước khi quyết định?
> 3. **Mục tiêu số vertices trung bình** cho mỗi part là bao nhiêu? Hiện tại ~33, có cần tăng/giảm?
> 4. **File output cần compact (nhỏ gọn)** hay giữ tab indent để dễ đọc?

## Verification Plan

### Automated Tests
- Chạy script trên hero1 trước/sau cải tiến, so sánh metrics
- Kiểm tra output JSON vẫn valid cho Spine import
- So sánh số internal points trước/sau

### Manual Verification
- Tạo debug visualization images, kiểm tra mesh quality bằng mắt
- Import output JSON vào Spine Editor để test biến dạng thực tế
