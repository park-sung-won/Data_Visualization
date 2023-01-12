import pandas as pd
import numpy as np

## 워드 클라우드 생성을 위한 패키지
from wordcloud import WordCloud

## 워드클라우드 모양을 변형시키고자 하는 이미지 활용에 사용 패키지
from PIL import Image

## 그래프 출력 패키지
import matplotlib.pyplot as plt

## 수치 연산 패키지
import numpy as np

## 데이터 핸들링
import pandas as pd



## 데이터 프레임 생성
df = pd.read_excel('./file_name.xlsx')
df = df.dropna()
df.info()

## 생성된 데이터 프레임을 딕셔너리로 변환
wc = df.set_index("job").to_dict()["cnt"]

# cand_mask=np.array(Image.open('circle.jpg')) #모양설정


wordCloud = WordCloud(
font_path = '/Library/Fonts/AppleGothic' , # 폰트 지정
width = 800, # 워드 클라우드의 너비 지정
height = 800, # 워드클라우드의 높이 지정
max_font_size=200, # 가장 빈도수가 높은 단어의 폰트 사이즈 지정
background_color = 'white' # 배경색 지정
# mask=cand_mask  # 워드클라우드 모양설정
).generate_from_frequencies(wc) # 워드 클라우드 빈도수 지정   ## 카운트된 숫자로 해야하는듯


plt.figure(figsize=(10,10))  
plt.imshow(wordCloud)
plt.axis('off')

#plt.savefig('test.png') # 저장
