# CookieBox
Huyền có s cái bánh quy, mỗi cái bánh quy nằm vừa trong 1 ô vuông kích thước 1x1. Huyền muốn tạo ra một cái hộp kích thước mxn để có thể chứa hết s cái bánh. (Hộp có thể đựng được nhiều hơn s cái bánh quy, nhưng Huyền chỉ có s cái bánh nên những ô còn lại Huyền phải để trống).

Huyền muốn tạo ra hộp kích thước mxn theo tiêu chí sau:

Hộp đó có thể đựng được hết số bánh Huyền có.
Hộp đó có chu vi nhỏ nhất.
Nếu có nhiều hộp có cùng chu vi thì chọn hộp dư ít ô trống nhất.
Nếu có nhiều hộp có cùng chu vì và dư ít ô trống nhất thì đưa ra hộp có chỉ số m nhỏ nhất.
Cho số bánh quy s, hãy tìm và in ra mảng kết quả là [m,n].

Ví dụ:

Với s = 7, thì CookieBox=[2,4].
Giải thích:
Có vô số hộp bánh có thể chứa được 7 cái bánh, nhưng hộp có chu vi nhỏ nhất là các hộp có kích thước 2x4, 3x3, 4x2.
Trong 3 hộp đó thì 2 hộp 2x4 và 4x2 sẽ dư 1 ô trống, còn hộp 3x3 dư 2 ô trống.
Trong 2 hộp 2x4 và 4x2 thì chỉ số m nhỏ nhất là hộp 2x4.
