# AzkaTronics – Smart Electronics Store Chatbot
A Python-based chatbot for an electronics store that allows users to order products, compare specs, track orders, and apply for jobs via a terminal or GUI interface.

Completed as a Level 4 group university project in 2022/2023.

## Features

- Order Products: Browse and add items to your cart, save orders, and proceed to checkout.
- Track Orders & Order History: Logged-in users can view past purchases and the status of ongoing orders.
- View & Compare Devices: Access and compare detailed technical specifications of phones, tablets, laptops, and desktops.
- Store Locator: Get directions to physical store locations via Google Maps.
- Job Application System: Apply for jobs through a dynamic, validated form interface.
- Graphical User Interface: A Tkinter-based GUI that enhances user interaction with the chatbot.

## Tech Stack

- Language: Python
- GUI: Tkinter
- Project Management: Azure DevOps (Scrum methodology)
- Version Control: SourceTree, Git
- Data Storage: JSON-based files for users, carts, and job applications

## Project Structure

- `main.py`: CLI version of the bot with full functionality.
- `gui.py`: Tkinter GUI logic and integration.
- `main_gui.py`: Adapted main logic for GUI compatibility.
- `data/`: Includes JSON files for accounts and application data.
- `device_db/`: Organized device specs categorized by type and manufacturer.

## Known Limitations

Some GUI components (login, ordering, tracking) are pending full implementation, though complete in the terminal version.

## What We Learned

- Practical application of Agile (Scrum) development.
- Complex user flow design and feature integration.
- GUI design and state management in Python.
- JSON handling and modular code architecture.
