# Book_search_engine



## TABLE OF CONTENTS

* [Problem Statement](#problem-statement)
* [Data Pre-Processing](#data-preprocessing)
* [Search Engine](#search-engine)
* [Result](#result)
* [References](#references)
* [Future Work](#future-work)


<hr>

## Problem Statement

This was a project for ML Challenge hosted by VEEVA

You’re driving the team to develop an innovative book search engine. Assume that
you have an inclusive catalogue containing information about 10k English books.
Over time you’ve also collected users' interactions with books including marked and
ratings.
Your goal is to provide users a personalized search experience for any type of bookhunting
intent query. More formally, your goal is to provide code that takes as input
a user id u and a query string q , and gives as output a ranked list of books
b , b , … , b . We expect your solution to have an information retrieval 1 2 n component.

<hr>

## Data Set

* **[Good Reads Data Set](https://drive.google.com/drive/folders/19QxGSfyN9nrFCqwXa24L8Vtdx5QexuGr)** 
* This link also contains a description of the dataset.




<hr> 


## DATA-PREPROCESSING
<b> Data Cleaning </b> 
<li>Features Selected: Book Title, Original Title, Book ID ,and Cover Image </li> 
<li>Created new data frames  reviews_per_book and liked_books grouped by user_id</li> 
<li>Removed unnecessary characters and spaces from titles using Regex</li> 
<li>Removed null titles </li>
<li> Modified Titles:</li>
<br>
<p float="left" >
  <img src="https://github.com/deepakcr7ms7/Book_search_engine/blob/master/images/BS1.jpg" alt="Preprocessing" height="400"width="300"  />
  <img src="https://github.com/deepakcr7ms7/Book_search_engine/blob/master/images/BS2.jpg" alt="Augmented Images" height="400" width="300" />
</p>
<li> Processed metadata using TfidfVectorizer() </li>
<br> 

<hr> 

## Search Engine

<table style="width:100%">
  <tr>
    <th>Task</th>
    <th>Description</th> 
    <th>Tools/Packages Used</th>
  </tr>
  <tr>
    <td>Search</td>
    <td>Find the  book titles, which has highest cosine similarity with the qurey and rank the result based on the ratings </td> 
    <td>re , TfidfVectorizer, cosine_similarity</td>
  </tr>
  <tr>
    <td>Recommendation</td>
    <td>Use Collabrative filetering technique to make recommendation based on users past data</td> 
    <td>nltk, CountVectorizer, pandas, numpy</td>
  </tr>
  <tr>
    <td>Final result</td>
    <td>Combine the result of both search and recommender system to give personalised search experience  </td> 
    <td> Jupyter Notebook</td>
  </tr>
  

</table><br>

<hr>

## Collabrative Filtering

I used collabrating filtering algorithm to make recommendations

<br> Steps were implemented in the algorithm. These steps are needed every time some enters a new playlist query:

* Import prepossed data and cluster them:

<br> <img src="https://github.com/deepakcr7ms7/Book_search_engine/blob/master/images/BS3.jpg" height=400 style="width:100%;">

* Retrive the list of books liked by the user based on past ratings:

<img src="https://github.com/deepakcr7ms7/Book_search_engine/blob/master/images/BS4.jpg" height=400 style="width:100%;">

* Find the user who liked the same books and filter them based on ratings count

<img src="https://github.com/deepakcr7ms7/Book_search_engine/blob/master/images/BS5.jpg" height=400 style="width:100%;">

* Create the recoomendation list of top 50 books the user might like

<img src="https://github.com/deepakcr7ms7/Book_search_engine/blob/master/images/BS6.jpg" height=400 style="width:100%;">

## Result
<br>Qurey : 
* Book Title : 'Salt to the Sea'
* user id    : id=2
     
<img src="https://github.com/deepakcr7ms7/Book_search_engine/blob/master/images/BS7.jpg"  height=1000 style="width:80%;"  >
 


## References
<li> W. Bruce Croft
Donald Metzler
Trevor Strohman
Search Engines
Information Retrieval in Practice
</li>
<li> Building Search Engine Using Machine Learning Technique Ch.Venkata Ramana, G. Meghana, M. Navya Sai, A. Pras</li>
<li>Machine Learning in Search Engines by Neenu Ann, Sunny Assistant Teacher ,Saintgits College of Applied Sciences </li>
<li> W. Scott, TF-IDF from scratch in python on a real-world dataset. (2019), on Towards Data Science </li>
<li> P. Shah, Sentiment Analysis using TextBlob (2020), on Towards Data Science</li>
<li> Spotipy, spotipy documentation (n.d.) </li>

## Future Work

Using neural networks, AI, and deep learning in the development of search engines as mentioned in Tommaso Teofili book about "Deep Learning for Search"  

