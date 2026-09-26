import pandas as pd

df = pd.read_csv("marketing_dataset.csv")

print(df.head())

df.columns = df.columns.astype(str).str.strip()

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate IDs:")
print(df["ID"].duplicated().sum())


print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nBasic statistics:")
print(df.describe())

print("\nIncome statistics:")
print(df["Income"].agg(["min", "max", "mean"]))

print("\nYear of birth statistics:")
print(df["Year_Birth"].agg(["min", "max", "mean"]))

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())
print("\nEducation distribution:")
print(df["Education"].value_counts())

print("\nEducation percentage:")
print(df["Education"].value_counts(normalize=True) * 100)

print("\nMarital status distribution:")
print(df["Marital_Status"].value_counts())


df["TotalSpending"] = df[
    [
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntSweetProducts",
        "MntGoldProds"
    ]
].sum(axis=1)

print("\nTotal spending statistics:")
print(df["TotalSpending"].agg(["min", "max", "mean"]))

print("\nAverage spending by education:")
print(
    df.groupby("Education")["TotalSpending"]
    .mean()
    .sort_values(ascending=False)
)

import matplotlib.pyplot as plt

education_spending = (
    df.groupby("Education")["TotalSpending"]
    .mean()
    .sort_values(ascending=False)
)

education_spending.plot(kind="bar")

plt.title("Average Spending by Education")
plt.xlabel("Education")
plt.ylabel("Average Total Spending")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nCustomer count by education:")
print(df["Education"].value_counts())

education_analysis = df.groupby("Education").agg(
    Customer_Count=("ID", "count"),
    Average_Spending=("TotalSpending", "mean")
).sort_values("Average_Spending", ascending=False)

print("\nEducation analysis:")
print(education_analysis)

print("\nIncome vs Total Spending correlation:")
print(df["Income"].corr(df["TotalSpending"]))



plt.figure(figsize=(8, 5))

plt.scatter(df["Income"], df["TotalSpending"])

plt.title("Income vs Total Spending")
plt.xlabel("Income")
plt.ylabel("Total Spending")

plt.tight_layout()
plt.show()

print("\nHighest income customers:")
print(
    df[["ID", "Income", "TotalSpending"]]
    .sort_values("Income", ascending=False)
    .head(10)
)

from datetime import datetime

current_year = datetime.now().year

df["Age"] = current_year - df["Year_Birth"]

print("\nAge statistics:")
print(df["Age"].agg(["min", "max", "mean", "median"]))

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 30, 40, 50, 60, 100],
    labels=["Under 30", "30-39", "40-49", "50-59", "60+"]
)

print("\nCustomer count by age group:")
print(df["Age_Group"].value_counts().sort_index())

print("\nAverage spending by age group:")
print(
    df.groupby("Age_Group", observed=True)["TotalSpending"]
    .mean()
    .sort_values(ascending=False)
)

campaign_columns = [
    "AcceptedCmp1",
    "AcceptedCmp2",
    "AcceptedCmp3",
    "AcceptedCmp4",
    "AcceptedCmp5"
]

df["TotalCampaignAccepted"] = df[campaign_columns].sum(axis=1)

print("\nCampaign acceptance distribution:")
print(df["TotalCampaignAccepted"].value_counts().sort_index())

print("\nAverage spending by campaigns accepted:")
print(
    df.groupby("TotalCampaignAccepted")["TotalSpending"]
    .mean()
    .sort_values(ascending=False)
)

campaign_spending = df.groupby(
    "TotalCampaignAccepted"
)["TotalSpending"].mean()

campaign_spending.plot(kind="bar")

plt.title("Average Spending by Number of Campaigns Accepted")
plt.xlabel("Number of Campaigns Accepted")
plt.ylabel("Average Total Spending")
plt.tight_layout()
plt.show()

product_columns = [
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds"
]

product_spending = df[product_columns].sum().sort_values(ascending=False)

print("\nTotal spending by product category:")
print(product_spending)


product_spending.plot(kind="bar")

plt.title("Total Spending by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Spending")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




product_average = df[product_columns].mean().sort_values(ascending=False)

print("\nAverage spending per customer by product category:")
print(product_average)

channel_columns = [
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases"
]

channel_usage = df[channel_columns].mean().sort_values(ascending=False)

print("\nAverage purchases by channel:")
print(channel_usage)

channel_usage.plot(kind="bar")

plt.title("Average Purchases by Channel")
plt.xlabel("Purchase Channel")
plt.ylabel("Average Number of Purchases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df["TotalPurchases"] = df[
    [
        "NumWebPurchases",
        "NumCatalogPurchases",
        "NumStorePurchases"
    ]
].sum(axis=1)

print("\nTotal purchases statistics:")
print(df["TotalPurchases"].agg(["min", "max", "mean", "median"]))

df["SpendingSegment"] = pd.qcut(
    df["TotalSpending"],
    4,
    labels=["Low", "Medium", "High", "Very High"]
)

print("\nSpending segment distribution:")
print(df["SpendingSegment"].value_counts().sort_index())

segment_analysis = df.groupby("SpendingSegment", observed=True).agg(
    Customer_Count=("ID", "count"),
    Average_Income=("Income", "mean"),
    Average_Age=("Age", "mean"),
    Average_Campaigns_Accepted=("TotalCampaignAccepted", "mean"),
    Average_Total_Purchases=("TotalPurchases", "mean"),
    Average_Spending=("TotalSpending", "mean")
)

print("\nCustomer segment analysis:")
print(segment_analysis)

campaign_by_segment = df.groupby(
    "SpendingSegment",
    observed=True
)["Response"].mean() * 100

print("\nCampaign response rate by spending segment:")
print(campaign_by_segment)

campaign_by_segment.plot(kind="bar")

plt.title("Campaign Response Rate by Spending Segment")
plt.xlabel("Spending Segment")
plt.ylabel("Response Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print(df["TotalSpending"].quantile([0.25, 0.50, 0.75]))