#Các thư viện cần thiết
import folder_op, web_op


def start():
    #Nhóm các biến toàn cục cung cấp thông số cho chương trình
    url_list = ['http:''vietnamnet.vn'] #Chứa các đường link sẽ được duyệt
    history = [] #Chứa các đường link đã duyệt
    max_page = 1000 #Quy định số lượng trang web được tải về
    count = 0  #Đếm số lượng trang web đã tải về
    data_folder = "C:\\Users\\DELL\\Downloads\\crawl\\"

    #Kịch bản tải các trang web
    while (count < max_page) and (len(url_list) > 0):
        url = url_list.pop(0)
        page = web_op.doc_noi_dung(url)
        links = web_op.lay_cac_duong_link(page)
        for item in links: #Duyệt từng đường link thu được để kiểm tra tính hợp lệ
            if web_op.kiem_tra_link(item): #Nếu đường link là hợp lệ thì tiếp tục thực hiện đoạn lệnh dưới
                item=web_op.chinh_sua_link(item) #Chỉnh sửa phần http://.......
                if not ((item in url_list) and (item in history)): #Nếu đường link chưa hề được duyệt và chưa có trong hàng đợi
                    url_list.append(item) #Thêm đường link mới vào danh sách chờ duyệt
        folder_op.luu_noi_dung_file(page, data_folder)
        history.append(url)
        count += 1



if __name__ == '__main__':
    start()