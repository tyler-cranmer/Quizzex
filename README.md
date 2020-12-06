Project title: Flash Card App (WIP)

Team members: Tyler Cranmer, Allison Bernstein, Samuel Terry, Benjamin Price

Vision statement: Our goal is to provide a platform for creating, studying, and sharing flash cards in an immersive and customizable environment.

Motivation: Our motivation is to assist us and others in learning and preparing for their coursework.  We understand the needs of students in today's learning environment and we want to create an application that we would want to utilize.  Finally, we want to encourage learning by making it fun for people to study subjects beyond just typical coursework.

Risks to project completion:  
- learning new languages such as Javascript, SQL, CSS, etc.
- time constraints for due date of project
- limited knowledge among team members in web application development
- staying consistent with SCRUM meetings and project management

Mitigation Strategy for above risks:
- Split up work evenly so new tools/languages are spread among the team
- Hold meetings where one member can share knowledge with others
- Set sprints to ensure meeting project deadlines on time
- Maintain consistent meetings to catch mistakes early
- Working with each other to highlight each others' strengths and shore up any knowledge gaps

Development method: Agile
- SCRUM two times a week at minimum, once early in the week and again later in the week to check in
- Track updates in Discord & GitHub projects
- Two-week period sprints
- End each sprint with a retrospective before next sprint
- Cycle through SCRUM master position

Project Tracking Software: GitHub Projects


Instructions for running:
- At the command line, navigate to the top directory ('projectRegex')
- Run the following command to ensure that all proper dependencies are installed:

  python -m pip install -r requirements.txt
  
- Enter the following commands:
    export FLASK_APP=root/flashcard.py

    flask run

- After the second command is entered, the server will start up, and you'll see a link to the landing page.
- After these commands have been entered at the command line once, you can instead use the following command line shortcut:
    python run.py

    - Doing so (in the projectRegex directory) will run the first two commands and start the server up the same way.
