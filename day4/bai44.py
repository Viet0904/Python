#List: list là một dạng dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác nhau. List được code là 1 mảng 
#List: có thể thay đổi, thêm ,sửa,xóa.
#truy xuất các phần tử bên trong nó thông qua vị trí của phần tử đó trong list.
# List có thể chứa các giá trị trùng nhau.
# append() thêm vào cuối. remove() loại bỏ 1 phần tử ở 1 thời điểm 
# https://docs.python.org/3/tutorial/datastructures.html
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
states_of_america[1] = "Banama"
print (states_of_america[1])
states_of_america.append("River") # thêm vào cuối List
print(states_of_america[-1])
states_of_america.extend(["a","b","c"]) # thêm nhiều phần tử vào cuối list
print(states_of_america)
states_of_america.remove("River") #xóa phần tử là River
print(states_of_america)
states_of_america.pop(2) # xóa phần tử ở vị trí số 2
print(states_of_america[2])
print(len(states_of_america)) # độ dài danh sách