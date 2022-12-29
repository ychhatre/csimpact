# **CSImpact**
### **A ranking of computer science programs of global institutions based on the impact of their research**



This project uses data from [Google Scholar](scholar.google.com) to accumulate data of various research papers of each institution's professors. We can quantify the overall "impact" of each institution, then assign a ranking to the university based on the collective data of its professors. 

We used a combination of web scraping using [Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/) and [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#), as well as data analysis using [Pandas](https://pandas.pydata.org) to gather and then rank the data. This project was created in Python 3.9 scripts.

### **Ranking System**

We combined four different ranking systems to get the overall ranking:
* Total Citations
* Total h-index
* Average Citations
* Average h-index

The 3rd and 4th rankings were derived by dividing the total of that metric (i.e. total citations, total h-index) by the number of professors. By using average indicies, we hoped to consider the holistic impacts of all of the faculty. 

To achieve the [overall ranking](https://github.com/ychhatre/csimpact/blob/main/data/college_avg_rank.csv), we took an average of the four indicies above. For example, UC Berkely has rankings of 0, 1, 1, 1, respectively and thus has an overall ranking of $$\dfrac{0 + 1 + 1 + 1}{4}$$ = 0.75 (with 0 being the highest). We then simply sorted the colleges based on their overall score.

### **Future Improvements**

We would like to make it so that the rankings would automatically update themselves, as well as incorporate other metrics to make these rankings more accurate, such as paper awards and possibly ranking sub-categories of their computer science programs (i.e. Systems, Robotics, and A.I.)

<br>

**Contributors**
- [kevins4202](https://github.com/kevins4202)
- [ychattre](https://github.com/ychhatre)
- Under the guidance of [remzi-arpacidusseau](https://github.com/remzi-arpacidusseau)
