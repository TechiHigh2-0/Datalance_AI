import pandas as pd
from dotenv import load_dotenv
load_dotenv()
from src.ask_data import answer_question

print("--- Testing Freelance Jobs Competition (Multi-step + Z-Score) ---")
df = pd.DataFrame({
    "platform": ["Upwork", "Upwork", "Upwork", "Fiverr", "Fiverr", "Fiverr"],
    "job_title": ["Dev", "Design", "Write", "Dev", "Design", "Write"],
    "proposals_count": [50, 10, 5, 200, 150, 20]
})

q = "Create a derived metric called competition_intensity = proposals_count normalized within each platform using a z-score. Identify the most unusually competitive jobs and explain why platform-wise normalization is preferable to global normalization."
print(answer_question(df, q))

print("\n--- Testing Conditional Multiple Filters ---")
q2 = "Among jobs with proposals_count > 15, which platform has the highest average proposals?"
print(answer_question(df, q2))
