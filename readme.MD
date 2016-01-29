### Ordinal Classification of Tweets

This project is the code for SemEval-2016 Task 4 sub-task C competition.

Task: Given a tweet known to be about a given topic, estimate the sentiment conveyed by the tweet towards the topic on a five-point scale.

### Data Description

|Name|Size|# Available (Percentage)|# Topics|#(-2)|#(-1)|#(0) |#(1)|#(2)|Max Length|Min Length|Average Length|
|------|------|------|------|------|------|------|------|------|------|------|------|
|Gold Train|6000|5346 (89.1%)|60|87|668|1654|3154|437|34|5|19.49|
|Gold Dev|2000|1795 (89.75%)|20|43|296|675|933|53|31|6|19.58|
|Gold Devtest|2000|1781 (89.05%)|20|31|233|583|1005|148|31|5|19.69|
|Input Devtest|2000|1781 (89.05%)|20|-|-|-|-|-|31|5|19.69|

Note: The "Not Available" terms are removed when gather statistics information of Max Length, Min Length, Average Length.

Number and Sentiment Intensity mapping method

|Sentiment Intensity|strongly negative|negative|negative or neutral|positive|strongly positive|
|------|------|------|------|------|------|
|Sentiment Score|-2|-1|0|1|2|

The topics in gold train, gold dev, gold devtest data: [topics](./MD/topics.MD). We can see that the topic in different data set is different. Exactly, there is no common topics between the three data set.

### Contact me

* [Yunchao He](https://plus.google.com/+YunchaoHe)
* yunchaohe@gmail.com
* [YZU](http://www.yzu.edu.tw/) at Taiwan
* [Weibo](http://weibo.com/heyunchao)
* [Facebook](https://www.facebook.com/yunchao.h)
* [Twitter](https://twitter.com/candlewill)
* @元智大学资讯工程学系1608B 民105年1月