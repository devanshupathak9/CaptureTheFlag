## Challenge: Character (950 points, difficulty: Very Easy)

## Description

*Security through Induced Boredom is a personal favourite approach of mine. Not as exciting as something like The Fray, but I love making it as tedious as possible to see my secrets, so you can only get one character at a time!*

---

## Summary

In this challenge, we're given an IP address and a port number. When we connect to the server via TCP, it asks us to input the index of the character in the flag. It then returns the character at that index and asks for the next index.

You can test the connection manually using tools like:

```bash
nc <ip> <port>
```

```bash
 % nc 83.136.253.59 53104
Which character (index) of the flag do you want? Enter an index: 0
Character at Index 0: H
Which character (index) of the flag do you want? Enter an index: 1
Character at Index 1: T
Which character (index) of the flag do you want? Enter an index: 3
Character at Index 3: {
Which character (index) of the flag do you want? Enter an index: 4
Character at Index 4: t
Which character (index) of the flag do you want? Enter an index: 110
Index out of range!
Which character (index) of the flag do you want? Enter an index: ^[[A
```

Since the server returns one character at a time and the flag is long, using a brute-force approach would be extremely tedious. The solution is to automate the process.

## Solution:
1. Create a client TCP socket and connect to the server.
2. Start with index 0, send it to the server, and receive the character.
3. Keep appending the character to a ctf_flag string.
4. Repeat until the server returns "Index out of range!", indicating we have reached the last index.
