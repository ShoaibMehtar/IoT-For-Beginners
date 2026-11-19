# Clearway PPL: EASA PPL(A) question bank (prototype)

An interactive question bank for EASA PPL(A) theory exams. It covers all 9 subjects, with a 75% pass mark per subject.

## Features
- **Sign in**: create an account with email and password, or continue with a Claude account when the app runs as a claude.ai artifact.
- **New test**: choose subjects and the number of questions, then pick a mode:
  - **Practice**: you see the answer and an explanation after each question.
  - **Exam**: timed (75 s per question) and marked at the end.
- **Save & exit**: keeps an unfinished test with its answers, flags and remaining time.
- **Saved tests tab**: shows each saved test with the date and time it was saved (local time and Zulu), and lets you resume or delete it.
- **Completed tests tab**: shows the date and time, score, pass or fail, and time taken. You can review every answer with its explanation, filter to incorrect, unanswered or flagged questions, and practise the questions you missed.
- **Progress by subject**: your accuracy in each subject compared with the 75% pass mark.

## Files
- `app.html` is the app: one file with no build step and no dependencies apart from Google Fonts.
- `index.html` is the standalone page generated from it (`node scripts/build.js`).

## Where data is stored (prototype)
| Running as | Login | Data |
|---|---|---|
| claude.ai artifact | Claude account | Private per-user cloud storage, synced across devices |
| `index.html` opened anywhere else | Email + password (PBKDF2-hashed) | This browser only (localStorage) |

All storage goes through a small store interface (`CloudStore` / `LocalStore` in `app.html`). To move to production, add a third store backed by a hosted database with real auth, such as Supabase or Firebase. The rest of the app does not need to change.

## Question content
The 81 sample questions are original, written against the EASA PPL(A) syllabus (Part-FCL, Part-SERA, Part-NCO, Part-MED). Each one has an explanation. Do not copy questions from commercial banks or the ECQB, which are copyrighted. The ECQB can be licensed if needed.

## Next steps
1. A hosted backend with auth and Stripe subscriptions.
2. An admin panel for writing and reviewing questions, mapped to learning-objective (LO) references.
3. Grow the bank to more than 1,000 questions, add images and diagrams to questions, and add spaced-repetition review.
