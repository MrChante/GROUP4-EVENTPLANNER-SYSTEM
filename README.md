System Description

The Event Planner System is a desktop-based application designed to manage, track, and log event schedules within a structured digital ecosystem. Developed using Python's tkinter library, the system provides a responsive, dark-themed graphical user interface (GUI) modeled after contemporary flat-design aesthetics. Security is implemented through a standalone login gateway, requiring specific administrative credentials (group4 / 12345) before unlocking access to the core dashboards. Once authenticated, users can seamlessly transition between a data management panel and a unified calendar overview tab, both supported by real-time calculation metric cards that keep a live tally of total scheduled entries and unique venues booked.

On the technical side, the application utilizes a lightweight, file-based database architecture that reads from and writes to a local events.json file. It operates on complete CRUD (Create, Read, Update, Delete) functional principles, empowering the user to log new gatherings with customized tracking parameters such as an Event ID, Name, Scheduled Date, Venue Location, and Main Organizer. Data integrity is carefully preserved through automated validation loops that prevent duplicate records, require structured fields, and dynamic event selection properties that safely lock or release primary identification markers during data modification cycles.
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

---

---

## Step 1: Save the Files Locally

Make sure both files are saved in the **exact same directory/folder** on your computer.

1. Create a new folder (e.g., named `EventPlanner`).
2. Save the first code snippet as **`eventplanner_gui.py`**.
3. Save the second JSON snippet as **`events.json`**.

---

## Step 2: Open Terminal or Command Prompt

Navigate to the directory where you saved your files.

* **Windows:** Press `Win + R`, type `cmd`, and press Enter.
* **Mac/Linux:** Open the `Terminal` application.

Use the `cd` command to move into your project folder. For example:

```bash
cd Path/To/Your/EventPlanner

```

---

## Step 3: Run the Application

Execute the Python script using the following command depending on your operating system:

* **Windows:**
```bash
python eventplanner_gui.py

```


* **Mac / Linux:**
```bash
python3 eventplanner_gui.py

```



---

## Step 4: System Access (Credentials)

Once the window opens, you will be prompted with a slick dark-themed login interface. Use the hardcoded administrative credentials present in your script:

* **Username:** `group4`
* **Password:** `12345`

Click **LOG IN** or press `Enter` on your keyboard to access your main Event Planner Dashboard!

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
6. NAVAL, KYLE LESTER A.
