import jieba
from wordcloud import WordCloud
import imageio
from PIL import Image
from imageio.core.functions import imread

def jieba_processig(stop_word, text):
    '''jieba分词'''
    with open(stop_word, 'r', encoding='utf-8', errors='ignore') as f:
        stop_words = f.read().splitlines()

    with open(text, 'r', encoding='utf-8') as fi:

        # jieba.add_word('细思极恐')
        # jieba.add_word('快银')
        cut_str = '/'.join(jieba.cut(fi.read(), cut_all=False))

    cut_word = []
    for word in cut_str.split('/'):
        if word not in stop_words and len(word) > 1:
            cut_word.append(word)

    return ' '.join(cut_word)


back_coloring = imread('static/robot.png')

wc = WordCloud(background_color='white',
            scale=5,
            max_words=600,
            mask=back_coloring,
            stopwords='static/baidu_stopwords.txt',
            font_path='static/font.ttf',  # 设置中文字体
            max_font_size=60,  # 设置字体最大值
            random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
            width=600,
            height=600).generate(jieba_processig('static/baidu_stopwords.txt', 'static/combinedProductName.txt'))
pUrl = "static/combinedProductName.png"
wc.to_file(pUrl)