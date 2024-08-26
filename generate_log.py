import os
from bs4 import BeautifulSoup

# HTML 파일을 검색할 디렉토리
directory = '.'

# 추가할 <div> 태그
div_content = '<div>Your content here</div>'

# 디렉토리 내의 모든 HTML 파일을 처리
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        
        # 파일 읽기
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # BeautifulSoup을 사용하여 HTML 파싱 및 수정
        soup = BeautifulSoup(content, 'html.parser')
        
        # <body> 태그 찾기
        body_tag = soup.find('body')
        if body_tag:
            # <body> 태그의 끝에 <div> 추가
            if not body_tag.find('div', text='Your content here'):
                new_div = soup.new_tag('div')
                new_div.string = 'Your content here'
                body_tag.append(new_div)
            
            # 수정된 HTML 파일을 다시 저장
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(str(soup))
        
        print(f'Updated {filename}')
