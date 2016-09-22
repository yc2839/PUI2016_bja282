#HW2
###Ben Alpert (bja282)

To complete this assignment, I followed the steps below: 

1. I joined a work group with fellow classmates Marc Toneatto, Sofiya Elyukin, Jonathan Geis, and Scott Smith. We met in the library and worked together on the assignment. 
2. Johnathan had previously been working together with Sebastian Bana Gutierrez, whose assignments I used as helpful guidance in understanding how to approach programming, especially for the MTA assignments. (Sebastian's github: https://github.com/sbg389/PUI2016_sbg389/tree/master/HW2_sbg389) I also used the materials posted online by Professor Bianco to understand concepts and work through the assignments. 
3. Through working with the team, I was able to understand how to connect to the API. At the suggestion of Jonathan and Sofiya, I downloaded Postman, which was extremely helpful for parsing the API output and determining how to access the longitude, latitude, stop name and status data.
4. After completing "Show_Bus_Location," I began "Get_Bus_info" by using the same file as a basis. I worked through Prof. Bianco's logic line by line and gradually created the final product. I also used Sebastian's file for reference, to understand the programming.
5. I attended Professor Bianco's office hours to help remedy a problem with my Github connection, which wasn't working. 
6. To complete the last assignment, I browsed the CUSP Green environment for a file that looked interesting. I first chose 311 data, but that file proved to be too massive and was slow to load - I decided on a gas consumption file instead. Again using Prof. Bianco's files and Sebastian's assignment as reference, I worked through the problem bit by bit.
7. The biggest complication I encountered in Assignment 3 had to do with the naming of the columns. I was able to remove text columns without issue in the first part of the assignment, but had significant trouble graphing 'Consumption (therms)' & 	'Consumption (GJ)'. I eventually determined this was because the column titles had rogue spaces included in the title, and were difficult to reference as a result. I finally determined their name by using list(df_gas.columns.values). 
