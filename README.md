# **CSImpact**
**A ranking of global computer science institutions based on the impact of their research**

This project uses data from [Google Scholar](scholar.google.com) to accumulate data of various research papers of each institution's professors. Specifically, for each professor under a specific institution, it sums up each paper's h-index and number of citations, as well as when their first paper was published. By gathering data for each professor's papers, we can quantify the overall "impact" of each institution, then assign a ranking. 

We used a combination of web scraping using [Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/) and [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#), as well as data analysis using [Pandas](https://pandas.pydata.org) to gather and then rank the data. This project was created in Python 3.9 scripts.

**Contributors**
- [ychattre](https://github.com/ychhatre)
- [kevins4202](https://github.com/kevins4202)
- Under the guidance of [remzi-arpacidusseau](https://github.com/remzi-arpacidusseau)
