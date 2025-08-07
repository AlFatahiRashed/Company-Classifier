import pandas as pd


company_df = pd.read_csv("ml_insurance_challenge.csv")
taxonomy_df = pd.read_excel("insurance_taxonomy.xlsx")


taxonomy_df['label_clean'] = taxonomy_df['label'].str.lower().str.strip()
insurance_labels = taxonomy_df['label_clean'].tolist()


print("Cleaned insurance labels:")
print(insurance_labels[:5])


company_df = company_df.fillna("")


def combine_info(row):
    return (
        row['description'].lower() + " " +
        row['business_tags'].lower() + " " +
        row['sector'].lower() + " " +
        row['category'].lower() + " " +
        row['niche'].lower()
    )


company_df['combined_text'] = company_df.apply(combine_info, axis=1)


print("Example company info:")
print(company_df['combined_text'].iloc[0])


def find_label(text, labels):
    for label in labels:
        label_words = label.split()  
        matches = sum(1 for word in label_words if word in text)
        if matches >= len(label_words) - 1:  
            return label
    return "No match"



company_df['insurance_label'] = company_df['combined_text'].apply(lambda text: find_label(text, insurance_labels))


print("\nSample matches:")
print(company_df[['description', 'insurance_label']].head())


company_df.to_csv("classified_companies.csv", index=False)

print("\nResults saved to classified_companies.csv")
