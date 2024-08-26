import os
from bs4 import BeautifulSoup

# HTML 파일을 검색할 디렉토리
directory = '.'

# 추가할 <div> 태그
div_content = '<div>유유유유</div>'

# 원하는 위치의 태그 (예: <p> 태그 뒤에 추가)
reference_tag_text = 'Click the link below to view the change log:'

# 디렉토리 내의 모든 HTML 파일을 처리
for filename in os.listdir(directory):
    if filename == 'index.html':
        filepath = os.path.join(directory, filename)
        
        # 파일 읽기
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # BeautifulSoup을 사용하여 HTML 파싱 및 수정
        soup = BeautifulSoup(content, 'html.parser')
        
        # 참조 태그 찾기
        reference_tag = soup.find(text=reference_tag_text)
        if reference_tag:
            # 참조 태그의 부모 태그를 찾습니다.
            parent_tag = reference_tag.parent
            
            # 추가할 <div> 태그 생성
            new_div = soup.new_tag('div')
            new_div.string = 'Your content here'
            
            # 참조 태그 뒤에 <div> 추가
            parent_tag.insert_after(new_div)
            
            # 수정된 HTML 파일을 다시 저장
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(str(soup))
        
        print(f'Updated {filename}')
