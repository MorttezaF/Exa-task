# Exalab Back-end Project Description 

In this project, we want to evaluate your coding and database manipulation skills. In this regard, we have defined project that consists of 3 parts, which are as follows:

## First Step: Design the database 

Attached file are some tweets in txt format. Tweets include hashtags, user information and other metadata. We want to extract two different insights from this data:

- For a received hashtag, finds most repetitive hashtags happened with the given hashtag. For example: in the tweet: "...this president is someone that doesn’t want to learn #Trump #MadeleineAlbright #US_intelligence https://t.co/hHP1zr9x7c" , #Trump, #US_intelligence and #MadeleineAlbright . So #Trump is happened with #US_intelligence.  and for given #Trump, you should the most hashtags who had happened with #Trump.
- For a received hashtag, find effective users who use that hashtag.

> Note: The effective user is a user who have most followers.

- Use the Neo4j database to model the data , store them and implement the desired queries.

## Second Step: Design API

We want to design an API which gets a hashtag, finds 10 repetitive hashtags next to it, as well as 10 effective users who use that hashtag, implemented in step 1. 

So Design Flask python API that gets hashtags and return desired output.

- Endpoint: 

```
GET localhost:5000/?hashtag=food
```

- Sample Output:

```json
{
 "repetitive_hashtags": ["hashtag_1","hashtag_2","hashtag_3"],
 "influenc_users":["user_1","user_2", "user_3"]
}
```

## Last Step: Compare Databases

We want to compare the performance of Neo4j and PostgreSQL databases in CRUD operation.
Therefore, repeat step1 for Postgres database too,benchmark the performances and compared with each other.

You should monitor these performance metrics:

- Maximum successful queries per second.
- CPU Consumption,RAM Utilization and runtime speed During Write operation(Storing phase)
- CPU Consumption,RAM Utilization and runtime speed During every Read operation(query phase)

> Note: You can use [locust](https://locust.io/) package to make a load test for your application.