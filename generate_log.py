import os

# HTML 파일을 검색할 디렉토리
directory = '.'

# 추가할 <div> 태그
div_tag = '<div>Your content here</div>'

# 디렉토리 내의 모든 HTML 파일을 처리
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        # 파일 읽기
        with open(filepath, 'r') as file:
            content = file.read()
        
        # <div> 태그 추가
        if div_tag not in content:
            content += f'\n{div_tag}\n'
        
            # 파일 쓰기
            with open(filepath, 'w') as file:
                file.write(content)
        
        print(f'Updated {filename}')
