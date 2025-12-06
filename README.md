**Health Analytics Dashboard**

	WHOOP Personal Data + Fitbit Public Dataset Analysis Using MongoDB, Python, and Streamlit.
	This project develops a comprehensive health analytics dashboard that compares Rafi’s personal WHOOP data with public Fitbit activity and sleep datasets.
	The dashboard provides visual insights into activity, sleep, HRV, strain, calories, and more, using a modern data pipeline:
		•	MongoDB Atlas (NoSQL database)
		•	Python (Pandas, PyMongo)
		•	Streamlit (interactive web dashboard)
		•	Altair (visualization library)



**Project Goals**

	This project successfully implements:
	•	Multi-source data integration
	•	ETL Pipeline (Extract, Transform, Load)
	•	Interactive dashboard in Streamlit
	•	Comparative Analysis



**Data Sources**

	Fitbit Public Dataset
		•	Daily Activity
		•	Sleep Logs
		•	Steps, Calories, Intensity Minutes
	
	WHOOP Personal Dataset
		•	Heart Rate Variability (HRV)
		•	Resting Heart Rate (RHR)
		•	Day Strain
		•	Energy Burn
		•	Sleep Duration
		•	Sleep Performance (%)



**MongoDB Schema**
	
	The project uses MongoDB Atlas as the central data store, organizing all Fitbit and WHOOP datasets into separate, well-structured collections. 
	Each collection represents a specific type of health data, allowing for flexible querying and efficient analysis. 
	The Fitbit datasets are stored in daily_activity and sleep_day, containing user activity logs, steps, calories, and sleep records for more than 30 users. 
	All collections use a consistent date field normalized to YYYY-MM-DD, making them easy to merge and compare during analysis. 
	This schema design leverages MongoDB’s document-based structure, enabling scalable storage, fast aggregation, and seamless integration with Python through 
	PyMongo for building the Streamlit dashboard.



**Dashboard Features**

	Your dashboard contains 6 main tabs:
	•	Project Description
	•	Fitbit Activity
	•	Fitbit Sleep
	•	WHOOP Activity
	•	WHOOP Sleep
	•	Comparisons



**Future Improvements**

	•	Add machine learning predictions
	•	Add personal vs population trend anomalies
	•	Integrate heart rate time series for deeper analysis
	•	Add user authentication to support multiple WHOOP users
