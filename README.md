# PRODIGY_SD_03
 Task - 3

Develop a program that allows users to store and manage contact information. The program should provide options to add a new contact by entering their name, phone number, and email address. It should also allow users to view their contact list, edit existing contacts, and delete contacts if needed. The program should store the contacts in memory or in a file for persistent storage.

What does this program do?
  Manages contacts with the features to add, view, edit and delete entries.

How does this program work?
1. Persistent Storage: Contacts are stored in a JSON file (contacts.json) for persistent storage. The program loads contacts from this file at startup and saves any changes to it.

2. Add Contact: Users can add a new contact by providing a name, phone number, and email address.

3. View Contacts: Users can view all stored contacts. If no contacts are stored, the program informs the user.

4. Edit Contact: Users can select an existing contact by name and update the phone number and/or email address.

5. Delete Contact: Users can delete an existing contact by name.

6. Exit: The program saves the contacts to the file before exiting.