import pandas as pd

# -----------------------------------------
# STEP 1: Load Input Files
# -----------------------------------------

# Read the company list (CSV file)
company_df = pd.read_csv("ml_insurance_challenge.csv")

# Read the insurance taxonomy (Excel file)
taxonomy_df = pd.read_excel("insurance_taxonomy.xlsx")

# -----------------------------------------
# STEP 2: Prepare and Clean the Taxonomy
# -----------------------------------------

# Convert taxonomy labels to lowercase and strip whitespace
taxonomy_df['label_clean'] = taxonomy_df['label'].str.lower().str.strip()

# Store all cleaned labels as a list for easy looping
insurance_labels = taxonomy_df['label_clean'].tolist()

# Optional: print first few labels to verify
print(" Cleaned insurance labels:")
print(insurance_labels[:5])

# -----------------------------------------
# STEP 3: Prepare the Company Info for Matching
# -----------------------------------------

# Fill missing (NaN) values with empty strings to avoid errors
company_df = company_df.fillna("")

# Combine all relevant fields into one searchable text string
def combine_info(row):
    return (
        row['description'].lower() + " " +
        row['business_tags'].lower() + " " +
        row['sector'].lower() + " " +
        row['category'].lower() + " " +
        row['niche'].lower()
    )

# Create a new column with the combined text for each company
company_df['combined_text'] = company_df.apply(combine_info, axis=1)

# Optional: show a sample combined entry
print("\n Example company info:")
print(company_df['combined_text'].iloc[0])

# -----------------------------------------
# STEP 4: Match Companies to Labels (Basic Logic)
# -----------------------------------------

# Match based on word overlap (at least N-1 words from label must be present)
def find_label(text, labels):
    for label in labels:
        label_words = label.split()  # Split label into individual words
        matches = sum(1 for word in label_words if word in text)
        if matches >= len(label_words) - 1:  # Allow one word to be missing
            return label
    return "No match"  # Return this if no label fits

# Apply label matching for each company
company_df['insurance_label'] = company_df['combined_text'].apply(
    lambda text: find_label(text, insurance_labels)
)

# -----------------------------------------
# STEP 5: Output the Results
# -----------------------------------------

# Show a few sample results
print("\n Sample matches:")
print(company_df[['description', 'insurance_label']].head())

# Save final results to a new CSV file
company_df.to_csv("classified_companies.csv", index=False)
print("\n Results saved to 'classified_companies.csv' 🎉")
