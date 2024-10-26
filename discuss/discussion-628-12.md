[quote="shujisado, post:6, topic:628"]
One thing I am concerned about is the phrase “**including for a fee**” in point (3).
[/quote]

You are right to be concerned about the "**including for a fee**" capitulation, but for the wrong reason.

That you can charge for source code has been an accepted tenet of Open Source — which is "free as in freedom, not as in beer" — but **only** because anyone can obtain and share the source under the same license if the software is conveyed to them. That is, the market price is kept at or near zero, because the cost of hosting software for download is close to zero (or borne by someone else; even the petabytes of Common Crawl are available for free on AWS)... you don't even need to pay for the CD/DVD any more! While it sounds similar, this is not at all the same thing.

With datasets like the NYT archive [estimated](https://www.perplexity.ai/search/how-much-would-it-cost-to-lice-.zEx2bMQRaqJQzSYgzWqLA) to cost in the tens to hundreds of millions of dollars range ($50-200m), the training cost (including licensing) of GPT-5 [said to cost $2-2.5bn](https://mpost.io/gpt-5-training-will-cost-2-5-billion-and-start-next-year/), and Anthropic already talking about [$10bn training runs within 2 years](https://arxiv.org/html/2405.21015v1), this concession risks restricting Open Source AI to the ranks of billionaires. As Japan's own NII "keeps advancing the research and development of open generative AI" with [LLM-jp](https://www.nii.ac.jp/en/news/release/2024/0401.html) in the LLM space, and [Molmo](https://molmo.allenai.org/blog) have shown in the VLM space, among others, this is not a problem... unless we violate our core beliefs to certify closed models as Open Source AI.

***Doing so would blatantly violate one of our community's core principles—that we 'must not discriminate against any person or group of persons'—by effectively discriminating against almost all Open Source users!***

@grugnog (welcome!) asks that "input" data (which is not the same as "Data Information": weasel words meaning metadata only) be made available under OSI licenses, but that's a bridge too far in the other direction that would also have chilling effects on Open Source AI adoption, not to mention the board's "cannot have an empty set" [criteria](https://github.com/samj/osaid/blob/main/presentations/2024-09-27-osi_townhall_18.pdf). We do need to compromise, but we've chosen the wrong one and the baby's going out with the bathwater. By opting for Open Access rather than Open Licenses for the data components we are not demanding vendors do the impossible (i.e., distribute unlicensed content), but we don't need to!

***Open access to data (e.g., Common Crawl) appears to be the only workable compromise that demonstrably protects the four essential freedoms, and it's already widely accepted in the industry, including [many/most of the 1,000,000 free public models on Hugging Face](https://x.com/ClementDelangue/status/1839375655688884305), as well as being reflected in the oft-cited [Model Openness Framework (MOF)](https://arxiv.org/abs/2403.13784v4)'s "**any license or unlicensed**" wording.***

The new FAQ introduces four classes of data, only one of which (the first) has been traditionally acceptable in the context of Open Source, the second being acceptable as a compromise to protect the four freedoms, and the latter two being unacceptable:

1. **Open training data**: Acceptable to Open Source and Open Data communities.
2. **Public training data**: Acceptable as a compromise to protect the four freedoms.
3. ~~**Obtainable training data**~~: Unacceptable due to obvious violation of non-discrimination clauses.
4. ~~**Unshareable non-public training data**~~: Unacceptable due to the violations of any/all of the four essential freedoms.

The charitable explanation for those claiming datasets made available “*including for a fee*” are acceptable is that they are confused about the historical context, but that is [not the only explanation](https://discuss.opensource.org/t/we-heard-you-lets-focus-on-substantive-discussion/589/16). The closer we get to the Kamikaze launch (to borrow another Japanese reference) at [12:45pm on 28 October](https://2024.allthingsopen.org/schedule), despite sustained, well-reasoned counter-arguments from many of Open Source's old guard, the more I'm inclined to come around to @Shamar's perspective that these discussions are just a front for decisions made in advance/behind closed doors, analogous to the smoke-filled back rooms of cloud (and other) standardisation efforts.

Per @thesteve0's [challenge](https://blog.techravenconsulting.com/model-weights-is-not-enough-for-open-source-ai/), you're welcome prove me wrong, not only on the rights to inspect, modify, and recreate models, and the field of use restriction, but also on the "implications of not labeling a model Open Source" — we don't owe anything to anyone but ourselves:

> The Open Source label is a restrictive condition that not everyone wants or should want. Weakening the meaning of Open Source is a mistaken means for hoping organizations will be “more Open Source”.
> 
> **Counterproof needed to falsify my position.**
> 
> Demonstrate how not allowing a model to be called Open Source prevents the owner from sharing their model weights.
