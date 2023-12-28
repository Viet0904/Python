#Dictionaries: cú pháp là {key1: value1, key2: value2,..., keyN: valueN}
# là một kiểu dữ liệu lưu trữ các giá trị chứa key và value
# Dictionaries là 1 danh sách sắp xếp theo thứ tự, có thể thay đổi và không cho phép trùng lặp.
    # - Key
        #   +Các phần tử đều phải có key.
        #   + Và Key chỉ có thể là số hoặc chuỗi.
        #   +Key phải là duy nhất, nếu không nó sẽ nhận giá trị của phần tử có key được xuất hiện cuối cùng.
        #   +Key khi đã được khai báo thì không thể đổi được tên.
        #   +Key có phân biệt hoa thường.
progaming_dictionary = {
    "Bug": "An error in a program",
    "Function": "A piece of code that you can easily"
}
# truy cập vào phần từ của Dictionaries thông qua key
print(progaming_dictionary["Bug"]) # in ra value

# thêm 1 phần tử vào Dictionaries 
progaming_dictionary["Loop"] = "The action of doing something over and over again. "
print(progaming_dictionary)

# Chỉnh sửa 1 phần tử trong Dictionaries
progaming_dictionary["Bug"]  = "Da chinh sua"
print(progaming_dictionary["Bug"])
# lặp qua progaming_dictionary để lấy ra key và value.
for key,val in progaming_dictionary.items():
    print(f"{key}: {val}")