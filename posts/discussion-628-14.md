[quote="grugnog, post:13, topic:628"]
The clarification on the meaning of “Data Information” in this context is helpful - that seems like a very confusing term! Especially given the widely used “information is data with meaning” definition, my intuitive sense on first reading this (as a native English speaker) was that was trying to include both raw data and manually curated information.
[/quote]

If we don't understand it ourselves here, what hope does anyone else have? This wordsmithing is attempting to square the circle, but terms like "skilled person" appear to be amateur lawyering borrowing from patent, contract, and/or tort law where they have a specific legal meaning (IANAL either, by the way).

Absent "judges" to "execute" this "code" and "police" to "enforce" those decisions under the threat of violence, they serve no purpose here.

[quote="grugnog, post:13, topic:628"]
While I would still prefer open licensed training data (which is the “source” of the model weights, surely), I am more concerned about the inclusion of latter two classes of data than I am public data, as they have a much more substantive negative impact on the freedoms to Share, Study, and Modify the model in its entirety.
[/quote]

Surely, because if not then what? Unobtainable inputs (* except for million- and billionaires) are obviously absolute kryptonite for openness, and it boggles the mind that intelligent people are saying with a straight face that either of the latter categories are even candidates for inclusion. I may not be right about this, but I'm definitely not wrong.

The [open definition](https://opendefinition.org/) most succinctly requires:

> “Open data and content can be **freely used, modified, and shared** by **anyone** for **any purpose**”

Open Source additionally explicitly protects the freedom to *study*, but that's implicit here. The [Free Software definition](https://www.gnu.org/philosophy/free-sw.en.html#make-changes) actually merges *study* and *modify* because you can't do the latter without the former (which is also why any and all documentation is optional):

> The freedom to study how the program works, and change it so it does your computing as you wish (freedom 1). Access to the source code is a precondition for this.

They also deviate from "preferred" form because that too is surprisingly subjective, opting instead for whatever the developer *actually* changes:

> Source code is defined as the preferred form of the program for making changes in. Thus, **whatever form a developer changes to develop the program** is the source code of that developer's version.

The way to test this is to look at what the original developers *actually* changed to develop the system, or have developers make *actual* modifications/improvements to an existing system and look over their shoulders to see what inputs they used. Eliminating "preferred" in favour of "actual" would sharpen up this discussion significantly.

Improvements are subjective too, and developers must be allowed to make whatever change they want, in no way restricted to, for example, what is possible by fine-tuning model weights. If I want to make my self-driving car's [ASS feature fart on failure](https://www.notateslaapp.com/news/2288/tesla-updates-actually-smart-summon-on-fsd-v12541) — that's actually a thing a developer implemented in production code that made it into my vehicle last week — then that's on me:

> Whether a change constitutes an **improvement is a subjective matter**. If your right to modify a program is limited, in substance, to changes that someone else considers an improvement, that program is not free.

For these and other reasons, the first release candidate remains a field of red flags.
