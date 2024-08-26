import os
from bs4 import BeautifulSoup
from datetime import datetime

# HTML 파일을 검색할 디렉토리
directory = '.'

# 추가할 <li> 태그의 내용
commit_message = 'Commit message placeholder'  # 여기에 커밋 메시지를 동적으로 입력할 수 있습니다.
file_path = 'path/to/your/file.html'  # 여기에 파일 경로를 동적으로 입력할 수 있습니다.
li_content = f'<li>{commit_message},{file_path},{datetime.now().strftime("%Y-%m-%d")}</li>'

# HTML 파일 내에서 참조할 태그 (여기서는 특정 <li> 태그 뒤에 추가)
reference_li_text = '회원 탈퇴 (B2C),html/user/member/mypage3.html,2018-04-04'

# 디렉토리 내의 모든 HTML 파일을 처리
for filename in os.listdir(directory):
    if filename == 'index.html':
        filepath = os.path.join(directory, filename)
        
        # 파일 읽기
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # BeautifulSoup을 사용하여 HTML 파싱 및 수정
        soup = BeautifulSoup(content, 'html.parser')
        
        # 참조 <li> 태그 찾기
        reference_li = soup.find('li', text=reference_li_text)
        if reference_li:
            # 새 <li> 태그 생성
            new_li = soup.new_tag('li')
            new_li.string = f'{commit_message},{file_path},{datetime.now().strftime("%Y-%m-%d")}'
            
            # 참조 <li> 태그 뒤에 새 <li> 태그 추가
            reference_li.insert_after(new_li)
            
            # 수정된 HTML 파일을 다시 저장
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(str(soup))
        
        print(f'Updated {filename}')
