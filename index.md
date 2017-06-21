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
<br>
<br>
<h4>Summary and Methodology</h4>
<br><br>
The team met with the project manager from Worldreader every two weeks for regular updates and direction on the project.
<br><br>
<h4>Project steps:</h4>
<br>
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
Worldreader gave our team 6 CSV files consisting of over 3,000,000 queries and related information.

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
</table>
<h2><a id="projectresults">Findings and Results</a></h2>
<br><br>
<h2><a id="projectconclusions">Conclusions</a></h2>
<br><br>
<h2><a id="projectnextsteps">Possible Next Steps</a></h2>
<br><br>
<h2><a id="projectreferences">References</a></h2>
