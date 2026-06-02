System Description: Event Planner System
The Event Planner System is a desktop-based Graphical User Interface (GUI) application designed to streamline the scheduling, tracking, and management of events. Built using Python’s native tkinter and ttk libraries, it delivers a sleek, responsive workspace tailored for individual organizers or small event production teams.

The system replaces traditional, error-prone console terminal menus with a modern, dark-themed visual dashboard inspired by high-end development environments. It unifies event data storage with an interactive workspace, ensuring all scheduling modifications persist safely in a local data file.

Here is a detailed breakdown of the **CRUD (Create, Read, Update, Delete)** features implemented inside the new Event Planner GUI system, showing how your original backend logic connects directly to the interactive user interface.

---

## 1. CREATE: Adding New Events

This feature allows you to register and schedule a new event into the system.

* **UI Element:** The entry input fields inside the **Event Planner Form** panel.
* **How it works:** You type the Event ID, Name, Date, Venue, and Organizer into the fields and click **Create Event**.
* **System Logic:** * The program validates that all fields contain text (no empty values allowed).
* It scans your existing `events.json` data to ensure the typed `Event ID` is unique. If a duplicate ID is found, it safely halts execution and throws an alert block.
* Once validated, the new entry is appended to the JSON array, written to your local disk, and the data grids refresh instantly.



---

## 2. READ: Viewing and Loading Records

This feature processes your raw stored data structures and presents them cleanly to the user.

* **UI Element:** The **Live Metrics Dashboard** cards, the interactive **Treeview Grid** on Tab 1, and the full spreadsheet viewport on Tab 2 (**All Events Calendar View**).
* **How it works:** Whenever the program starts or executes a modification, it silently parses `events.json`.
* **System Logic:**
* **Zebra Striping:** The system dynamically calculates alternating grid row backgrounds (`#171A21` and `#20242E`) to maintain high textual contrast and readability.
* **Dynamic Statistics:** The system extracts every unique venue value and calculates total row item counts to update the tracking cards at the top of the interface in real-time.



---

## 3. UPDATE: Editing Event Parameters

This feature lets you modify the schedule details of any previously saved event.

* **UI Element:** Single-clicking any row within the data grid.
* **How it works:** Selecting an event instantly pulls its data out of the grid and copies it back into the entry fields.
* **System Logic:**
* **State Locking Safeguard:** To ensure structural database integrity, selecting an event for modification triggers an immutable lock on the `Event ID` entry box (`state="disabled"`). This prevents you from accidentally breaking records by shifting IDs while changing details like names or venues.
* Clicking **Update Details** overwrites the specific record attributes within the JSON list and saves the file.



---

## 4. DELETE: Purging Schedule Items

This feature allows you to permanently remove an unneeded event record from your tracking database.

* **UI Element:** Selecting a row inside the grid, followed by the **Delete Event** button.
* **How it works:** It clears out dead entries that are canceled or no longer valid.
* **System Logic:**
* **Destructive Confirmation Prompt:** To prevent accidental mouse slips from deleting valuable scheduling data, the application interrupts the delete command by generating an explicit native confirmation message box (`askyesno`).
* If confirmed, the system filters out the active matching `Event ID` string, updates `events.json`, clears all text input entry slots, and updates the UI grids.

Here is a complete, step-by-step guide to setting up your files and executing the new Event Planner GUI interface application on your local machine.

---

### Step 1: Organize Your Project Directory

To ensure the application reads and writes to your database file seamlessly, create a unified project directory and arrange the files as shown below:

```text
comprog/
│
├── eventplanner_gui.py   <-- Save the newly generated GUI script here
└── events.json           <-- Place your existing events records file here

```

> **Note:** If `events.json` is not present in the directory, the system will automatically initialize an empty database file for you upon its first launch.

---

### Step 2: Open the Command Line Interface

You must interact with your operating system's terminal environment to run the script.

* **Windows:** Press `Windows Key + R`, type `cmd`, and hit **Enter**.
* **macOS:** Press `Command + Spacebar` to open Spotlight, type `Terminal`, and hit **Enter**.
* **Linux:** Press `Ctrl + Alt + T` on your keyboard.

---

### Step 3: Navigate to Your Project Folder

Use the change directory (`cd`) command to point your terminal environment directly to your workspace folder. If you saved your `comprog` folder on the Desktop, enter the following command:

* **Windows:**
```cmd
cd %USERPROFILE%\Desktop\comprog

```


* **macOS / Linux:**
```bash
cd ~/Desktop/comprog

```



---

### Step 4: Run the Application Script

Execute the program by calling the Python interpreter on your script file. Enter the following command into your terminal:

```bash
python eventplanner_gui.py

```

> **System Variation:** If your machine maps Python 3 installations to an explicit command name, execute this alternative instead:
> ```bash
> python3 eventplanner_gui.py
> 
> ```
> 
> 

---

### Quick Interface Operations Guide

Once the graphical dashboard initializes on your screen, you can manage your operations using these quick interactive workflows:

* **To Add Records:** Populate all text input entry slots (ID, Name, Date, Venue, Organizer) within the left control frame and click **Create Event**.
* **To Edit Records:** Left-click any existing entry row inside the data spreadsheet grid. This automatically populates the form fields and locks down the unique event ID. Modify the values you want to change, then click **Update Details**.
* **To Delete Records:** Highlight any target item inside the data grid table and click **Delete Event**. Respond to the secure window prompt to permanently wipe the record.
* **To View the Clean Calendar View:** Click on the **All Events Calendar View** tab at the top of the workspace to toggle over to a full-width, distraction-free reporting spreadsheet.


GROUP 4 EVENT PLANNER SYSTEM 
MEMBER:
1. CABAB, DAVE KEVIN N.
2. CASCARA, JOHN PAUL P.
3. GUASIL, JUSTIN PAUL P.
4. ESPERAS, GERRY C.
5. TUBIS, LORENZ 0.
6. NAVAL, KYLE LESTER 
