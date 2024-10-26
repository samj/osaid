[quote="nick, post:3, topic:589"]
I’m not sure how you arrived at these numbers:
[/quote]

I hand-counted the votes in the [spreadsheet](https://docs.google.com/spreadsheets/d/1SCT2K-8xvTIbozpoXGuvf1NVcB54vY8p2fKkJlyk4KM/edit#gid=0) immediately to the right of your screenshot, and double-checked by [tallying](https://docs.google.com/spreadsheets/d/1yXSOFMS-icJSQnYB5ec48WTT2acl9mPbu-I8x9OhBuc/edit?usp=sharing) the results from the working group reports for [Llama 2](https://discuss.opensource.org/t/report-from-llama2-working-group/213), [Pythia](https://discuss.opensource.org/t/report-from-pythia-working-group/226), [OpenCV](https://discuss.opensource.org/t/report-from-opencv-working-group/244), and [Bloom](https://discuss.opensource.org/t/report-from-bloom-working-group/243), double confirming that ***the results relied upon to make the recommendation to exclude training data were erroneous***:

| Model   | Use | Study | Modify | Share | Total |
|---------|-----|-------|--------|-------|-------|
| Llama 2 | 0   | 2     | 1      | 0     | 3     |
| Pythia  | 0   | 4     | 0      | 0     | 4     |
| OpenCV  | 4   | 4     | 2      | 0     | 10    |
| Bloom   | 2   | 5     | 3      | 1     | 11    |
| **Total**  | **6**   | **15**    | **6**      | **1**     | **28**    |

Furthermore, if you consolidate training and testing data (as is often the case), you'd pick up another 4 votes (DT, JL, JT, and RA), taking you into hard "Yes = Required (≥2μ votes)" territory.

For good measure I then [combined and totaled the vote totals](https://github.com/samj/osaid/blob/main/reports/vote_totals.csv) from the final reports to examine the votes by component and freedom:

![stacked_votes_by_component|690x413](upload://mOuRObsquL7Iys66rLWonIPa7zd.png)

I also applied the "pretty solid" statistics to see what that methodology would actually recommend (whether or not I agree with its validity — you can't vote butter out of a [pound cake](https://en.wikipedia.org/wiki/Pound_cake) and have it still function as a pound cake!):

![total_votes_by_component|690x413](upload://b6eqzhAZ4KYDgoyCI4tUSQBFGK3.png)

Finally, I went back to the original raw voting data [consolidated incomplete rows](https://github.com/samj/osaid/blob/main/data/consolidation.txt), [flattened the votes](https://github.com/samj/osaid/blob/main/scripts/flatten_votes.py) to [produce raw data](https://github.com/samj/osaid/blob/main/data/voting_data_flattened.csv), and [analysed that data](https://github.com/samj/osaid/blob/main/scripts/analyse_voting_data.py) to create this heatmap:

![heatmap_votes_by_component_and_freedom|690x413](upload://kMkJwPIXsEJ4nF7U5iFbe5lxqrh.png)

As for calls for civility, here like at Wikipedia I'm careful to [comment on content, not the contributor](https://en.wikipedia.org/wiki/Wikipedia:No_personal_attacks), and I have plenty of respect for those doing the work being led by @Mer . As a design thinking advocate I'm intrigued by the co-design process too.
 
I disagree with the results in part because they throw me and [my Open Source AI project](https://paios.org/) under the bus of the AI behemoths (who got a vote while we didn't, which is like the fox guarding the henhouse), but also because voting is not an appropriate way to reach consensus on technical topics, so the technical question of what is actually required to practically protect the four freedoms remains open.

That said, the vote tallies from the final reports do actually support the inclusion of training data so I'll respect those results provided you do too — given ***training, validation, and testing*** code [scores lower](https://github.com/samj/osaid/blob/main/reports/vote_totals.csv) but is required by the checklist, both ***training data sets*** and ***testing data sets*** should be as well. I look forward to seeing them added to the 0.0.10 draft.
