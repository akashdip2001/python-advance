<img align="right" alt="python_logo" width="300" src="https://github.com/akashdip2001/Python-Course-10h/raw/main/img/py_akashdip2001.png"> 

# python-advance

| [notes](https://github.com/akashdip2001/ML-Machine-Learning/blob/main/py/README.md) | [Python Projects](https://github.com/akashdip2001/Python-Projects) | [Django Projects](https://github.com/akashdip2001/pyTweet) | [python-advance](https://github.com/akashdip2001/python-advance) |
| --- | --- | --- | --- |


</br>
<div style="display: flex; align-items: center; gap: 10px;" align="center">
<a href="https://www.linkedin.com/posts/akashdip2001_python-cisconetworkingacademy-openedg-activity-7296757851341959168-IhOj?utm_source=share&utm_medium=member_desktop&rcm=ACoAADQRwRQBthwu1pD7TKHPClAilXa9CMan1H8"><img src="https://github.com/user-attachments/assets/8378642d-b779-44ef-939b-dede8c8dc004" width="140px" height="140px" /></a> &nbsp; &nbsp;
<a href="https://www.credly.com/badges/ee48f5b9-60c7-42a4-9ea4-4d9fee52d17b/public_url"><img src="https://github.com/user-attachments/assets/9d157163-1a6d-4d03-ae2b-0dbefb52b426" width="140px" height="140px" /></a> 
</div>
</br>
</br>

[![Screenshot (135)](https://github.com/user-attachments/assets/4399f437-5b35-4d9e-9479-f171381937fc)](https://www.netacad.com/courses/programming/pcap-programming-essentials-python)
[![Screenshot (136)](https://github.com/user-attachments/assets/77525285-1ac5-4b8e-b1be-69f477bbea2e)](https://pythoninstitute.org/pcep)

</br>

[![Screenshot (137)](https://github.com/user-attachments/assets/e2a5b1fc-6240-4d6a-9f79-479b8689a3af)](https://edube.org/study/pe2)
[![Screenshot (138)](https://github.com/user-attachments/assets/91ee86a9-c5ab-4bcb-a29f-29d701c18106)](https://pythoninstitute.org/pcap)

</br>
</br>

## Create a pdf using Python

```python
from fpdf import FPDF

# Create a PDF class instance
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Name area', align='C', ln=1)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add Text area
content = """
Text area
"""

pdf.multi_cell(0, 10, content)

# Save the PDF
output_path = "/mnt/data/File_Name.pdf"
pdf.output(output_path)

output_path
```

### fix errors

```python
# Replace problematic characters with simpler equivalents
corrected_content = content.replace("’", "'").replace("–", "-")

# Recreate the PDF with corrected content
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, corrected_content)

# Save the corrected PDF
output_path = "/mnt/data/File_Name.pdf"
pdf.output(output_path)

output_path
```

### Update font size

```python
# Adjusting the font size and line spacing to fit the content on one page
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=10)  # Reduced font size for more content per page
pdf.multi_cell(0, 7, corrected_content)  # Reduced line spacing

# Save the single-page PDF
output_path_one_page = "/mnt/data/File_Name.pdf"
pdf.output(output_path_one_page)

output_path_one_page
```

## Create a Word file

```python
from docx import Document

# Create a Word document
doc = Document()

# Add content to the Word document
doc.add_heading("Heading Text", level=1)
doc.add_paragraph("""
Akashdip Mahapatra
XXX, WB, India
+91-XXXXXXXXXX
akashdipXXX@gmail.com
28 November 2024
""")

doc.add_paragraph("""
Text Area
""")

# Save the Word document
output_word_path = "/mnt/data/File_Name.docx"
doc.save(output_word_path)

output_word_path
```
## Create a pptx

```python
from pptx import Presentation
from pptx.util import Inches

# Create a PowerPoint presentation
presentation = Presentation()

# Slide 1: Title Slide
slide = presentation.slides.add_slide(presentation.slide_layouts[0])
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "IAM Implementation Plan for TechCorp"
subtitle.text = "Ensuring Secure and Efficient Integration\nPrepared by [Your Team]\nDate: [Insert Date]"

# Slide 2: Introduction
slide = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Introduction"
content.text = (
    "TechCorp’s digital transformation requires robust IAM solutions.\n"
    "Challenges include global operations and integration complexity.\n"
    "Objective: Successfully implement a robust IAM platform aligned with business goals."
)

# Slide 3: Implementation Roadmap
slide = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Implementation Roadmap"
content.text = (
    "Phases:\n"
    "1. Planning & Requirement Analysis: Identify stakeholders, gather requirements.\n"
    "2. Platform Setup: Deploy IAM tools, configure access controls.\n"
    "3. Integration: Connect with legacy systems, third-party apps, cloud platforms.\n"
    "4. Testing & Validation: Conduct UAT, resolve vulnerabilities.\n"
    "5. Deployment & Go-Live: Migrate users, train staff.\n"
    "6. Post-Deployment Support: Monitor, audit, and provide support."
)

# Slide 4: Key Milestones
slide = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Key Milestones"
content.text = (
    "- Project kickoff\n"
    "- Platform installation and configuration\n"
    "- Integration completion\n"
    "- Testing and validation\n"
    "- Deployment and go-live\n"
    "- Post-deployment review"
)

# Slide 5: Resource Requirements
slide = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Resource Requirements"
content.text = (
    "Technical Resources:\n"
    "- IAM tools, licenses, middleware, and cloud services.\n\n"
    "Human Resources:\n"
    "- IAM specialists, security analysts, IT support staff.\n\n"
    "Budget Considerations:\n"
    "- Software and hardware costs, training expenses."
)

# Slide 6: Addressing Integration Challenges
slide = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Addressing Integration Challenges"
content.text = (
    "Challenges:\n"
    "- Compatibility with legacy systems.\n"
    "- Security during third-party and cloud integration.\n"
    "- Data migration complexity.\n\n"
    "Solutions:\n"
    "- Use middleware and API gateways.\n"
    "- Encrypt sensitive data during migration.\n"
    "- Conduct pilot tests for compatibility."
)

# Slide 7: Secure Access Management
slide = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Secure Access Management"
content.text = (
    "- User provisioning and lifecycle management.\n"
    "- Implement MFA and SSO.\n"
    "- Enforce least privilege and RBAC.\n"
    "- Adaptive authentication based on risk factors."
)

# Slide 8: Visual Representation
slide = presentation.slides.add_slide(presentation.slide_layouts[5])
title = slide.shapes.title
title.text = "Visual Representation"
# Placeholder text for a diagram or chart
content_box = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(2))
content = content_box.text_frame
content.text = "Insert diagram or flowchart showing IAM architecture here."

# Slide 9: Alignment with Business Goals
slide = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Alignment with Business Goals"
content.text = (
    "Enhanced Cybersecurity:\n"
    "- Protect data and mitigate unauthorized access risks.\n\n"
    "Streamlined Operations:\n"
    "- Automate user lifecycle processes.\n"
    "- Simplify access with SSO and RBAC."
)

# Slide 10: Conclusion
slide = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Conclusion"
content.text = (
    "IAM implementation ensures security and efficiency.\n"
    "Aligned with TechCorp’s digital transformation objectives.\n"
    "Next steps: Execute the plan and ensure collaboration."
)

# Save the PowerPoint presentation
file_path_pptx = "/mnt/data/IAM_Implementation_Plan_TechCorp.pptx"
presentation.save(file_path_pptx)
file_path_pptx
```




