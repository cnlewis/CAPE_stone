# ![Worldreader Logo](https://comms.worldreader.org/wp-content/themes/worldreader/assets/images/logo.png) 
# Query Data Project 


Created by Cary Lewis, Aina Pascual, Patricia Araguz and Enrique Rodríguez
<br>
<a href="http://www.ub.edu/datascience/postgraduate/">UB Data Science and Big Data</a> Capstone Project
<br><br>
Thank you to Worldreader for granting us access to its data and for supporting our Capstone Project.

<ol type="I">
<li><a href="#projectbackground">Project Background</a></li>
<li><a href="#projectscope">Project Scope and Methodology</a></li>
<li><a href="#projectwork">Project Work</a></li>
<li><a href="#projectresults">Findings and Results</a></li>
<li><a href="#projectconclusions">Conclusions</a></li>
<li><a href="#projectnextsteps">Possible Next Steps</a></li>
<li><a href="#projectreferences">References</a></li>
</ol>
<br><br><br><br>

<h2><a id="projectbackground">Project Background</a></h2>
<br>
Worldreader is non-profit organization working to reduce illiteracy through its reading applications and sponsorship programs. The organization has a collection of over 40,000 books in more than 40 languages with the mission "to unlock the potential of millions of people through the use of digital books in places where access to reading material is very limited."
<br><br>
The project team approached Worldreader as their large collection generates significant amounts data and particularly through the <a href="https://www.worldreader.org/what-we-do/worldreader-mobile/">Worldreader Open Library for mobile phones application</a>.
<br><br>
Worldreader was interested in the proposal of examining their data and in particular the organization wanted to focus on the queries from their mobile application. The project's aim was to examine the search query data with Worldreader providing a dataset of search queries and the corresponding fields from their application. All data provided would be anonymized and not include personal data in any form. Worldreader would provide supervision on the project with team members required to sign individualized agreements on data confidentiality.
<br><br><br><br>
<h2><a id="projectscope">Project Scope and Methodology</a></h2>
<br>
The Project Scope was to analyse queries made by users on the feature phone application by using clustering techniques to identify similar searches. Planned methodologies included sentiment and similarity analysis. Datasets from national libraries could be used to link with clustered search results and the texts identified. The result of the project would be to give Worldreader a better grasp on what their users are interested in reading and algorithms that the organization could use to improve upon its search queries and results in the future. The proposal left open the possibility to extend further into recommenders if possible with time permitting the project team. Another possibility was to use the Worldreader catalog to generate a recommenders system.
<h4>Summary and Methodology</h4>
The team met with the project manager from Worldreader every two weeks for regular updates and direction on the project.
<h4>Project steps:</h4>
<ul>
<li>Data cleaning</li>
<li>Data enrichment with information taken from word thesaurus and National Libraries</li>
<li>Data clustering using text analysis</li>
<ul>
<li>Identify search language and select searches in English</li>
<li>Split searches in Authors, Titles and “unknown text”</li>
<ul>
<li>Identify Book Category</li>
<li>Identify Authors</li>
</ul>
<li>Cluster the book list in k groups of items that Worldreader users could take as a recommendation book list.</li>
</ul>
<li>Cluster validation with control file</li>
<li>Script implementation in a development unit</li>
</ul>
<br><br>
<h2><a id="projectwork">Project Work</a></h2>
<br><br>
For an indepth review of the project work see the Capstone's <a href="https://github.com/cnlewis/CAPE_stone/blob/master/Script_proceso_busquedas_integrado.ipynb">Jupyter notebook</a>.
<br><br>
Figure 1: Flow Chart of Data in Capstone Project
<img src="https://raw.githubusercontent.com/cnlewis/CAPE_stone/master/images/Flujo_datos_WorldReader_en_traducidos.png">
<br><br>
Worldreader provided our team 6 CSV files consisting of over 3,000,000 queries and related information.
<br><br>
<table>
<tr>
<td><b>customer,</b></td>
<td><b>country,</b></td>
<td><b>url,</b></td>
<td><b>query,</b></td>
<td><b>created_at</b></td>
</tr>
<tr>
<td>157260,</td><td>"KE",</td><td>"/Search/Results?Query=New+Testament&Language=",</td><td>"New Testament",</td><td>"2016-12-27 15:48:16.893"</td>
</tr>
<tr>
<td>157261,</td><td>"PH",</td><td>"/Search/Results?Query=circles",</td><td>"circles",</td><td>"2016-11-12 18:14:11.933"</td>
</tr>
<tr>
<td>157261,</td><td>"PH",</td><td>"/Search/Results?Query=japanese",</td><td>"japanese",</td><td>"2016-11-18 17:15:54.19"</td>
</tr>
</table>
<h4>Examining the data required that we first clean the data and organize it.</h4>
After loading the data:
<ul>
<li>Removed the duplicate queries of each user</li>
<ul>
<li>This permitted us to see the individual unique queries from the users - duplicates could lead to errors in word frequencies</li>
</ul>
<li>Removed punctuation, irregular spacing at the beginning or end of queries, empty queries or queries that only contained numerical numbers and special characters</li>
<ul>
<li>Removing these pieces ensured our scripts would run properly without failing</li>
</ul>
<li>Used textblob and langdetect to determine query languages</li>
</ul>
<h4>Standardization of English Queries</h4>
Generating a word counter and string of corrected words
<ul>
<li>
Applying the cleaned file with language assigned and the remaining fields of interest to us, we used it to create a string variable by joining all the queries and transformed all the words to lowercase. Using the previous string variable we were then able create a word counter.</li>
<li>Selecting english for language we ran the words to determine if they were valid or invalid. We then generated a string of the incorrect words that remained to be corrected and removed the incorrect words from the corrected words counter.</li>
</ul>
Define the module with the functions from the word corrections
<ul>
<li>We generated another word counter building off the previous counter we created from our processed data files and defined the search and correcting functions for the incorrect words.</li>
<li>Begins with basic word correction (addition/removal of letters, transposing letters, and separation of words in two) selecting those words with greater likelihood of being correct when compared against the correct words.</li>
</ul>
Loading the cleaned file and using the string errors and the word correction module of the previous steps
<ul>
<li>Using the word correction module we loaded the incorrect word string generated from the spelling module.</li>
<li>The incorrect words get run through our word correction module, counting the searches once corrected and eliminating the duplicates and saving the file with corrected words.</li>
</ul>
<h4>Selected a random sample of 20,000 Queries</h4>
<ul><li>The random sample was taken from the corrected word and later is used for comparison against the total query data</li></ul>
<h4>Descriptive analysis of the most used terms in the sample of searches with generated graphs (Total vs Sample Data)</h4>
<ul>
<li>Comparison of the search distribution by country of the total file in relation to the sample file</li>
<li>Comparison of the distribution of terms from the sample with respect to the term distribution of the complete file (of searches with corrected words).</li>
<li>Generated a word cloud with the most used terms and identified the "n" first bigramas depending on their frequency of occurrence.</li>
</ul>
<h4>Supplementing the sample of 20,000 queries with Google Books API</h4>
<ul>
<li>Retriedved from the books: title, author, category and description with the Google Books API</li>
<li>Limited to a 1,000 daily searches of Google API (daily query limit per user).</li>
<li>Processed the information obtained to identify which book matches best (from a total of up to 5 candidates) depending on the appearance of terms in their title, author and description.</li>
<li>We returned a total of 5 books (the first being the best match) provided that the percentage of words in the query that appear in the title of the book returned is greater than 60%. If the search words have a percentage of appearance higher than 50% in the returned author, we consider that it is a search by author and we label it as such.</li>
<li>We then saved the results file with the 5 books associated with each query.</li>
</ul>


<h2><a id="projectresults">Findings and Results</a></h2>
<br><br>
<h2><a id="projectconclusions">Conclusions</a></h2>
<br><br>
<h2><a id="projectnextsteps">Possible Next Steps</a></h2>
<br><br>
<h4>Classification of queries based off user information</h4>
<ul>
<li>Supplement data further with user profile information (sex, age, and level of education) with the objective of studying whether there are differentiated segments of users by socio-demographic profile that allow to fine-tune the classifier for each of the groups obtained.</li>
<li>Supplement data further with information related to success or failure of the search results (with a dichotomous field, for example, that identifies whether the user found a satisfactory result or not) and analyze the predictive capacity of the model in each case.</li>
<h4>Increase sample size to see if it improves the function of the models</h4> 
<h4>Analysis of organization's catalog</h4>


<h2><a id="projectreferences">References</a></h2>
