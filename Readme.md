# Tap Search -
#### A project that takes in paragraph as input and assigns each of them unique ID. It has been built by taking reference of elasticsearch database.

### Technology Stack :
Django : hosted on heroku
Elasticsearch : hosted on AWS
Postman : locally and cloud testing

Project URL : https://tapsearchs.herokuapp.com

Elasticsearch URL : https://b0943016ef9146dcbb4006a5d58b5863.us-east-1.aws.found.io:9243 (requires authentication)

The Django project has been hosted on heroku while the elaticsearch connection has been made using AWS hosting.

# Contents

API documents

### Installation

Tapsearch requires [elasticsearch_dsl] to run.

Install the dependencies 

```sh
$ pip3 install requirements.txt
```




### API

#### To add new paragraphs to the data
https://tapsearchwork.herokuapp.com/add

```sh
{
    paragraph : String
}
```

```sh
{
    response : success
}
```

#### To search for paragraphs
https://tapsearchwork.herokuapp.com/search
```sh
{
    keywords : String
}
```

```sh
{
    paragraphs : [String]
}
```

#### To clear the data
```sh
{
    String: ""
}
```

#### To upload image
https://tapsearchwork.herokuapp.com/image
```sh
{
    image: image
}
```
#### Extracting objects from images
```sh

    Using YOLO and Keras

```


### Snapshots

#### 1. Home Page 

![Alt text](https://github.com/Sid11/Tap_Search/blob/master/homepage.png)

#### 2. Database gets updated

![Alt text](https://github.com/Sid11/Tap_Search/blob/master/db.png)

#### 3. Search paragraphs

![Alt text](https://github.com/Sid11/Tap_Search/blob/master/search.png)

#### 4. Upload Images (Still in progress)

![Alt text](https://github.com/Sid11/Tap_Search/blob/master/uploadimage.png)

#### 5. Output of getting keywords from image to find similar images

![Alt text](https://github.com/Sid11/Tap_Search/blob/master/nyc.jpg)

![Alt text](https://github.com/Sid11/Tap_Search/blob/master/nycnew.jpg)







