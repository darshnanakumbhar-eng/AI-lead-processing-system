# AI-lead-processing-system
# AI Lead Processing System

## Overview
This project demonstrates a simple AI-based system for processing leads in a SaaS platform like KeaBuilder.

It includes lead classification, response generation, and similarity matching.

---

## Features

### Lead Classification
Classifies leads into:
- Hot
- Warm
- Cold

Based on:
- Budget
- User intent (message urgency)

---

### Response Generation
Generates personalized responses:
- Uses user name
- Natural and human-like tone
- Suggests next steps

---

### Similarity Matching
- Uses cosine similarity
- Finds most similar input from given data

---

## Sample Input

```json
{
  "name": "Sakshi",
  "budget": "5000 USD",
  "timeline": "2 weeks",
  "message": "Need a landing page urgently"
}
