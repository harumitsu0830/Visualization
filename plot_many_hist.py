
def plot_many_hist(DF,COLUMN_COUNT):
    
    #各変数のヒストグラムを作成する

    #データを指定
    DF_ = DF.copy()

    #プロットする変数の指定 float型の変数のみ
    columns_toplot = DF_.select_dtypes(['float','int64']).columns.tolist()

    #横方向に何個グラフを並べるか指定
    COLUMN_COUNT_ = COLUMN_COUNT

    #縦方向に何個グラフを並べるか算出
    line_count = math.ceil(len(columns_toplot)/COLUMN_COUNT_)

    #グラフスタイル
    plt.style.use('fivethirtyeight')

    # フォント指定（日本語文字化け防止）
    plt.rcParams['font.family'] = 'IPAPGothic'

    #グラフサイズ
    plt.figure(figsize=(10,5*len(columns_toplot)))



    #作図
    for col_num, col in enumerate(columns_toplot):
       plt.subplot(len(columns_toplot),1, col_num+1)
       DF__ = DF_[[col]].copy().dropna()
       plt.hist(col, data=DF__,bins=100)
       plt.title(col)
       # フォントサイズ
       plt.tick_params(labelsize=15)