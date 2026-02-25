# Playlist Chaos

Your AI assistant tried to build a smart playlist generator. The app runs, but some of the behavior is unpredictable. Your task is to explore the app, investigate the code, and use an AI assistant to debug and improve it.

This activity is your first chance to practice AI-assisted debugging on a codebase that is slightly messy, slightly mysterious, and intentionally imperfect.

You do not need to understand everything at once. Approach the app as a curious investigator, work with an AI assistant to explain what you find, and make targeted improvements.

---

## How the code is organized

### `app.py`  

The Streamlit user interface. It handles things like:

- Showing and updating the mood profile  
- Adding songs  
- Displaying playlists  
- Lucky pick  
- Stats and history

### `playlist_logic.py`  

The logic behind the app, including:

- Normalizing and classifying songs  
- Building playlists  
- Merging playlist data  
- Searching  
- Computing statistics  
- Lucky pick mechanics

You will need to look at both files to understand how the app behaves.

---

## What you will do

### 1. Explore the app  

Run the app and try things out:

- Add several songs with different titles, artists, genres, and energy levels  
- Change the mood profile  
- Use the search box  
- Try the lucky pick  
- Inspect the playlist tabs and stats  
- Look at the history  

As you explore, write down at least five things that feel confusing, inconsistent, or strange. These might be bugs, quirks, or unexpected design decisions.

### 2. Ask AI for help understanding the code  

Pick one issue from your list. Use an AI coding assistant to:

- Explain the relevant code sections  
- Walk through what the code is supposed to do  
- Suggest reasons the behavior might not match expectations  

For example:

> "Here is the function that classifies songs. The app is mislabeling some songs. Help me understand what the function is doing and where the logic might need adjustment."

Before making changes, summarize in your own words what you think is happening.

### 3. Fix at least four issues  

Make improvements based on your investigation.

For each fix:

- Identify the source of the issue  
- Decide whether to accept or adjust the AI assistant's suggestions  
- Update the code  
- Add a short comment describing the fix  

Your fixes may involve logic, calculations, search behavior, playlist grouping, lucky pick behavior, or anything else you discover.

### 4. Test your changes  

After each fix, try interacting with the app again:

- Add new songs  
- Change the profile  
- Try search and stats  
- Check whether playlists behave more consistently  

Confirm that the behavior matches your expectations.

### 5. Optional stretch goals  

If you finish early or want an extra challenge, try one of these:

- Improve search behavior  
- Add a "Recently added" view  
- Add sorting controls  
- Improve how Mixed songs are handled  
- Add new features to the history view  
- Introduce better error handling for empty playlists  
- Add a new playlist category of your own design  

---

## Tips for success

- You do not need to solve everything. Focus on exploring and learning.  
- When confused, ask an AI assistant to explain the code or summarize behavior.  
- Test the app often. Small experiments reveal useful clues.  
- Treat surprising behavior as something worth investigating.  
- Stay curious. The unpredictability is intentional and part of the experience.

When you finish, Playlist Chaos will feel more predictable, and you will have taken your first steps into AI-assisted debugging.

---

### Part 1: Meet the Chaos
1. Playlist Chaos starter repo and fork it to your GitHub account.
The students should have Visual Studio Installed, which they can do here: https://code.visualstudio.com/download.

If they do have Visual Studio, the only thing they are supposed to do is fork the repository. And if they have Visual Studio set up, they can choose a location and run 

git clone https://github.com/nishalinishanmugan/ai110-module1tinker-playlistchaos-starter.git

If they do not have git, they can go on the left-hand side and choose Source Control in Visual Studio, and click install git, which will redirect you to here:  https://git-scm.com/install/windows

There is a chance that when the student runs the git command or even git  --version, it will show an error. If that happens, the student will need to do the following to make sure git is added as a path in Windows:

1. In the Start Menu or taskbar search, search for "environment variable".
2. Select "Edit the system environment variables".
3. Click the "Environment Variables" button at the bottom.
4. Double-click the "Path" entry under "System variables".
5. With the "New" button in the PATH editor, add C:\Program Files\Git\bin\ and C:\Program Files\Git\cmd\ to the end of the list.
6. Close and re-open your console.

After that, this command should work: git clone https://github.com/nishalinishanmugan/ai110-module1tinker-playlistchaos-starter.git

If the student does not have Visual Studio, they can click the “Code” button and then Codespaces. And open the project as a Codespace. However, I recommend opening it up in Visual Studio.  

2. Start the app:
streamlit run app.py

The first thing the student has to do is run pip install streamlit. If the student has an error with pip, then they need to first make sure they have Python downloaded: https://www.python.org/downloads/windows/. After that, the next thing they have to do is make sure pip is added as a path for Windows. 

1. In the Start Menu or taskbar search, search for "environment variable".
2. Select "Edit the system environment variables".
3. Click the "Environment Variables" button at the bottom.
4. Double-click the "Path" entry under "System variables".
5. With the "New" button in the PATH editor, add C:\Users\nisha\AppData\Local\Programs\Python\Python313\Scripts to the end of the list.
6. Close and re-open your console.

After that rerun, pip install streamlit. And run streamlit run app.py

---
###  Part 2 & Part 3: AI Debugging Collaboration and Copilot Refactor and Version Control
- Fixed search_song - Checks the entire field value inside the query string instead part of the query
- Fixed random_choice_or_none - If the list of empty, then this code will crash, so fixed it to check if the list is empty
- Fixed computer_playlist_stats - Fixed the hype_ratio and the avg_energy to include the total songs because right now it’s not including the whole set
- Fixed merged_playlists - The merge is causing a duplication, so fixed it so it is merged without duplicating
- Fixed Classify_song - Fixed the classification so it doesn't use the title to detect chill. Also fixed it to require energy for classifying hype because right now every rock song becomes hype even if the energy is low. 
- Fixed profile["favorite_genre"] - Fixed this selection so it doesn’t jump back to rock after each rerun
- Fixed is_chill_keyword - Fixed this so chill keyword section isn’t just depending on the title for matching

---
### Part 4: Reflect and Discuss
The summary should be 5–7 sentences covering:

- The core concept students needed to understand
- Where students are most likely to struggle
- Where AI was helpful vs misleading
- One way they would guide a student without giving the answer

The core concepts that the students need to understand is how to ask questions and utilize AI to understand a codebase. They start off with running the code and then after testing out the behavior, they will go back and examine the code and ask AI questions to find improvements and bugs. The students will struggle with setting up this lab. Because this is the first lab and the student needs github copilot, vs code, and python setup on their computer. Students that don’t have this setup before class will probably be spending more time on this during the breakout room. And they will probably need some help if they need to add the path to the environmental variables while setting up python for example. Also the lab doesn’t mention that you need to pip install streamlit, so that will probably be a common question. AI is helpful with understanding the structural issues with the code, but the AI can cause issues by suggesting changes without understanding how that plays into the overall behavior of the code. The AI can ask the student debugging questions without giving the answer or questions to help the student think like the Codepath AI Tutor with UMPIRE. The AI can help with asking questions to help the student think and understand the code. 

