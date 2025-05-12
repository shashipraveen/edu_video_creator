import win32com.client

powerpoint = win32com.client.Dispatch("PowerPoint.Application")
presentation = powerpoint.Presentations.Open(r"C:\path\to\your\presentation.pptx")
print("PowerPoint file opened successfully")
