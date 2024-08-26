import os
from bs4 import BeautifulSoup
from datetime import datetime

# 환경 변수에서 정보 가져오기
commit_message = os.getenv('COMMIT_MESSAGE', 'No commit message')
changed_files = os.getenv('CHANGED_FILES', '')

# 디렉토리 내의 모든 HTML 파일을 처리
index_html_path = 'index.html'

# <li> 태그의 내용 설정
li_contents = []
for file in changed_files.split('\n'):
    if file and file != index_html_path:
        li_contents.append(f'<li>{commit_message},{file},{datetime.now().strftime("%Y-%m-%d")}</li>')

# HTML 파일을 업데이트
if os.path.exists(index_html_path):
    with open(index_html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # 마지막 <li> 태그를 찾아 새 <li> 태그 추가
    last_li = soup.find('li')
    if last_li:
        for content in li_contents:
            new_li = soup.new_tag('li')
            new_li.string = content
            last_li.insert_after(new_li)
        
        with open(index_html_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

    print(f'Updated {index_html_path}') 
