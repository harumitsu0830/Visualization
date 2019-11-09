# 各パラメータのboxplot(TARGETのクラス毎に分けて表示)
def plot_many_box_comparison(DF,COLUMN_COUNT,TARGET):
    
    #データ指定
    DF_ = DF.copy()
    
    #プロットする変数の指定 floatとint型の変数のみ
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

    #作図 hueは色分け
    for col_num, col in enumerate(columns_toplot):
        plt.subplot(line_count,COLUMN_COUNT_,col_num+1)
        sns.boxplot(x=TARGET,y=col, data=DF_,hue=TARGET)
