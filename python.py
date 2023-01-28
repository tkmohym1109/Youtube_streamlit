import streamlit as st
import numpy as np
import pandas as pd

from PIL import Image
import time


st.title('streamlit 超入門')

#st.write('DateFrame')

'start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.03)

'done!!!'

#list = ( '','北海道コンサドーレ札幌','鹿島アントラーズ','浦和レッズ','柏レイソル',
        # 'FC東京','川崎フロンターレ','横浜・F・マリノス','横浜FC','湘南ベルマーレ','アルビレックス新潟',
         #'名古屋グランパス','京都サンガFC','ガンバ大阪','セレッソ大阪','ヴィッセル神戸','サンフレッチェ広島',
         #'アビスパ福岡','サガン鳥栖',)

#option = st.selectbox(
    #'あなたが好きなJ1クラブを教えてください',
    #list, index=0)

#left_column, right_column = st.columns(2)
#button = left_column.button('右カラムにボタン表示')

#if button:
    #right_column.write('ここは右カラムです。')

#'あなたが好きなJ1クラブは',option,'です。'

expander = st.expander('問い合わせ1')
expander.write('問い合わせ内容を書く1')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ内容を書く2')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ内容を書く3')

#text = st.text_input('あなたの趣味を教えてください')

#'あなたの趣味：',text

#x = st.slider('あなたの今の調子は？',0,100,50)
#'コンディション:',x


#if st.checkbox('Show Image'):
  #img = Image.open('IMG_1048.JPG')
  #st.image(img,caption='My town', use_column_width=True)

#dt = pd.DataFrame({
    #'１列目':[1,2,3,4],
    #'2列目':[10,20,30,40]
#}) 表
#df = pd.DataFrame(
    #np.random.rand(20,3),
    #columns=['a','b','c']
#)　折れ線グラフ　乱数

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69,139.70],
#    columns=['lat','lon']　座標
#)

#st.dataframe(df) データフレーム

#st.map(df)　マップ

#st.dataframe(dt.style.highlight_max(axis=0),width=300,height=300)
#st.line_chart(df)