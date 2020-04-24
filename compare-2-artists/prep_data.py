def drop_breaks(lyrics):
    '''
    Strip our section marker from lyrics i.e. ['Verse 1'] and line breaks
    '''
    return re.sub(r'\[(.*?)\]', '', lyrics)


def remove_digits(lyrics):
    '''
    Strip our section marker from lyrics i.e. ['Verse 1'] and line breaks
    '''
    return re.sub(r'[0-9]', '', lyrics)


def clean_song_names(df):
    '''
    Removes unwanted characters from song names
    '''
    df['song'] = df.song.str.replace('\n',' ')\
    return df


def process_text(songs, pos=False):
    '''
    Cleans sentences from stop words and punctuation and filters by pos tags if given
    returns cleaned sentence and tokenized sentence
    '''
    nlp = textacy.load_spacy_lang('en_core_web_sm')

    texts, tokenised_texts = [], []

    if pos:
        for lyrics in tqdm.notebook.tqdm(nlp.pipe(songs, batch_size=200)):
            assert lyrics.is_parsed
            tokens = [token
                      for token in lyrics
                      if token.is_stop == False
                      and token.pos_ in pos
                      and token.pos_ != 'PUNCT']
            doc_ = ''
            for token in tokens:
                doc_ += str(token) + ' '

            doc_ = doc_.strip()
            texts.append(doc_)
            tokenised_texts.append(tokens)

    else:
        for lyrics in tqdm.notebook.tqdm(nlp.pipe(songs, batch_size=200)):
            assert lyrics.is_parsed
            tokens = [token
                      for token in lyrics
                      if token.is_stop == False
                      and token.pos_ != 'PUNCT']
            doc_ = ''
            for token in tokens:
                doc_ += str(token) + ' '

            doc_ = doc_.strip()
            texts.append(doc_)
            tokenised_texts.append(tokens)

    return texts, tokenised_texts


def vectorise(ngram_range, max_feats, input_data):
    '''
    Returns non-sparse format. With a larger dataset rather return
    '''
    vect = TfidfVectorizer(ngram_range, max_features=max_feats)

    return vect.fit(input_data), pd.DataFrame(vect.fit_transform(input_data).todense(),
                                    columns=vect.get_feature_names(),
                                    index=input_data.index)


def clean_dataframe(df):
    '''
    Combines above functions to prepare data
    '''
    df = clean_song_names(df)
    pos = ['NOUN', 'ADJ', 'VERB', 'ADV']

    df['lyrics'] = df.lyrics.str.replace('\n',' ')\
                                .apply(lambda x: drop_breaks(x))\
                                .apply(lambda x: remove_digits(x))\
                                .str.lower()

    processed_quotes, tokenised_quotes = process_text(df.lyrics)

    df['lyrics_processed'] = processed_quotes
    df['lyrics_tokenised'] = tokenised_quotes

    return df
