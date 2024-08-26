import sys
import os
from bs4 import BeautifulSoup
from datetime import datetime

# 커밋 메시지와 변경된 파일 목록을 명령줄 인자로 받기
if len(sys.argv) != 3:
    print("Usage: python generate_log.py <commit_message> <changed_files>")
    sys.exit(1)

commit_message = sys.argv[1]
changed_files = sys.argv[2]

# 디렉토리 내의 HTML 파일을 처리
index_html_path = 'index.html'

# <li> 태그의 내용 설정
li_contents = []
if changed_files != "No previous commit":
    for file in changed_files.split(','):
        if file and file != index_html_path:
            li_contents.append(f'<li>{commit_message},{file},{datetime.now().strftime("%Y-%m-%d")}</li>')

# HTML 파일을 업데이트
if os.path.exists(index_html_path):
    with open(index_html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # 마지막 <li> 태그를 찾아 새 <li> 태그 추가
    last_li = soup.find_all('li')[-1] if soup.find_all('li') else None
    if last_li:
        for content in li_contents:
            new_li = soup.new_tag('li')
            new_li.string = content
            last_li.insert_after(new_li)
        
        with open(index_html_path, 'w', encoding='utf-8') as file:
            file.write(str(soup.prettify()))

    print(f'Updated {index_html_path}')
else:
    print(f'{index_html_path} does not exist')
