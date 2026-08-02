# 🚩 CTF Write-ups & Solutions

Welcome to my Capture The Flag (CTF) repository! This is my personal space where I document my journey in learning cybersecurity by solving CTF challenges from various platforms and competitions.

## 🎯 Purpose

The main goals of this repo are:
1.  **To Learn:** Deepen my understanding of cybersecurity concepts through hands-on practice.
2.  **To Document:** Keep a log of my problem-solving process for future reference.
3.  **To Share:** Help others in the community who might be stuck on similar challenges.

---

## 📂 Repository Layout

```
.
├── writeups/     # All solved challenges, grouped by source → category → challenge
├── handbook/     # Reusable notes, theory and cheat sheets
├── templates/    # Write-up template used for new challenges
└── tools/        # Helper scripts reused across challenges
```

Every challenge lives at `writeups/<source>/<category>/<challenge>/` and follows the
same internal layout:

```
<challenge>/
├── README.md     # The write-up
├── handout/      # Files provided by the organisers (source, binaries, Docker setup)
├── solve/        # My exploit / solver scripts and payloads
└── assets/       # Screenshots referenced by the write-up
```

Only the parts a challenge actually needs are present.

---

## 🗂️ Write-ups

| Source | Type | Index |
| --- | --- | --- |
| Hack The Box | Platform | [writeups/hack-the-box](./writeups/hack-the-box/README.md) |
| AdWorld (XCTF) | Platform | [writeups/adworld](./writeups/adworld/README.md) |
| EHAX CTF 2025 | Event | [writeups/ehax-ctf-2025](./writeups/ehax-ctf-2025/README.md) |
| Infobahn CTF 2025 | Event | [writeups/infobahn-ctf-2025](./writeups/infobahn-ctf-2025/README.md) |
| PatriotCTF 2025 | Event | [writeups/patriot-ctf-2025](./writeups/patriot-ctf-2025/README.md) |

See [writeups/README.md](./writeups/README.md) for the complete challenge index.

---

## 📚 Handbook

Notes and theory that aren't tied to a single challenge: [handbook/](./handbook/README.md)

---

## ✍️ Adding a New Write-up

1. Create `writeups/<source>/<category>/<challenge-name>/` (lower-case, `kebab-case`).
2. Copy [`templates/writeup-template.md`](./templates/writeup-template.md) to `README.md` inside it and fill it in.
3. Drop provided files in `handout/`, your scripts in `solve/`, screenshots in `assets/`.
4. Add a row to that source's index `README.md`.
