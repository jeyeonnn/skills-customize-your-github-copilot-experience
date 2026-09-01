---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files must follow this guide to ensure consistency, clarity, and an excellent learning experience for students.

## 1. Template Requirements

- **Follow the template structure**: All assignments must follow [`templates/assignment-template.md`](../../templates/assignment-template.md)
- **File naming**: Create each assignment as `README.md` within its own assignment folder (e.g., `assignments/python-basics/README.md`)
- **No section omissions**: Do not remove or skip any required sections from the template
- **Icon consistency**: Use the exact icons specified in the template (📘, 🎯, 📝, 🛠️)

## 2. Content Standards

### Learning-Focused Approach
- **Clear objectives**: Every assignment must have well-defined learning goals
- **Appropriate difficulty**: Structure tasks from foundational to more advanced concepts
- **Measurable outcomes**: Students should know exactly what success looks like

### Student-Friendly Language
- **Encouraging tone**: Use positive, motivating language that builds confidence
- **Clear instructions**: Write in simple, direct language without jargon
- **Helpful examples**: Provide code examples or sample input/output when helpful

## 3. Section Guidance

### Title (📘 Assignment: [Title])
- Use short, descriptive names that reflect the main concept
- Examples: `Python Basics`, `Loops and Conditionals`, `Data Analysis Project`, `Building Classes`

### Objective (🎯)
- Write 1-2 concise sentences explaining what students will learn or accomplish
- Focus on main skills/concepts, not implementation details
- Start with action verbs: "Learn to...", "Build...", "Understand..."

### Tasks (📝)
Each task should have:

#### Task Title (🛠️ [Task Name])
- Use specific, action-oriented names
- Examples: `Create a Calculator`, `Implement User Input`, `Add Data Validation`

#### Description
- Clearly explain what the student must do
- Provide context if needed (e.g., "This task builds on Task 1...")
- Include any specific requirements or constraints

#### Requirements
- Use a bulleted list under "Completed program should:"
- Make each requirement specific and measurable
- Avoid vague requirements; be precise about expected behavior
- Examples of good requirements:
  - ❌ "The program should work"
  - ✅ "The program prompts the user for input and validates that the input is a positive integer"

#### Optional: Examples
- Provide sample input/output in code blocks when helpful
- Show what correct behavior looks like
- Use this to clarify ambiguous requirements