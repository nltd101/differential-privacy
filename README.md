
# Diffential Privacy



## Một số định nghĩa
*Lưu ý:`[Tên cột]` tức là khi sử dụng thay được bằng tên của cột.*
### Bắt cặp so sánh

* ```([Tên cột]:[Giá trị])```

* **Ví dụ:** `(age:30)` nghĩa là so sánh `age` với `30`
### Toán tử so sánh
* ```{[Toán tử so sánh]:[Cặp so sánh]}```

Ký hiệu | Toán tử
------ | ----
`$gt` | >
`$lt` | <
`$eq` | =

*Lưu ý: Các toán tử khác có thể dùng những toán tử trên và toán tử logic **not** phía dưới để suy ra.*
* **Ví dụ:** `{$gt:(age:30)}` tương đương với `age>30`

### Toán tử logic
* ```{[Toán tử logic]:[[Toán tử con],..]}```

Ký hiệu | Toán tử | Số toán tử con
------ | ---- |---
`$and` | and | 2
`$or` | or | 2
`$not` | not | 1


* **Ví dụ 1:**  ​`{$and:[{$gt:(age:30)},{$lt:(age:50)}]}` tương đương với điều kiện `age>30` **và** `age<50` 
* **Ví dụ 2:**  ​`{$not:[{$gt:(age:30)}]}` tương đương với điều kiện `age<=30` 

* **Ví dụ 3** ​

```json
{
​$or:[
​ {$gt:(age:30)},
​ {$and:[
​         {$lt:(age:20)},
​         {$not:[
             {$eq:(workclass:Private)}
               ]}
        ]
​    ]
}
```
Tương đương với điều kiện sau:
```
(age>30) or (age<20 and not workclass==Private)
```

### Query hoàn chỉnh
* `[Tên cột].[Loại query]([Toán tử])`
* Ví dụ: `age.mean({$eq:(workclass:Private)})` kết quả trả về trung bình `age` của các record có `wordclass` là `Private`

#### Danh sách loại query:
* `min`: giá trị nhỏ nhất
* `max`: giá tị lớn nhất
* `mean`: trung bình
* `count`: số lượng
* `median`: ví trí giữa
* `sum`: tổng
*Lưu ý: Đối với các query số thì dữ liệu ở cột phải là số.*

## Cài đặt

Sử dụng [pip](https://pip.pypa.io/en/stable/) để cài đặt các gói cần thiết.

```bash
pip install -r requirements.txt
```

## Sử dụng

```bash
python main.py
```

## Đóng góp
Đối với các yêu cầu thay đổi, xin hãy liên lạc và thảo luận với tôi về vấn đề này.
