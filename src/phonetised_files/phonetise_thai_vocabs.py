import tltk
import codecs
from tqdm import tqdm
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('lexicon.tsv', sep='\t', names=['text', 'phoneme'])
    f = codecs.open('thai_lexicon.txt', 'w', 'utf-8')
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        text = row['text']
        pho = tltk.nlp.g2p(text).split('<tr/>')[1].replace('|<s/>', '')
        pho = pho.replace('~', ' ').replace('|', ' ').upper()
        f.write(f"{text}\t{pho}\n")
