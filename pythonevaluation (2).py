import pandas as pd
import numpy as np

#task1: create dataframes and saving

Project_dataframe = 
{
    "ID"=['A001','A002','A003','A004','A005','A002','A005','A003','A001','A003','A001','A004','A004','A005'],
    "Project"=['Project 1','Project 2','Project 3','Project 4','Project 5','Project 6','Project 7','Project 8','Project 9','Project 10','Project 11','Project 12','Project 13','Project 14'],
    "Cost"=[1002000,2000000,4500000,5500000,np.nan,680000,400000,350000,np.nan,300000,2000000,1000000,3000000,200000],
    "Status"=['Finished','Ongoing','Finished','Ongoing','Finished','Failed','Finished','Failed','Ongoing','Finished','Failed','Ongoing','Finished','Finished'],
}
Employee_dataframe =
{
    "ID"=['A001','A002','A003','A004','A005'],
    "Name"=['John Alter','Alice Luxumberg','Tom Sabestine','Nina Adgra','Amy Johny'],
    "Gender"=['M','F','M','F','F'],
    "City"=['Paris','London','Berlin','Newyork','Madrid'],
    "Age"=[25,27,29,31,30]
}
Seniority_Level_DataFrame =
{
  "ID"=['A001','A002','A003','A004','A005'],
  "Designation level"=[2,2,3,2,3]
}
Project = pd.dataframes(Project_dataframe)
employee = pd.dataframes(Employee_dataframe)
seniority = pd.dataframes(Seniority_Level_DataFrame)

Project.to_csv("Project.csv",index=False)
employee.to_csv("employee.csv",index=False)
seniority.to_csv("seniority.csv",index=False)

#task2 : Replace the missing values by running average

Project=pd.read_csv("Project.csv")
costs = Project["cost"].tolist()

for i in range(len(costs)):
    if pd.isna(costs[i]):
        prev_vals = [c for c in costs[:i] if not pd.isna(c)]
        if prev_vals:
            costs[i] = sum(prev_vals)/ len(prev_vals)
Project["cost"]= costs
Project.to_csv("Project.csv",index=False)

#Task3 : Split the name column in the Employee dataframe into two new columns “First Name”,and “LastName” 

Employee = pd.read_csv("Employee.csv")
Employee[["First Name","LastName"]] = Employee["Name"].str.Split(" ",1,expand=True)
Employee.drop("Name",axis=1,inplace=True)
employee.to_csv("employee.csv",index=False)

#Task 4 : Join all three dataframes in one single dataframe

Final = employee.merge(Project,on="ID").merge(seniority,on="ID")
Final.to_csv("Final.csv",index=False)

#Task 5 : add bonus

Final["bonus"] = Final.apply(lambda x: 0.05*x["cost"] if x["Status"] == "finish" else 0, axis=1)

#Task6 : demote Fail
Final.loc[Final["Status"] == "Fail","Designation level"] -=1
Final=Final[Final["Designation level"] <=4]

#task 8 : promote Age
Final.loc[Final["Age"]>20,"Designation level"] +=1
