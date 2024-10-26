[quote="nick, post:5, topic:589, full:true"]
Hi @samj, thank you for diving deep into the data. I like your charts.
[/quote]

Thank you... you'll be pleased to know I have more then.

[quote="nick, post:5, topic:589, full:true"]
I believe @mer used the following methodology to count the votes: +1 (required), 0 (neutral), -1 (not necessary). Did you include the “not necessary” votes?
[/quote]

The call for a vote and setting of arbitrary thresholds aside, how and why was this methodology decided on? Where was it discussed and/or documented, whether before or after the fact? That key information doesn't appear anywhere in the [public posts](https://opensource.org/blog/mer-joyce-voices-of-the-open-source-ai-definition) nor final reports, and was only ever captured in the spreadsheet for 1 of the 4 working groups (Llama 2). As such, it must obviously be excluded, and no it wasn't counted by my scripts.

That one decision would effectively give **only** the Llama 2 working group the superpower of not only being able to cast their own votes, but also to silently **erase** the votes of others, even from other working groups! It would explain why the *Data* category is a sea of red! It's like me sitting in the next room saying I absolutely need the data to do X, and you saying "yeah, nah, no you don't", or voting for Trump yourself while **also** quietly tearing up my vote for Harris — that's not how voting works!

I wonder if the working group members even understood that's what they were doing? Does @stefano realise he erased more votes than he cast? Does @zack realise he erased more votes than all the others put together (49 vs 43), and double what he cast himself (25), making him by far the strongest opponent to openness (-24)? It seems strange to me that the **Open** Source Initiative's own members would knowingly cast votes **against** openness, unless it was so unclear even to them in the room that they didn't know that's what they were being asked to do?

[quote="nick, post:5, topic:589, full:true"]
This does highlight one of the major drawbacks of sharing the original data: lack of privacy. One can guess who voted for what based on their initials.
[/quote]

No need to guess as we can see exactly who voted for (and against) what. 

That's how I also know that of the **two** Meta employees(!) in the Llama 2 working group with superpowers(!!), their lawyer voted **against** requiring data every time(!!!), erasing more votes than they cast too. This one's less surprising given the [discussion next door](https://discuss.opensource.org/t/case-in-point-zuckerbergs-blog-on-open-source/579) about Meta concealing its data sources (which is fine — just [don't call it Open Source](https://opensource.org/blog/metas-llama-2-license-is-not-open-source)!), but it raises even more questions about the validity of the vote.

Assuming enough has already been said publicly about the vote that we're stuck with it—though I'm confident that vote erasing superpowers are a bridge too far for everyone here, or else perhaps I'm in the wrong room—I used k-means clustering for n in { 2, 3, 4, 5} to at least find somewhat more statistically justifiable/less arbitrary cut-offs. Given the binary nature of the decision and the large cliff, n=2 likely makes the most sense, and as a practitioner it aligns with common sense. I've included the raw data below, and the scripts/data/figures/etc. are in the [samj/osaid](https://github.com/samj/osaid/) repo.

That or we've designed by committee a car with no wheels. What next?

n=2
![kmeans_cluster_2|690x345](upload://6HkpyjTfXrSP5HM65iq8BBNBnl4.png)

n=3
![kmeans_cluster_3|690x345](upload://mNt2wu9J09gIgJYw71fyDh0t8m1.png)

n=4
![kmeans_cluster_4|690x345](upload://isqliVhIGY3JkavW12SlDfYyhDC.png)

n=5
![kmeans_cluster_5|690x345](upload://zqVPmgW6sTckHoF3yfPL28JgYk5.png)

```
Clustering results for n=2:
Cluster centers: [31.91666667  9.73333333]
Ordered names: ['Yes', 'No']
Ordered colors: ['#a4ea78', '#d1a09b']

Components by cluster for n=2:
Cluster Yes (Mean: 31.92):
  - Other libraries or code artifacts (Mean: 49.00)
  - Inference code (Mean: 43.00)
  - Model parameters (Mean: 42.00)
  - Model architecture (Mean: 37.00)
  - Data preprocessing code (Mean: 35.00)
  - Supporting tools (Mean: 30.00)
  - Training data sets (Mean: 28.00)
  - Testing data sets (Mean: 27.00)
  - Training, validation and testing code (Mean: 25.00)
  - Usage documentation (Mean: 23.00)
  - Benchmarking data sets (Mean: 22.00)
  - Research paper (Mean: 22.00)

Cluster No (Mean: 9.73):
  - Validation data sets (Mean: 19.00)
  - All other data documentation (Mean: 17.00)
  - Evaluation code (Mean: 17.00)
  - Model card (Mean: 15.00)
  - Training code (Mean: 13.00)
  - Code used to perform inference for benchmark tests (Mean: 10.00)
  - Sample model outputs (Mean: 8.00)
  - Technical report (Mean: 8.00)
  - Data card (Mean: 7.00)
  - Evaluation data (Mean: 7.00)
  - Evaluation results (Mean: 6.00)
  - Model metadata (Mean: 6.00)
  - Evaluation metrics and results (Mean: 5.00)
  - Test code (Mean: 4.00)
  - Validation code (Mean: 4.00)


Clustering results for n=3:
Cluster centers: [23.    7.75 41.2 ]
Ordered names: ['Yes', 'Maybe', 'No']
Ordered colors: ['#a4ea78', '#f9f3d1', '#d1a09b']

Components by cluster for n=3:
Cluster Yes (Mean: 41.20):
  - Other libraries or code artifacts (Mean: 49.00)
  - Inference code (Mean: 43.00)
  - Model parameters (Mean: 42.00)
  - Model architecture (Mean: 37.00)
  - Data preprocessing code (Mean: 35.00)

Cluster Maybe (Mean: 23.00):
  - Supporting tools (Mean: 30.00)
  - Training data sets (Mean: 28.00)
  - Testing data sets (Mean: 27.00)
  - Training, validation and testing code (Mean: 25.00)
  - Usage documentation (Mean: 23.00)
  - Benchmarking data sets (Mean: 22.00)
  - Research paper (Mean: 22.00)
  - Validation data sets (Mean: 19.00)
  - All other data documentation (Mean: 17.00)
  - Evaluation code (Mean: 17.00)

Cluster No (Mean: 7.75):
  - Model card (Mean: 15.00)
  - Training code (Mean: 13.00)
  - Code used to perform inference for benchmark tests (Mean: 10.00)
  - Sample model outputs (Mean: 8.00)
  - Technical report (Mean: 8.00)
  - Data card (Mean: 7.00)
  - Evaluation data (Mean: 7.00)
  - Evaluation results (Mean: 6.00)
  - Model metadata (Mean: 6.00)
  - Evaluation metrics and results (Mean: 5.00)
  - Test code (Mean: 4.00)
  - Validation code (Mean: 4.00)


Clustering results for n=4:
Cluster centers: [20.          7.09090909 44.66666667 31.4       ]
Ordered names: ['Yes', 'Lean Yes', 'Lean No', 'No']
Ordered colors: ['#a4ea78', '#d6fbc4', '#e8cea3', '#d1a09b']

Components by cluster for n=4:
Cluster Yes (Mean: 44.67):
  - Other libraries or code artifacts (Mean: 49.00)
  - Inference code (Mean: 43.00)
  - Model parameters (Mean: 42.00)

Cluster Lean Yes (Mean: 31.40):
  - Model architecture (Mean: 37.00)
  - Data preprocessing code (Mean: 35.00)
  - Supporting tools (Mean: 30.00)
  - Training data sets (Mean: 28.00)
  - Testing data sets (Mean: 27.00)

Cluster Lean No (Mean: 20.00):
  - Training, validation and testing code (Mean: 25.00)
  - Usage documentation (Mean: 23.00)
  - Benchmarking data sets (Mean: 22.00)
  - Research paper (Mean: 22.00)
  - Validation data sets (Mean: 19.00)
  - All other data documentation (Mean: 17.00)
  - Evaluation code (Mean: 17.00)
  - Model card (Mean: 15.00)

Cluster No (Mean: 7.09):
  - Training code (Mean: 13.00)
  - Code used to perform inference for benchmark tests (Mean: 10.00)
  - Sample model outputs (Mean: 8.00)
  - Technical report (Mean: 8.00)
  - Data card (Mean: 7.00)
  - Evaluation data (Mean: 7.00)
  - Evaluation results (Mean: 6.00)
  - Model metadata (Mean: 6.00)
  - Evaluation metrics and results (Mean: 5.00)
  - Test code (Mean: 4.00)
  - Validation code (Mean: 4.00)


Clustering results for n=5:
Cluster centers: [22.2         6.5        44.66666667 31.4        15.5       ]
Ordered names: ['Yes', 'Lean Yes', 'Maybe', 'Lean No', 'No']
Ordered colors: ['#a4ea78', '#d6fbc4', '#f9f3d1', '#e8cea3', '#d1a09b']

Components by cluster for n=5:
Cluster Yes (Mean: 44.67):
  - Other libraries or code artifacts (Mean: 49.00)
  - Inference code (Mean: 43.00)
  - Model parameters (Mean: 42.00)

Cluster Lean Yes (Mean: 31.40):
  - Model architecture (Mean: 37.00)
  - Data preprocessing code (Mean: 35.00)
  - Supporting tools (Mean: 30.00)
  - Training data sets (Mean: 28.00)
  - Testing data sets (Mean: 27.00)

Cluster Maybe (Mean: 22.20):
  - Training, validation and testing code (Mean: 25.00)
  - Usage documentation (Mean: 23.00)
  - Benchmarking data sets (Mean: 22.00)
  - Research paper (Mean: 22.00)
  - Validation data sets (Mean: 19.00)

Cluster Lean No (Mean: 15.50):
  - All other data documentation (Mean: 17.00)
  - Evaluation code (Mean: 17.00)
  - Model card (Mean: 15.00)
  - Training code (Mean: 13.00)

Cluster No (Mean: 6.50):
  - Code used to perform inference for benchmark tests (Mean: 10.00)
  - Sample model outputs (Mean: 8.00)
  - Technical report (Mean: 8.00)
  - Data card (Mean: 7.00)
  - Evaluation data (Mean: 7.00)
  - Evaluation results (Mean: 6.00)
  - Model metadata (Mean: 6.00)
  - Evaluation metrics and results (Mean: 5.00)
  - Test code (Mean: 4.00)
  - Validation code (Mean: 4.00)
```
