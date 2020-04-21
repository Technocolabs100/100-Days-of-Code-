'''
Many-to-many data merge

The final merging scenario occurs when both DataFrames do not have unique keys for a merge. What happens here is that for each duplicated key, every pairwise combination will be created.

Two example DataFrames that share common key values have been pre-loaded: df1 and df2. Another DataFrame df3, which is the result of df1 merged with df2, has been pre-loaded. All three DataFrames have been printed - look at the output and notice how pairwise combinations have been created. This example is to help you develop your intuition for many-to-many merges.

Here, you'll work with the site and visited DataFrames from before, and a new survey DataFrame. Your task is to merge site and visited as you did in the earlier exercises. You will then merge this merged DataFrame with survey.

Begin by exploring the site, visited, and survey DataFrames in the IPython Shell.

INSTRUCTIONS
100XP
-Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited, exactly as you did in the previous two exercises. Save the result as m2m.
-Merge the m2m and survey DataFrames on the 'ident' column of m2m and 'taken' column of survey.
-Hit 'Submit Answer' to print the first 20 lines of the merged DataFrame!
'''
# Merge survey, visited and site to a single data frame
# of surveys with visit and site details

# Merge survey and visited on visit IDs
survey_with_visits = pd.merge(survey, visited, left_on='taken', right_on='ident')
# or 
# survey_with_visits = survey.merge(visited, left_on='taken', right_on='ident')

# Merge previous result with site on site IDs: m2m
m2m = pd.merge(survey_with_visits, site, left_on='site', right_on='name')
# or 
# m2m = survey_with_visits.merge(site, left_on='site', right_on = 'name')

# Print m2m
print(m2m)
