# 🚩 CTF Write-ups & Solutions

Welcome to my Capture The Flag (CTF) repository! This repository contains my write-ups and solutions for CTF challenges from various platforms and competitions. Feel free to explore the write-ups if you're looking for references or different ways to solve similar challenges.

---

## 📂 Repository Layout

```
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