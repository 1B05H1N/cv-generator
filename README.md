# **CV Generator – McDowell-Inspired Resume Builder**  

This is an **ATS-optimized resume generator** inspired by the **McDowell CV format**, originally designed by [Gayle McDowell](https://www.gayle.com/resume). It automates resume creation using **structured JSON data**, renders it into **HTML**, and converts it to a **PDF** using **WeasyPrint**.  

## **Features**  
- **ATS-Optimized Formatting** – Ensures proper parsing by Applicant Tracking Systems.  
- **Dynamic Resume Generation** – Generates resumes from structured JSON data.  
- **Customizable HTML and CSS** – Modify templates to fit specific design needs.  
- **WeasyPrint PDF Conversion** – Converts structured HTML to a polished PDF.  
- **One-Page Resume Optimization** – Designed for clarity and conciseness.  

## **Installation**  

### **Requirements**  
- **Python 3.x**  
- **WeasyPrint** (for PDF generation)  
- System dependencies for **WeasyPrint** may be required. See [WeasyPrint installation guide](https://weasyprint.org/docs/install/) for details.  

### **Install Dependencies**  
Run:  

```sh
pip install -r requirements.txt
```

## **Usage**  

### **Prepare Your Files**  
- **Resume Data (`data.json`)** – Contains structured information including experience, education, and skills.  
- **Template Files (`cv_template.html` & `cv_template.css`)** – Define the resume layout and styling.  

### **Generate a Resume**  
Run:  

```sh
python cv_generator.py
```

This will:  
1. Render `data.json` into `cv_template.html`, creating `output.html`.  
2. Convert `output.html` to a PDF saved as `resume.pdf`.  

The file `Juan_Dough_Resume.pdf` is an example of the output generated using the included sample data (`data.json`). To create your own resume, update `data.json` with your details.

## **Customization**  

- **Modify `cv_template.html`** – Adjust section titles, layout, and fonts.  
- **Edit `cv_template.css`** – Customize styling, spacing, and design.  
- **Update `data.json`** – Change resume content as needed.  

## **ATS Optimization Tips**  
- Use standard fonts and avoid tables or images.  
- Format dates consistently (e.g., `2020 – Present`).  
- Quantify achievements where possible.  
- Ensure keywords match the job description.  

## **License**  
This project is licensed under the MIT License. See `LICENSE` for details.
