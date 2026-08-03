# 🚩 CTF Write-ups & Solutions

Welcome to my Capture The Flag (CTF) repository! This repository contains my write-ups and solutions for CTF challenges from various platforms and competitions. Feel free to explore the write-ups if you're looking for references or different ways to solve similar challenges.

---

## 📂 Repository Layout

```
├── writeups/     # All solved challenges, grouped by source → challenge
├── handbook/     # Reusable notes, theory and cheat sheets
├── templates/    # Write-up template used for new challenges
└── tools/        # Helper scripts reused across challenges
```

Each challenge folder is named `<category>_<challenge>` so you can see the category
at a glance without opening it, and follows the same internal layout:

```
web_timekorp/
├── writeup.md    # The write-up / solution
├── handout/      # Files provided by the organisers (source, binaries, Docker setup)
├── solve/        # My exploit / solver scripts and payloads
└── assets/       # Screenshots referenced by the write-up
```

Category prefixes: `web`, `pwn`, `rev`, `crypto`, `forensics`, `osint`, `misc`.
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

## 🎯 Where to Practice

Platforms and resources I use to find challenges:

| Platform | What it's for |
| --- | --- |
| [Hack The Box](https://www.hackthebox.com/) | Machines, and the [HTB CTF](https://ctf.hackthebox.com/) events / Try Out labs |
| [HTB CTF Try Out](https://ctf.hackthebox.com/ctf/try-out) | Beginner-friendly starter challenges across all categories |
| [CTFtime](https://ctftime.org/) | Calendar of upcoming/ongoing CTF events, team rankings and archives |
| [picoCTF](https://picoctf.org/) | Great starting point for beginners |
| [AdWorld (XCTF)](https://adworld.xctf.org.cn/) | Large archive of categorised practice challenges |
| [OverTheWire](https://overthewire.org/wargames/) | Wargames for Linux, networking and binary basics |
| [pwn.college](https://pwn.college/) | Structured binary exploitation & reverse engineering course |
| [Root Me](https://www.root-me.org/) | Hundreds of hands-on challenges across every category |

---

## 📚 Handbook

Notes and theory that aren't tied to a single challenge: [handbook/](./handbook/README.md)

---
