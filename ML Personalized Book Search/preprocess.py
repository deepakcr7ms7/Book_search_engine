import csv
import pandas as pd
FILENAME = "goodbooks/books.csv"
ENCODING = 'utf-8'
def parse_fields(line):
    return {'book_id':line['book_id'],'title':line['original_title'],'ratings':reviews_per_book[int(line['book_id'])],'cover_image':line['image_url']}


r = pd.read_csv( 'goodbooks/ratings.csv' )
tr = pd.read_csv( 'goodbooks/to_read.csv' )
b = pd.read_csv( 'goodbooks/books.csv' )

t = pd.read_csv( 'goodbooks/tags.csv' )
bt = pd.read_csv( 'goodbooks/book_tags.csv')

reviews_per_book = r.groupby('book_id').book_id.apply( lambda x: len( x ))

#test=r.groupby('user_id')['rating'].apply(list)

test=r.loc[pd.to_numeric(r['rating'])>3]
liked_books=test.groupby('user_id')['book_id'].apply(set)#.reset_index(name="liked")
liked_books.to_json('liked_books.json')
print(liked_books[1])
"""
for id1 in test['user_id']:
    overlap=set()
    for id2 in test['user_id']:
        if liked_books[id1]&liked_books[id2]:
            overlap.add(id2)
    print(overlap)
    exit()
"""
#print(type(liked_books))
#liked_books=test.groupby('user_id')['book_id'].apply(list).reset_index(name="liked")
#print(liked_books.head(50))
#ovelap=liked_books.groupby('likes')['user_id'].apply(lt).reset_index(name="overlap")
#print(ovelap.head(10))

with open('goodbooks/books.csv', encoding='utf-8') as csvf:
    # load csv file data using csv library's dictionary reader
    csvReader = csv.DictReader(csvf)

    # convert each csv row into python dict
    book_titles=[]
    for row in csvReader:
        fields=parse_fields(row)
        try:
            ratings=int(fields['ratings'])
        except ValueError:
            continue
        if reviews_per_book[int(fields['book_id'])]>50:
            book_titles.append(fields)

titles=pd.DataFrame.from_dict(book_titles)

titles['ratings']=pd.to_numeric(titles['ratings'])

#get rid of  unnecessary characters from titles

titles['mod_title']=titles['title'].str.replace('[^a-zA-Z0-9]','',regex=True)
titles['mod_title']=titles['mod_title'].str.lower()

#remove spaces regex to remove any continuos str like ,,, or +++ or three spaces
titles['mod_title']=titles['mod_title'].str.replace('\s+','',regex=True)

#remove null titles
titles=titles[titles['mod_title'].str.len()>0]

titles.to_json('books_titles.json')
#print(titles.head())