# UI Mockup: Source Citations

This document defines how source citations should appear under the bot's answers in the chat UI. 
To build trust, every factual answer must include a collapsible or clearly separated source block.

## Design Rules
- The source should appear immediately after the bot's main text.
- Use a blockquote (`>`) or a lighter font color to separate it from the main answer.
- Include a book icon (📚) or link icon (🔗) for better UX.

---

## Example 1: Single Source Citation
**User:** Where is the Training Office?

**Bot:** 
The Training Office is located in room **I.101**.

> 📚 **Source:** `offices.csv` (Row: Training Office)

---

## Example 2: Multiple Sources / Complex Answer
**User:** What is the rule for retaking a course and how much is the fee?

**Bot:**
To retake a course, you must register during the first 2 weeks of the semester. Please note that retake credits cost 1.5x the normal rate.

> 📚 **Sources:** 
> 1. `student_handbook_2026.pdf` (Section 4.2: Course Registration)
> 2. `Fee notice 2026` (Section 2: Retake Policies)