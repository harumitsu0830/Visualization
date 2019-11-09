#相関係数のヒートマップを作成
def plot_corr_heatmap(DF):
    #欠損のある行を削除
    DF_ = DF.copy().dropna(how='any')
    #.dropna(axis=1)

    plt.style.use('fivethirtyeight')

    #グラフサイズ
    plt.figure(figsize=(20,20))

    # フォント指定（日本語文字化け防止）
    plt.rcParams['font.family'] = 'IPAPGothic' 

    sns.heatmap(DF_.corr(),\
                vmax=1, vmin=-1, center=0,cmap='bwr',annot=True,fmt='.2f')
    plt.title('Correlation coefficients between the explanatory variables')
    # フォントサイズ
    plt.tick_params(labelsize=25)
    sns.set(font_scale=3) 

    plt.show()
