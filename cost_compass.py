
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cost Compass", layout="centered")
st.title("📊 Cost Compass: Indirect Expense Analyzer")

st.write("Upload your general ledger (GL) data and compare it against benchmark costs by category.")

# File uploaders
gl_file = st.file_uploader("Upload your General Ledger (GL) file", type=["csv", "xlsx"])
benchmark_file = st.file_uploader("Upload Benchmark Cost Table", type=["csv", "xlsx"])

if gl_file and benchmark_file:
    try:
        if gl_file.name.endswith(".csv"):
            gl_df = pd.read_csv(gl_file)
        else:
            gl_df = pd.read_excel(gl_file)

        if benchmark_file.name.endswith(".csv"):
            benchmark_df = pd.read_csv(benchmark_file)
        else:
            benchmark_df = pd.read_excel(benchmark_file)
    except Exception as e:
        st.error(f"Error reading files: {e}")
    else:
        merged_df = pd.merge(gl_df, benchmark_df, on="Category", how="left")
        merged_df["Over_Benchmark_By"] = merged_df["Amount"] - merged_df["Benchmark_Cost"]
        merged_df["Flagged"] = merged_df["Over_Benchmark_By"] > 0

        st.subheader("🔍 Analysis Results")
        st.dataframe(merged_df)

        total_flagged = merged_df["Flagged"].sum()
        total_over = merged_df.loc[merged_df["Flagged"], "Over_Benchmark_By"].sum()

        st.markdown(f"**Vendors Flagged Over Benchmark:** {total_flagged}")
        st.markdown(f"**Total Overspend Identified:** ${total_over:,.2f}")

        csv = merged_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Full Report as CSV",
            data=csv,
            file_name="cost_compass_report.csv",
            mime="text/csv"
        )
else:
    st.info("Please upload both the GL file and the benchmark file to begin analysis.")
