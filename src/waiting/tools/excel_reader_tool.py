# src/your_project/tools/excel_reader_tool.py

from crewai_tools import tool
import pandas as pd

@tool("ExcelDataExtractorTool")
def extract_data_from_excel(file_path: str, labels: list, sheet_name: str = None) -> str:
    """
    Extracts specific labeled rows or cells from an Excel spreadsheet.
    
    Args:
        file_path (str): Path to the Excel file.
        labels (list): A list of labels to look for in the first column or index.
        sheet_name (str, optional): Name of the sheet to read. Defaults to the first sheet.
    
    Returns:
        str: A markdown table of matching label-value pairs.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    except Exception as e:
        return f"Failed to read the Excel file: {str(e)}"

    results = []
    for label in labels:
        # Look for label in first column
        match = df[df.iloc[:, 0].astype(str).str.lower() == label.lower()]
        if not match.empty:
            value = match.iloc[0, 1]  # Value in next column
            results.append((label, value))

    if not results:
        return "No matching labels found in the Excel file."

    # Build markdown table
    table = "| Label | Value |\n|-------|-------|\n"
    for label, value in results:
        table += f"| {label} | {value} |\n"

    return table
