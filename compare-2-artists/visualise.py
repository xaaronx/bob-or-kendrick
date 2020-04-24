def plot_clouds(data):
    '''
    Create word clouds based on single string of text
    '''
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(data)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def create_text_embeddings(ncomponents, data, lr):
    '''
    Create t-sne text embeddings.
    '''
    embedded_data = pd.DataFrame(TSNE(n_components=ncomponents, random_state=1, learning_rate=lr)\
                                 .fit_transform(data),
                       columns=['c{}'.format(i) for i in range(ncomponents)],
                       index=X.index)

    embedded_data['artist'] = df['artist']
    embedded_data['song'] = df['song']

    return embedded_data


def plot_confusion(cm):
    '''
    Generate a confusion matrix
    '''
    plt.figure(figsize=(6,6))
    ax = sns.heatmap(cm, annot=True, fmt=".0f", linewidths=.5, square = True,  cmap = 'coolwarm')
    plt.ylabel('Actual label');
    plt.xlabel('Predicted label');
    plt.xticks([i-0.5 for i in range(1,3)], ['Bob Dylan', 'Kendrick Lamar'])
    plt.yticks([i-0.5 for i in range(1,3)], ['Bob Dylan', 'Kendrick Lamar'])
    b, t = plt.ylim()
    b += 0.5
    t -= 0.5
    plt.ylim(b, t)
    plt.show()
