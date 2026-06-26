import os
import asyncio
from playwright.async_api import async_playwright

# Data for 10 diverse Indian resumes
RESUMES_DATA = [
    {
        "filename": "aarav_sharma_it.pdf",
        "title": "Aarav Sharma - Software Engineer",
        "html": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Aarav Sharma - Software Engineer</title>
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Inter', sans-serif;
                    color: #1f2937;
                    margin: 0;
                    padding: 40px;
                    line-height: 1.5;
                    background-color: #ffffff;
                }
                .header {
                    border-bottom: 2px solid #1e3a8a;
                    padding-bottom: 20px;
                    margin-bottom: 25px;
                }
                .name {
                    font-size: 28px;
                    font-weight: 700;
                    color: #1e3a8a;
                    margin: 0;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }
                .title {
                    font-size: 16px;
                    font-weight: 600;
                    color: #4b5563;
                    margin: 5px 0 10px 0;
                }
                .contact {
                    font-size: 13px;
                    color: #6b7280;
                    display: flex;
                    gap: 15px;
                    flex-wrap: wrap;
                }
                .contact a { color: #1e3a8a; text-decoration: none; }
                .section {
                    margin-bottom: 25px;
                }
                .section-title {
                    font-size: 14px;
                    font-weight: 700;
                    color: #1e3a8a;
                    text-transform: uppercase;
                    border-bottom: 1px solid #e5e7eb;
                    padding-bottom: 4px;
                    margin-bottom: 12px;
                    letter-spacing: 0.5px;
                }
                .summary-text {
                    font-size: 13px;
                    color: #374151;
                }
                .exp-item {
                    margin-bottom: 15px;
                }
                .exp-header {
                    display: flex;
                    justify-content: space-between;
                    font-weight: 600;
                    font-size: 13px;
                    color: #111827;
                }
                .exp-company {
                    color: #1e3a8a;
                }
                .exp-date {
                    color: #6b7280;
                    font-weight: 400;
                }
                .exp-title {
                    font-style: italic;
                    font-size: 13px;
                    color: #4b5563;
                    margin: 2px 0 6px 0;
                }
                .exp-bullets {
                    margin: 0;
                    padding-left: 20px;
                    font-size: 12.5px;
                    color: #4b5563;
                }
                .exp-bullets li {
                    margin-bottom: 4px;
                }
                .grid-2 {
                    display: grid;
                    grid-template-columns: 2fr 1fr;
                    gap: 30px;
                }
                .skills-list {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 8px;
                    padding: 0;
                    list-style: none;
                    margin: 0;
                }
                .skills-list li {
                    background-color: #f3f4f6;
                    color: #1f2937;
                    padding: 4px 10px;
                    border-radius: 4px;
                    font-size: 12px;
                    font-weight: 500;
                }
                .edu-item {
                    font-size: 13px;
                    margin-bottom: 8px;
                }
                .edu-degree { font-weight: 600; }
                .edu-school { color: #4b5563; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1 class="name">Aarav Sharma</h1>
                <div class="title">Lead Full-Stack Software Engineer</div>
                <div class="contact">
                    <span>Email: aarav.sharma@example.com</span>
                    <span>Phone: +91 98765 43210</span>
                    <span>Bengaluru, India</span>
                    <span><a href="#">linkedin.com/in/aaravsharma</a></span>
                </div>
            </div>
            
            <div class="section">
                <!-- NOTE: NO header, starts directly with years of experience in first line -->
                <p class="summary-text">
                    <strong>Lead Software Engineer with 7+ years of experience</strong> architecting and implementing robust web solutions. Expert in Javascript, Python, and cloud infrastructure with a proven history of boosting page speed by 40% and leading agile development squads in high-growth SaaS environments.
                </p>
            </div>
            
            <div class="grid-2">
                <div>
                    <div class="section">
                        <div class="section-title">Professional History</div>
                        
                        <div class="exp-item">
                            <div class="exp-header">
                                <span class="exp-company">TechVanguard Solutions</span>
                                <span class="exp-date">2022 - Present</span>
                            </div>
                            <div class="exp-title">Lead Software Engineer</div>
                            <ul class="exp-bullets">
                                <li>Re-architected legacy monolithic services into Python/FastAPI microservices, boosting throughput by 150%.</li>
                                <li>Led a team of 6 engineers to launch a real-time analytics dashboard using React, TailwindCSS, and WebSocket integrations.</li>
                                <li>Optimized CI/CD pipelines, cutting deployment times from 45 minutes down to 8 minutes.</li>
                            </ul>
                        </div>
                        
                        <div class="exp-item">
                            <div class="exp-header">
                                <span class="exp-company">Infosys Ltd</span>
                                <span class="exp-date">2019 - 2022</span>
                            </div>
                            <div class="exp-title">Senior Software Developer</div>
                            <ul class="exp-bullets">
                                <li>Designed and deployed secure payment gateway integrations handling over 50,000 daily transactions.</li>
                                <li>Refactored UI components to utilize React hook patterns, resulting in a 25% reduction in client-side bundle size.</li>
                                <li>Mentored 4 junior engineers and conducted regular code quality audits.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div>
                    <div class="section">
                        <div class="section-title">Technical Expertise</div>
                        <ul class="skills-list">
                            <li>React.js</li>
                            <li>Node.js</li>
                            <li>Python</li>
                            <li>FastAPI</li>
                            <li>PostgreSQL</li>
                            <li>Docker</li>
                            <li>AWS</li>
                            <li>CI/CD</li>
                            <li>GraphQL</li>
                        </ul>
                    </div>
                    
                    <div class="section">
                        <div class="section-title">Education</div>
                        <div class="edu-item">
                            <div class="edu-degree">B.Tech in Computer Science</div>
                            <div class="edu-school">B.M.S. College of Engineering</div>
                            <div style="color: #6b7280; font-size: 11px;">Graduated: 2019 | Bengaluru</div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    },
    {
        "filename": "priya_patel_hr.pdf",
        "title": "Priya Patel - HR Manager",
        "html": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Priya Patel - HR Manager</title>
            <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Outfit', sans-serif;
                    color: #27272a;
                    margin: 0;
                    padding: 0;
                    background-color: #f8fafc;
                    display: flex;
                    min-height: 100vh;
                }
                .sidebar {
                    width: 28%;
                    background-color: #065f46;
                    color: #f0fdf4;
                    padding: 40px 25px;
                }
                .main-content {
                    width: 72%;
                    background-color: #ffffff;
                    padding: 40px;
                }
                .name {
                    font-size: 28px;
                    font-weight: 700;
                    margin-bottom: 5px;
                    letter-spacing: 0.5px;
                }
                .title {
                    font-size: 14px;
                    font-weight: 600;
                    text-transform: uppercase;
                    color: #a7f3d0;
                    margin-bottom: 30px;
                    letter-spacing: 1px;
                }
                .sidebar-section {
                    margin-bottom: 30px;
                }
                .sidebar-title {
                    font-size: 13px;
                    font-weight: 700;
                    text-transform: uppercase;
                    border-bottom: 1px solid #047857;
                    padding-bottom: 5px;
                    margin-bottom: 15px;
                    letter-spacing: 0.8px;
                    color: #34d399;
                }
                .sidebar-contact {
                    font-size: 12.5px;
                    line-height: 1.8;
                }
                .sidebar-skills {
                    list-style: none;
                    padding: 0;
                    margin: 0;
                }
                .sidebar-skills li {
                    font-size: 12.5px;
                    margin-bottom: 8px;
                    display: flex;
                    align-items: center;
                }
                .sidebar-skills li::before {
                    content: "•";
                    color: #34d399;
                    margin-right: 8px;
                    font-weight: bold;
                }
                .section-title {
                    font-size: 15px;
                    font-weight: 700;
                    text-transform: uppercase;
                    color: #065f46;
                    border-bottom: 2px solid #ecfdf5;
                    padding-bottom: 6px;
                    margin-top: 0;
                    margin-bottom: 15px;
                    letter-spacing: 0.5px;
                }
                .section {
                    margin-bottom: 30px;
                }
                .profile-text {
                    font-size: 13.5px;
                    line-height: 1.6;
                    color: #4b5563;
                }
                .job-card {
                    margin-bottom: 20px;
                }
                .job-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: baseline;
                    margin-bottom: 4px;
                }
                .job-role {
                    font-size: 14px;
                    font-weight: 700;
                    color: #18181b;
                }
                .job-company-location {
                    font-size: 12.5px;
                    color: #065f46;
                    font-weight: 600;
                }
                .job-dates {
                    font-size: 12px;
                    color: #71717a;
                }
                .job-bullets {
                    margin: 0;
                    padding-left: 20px;
                    font-size: 13px;
                    color: #4b5563;
                    line-height: 1.6;
                }
                .job-bullets li {
                    margin-bottom: 6px;
                }
            </style>
        </head>
        <body>
            <div class="sidebar">
                <h1 class="name">Priya Patel</h1>
                <div class="title">Human Resources Manager</div>
                
                <div class="sidebar-section">
                    <div class="sidebar-title">Contact</div>
                    <div class="sidebar-contact">
                        📞 +91 91234 56789<br>
                        ✉️ priya.patel@example.com<br>
                        📍 Mumbai, Maharashtra<br>
                        🔗 linkedin.com/in/priyapatel-hr
                    </div>
                </div>
                
                <div class="sidebar-section">
                    <div class="sidebar-title">Core Competencies</div>
                    <ul class="sidebar-skills">
                        <li>Talent Acquisition</li>
                        <li>Employee Relations</li>
                        <li>Performance Management</li>
                        <li>HR Policy & Compliance</li>
                        <li>HRIS Tools (Workday)</li>
                        <li>Conflict Resolution</li>
                    </ul>
                </div>

                <div class="sidebar-section">
                    <div class="sidebar-title">Education</div>
                    <div style="font-size: 12.5px; line-height: 1.5;">
                        <strong>MBA in Human Resources</strong><br>
                        NMIMS, Mumbai<br>
                        <span style="color: #a7f3d0; font-size: 11px;">Class of 2018</span>
                    </div>
                </div>
            </div>
            
            <div class="main-content">
                <div class="section">
                    <div class="section-title">Career Profile</div>
                    <p class="profile-text">
                        Dynamic and results-driven HR professional with over 8 years of success in managing full-cycle talent acquisition, driving employee engagement initiatives, and aligning HR strategies with corporate goals. Adept at establishing highly collaborative office environments and streamlining onboarding procedures to reduce early turnover by 30%.
                    </p>
                </div>
                
                <div class="section">
                    <div class="section-title">Professional Experience</div>
                    
                    <div class="job-card">
                        <div class="job-header">
                            <span class="job-role">Human Resources Manager</span>
                            <span class="job-dates">Oct 2021 - Present</span>
                        </div>
                        <div class="job-company-location">Reliance Industries Ltd | Mumbai</div>
                        <ul class="job-bullets">
                            <li>Manage employee relations and HR policies for a business unit of 450+ corporate employees.</li>
                            <li>Designed a modern performance appraisal framework, leading to a 15% boost in average worker engagement scores.</li>
                            <li>Partnered with executive leadership to identify staffing gaps and hired 80+ top-tier professionals.</li>
                        </ul>
                    </div>
                    
                    <div class="job-card">
                        <div class="job-header">
                            <span class="job-role">Assistant HR Manager</span>
                            <span class="job-dates">Jun 2018 - Sep 2021</span>
                        </div>
                        <div class="job-company-location">Tata Consultancy Services | Pune</div>
                        <ul class="job-bullets">
                            <li>Spearheaded a modernized corporate onboarding program, slashing training ramp-up times from 6 weeks to 4 weeks.</li>
                            <li>Resolved complex employee grievances and conducted independent internal reviews.</li>
                            <li>Administered monthly payroll operations and updated benefits structures for regional branches.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    },
    {
        "filename": "amit_verma_pm.pdf",
        "title": "Amit Verma - Project Manager",
        "html": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Amit Verma - Project Manager</title>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Roboto', sans-serif;
                    color: #2b2b2b;
                    margin: 0;
                    padding: 45px;
                    background-color: #ffffff;
                }
                .name {
                    font-size: 32px;
                    font-weight: 700;
                    color: #4c1d95;
                    margin: 0 0 5px 0;
                }
                .title {
                    font-size: 16px;
                    font-weight: 500;
                    color: #6d28d9;
                    text-transform: uppercase;
                    letter-spacing: 1.5px;
                    margin-bottom: 15px;
                }
                .contact-info {
                    font-size: 13px;
                    color: #555;
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    border-top: 1px solid #ddd;
                    border-bottom: 1px solid #ddd;
                    padding: 10px 0;
                    margin-bottom: 25px;
                }
                .section {
                    margin-bottom: 25px;
                }
                .section-header {
                    font-size: 15px;
                    font-weight: 700;
                    color: #4c1d95;
                    margin-bottom: 10px;
                    text-transform: uppercase;
                    border-left: 4px solid #8b5cf6;
                    padding-left: 10px;
                }
                .summary {
                    font-size: 13.5px;
                    line-height: 1.6;
                }
                .exp-item {
                    margin-bottom: 20px;
                }
                .exp-title-row {
                    display: flex;
                    justify-content: space-between;
                    font-weight: 700;
                    font-size: 14px;
                }
                .exp-org {
                    color: #6d28d9;
                }
                .exp-dates {
                    color: #666;
                    font-weight: 400;
                }
                .exp-subtitle {
                    font-weight: 500;
                    color: #444;
                    font-size: 13px;
                    margin: 3px 0 8px 0;
                }
                .bullets {
                    margin: 0;
                    padding-left: 20px;
                    font-size: 13px;
                    color: #444;
                }
                .bullets li {
                    margin-bottom: 6px;
                }
                .skills-grid {
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 10px;
                    font-size: 13px;
                }
                .skills-cat {
                    font-weight: 700;
                    color: #4c1d95;
                }
            </style>
        </head>
        <body>
            <h1 class="name">Amit Verma</h1>
            <div class="title">Senior Project Manager</div>
            
            <div class="contact-info">
                <div>📞 +91 93456 78901</div>
                <div>✉️ amit.verma@example.com</div>
                <div>📍 New Delhi, India</div>
                <div>🔗 linkedin.com/in/amitvermapm</div>
            </div>
            
            <div class="section">
                <div class="section-header">Executive Summary</div>
                <div class="summary">
                    <strong>PMP® certified Senior Project Manager with 9+ years of professional experience</strong> directing high-impact enterprise software deployments. Expert in Agile/Scrum methodologies, cross-functional team leadership, and risk mitigation strategies. Successfully managed portfolios worth up to $3M with a 98% on-time delivery rate.
                </div>
            </div>
            
            <div class="section">
                <div class="section-header">Employment History</div>
                
                <div class="exp-item">
                    <div class="exp-title-row">
                        <span class="exp-org">Cognizant Technology Solutions</span>
                        <span class="exp-dates">2021 - Present</span>
                    </div>
                    <div class="exp-subtitle">Senior Project Manager</div>
                    <ul class="bullets">
                        <li>Supervise development cycles for 3 offshore agile scrum teams developing core cloud infrastructure projects.</li>
                        <li>Coordinated resource planning and sprint planning using Jira, enhancing sprint predictability by 35%.</li>
                        <li>Spearheaded risk management workshops, identifying bottlenecks early and saving $80K in potential cost overrun.</li>
                    </ul>
                </div>
                
                <div class="exp-item">
                    <div class="exp-title-row">
                        <span class="exp-org">Wipro Technologies</span>
                        <span class="exp-dates">2017 - 2021</span>
                    </div>
                    <div class="exp-subtitle">Project Coordinator / Scrum Master</div>
                    <ul class="bullets">
                        <li>Facilitated daily stand-ups, retrospective meetings, and product backlog grooming for dual development teams.</li>
                        <li>Managed communication channels between stakeholders and developer teams, resolving scope creep issues.</li>
                        <li>Assisted in tracking project milestones, delivering 4 critical releases ahead of schedule.</li>
                    </ul>
                </div>
            </div>
            
            <div class="section">
                <div class="section-header">Core Expertise</div>
                <div class="skills-grid">
                    <div><span class="skills-cat">Project Management:</span> Agile, Scrum, Kanban, PMP</div>
                    <div><span class="skills-cat">Tools & Platforms:</span> Jira, Confluence, MS Project, Trello</div>
                    <div><span class="skills-cat">Processes:</span> Budgeting, Risk Analysis, SDLC</div>
                </div>
            </div>
        </body>
        </html>
        """
    },
    {
        "filename": "neha_gupta_devops.pdf",
        "title": "Neha Gupta - DevOps Engineer",
        "html": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Neha Gupta - DevOps Engineer</title>
            <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Poppins', sans-serif;
                    color: #1e293b;
                    margin: 0;
                    padding: 0;
                    background-color: #ffffff;
                }
                .top-block {
                    background-color: #0f172a;
                    color: #f8fafc;
                    padding: 40px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .name {
                    font-size: 28px;
                    font-weight: 700;
                    margin: 0;
                }
                .title {
                    font-size: 14px;
                    font-weight: 400;
                    color: #f59e0b;
                    margin-top: 5px;
                    letter-spacing: 2px;
                    text-transform: uppercase;
                }
                .contact-details {
                    font-size: 12.5px;
                    text-align: right;
                    line-height: 1.6;
                }
                .content-wrapper {
                    padding: 40px;
                }
                .section-header {
                    font-size: 14px;
                    font-weight: 700;
                    text-transform: uppercase;
                    color: #0f172a;
                    border-bottom: 2px solid #f59e0b;
                    padding-bottom: 4px;
                    margin-top: 0;
                    margin-bottom: 15px;
                    letter-spacing: 1px;
                }
                .summary {
                    font-size: 13px;
                    color: #475569;
                    margin-bottom: 30px;
                }
                .experience-card {
                    margin-bottom: 25px;
                }
                .exp-title {
                    display: flex;
                    justify-content: space-between;
                    font-weight: 700;
                    font-size: 13.5px;
                }
                .exp-company {
                    color: #f59e0b;
                }
                .exp-meta {
                    font-size: 12px;
                    color: #64748b;
                    margin: 4px 0 8px 0;
                }
                .exp-bullets {
                    padding-left: 20px;
                    margin: 0;
                    font-size: 12.5px;
                    color: #334155;
                }
                .exp-bullets li {
                    margin-bottom: 6px;
                }
                .skills-container {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 8px;
                    margin-bottom: 30px;
                }
                .skill-badge {
                    font-family: 'Fira Code', monospace;
                    background-color: #f1f5f9;
                    color: #0f172a;
                    padding: 4px 10px;
                    border-radius: 4px;
                    font-size: 11px;
                    font-weight: 600;
                    border: 1px solid #e2e8f0;
                }
            </style>
        </head>
        <body>
            <div class="top-block">
                <div>
                    <h1 class="name">Neha Gupta</h1>
                    <div class="title">Lead DevOps & Cloud Engineer</div>
                </div>
                <div class="contact-details">
                    ✉️ neha.gupta@example.com<br>
                    📞 +91 94567 89012<br>
                    📍 Hyderabad, Telangana
                </div>
            </div>
            
            <div class="content-wrapper">
                <div style="margin-bottom: 30px;">
                    <div class="section-header">Summary of Qualifications</div>
                    <p class="summary">
                        Highly collaborative DevOps specialist with over 6 years of expertise implementing continuous deployment and server scaling models. Expert in AWS, Kubernetes, Terraform, and Docker configurations. Proven record of migrating 20+ legacy servers to cloud environments, resulting in an immediate 35% decrease in hosting expenses.
                    </p>
                </div>

                <div style="margin-bottom: 30px;">
                    <div class="section-header">Career Achievements & Experience</div>
                    
                    <div class="experience-card">
                        <div class="exp-title">
                            <span>Senior Cloud Infrastructure Architect</span>
                            <span class="exp-company">Tech Mahindra</span>
                        </div>
                        <div class="exp-meta">Hyderabad, India | 2021 - Present</div>
                        <ul class="exp-bullets">
                            <li>Automated cloud deployments by designing modular Terraform scripts, reducing setup times by 75%.</li>
                            <li>Engineered highly-available EKS Kubernetes clusters handling peak loads of up to 100K concurrent client requests.</li>
                            <li>Set up robust Prometheus and Grafana alerts, reducing time-to-incident discovery by 50%.</li>
                        </ul>
                    </div>
                    
                    <div class="experience-card">
                        <div class="exp-title">
                            <span>DevOps Associate Engineer</span>
                            <span class="exp-company">Capgemini</span>
                        </div>
                        <div class="exp-meta">Pune, India | 2019 - 2021</div>
                        <ul class="exp-bullets">
                            <li>Developed and debugged Jenkins automation pipelines for Java and Node.js microservices.</li>
                            <li>Managed and upgraded system patches across 120 Linux staging and production servers.</li>
                            <li>Collaborated with QA engineers to implement automated testing suites in CI pipelines.</li>
                        </ul>
                    </div>
                </div>

                <div>
                    <div class="section-header">Core Competencies</div>
                    <div class="skills-container">
                        <span class="skill-badge">Kubernetes</span>
                        <span class="skill-badge">Docker</span>
                        <span class="skill-badge">Terraform</span>
                        <span class="skill-badge">Ansible</span>
                        <span class="skill-badge">AWS (EC2, EKS, RDS)</span>
                        <span class="skill-badge">Jenkins</span>
                        <span class="skill-badge">Linux Administration</span>
                        <span class="skill-badge">Python Bash scripting</span>
                        <span class="skill-badge">Git/GitHub</span>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    },
    {
        "filename": "rohan_das_data_science.pdf",
        "title": "Rohan Das - Data Scientist",
        "html": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Rohan Das - Data Scientist</title>
            <link href="https://fonts.googleapis.com/css2?family=PT+Sans:wght@400;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'PT Sans', sans-serif;
                    color: #333333;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    min-height: 100vh;
                    background-color: #ffffff;
                }
                .left-bar {
                    width: 30%;
                    background-color: #f3f2ee;
                    padding: 40px 25px;
                    border-right: 1px solid #e0e0d8;
                }
                .right-body {
                    width: 70%;
                    padding: 40px;
                }
                .name {
                    font-size: 26px;
                    font-weight: 700;
                    color: #1e3a8a;
                    margin: 0 0 5px 0;
                }
                .title {
                    font-size: 14px;
                    color: #4b5563;
                    font-weight: 700;
                    text-transform: uppercase;
                    margin-bottom: 25px;
                }
                .left-section-title {
                    font-size: 13px;
                    font-weight: 700;
                    color: #1e3a8a;
                    text-transform: uppercase;
                    border-bottom: 1.5px solid #d1d5db;
                    padding-bottom: 4px;
                    margin-top: 25px;
                    margin-bottom: 12px;
                    letter-spacing: 0.5px;
                }
                .left-text {
                    font-size: 12.5px;
                    line-height: 1.6;
                    color: #4b5563;
                }
                .main-section-title {
                    font-size: 14px;
                    font-weight: 700;
                    color: #1e3a8a;
                    text-transform: uppercase;
                    border-bottom: 1.5px solid #1e3a8a;
                    padding-bottom: 4px;
                    margin-top: 0;
                    margin-bottom: 15px;
                }
                .main-section {
                    margin-bottom: 30px;
                }
                .experience-item {
                    margin-bottom: 20px;
                }
                .exp-header {
                    font-weight: 700;
                    font-size: 13.5px;
                    display: flex;
                    justify-content: space-between;
                }
                .company { color: #1e3a8a; }
                .date { color: #6b7280; font-weight: 400; }
                .exp-bullets {
                    padding-left: 20px;
                    margin: 8px 0 0 0;
                    font-size: 13px;
                    color: #4b5563;
                    line-height: 1.5;
                }
                .exp-bullets li {
                    margin-bottom: 5px;
                }
            </style>
        </head>
        <body>
            <div class="left-bar">
                <h1 class="name">Rohan Das</h1>
                <div class="title">Data Scientist</div>
                
                <div class="left-section-title">Contact Details</div>
                <div class="left-text">
                    ✉️ rohan.das@example.com<br>
                    📞 +91 95678 90123<br>
                    📍 Kolkata, West Bengal<br>
                    🔗 linkedin.com/in/rohandasds
                </div>
                
                <div class="left-section-title">Technical Skills</div>
                <div class="left-text">
                    Python (Pandas, Numpy)<br>
                    Machine Learning (Scikit-Learn)<br>
                    Deep Learning (PyTorch)<br>
                    SQL (PostgreSQL, MySQL)<br>
                    Tableau & PowerBI<br>
                    Git / Version Control
                </div>
                
                <div class="left-section-title">Education</div>
                <div class="left-text">
                    <strong>M.Sc. in Statistics</strong><br>
                    Indian Statistical Institute (ISI)<br>
                    <span style="font-size:11px; color:#6b7280;">2018 - 2020 | Kolkata</span>
                </div>
            </div>
            
            <div class="right-body">
                <div class="main-section">
                    <div class="main-section-title">Summary</div>
                    <p style="font-size: 13.5px; line-height: 1.6; color: #374151; margin-top: 0;">
                        Experienced Data Scientist with 5 years of industry experience uncovering valuable insights from structured and unstructured data. Skilled in statistical modeling, predictive analytics, and building robust machine learning pipelines. Successfully saved 20% in customer churn through advanced retention modeling.
                    </p>
                </div>
                
                <div class="main-section">
                    <div class="main-section-title">Work Experience</div>
                    
                    <div class="experience-item">
                        <div class="exp-header">
                            <span class="company">Mu Sigma Inc</span>
                            <span class="date">2022 - Present</span>
                        </div>
                        <div style="font-size:12.5px; font-style:italic; color:#4b5563; margin-top:2px;">Senior Decision Scientist</div>
                        <ul class="exp-bullets">
                            <li>Built predictive customer lifetime value models that improved marketing ROI by 25%.</li>
                            <li>Engineered NLP pipelines using HuggingFace models to classify customer support tickets with 92% accuracy.</li>
                            <li>Collaborated with product teams to design A/B tests for recommendation engines.</li>
                        </ul>
                    </div>
                    
                    <div class="experience-item">
                        <div class="exp-header">
                            <span class="company">Fractal Analytics</span>
                            <span class="date">2020 - 2022</span>
                        </div>
                        <div style="font-size:12.5px; font-style:italic; color:#4b5563; margin-top:2px;">Analytics Consultant</div>
                        <ul class="exp-bullets">
                            <li>Developed predictive regression models to forecast monthly retail supply chain inventory demands.</li>
                            <li>Designed SQL dashboards and automated daily ETL reports, saving 10 developer hours weekly.</li>
                            <li>Conducted exploratory analysis on customer transaction datasets containing over 5M entries.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    },
    {
        "filename": "ananya_iyer_design.pdf",
        "title": "Ananya Iyer - Product Designer",
        "html": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Ananya Iyer - Product Designer</title>
            <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Space Grotesk', sans-serif;
                    color: #1c1917;
                    margin: 0;
                    padding: 40px;
                    background-color: #fafaf9;
                }
                .designer-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: baseline;
                    border-bottom: 3px solid #ea580c;
                    padding-bottom: 15px;
                    margin-bottom: 30px;
                }
                .name {
                    font-size: 32px;
                    font-weight: 700;
                    color: #ea580c;
                    margin: 0;
                }
                .title {
                    font-size: 15px;
                    font-weight: 600;
                    color: #44403c;
                    letter-spacing: 0.5px;
                }
                .contact-strip {
                    display: flex;
                    gap: 20px;
                    font-size: 13px;
                    color: #78716c;
                    margin-bottom: 25px;
                }
                .contact-strip a { color: #ea580c; text-decoration: none; }
                .layout-grid {
                    display: grid;
                    grid-template-columns: 1fr 2.5fr;
                    gap: 40px;
                }
                .section-header {
                    font-size: 13px;
                    font-weight: 700;
                    text-transform: uppercase;
                    color: #ea580c;
                    letter-spacing: 1px;
                    margin-bottom: 12px;
                }
                .about-text {
                    font-size: 14px;
                    line-height: 1.6;
                    color: #44403c;
                }
                .job-box {
                    margin-bottom: 25px;
                }
                .job-title {
                    font-size: 14px;
                    font-weight: 700;
                    color: #1c1917;
                }
                .job-org {
                    color: #78716c;
                    font-size: 12.5px;
                    margin-bottom: 6px;
                }
                .job-desc {
                    margin: 0;
                    padding-left: 18px;
                    font-size: 13px;
                    color: #44403c;
                }
                .job-desc li {
                    margin-bottom: 5px;
                }
                .skills-list {
                    list-style: none;
                    padding: 0;
                    margin: 0;
                    font-size: 13px;
                }
                .skills-list li {
                    margin-bottom: 8px;
                    border-left: 2px solid #ea580c;
                    padding-left: 8px;
                }
            </style>
        </head>
        <body>
            <div class="designer-header">
                <h1 class="name">Ananya Iyer</h1>
                <div class="title">Lead UI/UX & Product Designer</div>
            </div>
            
            <div class="contact-strip">
                <span>✉️ ananya.iyer@example.com</span>
                <span>📞 +91 96789 01234</span>
                <span>📍 Chennai, Tamil Nadu</span>
                <span>🔗 <a href="#">ananyadesigns.com</a></span>
            </div>
            
            <div class="layout-grid">
                <div>
                    <div style="margin-bottom: 25px;">
                        <div class="section-header">Skills</div>
                        <ul class="skills-list">
                            <li>Figma</li>
                            <li>Wireframing</li>
                            <li>User Research</li>
                            <li>Prototyping</li>
                            <li>Design Systems</li>
                            <li>Webflow</li>
                        </ul>
                    </div>
                    
                    <div>
                        <div class="section-header">Education</div>
                        <div style="font-size: 12.5px; line-height: 1.5; color: #44403c;">
                            <strong>B.Des in Product Design</strong><br>
                            NID, Ahmedabad<br>
                            <span style="color:#78716c; font-size:11px;">Class of 2020</span>
                        </div>
                    </div>
                </div>
                
                <div>
                    <div style="margin-bottom: 30px;">
                        <div class="section-header">About Me</div>
                        <p class="about-text">
                            <strong>Creative UI/UX Designer with 6 years of expertise</strong> crafting user-centered digital solutions. Focused on designing accessible, high-fidelity prototypes and scalable design systems that bridge engineering and design teams. Passionate about solving user pain points through qualitative research.
                        </p>
                    </div>
                    
                    <div>
                        <div class="section-header">Relevant Experience</div>
                        
                        <div class="job-box">
                            <div class="job-title">Senior Product Designer</div>
                            <div class="job-org">Freshworks | Chennai, India | 2022 - Present</div>
                            <ul class="job-desc">
                                <li>Spearheaded redesign of customer self-service portal, yielding a 35% decline in help desk tickets.</li>
                                <li>Created and documented a unified web component design system, shortening design handoff times by 40%.</li>
                                <li>Conducted 25+ moderated user interviews to extract product insights and guide design roadmap decisions.</li>
                            </ul>
                        </div>
                        
                        <div class="job-box">
                            <div class="job-title">UI/UX Designer</div>
                            <div class="job-org">Zoho Corporation | Chennai, India | 2020 - 2022</div>
                            <ul class="job-desc">
                                <li>Designed interactive mobile app flows for finance tools, resulting in a 4.7-star rating on the App Store.</li>
                                <li>Collaborated directly with front-end developers to audit pixel perfection during deployment.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    },
    {
        "filename": "vikram_singh_ba.pdf",
        "title": "Vikram Singh - Business Analyst",
        "html": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Vikram Singh - Business Analyst</title>
            <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,400&family=Work+Sans:wght@300;400;600&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Work Sans', sans-serif;
                    color: #1c1c1c;
                    margin: 0;
                    padding: 40px;
                    line-height: 1.4;
                    background-color: #ffffff;
                }
                .name-header {
                    text-align: center;
                    border-bottom: 2px solid #556b2f;
                    padding-bottom: 15px;
                    margin-bottom: 25px;
                }
                .name {
                    font-family: 'Playfair Display', serif;
                    font-size: 32px;
                    font-weight: 600;
                    color: #556b2f;
                    margin: 0;
                }
                .role-title {
                    font-size: 13.5px;
                    font-weight: 600;
                    color: #71717a;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    margin-top: 5px;
                }
                .contact-details {
                    display: flex;
                    justify-content: center;
                    gap: 25px;
                    font-size: 12px;
                    color: #52525b;
                    margin-top: 10px;
                }
                .grid-sections {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 35px;
                }
                .section-header {
                    font-family: 'Playfair Display', serif;
                    font-size: 16px;
                    font-weight: 600;
                    color: #556b2f;
                    border-bottom: 1px solid #556b2f;
                    padding-bottom: 3px;
                    margin-bottom: 12px;
                }
                .objective-text {
                    font-size: 12.5px;
                    color: #4b5563;
                }
                .job-item {
                    margin-bottom: 15px;
                    font-size: 12.5px;
                }
                .job-title-row {
                    display: flex;
                    justify-content: space-between;
                    font-weight: 600;
                }
                .job-company {
                    color: #556b2f;
                }
                .job-date {
                    font-weight: 400;
                    color: #71717a;
                }
                .job-bullets {
                    padding-left: 15px;
                    margin: 5px 0 0 0;
                    color: #3f3f46;
                }
                .job-bullets li {
                    margin-bottom: 4px;
                }
                .skills-list {
                    padding-left: 15px;
                    margin: 0;
                    font-size: 12.5px;
                    color: #4b5563;
                }
                .skills-list li {
                    margin-bottom: 6px;
                }
            </style>
        </head>
        <body>
            <div class="name-header">
                <h1 class="name">Vikram Singh</h1>
                <div class="role-title">Senior Business Analyst</div>
                <div class="contact-details">
                    <span>📞 +91 97890 12345</span>
                    <span>✉️ vikram.singh@example.com</span>
                    <span>📍 Gurugram, Haryana</span>
                </div>
            </div>
            
            <div class="grid-sections">
                <div>
                    <div style="margin-bottom: 25px;">
                        <div class="section-header">Objective</div>
                        <p class="objective-text">
                            <strong>Analytically driven professional</strong> seeking to leverage my data analysis and business understanding skills as a senior business analyst. Eager to provide actionable deliverables to stakeholders and translate complex business requirements into detailed technical specifications.
                        </p>
                    </div>
                    
                    <div style="margin-bottom: 25px;">
                        <div class="section-header">Skills</div>
                        <ul class="skills-list">
                            <li><strong>Methodologies:</strong> Agile, Scrum, Waterfall</li>
                            <li><strong>Tools:</strong> SQL, Python, Excel, Jira, Power BI</li>
                            <li><strong>Techniques:</strong> GAP Analysis, SWOT, UML diagrams</li>
                            <li><strong>Soft Skills:</strong> Client relations, Stakeholder coordination</li>
                        </ul>
                    </div>

                    <div>
                        <div class="section-header">Education</div>
                        <div style="font-size: 12.5px; color: #4b5563; line-height: 1.5;">
                            <strong>B.E. in Information Technology</strong><br>
                            Delhi Technological University (DTU)<br>
                            <span style="color:#71717a; font-size:11px;">September 2016 - June 2020</span>
                        </div>
                    </div>
                </div>
                
                <div>
                    <div>
                        <div class="section-header">Key Projects & Roles</div>
                        
                        <div class="job-item">
                            <div class="job-title-row">
                                <span class="job-company">Deloitte India</span>
                                <span class="job-date">2022 - Present</span>
                            </div>
                            <div style="font-style: italic; color:#52525b; margin: 2px 0 5px 0;">Senior Business Consultant</div>
                            <ul class="job-bullets">
                                <li>Conducted GAP analysis for a financial services client, resulting in a project pipeline restructure that saved $120K.</li>
                                <li>Facilitated requirements elicitation workshops with 15+ senior executives.</li>
                                <li>Authored detailed BRD and FRD documents with zero revision requests.</li>
                            </ul>
                        </div>
                        
                        <div class="job-item">
                            <div class="job-title-row">
                                <span class="job-company">Accenture</span>
                                <span class="job-date">2020 - 2022</span>
                            </div>
                            <div style="font-style: italic; color:#52525b; margin: 2px 0 5px 0;">Business Analyst</div>
                            <ul class="job-bullets">
                                <li>Created interactive SQL and Tableau dashboards to track regional sales metrics.</li>
                                <li>Documented system use cases and designed workflow process flows (BPMN).</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    },
    {
        "filename": "sneha_reddy_qa.pdf",
        "title": "Sneha Reddy - QA Lead",
        "html": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Sneha Reddy - QA Lead</title>
            <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400&family=Nunito:wght@300;400;600&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Nunito', sans-serif;
                    color: #27272a;
                    margin: 0;
                    padding: 40px;
                    border: 8px solid #991b1b;
                    background-color: #fafafa;
                }
                .center-header {
                    text-align: center;
                    margin-bottom: 25px;
                }
                .name {
                    font-family: 'Lora', serif;
                    font-size: 30px;
                    color: #991b1b;
                    margin: 0;
                    font-weight: 700;
                }
                .role-title {
                    font-size: 14px;
                    font-weight: 600;
                    color: #4b5563;
                    letter-spacing: 1px;
                    margin-top: 4px;
                }
                .contact-details {
                    font-size: 12px;
                    color: #6b7280;
                    margin-top: 6px;
                }
                .section-header {
                    font-family: 'Lora', serif;
                    font-size: 15px;
                    font-weight: 700;
                    color: #991b1b;
                    border-bottom: 1.5px solid #d1d5db;
                    padding-bottom: 4px;
                    margin-top: 20px;
                    margin-bottom: 12px;
                }
                .summary-text {
                    font-size: 13px;
                    line-height: 1.6;
                    color: #374151;
                }
                .exp-item {
                    margin-bottom: 15px;
                }
                .exp-title-row {
                    display: flex;
                    justify-content: space-between;
                    font-weight: 600;
                    font-size: 13px;
                }
                .exp-company {
                    color: #991b1b;
                }
                .exp-bullets {
                    padding-left: 20px;
                    margin: 5px 0 0 0;
                    font-size: 12.5px;
                    color: #4b5563;
                }
                .exp-bullets li {
                    margin-bottom: 4px;
                }
                .skills-table {
                    width: 100%;
                    font-size: 12.5px;
                    margin-top: 10px;
                    border-collapse: collapse;
                }
                .skills-table td {
                    padding: 4px 0;
                }
                .skills-title {
                    font-weight: 600;
                    width: 30%;
                    color: #991b1b;
                }
            </style>
        </head>
        <body>
            <div class="center-header">
                <h1 class="name">Sneha Reddy</h1>
                <div class="role-title">Senior QA Automation Lead</div>
                <div class="contact-details">
                    ✉️ sneha.reddy@example.com | 📞 +91 98901 23456 | 📍 Bengaluru, Karnataka
                </div>
            </div>
            
            <div>
                <div class="section-header">Professional Summary</div>
                <p class="summary-text">
                    <strong>Lead QA Engineer with 6+ years of expertise</strong> directing test automation strategies for complex web and mobile ecosystems. Highly proficient in Selenium Webdriver, PyTest, Java, and Appium. Spearheaded testing for product migrations with zero post-release bugs.
                </p>
            </div>
            
            <div>
                <div class="section-header">Experience</div>
                
                <div class="exp-item">
                    <div class="exp-title-row">
                        <span class="exp-company">Capgemini Technologies</span>
                        <span>2022 - Present</span>
                    </div>
                    <div style="font-size:12.5px; font-style:italic; color:#4b5563; margin-top:2px;">QA Automation Lead</div>
                    <ul class="exp-bullets">
                        <li>Designed a customized hybrid test automation framework using Selenium and PyTest, reducing test execution times by 45%.</li>
                        <li>Supervise regression testing suites run on Jenkins CI pipelines for 4 distinct release branches.</li>
                    </ul>
                </div>
                
                <div class="exp-item">
                    <div class="exp-title-row">
                        <span class="exp-company">LTI Mindtree</span>
                        <span>2020 - 2022</span>
                    </div>
                    <div style="font-size:12.5px; font-style:italic; color:#4b5563; margin-top:2px;">Software QA Engineer</div>
                    <ul class="exp-bullets">
                        <li>Wrote and executed automated scripts for RestAPI integrations using Postman and RestAssured.</li>
                        <li>Identified and reported 200+ functional bugs using Jira, collaborating directly with developers to resolve.</li>
                    </ul>
                </div>
            </div>
            
            <div>
                <div class="section-header">Automation & Testing Skills</div>
                <table class="skills-table">
                    <tr>
                        <td class="skills-title">Languages:</td>
                        <td>Java, Python, Javascript, SQL</td>
                    </tr>
                    <tr>
                        <td class="skills-title">Automation Tools:</td>
                        <td>Selenium WebDriver, Appium, PyTest, RestAssured</td>
                    </tr>
                    <tr>
                        <td class="skills-title">QA Methodologies:</td>
                        <td>Functional, Regression, API Testing, Agile/Scrum</td>
                    </tr>
                </table>
            </div>
        </body>
        </html>
        """
    },
    {
        "filename": "karan_malhotra_product.pdf",
        "title": "Karan Malhotra - Product Manager",
        "html": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Karan Malhotra - Product Manager</title>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Montserrat', sans-serif;
                    color: #0f172a;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    min-height: 100vh;
                    background-color: #ffffff;
                }
                .main-column {
                    width: 70%;
                    padding: 40px;
                }
                .right-column {
                    width: 30%;
                    background-color: #0f172a;
                    color: #f8fafc;
                    padding: 40px 25px;
                }
                .name {
                    font-size: 28px;
                    font-weight: 700;
                    color: #0f172a;
                    margin: 0;
                }
                .role-title {
                    font-size: 14px;
                    font-weight: 600;
                    color: #06b6d4;
                    text-transform: uppercase;
                    letter-spacing: 1.5px;
                    margin-top: 5px;
                    margin-bottom: 25px;
                }
                .section-header {
                    font-size: 13px;
                    font-weight: 700;
                    color: #0f172a;
                    text-transform: uppercase;
                    border-bottom: 2px solid #0f172a;
                    padding-bottom: 4px;
                    margin-top: 25px;
                    margin-bottom: 12px;
                }
                .exp-item {
                    margin-bottom: 20px;
                }
                .exp-title-row {
                    display: flex;
                    justify-content: space-between;
                    font-weight: 700;
                    font-size: 13.5px;
                }
                .exp-company {
                    color: #06b6d4;
                }
                .exp-date {
                    color: #64748b;
                    font-weight: 400;
                }
                .exp-bullets {
                    padding-left: 20px;
                    margin: 6px 0 0 0;
                    font-size: 12.5px;
                    color: #334155;
                    line-height: 1.6;
                }
                .exp-bullets li {
                    margin-bottom: 5px;
                }
                .side-title {
                    font-size: 12.5px;
                    font-weight: 700;
                    text-transform: uppercase;
                    color: #06b6d4;
                    border-bottom: 1px solid #1e293b;
                    padding-bottom: 4px;
                    margin-top: 25px;
                    margin-bottom: 12px;
                }
                .side-text {
                    font-size: 12px;
                    line-height: 1.6;
                    color: #cbd5e1;
                }
            </style>
        </head>
        <body>
            <div class="main-column">
                <h1 class="name">Karan Malhotra</h1>
                <div class="role-title">Principal Product Manager</div>
                
                <!-- NOTE: NO header, starts directly with years of experience -->
                <p style="font-size: 13.5px; line-height: 1.6; color: #334155; margin-top: 0;">
                    <strong>Product Management Lead with 10+ years of experience</strong> leading the definition and scaling of mobile and SaaS platforms. Highly experienced in data-driven prioritization frameworks, product analytics, and customer discovery. Led teams to build features used by 12M+ monthly active users.
                </p>
                
                <div>
                    <div class="section-header">Work History</div>
                    
                    <div class="exp-item">
                        <div class="exp-title-row">
                            <span class="exp-company">Paytm Payments Bank</span>
                            <span class="exp-date">2021 - Present</span>
                        </div>
                        <div style="font-size:12.5px; font-weight:600; color:#334155; margin-top:2px;">Principal Product Manager</div>
                        <ul class="exp-bullets">
                            <li>Defined and launched a digital investment feature yielding 1.2M onboarding sign-ups in 90 days.</li>
                            <li>Created priority matrices and alignment maps for cross-functional design, tech, and marketing teams.</li>
                        </ul>
                    </div>
                    
                    <div class="exp-item">
                        <div class="exp-title-row">
                            <span class="exp-company">Ola (Ani Technologies)</span>
                            <span class="exp-date">2018 - 2021</span>
                        </div>
                        <div style="font-size:12.5px; font-weight:600; color:#334155; margin-top:2px;">Senior Product Manager</div>
                        <ul class="exp-bullets">
                            <li>Headed ride-allocation algorithm enhancements, decreasing driver idle times by 14%.</li>
                            <li>Executed direct user research and telemetry audits to solve driver retention loops.</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="right-column">
                <div class="side-title">Contact</div>
                <div class="side-text">
                    ✉️ karan.m@example.com<br>
                    📞 +91 99012 34567<br>
                    📍 Bengaluru, India
                </div>
                
                <div class="side-title">Expertise</div>
                <div class="side-text" style="line-height: 1.8;">
                    • Product Strategy<br>
                    • User Telemetry<br>
                    • Roadmapping<br>
                    • Agile / Jira / Mixpanel<br>
                    • A/B Experimentation
                </div>
                
                <div class="side-title">Education</div>
                <div class="side-text">
                    <strong>MBA</strong><br>
                    IIM Bangalore<br>
                    <span style="font-size: 11px; color:#94a3b8;">Class of 2018</span>
                </div>
            </div>
        </body>
        </html>
        """
    },
    {
        "filename": "deepika_rao_sysadmin.pdf",
        "title": "Deepika Rao - Systems Admin",
        "html": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Deepika Rao - Systems Admin</title>
            <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;500;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Ubuntu', sans-serif;
                    color: #1e293b;
                    margin: 0;
                    padding: 40px;
                    background-color: #ffffff;
                }
                .name {
                    font-size: 28px;
                    font-weight: 700;
                    color: #0369a1;
                    margin: 0;
                }
                .role-title {
                    font-size: 14px;
                    font-weight: 500;
                    color: #64748b;
                    text-transform: uppercase;
                    margin-top: 4px;
                    letter-spacing: 1px;
                }
                .contact-grid {
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 15px;
                    background-color: #f8fafc;
                    border: 1px solid #e2e8f0;
                    padding: 12px;
                    margin-top: 15px;
                    margin-bottom: 25px;
                    font-size: 12px;
                    color: #475569;
                }
                .section-header {
                    font-size: 14px;
                    font-weight: 700;
                    color: #0369a1;
                    text-transform: uppercase;
                    border-bottom: 1.5px solid #0369a1;
                    padding-bottom: 4px;
                    margin-top: 20px;
                    margin-bottom: 12px;
                }
                .summary {
                    font-size: 13px;
                    line-height: 1.6;
                    color: #334155;
                }
                .exp-box {
                    margin-bottom: 20px;
                }
                .exp-title-row {
                    display: flex;
                    justify-content: space-between;
                    font-weight: 700;
                    font-size: 13.5px;
                }
                .company {
                    color: #0369a1;
                }
                .bullets {
                    padding-left: 20px;
                    margin: 6px 0 0 0;
                    font-size: 12.5px;
                    color: #475569;
                }
                .bullets li {
                    margin-bottom: 4px;
                }
                .skills-block {
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 15px;
                    font-size: 12.5px;
                }
            </style>
        </head>
        <body>
            <h1 class="name">Deepika Rao</h1>
            <div class="role-title">Senior Systems Administrator</div>
            
            <div class="contact-grid">
                <div>✉️ deepika.rao@example.com</div>
                <div>📞 +91 90123 45678</div>
                <div>📍 Noida, Uttar Pradesh</div>
            </div>
            
            <div>
                <div class="section-header">Professional Overview</div>
                <p class="summary">
                    Certified Systems Administrator with over 7 years of specialized experience managing complex IT infrastructures, virtualization systems, and hybrid environments. Proven track record of auditing network architectures and improving uptime profiles from 99.1% to 99.98% across multi-site production offices.
                </p>
            </div>
            
            <div>
                <div class="section-header">Professional Experience</div>
                
                <div class="exp-box">
                    <div class="exp-title-row">
                        <span class="company">HCL Technologies</span>
                        <span>2022 - Present</span>
                    </div>
                    <div style="font-size:12px; font-style:italic; color:#64748b; margin-top:2px;">Senior System Operations Specialist</div>
                    <ul class="bullets">
                        <li>Supervise and maintain patch management routines for 200+ CentOS and Windows servers.</li>
                        <li>Configured automated backup routines, reducing potential data recovery objectives by 4 hours.</li>
                    </ul>
                </div>
                
                <div class="exp-box">
                    <div class="exp-title-row">
                        <span class="company">Tech Mahindra</span>
                        <span>2019 - 2022</span>
                    </div>
                    <div style="font-size:12px; font-style:italic; color:#64748b; margin-top:2px;">Systems Administrator</div>
                    <ul class="bullets">
                        <li>Managed user provisioning and system access controls using Active Directory and LDAP.</li>
                        <li>Investigated and resolved priority network downtime events, ensuring strict compliance with SLAs.</li>
                    </ul>
                </div>
            </div>
            
            <div>
                <div class="section-header">Core Competencies</div>
                <div class="skills-block">
                    <div><strong>OS:</strong> Linux (CentOS/Ubuntu), Windows Server</div>
                    <div><strong>Networking:</strong> TCP/IP, DNS, VPN, Firewalls</div>
                    <div><strong>Virtualization:</strong> VMware vSphere, Hyper-V</div>
                </div>
            </div>
        </body>
        </html>
        """
    }
]

async def generate_pdf(browser, resume):
    filename = resume["filename"]
    html_content = resume["html"]
    
    # Create the output directory if it doesn't exist
    os.makedirs("ourresumes", exist_ok=True)
    output_path = os.path.join("ourresumes", filename)
    
    print(f"Generating PDF for: {resume['title']} -> {output_path}")
    
    page = await browser.new_page()
    
    # Set HTML content directly
    await page.set_content(html_content)
    
    # Add a small wait for external web fonts to load
    await page.wait_for_timeout(1000)
    
    # Print page to PDF with standard styling configurations
    await page.pdf(
        path=output_path,
        format="A4",
        print_background=True,
        margin={
            "top": "0px",
            "bottom": "0px",
            "left": "0px",
            "right": "0px"
        }
    )
    await page.close()

async def main():
    print("Starting resume generation...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        tasks = [generate_pdf(browser, resume) for resume in RESUMES_DATA]
        await asyncio.gather(*tasks)
        await browser.close()
    print("All 10 resumes generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
