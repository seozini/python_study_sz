
class book :
    # 인스턴스 변수
    title = ""
    author = ""
    
    # 인스턴스 매서드
    def set_info(self, title, author) :
        self.title = title
        self.author = author
        
    def print_info(self) :
        print(f'Title : {self.title}, Author : {self.author}')
        
book1 = book()
book2 = book()

book1.set_info('지구에서 한아뿐', '정세랑')
book2.set_info('marry me, mark', 'seozin')

book_list = {book1, book2}