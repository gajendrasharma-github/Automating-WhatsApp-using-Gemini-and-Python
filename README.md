# Personalized WhatsApp Message Automation

This project automates the process of sending personalized WhatsApp messages using data from Google Sheets, Gemini AI for natural language generation, and Python for orchestration.

## Overview

The system reads user data (name, number, description) from a Google Sheet, uses Gemini Pro to generate customized messages based on the user's traits and a defined task, and sends the message via WhatsApp using the `pywhatkit` library.

## Key Features

- Reads user context from Google Sheets
- Uses Gemini for personalized message generation
- Sends messages via WhatsApp Web
- Human-like tone and structure
- Mobile-friendly message formatting

## Technologies Used

- Python
- gspread (Google Sheets API)
- google-generativeai (Gemini Pro)
- pywhatkit (WhatsApp automation)

## Google Sheet Format

The Google Sheet includes the following columns:
Name | Number | Description


For more detailed personalization, you can include:

Name | Number | Profession | Age/DOB | City | ReasonToJoin | Personality | Hobbies


## Example Use Case
You launch a free workshop. People sign up via a Google Form, answering few questions:



- Name, profession, city

- Why you want to join the course?

- What describes your personality the best?

- What do you do in your free time?



This data lands in a Google Sheet. From there, Gemini crafts personalized messages that truly connect — not just “Hey, thanks for signing up” but something more like:



“Hey Priya! I truly resonate with your passion for cooking. Let me tell you that this workshop will definitely be an amazing experience for you. Can't wait to see you there. ”





