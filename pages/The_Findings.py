import streamlit as st;
import pandas as pd;
import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt 

data = pd.read_csv('fitbit_mean_miles_df.csv')
totals_by_id_df = data.groupby('Id')[["TotalSteps", "TotalDistance", "Calories", 'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', "SedentaryMinutes"]].sum()
st.title('Fitbit Findings:')

st.markdown("***")
st.markdown("The Objective:")
st.markdown("With our goal being to determine whether step count is a good indicator of weight loss, we would need to first start with a simple EDA looking at distribution, outliers, and other tracked metrics that could be better indicators of weight loss/health (distance, very active minutes, etc). ")
st.markdown("***")
# Quick by the numbers...
col1, col2, col3 = st.columns(3)

col1.metric("Avg. Daily Step Count", "8,253")
col2.metric("Number of Participants", "32")
col3.metric("Total Daily Log (sample size)", "940")

st.markdown("***")
st.markdown("Distributions:")
st.markdown("I first started by looking at distributions of each data point to verify that we had normal distributions and no absurd outliers. I then merged each of the categories (step count, total distance, active minutes) on ID to see if we had any outlier participants. All in all, there were several participants that were clearly more active than the average Fitbit user, but nothing that was alarming or seemed out of the ordinary. With that information, I was able to move onto the next phase of the EDA correlations.")
st.markdown("Note: In the distributions below, you'll see large spikes near the middle or top of the bell curve. This is because I replace irregular data with the mean in order to maintain a large sample size (for more details see about the data).")
col1, col2, col3 = st.columns(3)
#Distribution of Step Count By Day (mean data)
figure = plt.figure(figsize=(12,12))

ax = sns.displot(data['TotalSteps'], kde=True)

plt.ylabel('Number of Logs')
plt.xlabel('Total Steps')
plt.title('Distribution of Step Count by day (mean data)')
col1.pyplot(plt)
#Distribution of Total Distance (miles) By Day (mean data)
figure = plt.figure(figsize=(12,12))

ax = sns.displot(data['TotalDistance'], kde=True)

plt.ylabel('Number of Logs')
plt.xlabel('Total Distance')
plt.title('Distribution of Total Distance by day (mean data)')
col2.pyplot(plt)
#Distribution of Very Active Minutes By Day (mean data)
figure = plt.figure(figsize=(12,12))

ax = sns.displot(data['VeryActiveMinutes'], kde=True)

plt.ylabel('Number of Logs')
plt.xlabel('Total Very Active Minutes')
plt.title('Distribution of Very Active Minutes by day (mean data)')
col3.pyplot(plt)
#Distribution of Calories Burned By Day (mean data)
figure = plt.figure(figsize=(12,12))

ax = sns.displot(data['Calories'], kde=True)

plt.ylabel('Number of Logs')
plt.xlabel('Calories Burned')
plt.title('Distribution of Calories Burned by day (mean data)')
st.pyplot(plt)

st.markdown("As we can see from the distributions, there tend to be a few outliers as the number increase creating longer tails. However, there is nothing irregular or misleading that would cause a need for another transformation or to toss out the data. One interesting thing to note is that the distribution of step count and total distance is nearly identical, meaning that both should have high correlations and be good indicators of step count. To get a better idea of the participants in the sample, we can look at distributions of the totals by participant of each health metric category.")



col1, col2 = st.columns(2)

#Distribution of total step count by participant 
figure = plt.figure(figsize=(12,12))

ax = sns.displot(totals_by_id_df['TotalSteps'], kde=True)

plt.ylabel('Number of Participants')
plt.xlabel('Total Steps over Test')
plt.title('Distribution of total steps by Participant')
col1.pyplot(plt)
#Distribution of total distance by participant
figure = plt.figure(figsize=(12,12))
ax = sns.displot(totals_by_id_df['TotalDistance'], kde=True)
plt.ylabel('Number of Participants')
plt.xlabel('Total Distance over the course of Experiment')
plt.title('Distribution of Total Distance by Participant')
col2.pyplot(plt)

st.markdown("As you can see there was one participant with an alarmingly low step count/total distance over the course of the study. Because of this, I decided to inspect further by creating a count plot by id which can be seen below. With this infograph we can clearly see that there was not faulty data but a lack of logs. Thus, no need to scrap, and it can be used for the regressions.")

# Count plot for particpant # of daily logs
participant_counts = data['Id'].value_counts()
ordered_participant_ids = participant_counts.index
plt.figure(figsize=(40, 10))  
sns.countplot(data=data, x="Id", order=ordered_participant_ids)
plt.ylabel('Number of daily logs')
plt.xlabel('Participant ID')
plt.title('Number of daily logs by participant')
st.pyplot(plt)



col1, col2, col3= st.columns(3)

#Distribution of Lightly Minutes by participant
figure = plt.figure(figsize=(12,12))

ax = sns.displot(totals_by_id_df['LightlyActiveMinutes'], kde=True)

plt.ylabel('Number of Participants')
plt.xlabel('Total Lightly Active Minutes over Experiment')
plt.title('Distribution of Lightly Active Minutes by Participant')
col1.pyplot(plt)


#Distribution of Very Active Minutes by participant
figure = plt.figure(figsize=(12,12))

ax = sns.displot(totals_by_id_df['FairlyActiveMinutes'], kde=True)

plt.ylabel('Number of Participants')
plt.xlabel('Total Fairly Active Minutes over Experiment')
plt.title('Distribution of Fairly Active Minutes by Participant')
col2.pyplot(plt)

#Distribution of Very Active Minutes by Participant
figure = plt.figure(figsize=(12,12))

ax = sns.displot(totals_by_id_df['VeryActiveMinutes'], kde=True)

plt.ylabel('Number of Participants')
plt.xlabel('Total Very Active Minutes over Experiment')
plt.title('Distribution of Very Active Minutes by Participant')
col3.pyplot(plt)

st.markdown("This final trio of distributions is to take a look at the activity levels of particpants. Based upon the lightly, fairly, and very active minute categories (see data dictionary for more details) we can see that the majority of the particpants exercised regularly. Some of the top outliers appear to be distance runners, which is why they are far ahead on very active minutes.")

st.markdown("***")
st.markdown("Correlation:")
st.markdown("After the distributions had been performed, I then was able to look at correlations between each category and calories burned. This would help us understand if there were any clear winners for predicting weight loss across all the categories. However, we must remember that correlation does not mean causation. Thus, we need to look at the models and perform testing in order to really say whether step count, total distance or active minutes are good indicators of calories burned and in turn cause weight loss.")
#Heatmaps 
heat_map_chart_mean_df = data[['TotalSteps', "TotalDistance", "VeryActiveMinutes", "Calories"]]
corr_matrix = heat_map_chart_mean_df.corr()
fig = plt.figure()
plt.title("Heatmap of Health Metric Correlations")
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
st.pyplot(plt)
st.markdown("The heat map above shows the categories that ended up having the highest correlations to calories burned (lightly active minutes, fairly active minutes, and sedintary minutes were all lower than .25)... From the heatmap we can see that TotalDistance and VeryActiveMinutes have very similiar correlations to calories. Total steps is right below both categories. Thus, it is important that we build both simple linear and multivariate regression models to see what health metric is truly the best fit.")

st.markdown("***")

st.markdown("***")
st.markdown("Correlation:")
st.markdown("")
st.markdown("***")

st.markdown("***")
st.markdown("Model Building:")
st.markdown("")
st.markdown("***")

st.markdown("***")
st.markdown("Me vs. the Model:")
st.markdown("")
st.markdown("***")

st.markdown("***")
st.markdown("Conclusion")
st.markdown("")
st.markdown("***")